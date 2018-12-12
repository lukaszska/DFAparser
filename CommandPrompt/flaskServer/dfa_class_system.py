class DFA:
    # Create the data structure that will represent the DFA
    def __init__(self):
        self.dfa_dict = {'alphabet': [], 'accepted_states': [], 'transitions': [], 'start': None, 'graph': [],
                         'path': {}, 'result': None}

    # Manipulation methods below
    # Adds nodes into the list, if list is empty first node is start
    def add_nodes(self, nodes):
        for node in nodes:
            if node in self.dfa_dict['graph']:
                continue
            self.dfa_dict['graph'].append(node)
            self.dfa_dict['path'][node] = {}

    # Adds starting node
    def add_starting_node(self, node):
        if node not in self.dfa_dict['graph']:
            return
        self.dfa_dict['start'] = node

    # Removes the nodes from the list and all transitions to the node
    def remove_nodes(self, nodez):
        if len(self.dfa_dict['graph']) == 0:
            return
        for node in nodez:
            if node is self.dfa_dict['start']:
                self.dfa_dict['start'] = None
            if node not in self.dfa_dict['graph']:
                continue
            node_index = self.dfa_dict['graph'].index(node)
            deleted_node = self.dfa_dict['graph'].pop(node_index)
            self.dfa_dict['path'].pop(node, None)
            for path_key in self.dfa_dict['path']:
                if node in self.dfa_dict['path'][path_key]:
                    self.dfa_dict['path'][path_key].pop(self.dfa_dict['path'][path_key][node])
            transitions = self.dfa_dict['transitions']
            i = 0
            while i < len(transitions):
                if deleted_node in transitions[i]:
                    transitions.pop(transitions.index(transitions[i])) # HERE
                    i -= 1
                i += 1

    # Updates the inner dict with new transtions (begin_node, destination_node, edge)
    def add_transitions(self, transitions):
        transition = []
        for i in range(0, len(transitions) - 1):
            if transitions[i] not in self.dfa_dict['graph']:
                continue
            transition.append(transitions[i])
        if len(transition) <= 1\
                or transition in self.dfa_dict['transitions']\
                or transitions[2] in self.dfa_dict['path'][transition[0]]:
            return
        self.dfa_dict['transitions'].append(transition)
        self.dfa_dict['path'][transition[0]].update({transitions[2]: transition[1]})

    # Updates the inner dict with new transitions (begin_node, destination_node, edge)
    def remove_transitions(self, transitions):
        transition = []
        for i in range(0, len(transitions) - 1):
            if transitions[i] not in self.dfa_dict['graph']:
                continue
            transition.append(transitions[i])
        if len(transition) <= 1\
                or transition not in self.dfa_dict['transitions']\
                or transitions[2] not in self.dfa_dict['path'][transition[0]]:
            return
        transition_index = self.dfa_dict['transitions'].index(transition)
        for path_key in self.dfa_dict['path']:
            if transitions[2] in self.dfa_dict['path'][path_key]:
                self.dfa_dict['path'][path_key].pop(self.dfa_dict['path'][path_key][transitions[2]])
                break
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
        for character in alph:
            if character not in self.dfa_dict['alphabet']:
                self.dfa_dict['alphabet'].append(character)

    # remove alphabet
    def remove_alphabet(self, alph):
        for character in alph[0]:
            if character in self.dfa_dict['alphabet']:
                self.dfa_dict['alphabet'].pop(self.dfa_dict['alphabet'].index(character))

    # Runs through the graph and checks if the string is accepted
    def check_string(self, s):
        if self.dfa_dict['start'] is None \
                or len(self.dfa_dict['graph']) == 0 \
                or len(self.dfa_dict['path']) == 0 \
                or len(self.dfa_dict['alphabet']) == 0 \
                or len(s) == 0:
            return None
        current = self.dfa_dict['start']
        path = self.dfa_dict['path']
        alphabet = self.dfa_dict['alphabet']
        for character in s:
            if character in alphabet:
                current = path[current][character]
            else:
                current = None
                break
        self.dfa_dict['result'] = current

    #   Checks tuple and decides what function to run
    def tuple_reader(self, tup):
        if tup is None or len(tup) == 1:
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
            self.add_transitions(list(tup).pop(1))
        elif flag == '6':
            self.remove_transitions(list(tup).pop(1))
        # create or remove accepted states
        elif flag == '7':
            self.add_accepts(tup[1:])
        elif flag == '8':
            self.remove_accepts(tup[1:])
        # declare start
        elif flag == '9':
            self.add_starting_node(list(tup).pop())
        elif flag == '0':
            return self.check_string(tup[1:])

