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
        self.alphabet = []
        self.accepted_states = []
        self.start = None
    
    # Manipulation methods below
    # Adds nodes into the list, if list is empty first node is start
    def add_nodes(self, nodes):
        n_list = list(nodes)
        for node in n_list[1:]:
            self.dfa_dict[node] = self.dfa_dict.get(node, {})

    # Adds starting node
    def add_starting_node(self, nodes):
        n_list = list(nodes)
        self.start = n_list[1]
    
    # Removes the nodes from the list and all transitions to the node
    def remove_nodes(self, nodes):
        n_list = list(nodes)
        for node in n_list[1:]:
            self.dfa_dict.pop(node)
        '''
        NEEDS TO BE DEBUGGED, removes transitions to removed node
        for node in self.dfa_dict:
            for transition in self.dfa_dict:
                for yoink in n_list[1:]:
                    if self.dfa_dict[node][transition] == yoink:
                        self.dfa_dict[node].pop(transition)
        '''
        


    # Updates the inner dict with new transtions
    def add_transitions(self, transitions):
        t_list = list(transitions)
        for i in range(1, len(t_list), 3):
            self.dfa_dict[t_list[i]][t_list[i + 2]] = t_list[i + 1]

    # Removes existing transitions
    def remove_transition(self, transitions):
        t_list = list(transitions)
        for i in range(1, len(t_list), 3):
            self.dfa_dict[t_list[i]].pop(t_list[i + 2])

    # If node already exists, removed. If node does exist, add.
    def set_accepts(self, accepts):
        n_list = list(accepts)
        for i in range(1, len(n_list)):
            if n_list[i] in self.accepted_states:
                self.accepted_states.pop(self.accepted_states.index(n_list[i]))
            else:
                self.accepted_states.append(n_list[i])

    # Create alphabet
    def set_alphabet(self, alph):
        a_list = list(alph)
        for i in range(1, len(a_list)):
            if a_list[i] in self.alphabet:
                self.alphabet.pop(self.alphabet.index(a_list[i]))
            else:
                self.alphabet.append(a_list[i])

    def check_string(self, s):
        current_node = self.start
        for c in s:
            print(current_node)
            print(self.dfa_dict[current_node][c])
            current_node = self.dfa_dict[current_node][c]
        return current_node in self.accepted_states