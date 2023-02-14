def slr_parser(productions,headers,table, input_str):
    stack = [0]
    
    input_str = input_str.split(' ') + ['$']
    step = 1
    result = [["step","stack","input","action"]]
    while input_str:
        current_state = stack[-1]
        current_input = input_str[0]
        if current_input not in headers:
            raise SyntaxError(f"Error: invalid input: {current_input}")
        
        
        action = table[int(current_state)][headers.index(current_input)+1]
        
        if action=="err":
            expected=[]
            for i,col in enumerate(table[int(current_state)]):
                if col[0] in "rs":
                    expected.append(headers[i-1])
            raise Exception(f"SyntaxError \n{input_str} \n ^\n unexpected {current_input} \n expected symbols: {expected}")

        if action[0] == 's':
            stack.append(current_input)
            stack.append(int(action[1:]))
            input_str.pop(0) #pop str[0]

            stack_log=' '.join(tuple(str(i)[:3] for i in stack))
            str_log=' '.join(tuple(str(i)[:3] for i in input_str))

            result.append((step, stack_log, str_log, f"Shift {action[1:]}"))
            step += 1

        elif action[0] == 'r': # checkpoint
            production = int(action[1:]) #number of the production
            num_pop = 2 * (len(productions[production]) - 1) #
            for i in range(num_pop):
                stack.pop()
            state = int(stack[-1])# pop 2 *length
            stack.append(productions[production][0]) # push rule root 
            stack.append(table[state][headers.index(productions[production][0])+1])# append state number 
            
            stack_log=' '.join(tuple(str(i)[:3] for i in stack))
            str_log=' '.join(tuple(str(i)[:3] for i in input_str))

            result.append((step, stack_log, str_log, f"Reduce {production}")) # log
            step += 1
        elif action in [str(i) for i in range(10)]:
            stack.append(int(action))
            
            stack_log=' '.join(tuple(str(i)[:3] for i in stack))
            str_log=' '.join(tuple(str(i)[:3] for i in input_str))

            result.append((step, stack_log, str_log, f"Shift {action[1:]}"))
            step += 1
        elif action == 'acc':
            
            stack_log=' '.join(tuple(str(i)[:3] for i in stack))
            str_log=' '.join(tuple(str(i)[:3] for i in input_str))
            
            result.append((step, stack_log, str_log, "Accept"))
            return result
    return SyntaxError

#todo: inv syntax @ line
#stack & input keep updating with every iteration in result ??