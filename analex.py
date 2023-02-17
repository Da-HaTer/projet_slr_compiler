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
        elif text[i] in '<->=!':
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
        else:
            raise Exception('{} is undefined'.format(text[i]))
    return tokens

def analysis(longstr):
    output=lex(longstr)
    output=[i[0].lower() for i in output]
    return (' '.join(output))