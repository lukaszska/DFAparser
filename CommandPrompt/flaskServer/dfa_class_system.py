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
        self.dfa_dict['transitions'] = []
        self.dfa_dict['start'] = None
        self.dfa_dict['graph'] = []

    # Manipulation methods below
    # Adds nodes into the list, if list is empty first node is start
    def add_nodes(self, nodes):
        for node in nodes:
            if node in self.dfa_dict['graph']:
                continue
            self.dfa_dict['graph'].append(node)

    # Adds starting node
    def add_starting_node(self, nodes):
        n_list = list(nodes)
        self.dfa_dict['start'] = n_list[1]

    # Removes the nodes from the list and all transitions to the node
    def remove_nodes(self, nodez):
        if len(self.dfa_dict['graph']) == 0:
            return
        for node in nodez:
            if node not in self.dfa_dict['graph']:
                print(node)
                continue
            node_index = self.dfa_dict['graph'].index(node)
            deleted = self.dfa_dict['graph'].pop(node_index)
            transitions = self.dfa_dict['transitions']
            i = 0
            while i < len(transitions):
                if deleted in transitions[i]:
                    self.dfa_dict['transitions'].pop(self.dfa_dict['transitions'].index(transitions[i]))
                    i -= 1
                i += 1


    # Updates the inner dict with new transtions (begin_node, destination_node, edge)
    def add_transitions(self, transitions):
        transition = []
        for i in range(0, len(transitions) - 1):
            if transitions[i] not in self.dfa_dict['graph']:
                continue
            transition.append(transitions[i])
        if len(transition) == 0:
            return
        self.dfa_dict['transitions'].append(transition)

    # Updates the inner dict with new transitions (begin_node, destination_node, edge)
    def remove_transitions(self, transitions):
        transition = []
        for i in range(0, len(transitions) - 1):
            if transitions[i] not in self.dfa_dict['graph']:
                continue
            transition.append(transitions[i])
        if len(transition) == 0 or transition not in self.dfa_dict['transitions']:
            return
        transition_index = self.dfa_dict['transitions'].index(transition)
        self.dfa_dict['transitions'].pop(transition_index)

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
        for c in s:
            current_node = self.dfa_dict['graph'][current_node][c]
        return current_node in self.dfa_dict['accepted_states']

    # Checks tuple and decides what function to run
    def tuple_reader(self, tup):
        if tup is None:
            return
        flag = tup[0]
        # create nodes
        if flag == '1':
            self.add_nodes(tup[1:])
        if flag == '2':
            self.remove_nodes(tup[1:])
        # set alphabet
        elif flag == '3':
            self.add_alphabet(tup[1:])
        elif flag == '4':
            self.remove_alphabet(tup[1:])
        # set transitions
        elif flag == '5':
            if len(tup) == 1:
                return
            self.add_transitions(list(tup).pop(1))
        elif flag == '6':
            if len(tup) == 1:
                return
            self.remove_transitions(list(tup).pop(1))
        # create or remove accepted states
        elif flag == '7':
            self.add_accepts(tup[1:])
        elif flag == '8':
            self.remove_accepts(tup[1:])
        # declare start
        elif flag == '9':
            self.add_starting_node(tup[1:])
        elif flag == '0':
            return self.check_string(tup[1])


#TESTS WITH SIMPLE GRAPH
test_dfa = DFA()
nodes = ('1', 'a', 'b', 'c')
alphy = ('3', '0', '1')
trans = ('5', 'a', 'a', '0', 'a', 'b', '1', 'b', 'a', '0', 'b', 'c', '1', 'c', 'c', '0', 'c', 'c', '1')
accepter = ('7', 'c')
starty = ('9', 'a')

#   print(test_dfa.tuple_reader(('0', '10')))
#   print (test_dfa.dfa_dict['accepted_states'])

#   print('test')
#   print('c' in ['c'])
