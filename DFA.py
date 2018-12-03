'''
1. Need to create alphabet
2. Need to be able to create nodes
3. Need to be able to create transitions
4. Need to be able to create accepted states
5. Need to be able to create starting state
'''
node_amnt = int(input('Enter number of nodes: '))
print("First node entered is the starting node")
nodes = [input('Enter node: ') for i in range(0, node_amnt)]
key_amnt = int(input('Enter number of keys: '))
keys = [input('enter key: ') for i in range(0, key_amnt)]
accepted_state_amnt = int(input('Enter number of accepted states: '))
accepted_states = [input('Enter accepted state: ') for i in range(0, accepted_state_amnt)]
transitions = [0 for i in range(len(nodes))]
for i in range(len(nodes)):
    transitions[i] = [0 for j in range(len(keys))]
    for j in range(len(keys)):
        transitions[i][j] = input('from ' + nodes[i] + ' if ' + keys[j] + ' go: ')
def spot(q,w):
    lis.append(transitions[nodes.index(q)][keys.index(w)])
    return transitions[nodes.index(q)][keys.index(w)]
while True:
    meme = False
    lis = []
    start = nodes[0]
    input_String = input('String to check: ')
    for c in input_String:
        start = spot(start, c)
    for i in accepted_states:
        if lis[-1] == i:
            print('String was accepted! ( ' + nodes[0] + '-->' + '-->'.join(lis)+' )')
            meme = True
    if meme == False:
        print('String not accepted.')