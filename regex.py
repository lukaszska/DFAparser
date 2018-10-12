import re

text = '''enter test text here
'''

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

matches = createNode.finditer(text)
#change "createNode" to whatever is being used
for match in matches:
    print(match)
print(match.group(0))

"""
if "data.txt" is in same directory, containing entries from a user

with open('data.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    
    matches = pattern.finditer(contents)
    
    for match in matches:
        print(matches)
            if (match.group(0) == "123"):
                print("hi")
"""