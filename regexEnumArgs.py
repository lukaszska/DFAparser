import re


'''
Takes user input and turns it into a tuple which the DFA machine can use to interact with.
@var text as user's input String to take data from
@return tuple of variable size according to the action taken by the user, with first element as ENUM for class of action
'''


def get_information(text):
    detect_type = re.compile(
        r'alphabet(?!\')|transition(?!\')|(accept(?!\')|reject(?!\'))|'
        r'(start(?!\')|begin(?!\'))|node(?!\')|(run(?!\')|execute(?!\'))'
    )

    add_remove = re.compile(
        r'(create|make|build|generate|produce)|'
        r'(delete|destroy|erase|discard|cut out|kill)|'
    )

    create_node = re.compile(
        r'(\'[\w]+\')'
    )

    create_alphabet = re.compile(
        r'(add|remove)|'
        r'(from|between)|'
        r'(\'[\w]+\'\sto\s\'[\w]+\')|'
        r'(\'[\w]+\')'
    )

    create_transition = re.compile(
        r'(\'[\w]+\')|'
        r'(to\s*\'[\w]+\')|'
        r'(if|when\s\'[\w]+\')|'
    )

    create_accept = re.compile(
        r'(accept|reject)'
        r'(all)|'
        r'(except|other than)|'
        r'(\'[\w]+\')+'
    )

    create_start = re.compile(
        r'(\'[\w]+\')|'
        r'(except|other than)'
    )

    run_machine = re.compile(
        r'([\w]+)'
    )

    collection = None
    collection_list = []
    if detect_type.search(text).group(0) == "node":
        collection = re.findall(create_node, text)
        collection_list = [''] * (len(collection[0]) + 1)
        if add_remove.search(text).group(1) is not None:
            collection_list[0] = '1'
        else:
            collection_list[0] = '2'
    if detect_type.search(text).group(0) == "alphabet":
        collection = re.findall(create_alphabet, text)
        collection_list = [''] * (len(collection[0]) + 1)
        if add_remove.search(text).group(1) is not None:
            collection_list[0] = '3'
        else:
            collection_list[0] = '4'
    if detect_type.search(text).group(0) == "transition":
        collection = re.findall(create_transition, text)
        collection_list = [''] * (len(collection[0]) + 1)
        if add_remove.search(text).group(1) is not None:
            collection_list[0] = '5'
        else:
            collection_list[0] = '6'
    if detect_type.search(text).group(0) == "accept":
        collection = re.findall(create_accept, text)
        collection_list = [''] * (len(collection[0]) + 1)
        collection_list[0] = '7'
    if detect_type.search(text).group(0) == "reject":
        collection = re.findall(create_accept, text)
        collection_list = [''] * (len(collection[0]) + 1)
        collection_list[0] = '8'
    if detect_type.search(text).group(0) == "start" or detect_type.search(text).group(0) == "begin":
        collection = re.findall(create_start, text)
        collection_list = [''] * (len(collection[0]) + 1)
        collection_list[0] = '9'
    if detect_type.search(text).group(0) == "run" or detect_type.search(text).group(0) == "execute":
        collection = re.findall(run_machine, text)
        collection_list = ['0', collection[1]]
        return tuple(collection_list)

    if collection is None:
        return None

    for x in collection:
        for i in range(len(x)):
            if x[i] != '':
                collection_list[i+1] = x[i]
    return tuple(collection_list)
