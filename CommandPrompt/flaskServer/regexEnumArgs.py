import re

#"Now made so that it's actually comprehensible!"

#text as input string
def get_information(text):
    detect_type = re.compile(
        r'alphabet(?!\')|transition(?!\')|(accept(?!\')|reject(?!\'))|(start(?!\')|begin(?!\'))|node(?!\')')

    create_node = re.compile(
        r'(create|make|add|build|generate|produce)|'
        r'(delete|destroy|erase|discard|cut out|kill)|'
        r'(\'[\w]+\')')

    create_alphabet = re.compile(
        r'(create|make|build|generate|produce)|'
        r'(delete|destroy|erase|discard|cut out|kill)|'
        r'(add|remove)|'
        r'(from|between)|'
        r'(\'[\w]+\'\sto\s\'[\w]+\')|'
        r'(\'[\w]+\')')

    create_transition = re.compile(
        r'(create|make|add|build|generate|produce)|'
        r'(delete|destroy|erase|discard|cut out|kill)|'
        r'(to\s*\'[\w]+\')|'
        r'(if|when\s\'[\w]+\')|'
        r'(\'[\w]+\')')

    create_accept = re.compile(
        r'(accept|reject)'
        r'(all)|'
        r'(except|other than)|'
        r'(\'[\w]+\')+')

    create_start = re.compile(
        r'(\'[\w]+\')|'
        r'(except|other than)')

    collection = None
    thing = []
    if detect_type.search(text).group(0) == "node":
        collection = re.findall(create_node, text)
        thing = ['']*len(collection[0])
        thing[0] = '1'
    if detect_type.search(text).group(0) == "alphabet":
        collection = re.findall(create_alphabet, text)
        thing = [''] * len(collection[0])
        thing[0] = '2'
    if detect_type.search(text).group(0) == "transition":
        collection = re.findall(create_transition, text)
        thing = [''] * len(collection[0])
        thing[0] = '3'
    if detect_type.search(text).group(0) == "accept" or detect_type.search(text).group(0) == "reject":
        collection = re.findall(create_accept, text)
        thing = [''] * len(collection[0])
        thing[0] = '4'
    if detect_type.search(text).group(0) == "start" or detect_type.search(text).group(0) == "begin":
        collection = re.findall(create_start, text)
        thing = [''] * len(collection[0])
        thing[0] = '5'

    for x in collection:
        for i in range(len(x) - 1):
            if x[i] != '':
                thing[i+1] = x[i]

    return tuple(thing)
