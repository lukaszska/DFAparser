import re

text = '''make the node 57 please
'''
def regex_name_tba(command):
    createNode = re.compile(r'((create|make|add|build|generate|produce)|(delete|destroy|erase|discard|cut out|kill))|'
                            r'(node)|(\'[\w]+\')')

    createAlphabet = re.compile(r'(create|make|build|generate|produce)|'
                                r'(add|remove)|(alphabet)|(from|between)|((\'[\w]+\')\sto\s(\'[\w]+\'))|(\'[\w]+\')')

    createTransition = re.compile(r'((create|make|add|build|generate|produce)|(delete|destroy|erase|discard|cut out|kill))|'
                                r'(transition)|(to\s*(\'[\w]+\'))|(\'[\w]+\')|((if|when)\s(\'[\w]+\'))')

    createAccept = re.compile(r'(accept|reject)|(node)|(all)|(except|other than)|((\'[\w]+\')+)')

    createStart = re.compile(r'(start|begin)|(\'[\w]+\')|(all)|(except|other than)')

    switchFocus = re.compile(r'(switch|change)|(node|alphabet|transition|accept)')
    # might use this so that people don't have to type the same thing repeatedly

    if createNode.finditer(command) != None:
        matches = createNode.finditer(command)
        for match in matches:
            print(match)
            print(match.group(0))
        #make code
    elif createAlphabet.finditer(command) != None:
        matches = createAlphabet.finditer(command)
        for match in matches:
            print(match)
            print(match.group(0))
        #make code
    elif createTransition.finditer(command) != None:
        matches = createTransition.finditer(command)
        for match in matches:
            print(match)
            print(match.group(0))
        #make code
    elif createAccept.finditer(command) != None:
        matches = createAccept.finditer(command)
        for match in matches:
            print(match)
            print(match.group(0))
        #make code
    elif createStart.finditer(command) != None:
        matches = createStart.finditer(command)
        for match in matches:
            print(match)
            print(match.group(0))
        #make code
    elif switchFocus.finditer(command) != None:
        matches = switchFocus.finditer(command)
        for match in matches:
            print(match)
            print(match.group(0))
        #make code


regex_name_tba(text)
"""
if "data.txt" is in same directory, containing entries from a user
to create a file, f= open("englishtocode.txt","w+")
we use f.write("").
How are we storing the data, each line is a command in english or is it paragraph
and we need to parse for periods?

with open('data.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    
    matches = pattern.finditer(contents)
    
    for match in matches:
        print(matches)
            if (match.group(0) == "123"):
                print("hi")
"""