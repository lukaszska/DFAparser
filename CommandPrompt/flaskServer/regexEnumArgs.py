import re


'''
Takes user input and turns it into a tuple which the DFA machine can use to interact with.
@var text as user's input String to take data from
@return tuple of variable size according to the action taken by the user, with first element as ENUM for class of action
'''


def get_information(text):
    if len(text) == 0 or text is None:
        return None

    detect_type = re.compile(
        r'alphabet(?!\')|transition(?!\')|(accept(?!\')|reject(?!\'))|'
        r'(start(?!\')|begin(?!\'))|node(?!\')|(run(?!\')|execute(?!\'))')

    add = re.compile(r'(create|make|build|generate|produce|add|)')

    remove = re.compile(r'(delete|destroy|erase|discard|cut out|kill|remove|)')

    create_node = re.compile(
        r'node ([\S]+)'
    )

    create_alphabet = re.compile(
        r'alphabet ([\S]+)'
    )

    create_transition = re.compile(
        r'transition ([\S]+) to ([\S]+) if ([\S]+)'
    )

    create_accept = re.compile(
        r'(accept|reject)'
        r'(all)|'
        r'(except|other than)|'
        r'(\'[\w]+\')+'
    )

    create_start = re.compile(
        r'start at node ([\S]+)'
    )

    run_machine = re.compile(
        r'([\w]+)'
    )

    if detect_type.search(text) is None:
        return None

    collection = None
    collection_list = []

    if detect_type.search(text).group() == "node":
        collection = re.findall(create_node, text)
        if len(add.search(text).group()) > 0:
            collection_list.append('1')
        elif len(remove.search(text).group()) > 0:
            collection_list.append('2')
    elif detect_type.search(text).group() == "alphabet":
        collection = re.findall(create_alphabet, text)
        if len(add.search(text).group()) > 0:
            collection_list.append('3')
        elif len(remove.search(text).group()) > 0:
            collection_list.append('4')
    elif detect_type.search(text).group() == "transition":
        collection = re.findall(create_transition, text)
        if len(add.search(text).group()) > 0:
            collection_list.append('5')
        elif len(remove.search(text).group()) > 0:
            collection_list.append('6')
    elif detect_type.search(text).group() == "accept":
        collection = re.findall(create_accept, text)
        collection_list = [''] * (len(collection[0]) + 1)
        collection_list[0] = '7'
    elif detect_type.search(text).group() == "reject":
        collection = re.findall(create_accept, text)
        collection_list = [''] * (len(collection[0]) + 1)
        collection_list[0] = '8'
    elif detect_type.search(text).group() == "start" or detect_type.search(text).group(0) == "begin":
        collection = re.findall(create_start, text)
        collection_list.append('9')
    elif detect_type.search(text).group() == "run" or detect_type.search(text).group(0) == "execute":
        collection = re.findall(run_machine, text)
        collection_list = ['0', collection[1]]
        return tuple(collection_list)

    if collection is None or len(collection_list) == 0:
        return None
    for element in collection:
        collection_list.append(element)
    print(collection_list)
    return tuple(collection_list)
