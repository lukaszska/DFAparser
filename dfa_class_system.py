"""
BUGS TO FIX:
- remove doesn't remove transitions
- remove node crashes for nodes that don't exist
- remove transition crashes for nodes that don't exist
- remove transition needs the transition key and any node to delete, should only need one or the other
- assumes that transitions parameter fits nicely in 3s
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
        for c in s:
            self.start = self.dfa_dict[self.start][c]
        return self.start in self.accepted_states

meme = DFA()
meme.add_nodes(('0', 'a', 'b', 'c'))
print(meme.dfa_dict)
meme.add_transitions(('5', 'a', 'b', '0', 'b', 'c', '0', 'c', 'c', '0', 'a', 'a', '1', 'b', 'a', '1', 'c', 'c', '1'))
print(meme.dfa_dict)
meme.set_alphabet(('yikes', '0', '1'))
print(meme.alphabet)
meme.set_accepts(('0', 'c'))
    
