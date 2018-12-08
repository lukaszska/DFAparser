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
    def add_transitions(self, transitions):
        t_list = list(transitions)
        for i in range(1, len(t_list), 3):
            self.dfa_dict['graph'][t_list[i]][t_list[i + 2]] = t_list[i + 1]

    # Updates the inner dict with new transtions (begin_node, destination_node, edge)
    def remove_transitions(self, transitions):
        t_list = list(transitions)
        for i in range(1, len(t_list), 3):
            self.dfa_dict['graph'][t_list[i]].pop(t_list[i + 2])

    # If node already exists, removed. If node does exist, add.
    def add_accepts(self, accepts):
        n_list = list(accepts)
        for i in range(1, len(n_list)):
            if n_list[i] in self.dfa_dict['accepted_states']:
                self.dfa_dict['accepted_states'].pop(self.dfa_dict['accepted_states'].index(n_list[i]))
            else:
                self.dfa_dict['accepted_states'].append(n_list[i])

    # If node already exists, removed. If node does exist, add.
    def remove_accepts(self, accepts):
        n_list = list(accepts)
        for i in range(1, len(n_list)):
            self.dfa_dict['accepted_states'].pop(self.dfa_dict['accepted_states'].index(n_list[i]))           

    # Create alphabet
    def add_alphabet(self, alph):
        a_list = list(alph)
        for i in range(1, len(a_list)):
            self.dfa_dict['alphabet'].append(a_list[i])
    
    # remove alphabet
    def remove_alphabet(self, alph):
        a_list = list(alph)
        for i in range(1, len(a_list)):
            self.dfa_dict['alphabet'].pop(self.dfa_dict['alphabet'].index(a_list[i]))

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
        # create nodes
        if flag == '1':
            self.add_nodes(tup)
        if flag == '2':
            self.remove_nodes(tup)
        # set alphabet
        elif flag == '3':
            self.add_alphabet(tup)
        elif flag == '4':
            self.remove_alphabet(tup)
        # set transitions
        elif flag == '5':
            self.add_transitions(tup)
        elif flag == '6':
            self.remove_transitions(tup)
        # create or remove accepted states
        elif flag == '7':
            self.add_accepts(tup)
        elif flag == '8':
            self.remove_accepts(tup)
        # declare start
        elif flag == '9':
            self.add_starting_node(tup)
        elif flag == '0':
            return self.check_string(tup[1])


#TESTS WITH SIMPLE GRAPH
test_dfa = DFA()
nodes = ('1', 'a', 'b', 'c')
alphy = ('3', '0', '1')
trans = ('5', 'a', 'a', '0', 'a', 'b', '1', 'b', 'a', '0', 'b', 'c', '1', 'c', 'c', '0', 'c', 'c', '1')
accepter = ('7', 'c')
starty = ('9', 'a')

test_dfa.tuple_reader(nodes)
test_dfa.tuple_reader(alphy)
test_dfa.tuple_reader(trans)
test_dfa.tuple_reader(accepter)
test_dfa.tuple_reader(starty)
print(test_dfa.tuple_reader(('0', '10')))
print (test_dfa.dfa_dict['accepted_states'])

print('test')
print('c' in ['c'])