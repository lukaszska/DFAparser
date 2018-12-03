"""
BUGS TO FIX:
- remove doesn't remove transitions
- remove node crashes for nodes that don't exist
- remove transition crashes for nodes that don't exist
- remove transition needs the transition key and any node to delete, should only need one or the other
- assumes that transitions parameter fits nicely in 3s
- doesn't check if key is in alphabet
- assumes every node has a transition for each letter in alphabet and no dead ends

GOALS:
- get it to use the regex script
- combind add/remove methods into one method, or make separate function that decides which to call
- function needs to read beginning flag of tuple and call appropriate function
- clean tuple in flag reading function, and send a list to DFA creation methods
- change script to store all vars in dict
"""
class DFA:
    # Create the data structure that will represent the DFA
    def __init__(self):
        self.dfa_dict = {}
        self.dfa_dict['alphabet'] = []
        self.dfa_dict['accepted_states'] = []
        self.dfa_dict['start'] = None
        self.dfa_dict['graph'] = {}
    
    # Manipulation methods below
    # Adds nodes into the list, if list is empty first node is start
    def add_nodes(self, nodes):
        n_list = list(nodes)
        for node in n_list[1:]:
            self.dfa_dict['graph'][node] = self.dfa_dict.get(node, {})

    # Adds starting node
    def add_starting_node(self, nodes):
        n_list = list(nodes)
        self.dfa_dict['start'] = n_list[1]
    
    # Removes the nodes from the list and all transitions to the node
    def remove_nodes(self, nodes):
        n_list = list(nodes)
        for node in n_list[1:]:
            self.dfa_dict['graph'].pop(node)

    # Updates the inner dict with new transtions (begin_node, destination_node, edge)
    def set_transitions(self, transitions):
        t_list = list(transitions)
        for i in range(1, len(t_list), 3):
            if t_list[i + 2] in self.dfa_dict['graph'][t_list[i]]:
                self.dfa_dict['graph'][t_list[i]].pop(t_list[i + 2])
            else:
                self.dfa_dict['graph'][t_list[i]][t_list[i + 2]] = t_list[i + 1]

    # If node already exists, removed. If node does exist, add.
    def set_accepts(self, accepts):
        n_list = list(accepts)
        for i in range(1, len(n_list)):
            if n_list[i] in self.dfa_dict['accepted_states']:
                self.dfa_dict['accepted_states'].pop(self.dfa_dict['accepted_states'].index(n_list[i]))
            else:
                self.dfa_dict['accepted_states'].append(n_list[i])

    # Create alphabet
    def set_alphabet(self, alph):
        a_list = list(alph)
        for i in range(1, len(a_list)):
            if a_list[i] in self.dfa_dict['alphabet']:
                self.dfa_dict['alphabet'].pop(self.dfa_dict['alphabet'].index(a_list[i]))
            else:
                self.dfa_dict['alphabet'].append(a_list[i])

    # Runs through the graph and checks if the string is accepted
    def check_string(self, s):
        current_node = self.dfa_dict['start']
        print(current_node)
        for c in s:
            print(self.dfa_dict['graph'][current_node][c])
            current_node = self.dfa_dict['graph'][current_node][c]
        return current_node in self.dfa_dict['accepted_states']

    # Checks tuple and decides what function to run
    def tuple_reader(self, tup):
        flag = tup[0]
        # create or remove node
        if flag == '1':
            if tup[1] in self.dfa_dict['graph']:
                self.remove_nodes(tup)
            else:
                self.add_nodes(tup)
        # set alphabet
        elif flag == '2':
            self.set_alphabet(tup)
        # set transitions
        elif flag == '3':
            self.set_transitions(tup)
        # create or remove accepted states
        elif flag == '4':
            self.set_accepts(tup)
        # declare start
        elif flag == '5':
            self.add_starting_node(tup)

'''
TESTS WITH SIMPLE GRAPH
test_dfa = DFA()
nodes = ('1', 'a', 'b', 'c')
alphy = ('2', '0', '1')
trans = ('3', 'a', 'a', '0', 'a', 'b', '1', 'b', 'a', '0', 'b', 'c', '1', 'c', 'c', '0', 'c', 'c', '1')
accepter = ('4', 'c')
starty = ('5', 'a')

test_dfa.tuple_reader(nodes)
test_dfa.tuple_reader(alphy)
test_dfa.tuple_reader(trans)
test_dfa.tuple_reader(accepter)
test_dfa.tuple_reader(starty)
print(test_dfa.check_string('10101011'))
'''
