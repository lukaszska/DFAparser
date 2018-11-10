dfa_1 = {
    'map' : {
        'a' : {
            '0' : 'b',
            '1' : 'a'
        },
        'b' : {
            '0' : 'c',
            '1' : 'a'
        },
        'c' : {
            '0' : 'c',
            '1' : 'c'
        }
    },
    'start_node' : 'a',
    'accepted_nodes' : ['c'],
    'alphabet' : ['0', '1'],
}

dfa_2 = {
    'map' : {
        'q0' : {
            'a' : 'q1',
            'b' : 'q2'
        },
        'q1' : {
            'a' : 'q3',
            'b' : 'q4'
        },
        'q2' : {
            'a' : 'q1',
            'b' : 'q2'
        },
        'q3' : {
            'a' : 'q1',
            'b' : 'q3'
        },
        'q4' : {
            'a' : 'q5',
            'b' : 'q4'
        },
        'q5' : {
            'a' : 'q5',
            'b' : 'q5'
        }
    },
    'start_node' : 'q0',
    'accepted_nodes' : ['q3', 'q5'],
    'alphabet' : ['a', 'b'],
}
dfa_3 = {
    'map' : {
        'ISR' : {
            'walk' : 'LAR',
            'bus' : 'IKE'
        },
        'LAR' : {
            'walk' : 'PAR',
            'bus' : 'FAR'
        },
        'FAR' : {
            'walk' : 'ISR',
            'bus' : 'PAR'
        },
        'PAR' : {
            'walk' : 'IKE',
            'bus' : 'ISR'
        },
        'IKE' : {
            'walk' : 'FAR',
            'bus' : 'LAR'
        }
    },
    'start_node' : 'PAR',
    'accepted_nodes' : ['ISR', 'IKE'],
    'alphabet' : ['walk', 'bus'],
} 