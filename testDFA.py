# Nodes 'a' through 'e'
# Alphabet of '0', '1', '2'
# '0' is go back, '1' is go forward, '2' is stay
# Starts at 'a'
# Accepts at 'b' and 'd'

# 'DFAmap' is a dictionary, with keys of each node. Each key node then has a value of another dictionary,
# with keys of a potential movement direction and values of where you will end up

# 'accept' and 'alphabet' are tuples of strings which contain each accepting state or alphabet character

DFA_dictionary = {
    'start': 'a',
    'DFAmap': {
        'a': {
            '0': 'e',
            '1': 'b',
            '2': 'a'},
        'b': {
            '0': 'a',
            '1': 'c',
            '2': 'b'
        },
        'c': {
            '0': 'b',
            '1': 'd',
            '2': 'c'
        },
        'd': {
            '0': 'c',
            '1': 'e',
            '2': 'd'
        },
        'e': {
            '0': 'd',
            '1': 'a',
            '2': 'e'
        }
    },
    'accept': ('b', 'd'),
    'alphabet': ('0', '1', '2')
}