import re

def lex(text):
    tokens = []
    text = re.sub(r'//.*\n', '\n', text) # remove single-line comments
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL) # remove multi-line comments
    i = 0
    while i < len(text):
        if text[i].isspace():
            i+=1
        elif text[i].isalpha():
            j = i + 1
            while j < len(text) and text[j].isalnum():
                j += 1
            word = text[i:j]
            if word.lower() in ["entier", "reel", "booleen", "tableau d'entiers",]:
                tokens.append(('type', word))
            elif word.lower() in ["et","ou"]:
                tokens.append(('logOp', word))
            elif word.lower() in ["lire", "afficher", "si", "alors", "sinon", "finsi", "pour", "de", "à", "faire", "finpour","debut","fin","algorithme"]:
                tokens.append((word, None))
            else:
                tokens.append(('identifier', word))
            i = j
        elif text[i].isdigit():
            j = i + 1
            while j < len(text) and text[j].isdigit():
                j += 1
            tokens.append(('number', int(text[i:j])))
            i = j
        elif text[i] in '<->':
            if i + 1 < len(text) and text[i:i+2]=='<-':
                tokens.append(('<-', None))
                i += 2
            elif i + 1 < len(text) and text[i:i+2] in ['>=', '<=', '==', '!=']:
                tokens.append(('relOp', text[i:i+2]))
                i += 2
            else:
                tokens.append(('relOp', text[i]))
                i += 1
                
        elif text[i] in '+-':  
            tokens.append(('addOp', text[i]))
            i += 1
        elif text[i] in '*/':  
            tokens.append(('mulOp', text[i]))
            i += 1
        elif text[i] in ',;()':  
            tokens.append((text[i], None))
            i += 1
        elif text[i] == '"':
            j = i + 1
            while j < len(text) and text[j] != '"':
                if text[j] == '\\' and text[j + 1] == '"':
                    j += 1
                j += 1
            tokens.append(('stringLiteral', text[i + 1:j].replace('\\"', '"')))
            i = j + 1
        # elif text[i] in ';,()+-*/':
        #     i+=1
        else:
            raise Exception('{} is undefined'.format(text[i]))
        # i += 1
    return tokens
    #todo minusequal,assigment,  remove ; ? (expression) in table ?
# print(lex())

# longstr="""Algorithme maximum 
# entier a, b, c; 
# debut 
# lire a ; 
# lire b ;
# si a < b alors 
# afficher "a est plus petit b" ;
# sinon
# afficher "a est plus grand b" ;
# finsi 
# c <- b * b + 4 * a *c ;
# afficher c ;
# fin """

def analysis(longstr):
    instructions= longstr.split('\n')
    for j,instruction in enumerate(instructions):
        # input= instruction
        # print(f'input: {input}')
        output=lex(instruction)
        output=[i[0].lower() for i in output]
        instructions[j]=' '.join(output)
        # print(f'output: {output}')
        # print("-"*20)
    return ' '.join(instructions)


#todo: fix many none types like operators and instructions
"""
algorithme maximum 
entier a, b, c; 
debut 
lire a ; 
lire b ;
si a < b alors 
afficher "a est plus petit b" 
sinon
afficher "a est plus grand b" 
finsi 
c <- b * b + 4 * a *c 
afficher c 
fin """