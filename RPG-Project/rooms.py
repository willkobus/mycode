## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'description' : '''The hall is the hub of the house. Centrally located it has direct access the Closet (north), Dining Room (east), Kitchen (south), and the Beat Lab (west)''',
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west' : 'Beat Lab',
                  'north' : 'Closet',
                  'item'  : ['big gun']
                },

            'Kitchen' : {
                  'description' : '''Ah, the Kitchen. Who wants snacks? Not hungry? No Worries. The kitchen has access to the Hall (north), the Basement (west), the Garden (east), and the oh so wonderful Exit (south).''',
                  'north' : 'Hall',
                  'west' : 'Basement',
                  'east' : 'Garden',
                  'south' : 'Exit',
                  'item'  : ['banana'],
                },
            'Dining Room' : {
                'description' : '''Ye olde Dining Room! Home of the dinner table and where fancy parties are held. The Dining Room has access to the Hall (west), the Pantry (north), the Animal Pen (east), and the beautiful Garden (south).''',
                  'west' : 'Hall',
                  'south': 'Garden',
                  'east' : 'Animal Pen',
                  'north' : 'Pantry',
                  'item' : ['rocking chair'],
               },
            'Garden' : {
                  'description' : '''Plants, flowers, and the occasional grue, welcome to the Garden. The Garden has access to the Dining Room (north) and the Kitchen (west).''',
                  'north' : 'Dining Room',
                  'west': "Kitchen",
                  'item' : [],
                  'monster' : ['elmer grue']
               },
            'Pantry' : {
                  'description' : '''The Pantry, AKA where the food lives. Be polite and remove your shoes. The Pantry has access to the Dining Room (south).''',
                  'south' : 'Dining Room',
                  'item' : ['banana'],
            },

            'Beat Lab' : {
                'description' : '''You hear that? The sound of the bass? The rantings of rapper gone mad? This is the Beat Lab. The Beat Lab has access to The Office (north), the Basement (south), and the Hall (east).''',                  
                  'south': 'Basement',
                  'east' : 'Hall',
                  'north' : 'Office',
                                    
            },
            'Office' : {
                'description' : '''There may be no Jim or Pam but its got the \"old book smell\" you all know and love. The Office has access to the Beat Lab (south).''',
                'south' : 'Beat Lab',
                'item' : ['translator']
            },
            'Closet' : {
                'description' : '''It\'s like the Pantry...but for clothes and junk you want to hide before your parents come over. The Closet has access to the Hall (south).''',
                'south' : 'Hall',
                'item' : ['overalls']
            },
            'Animal Pen' : {
                'description' : '''Doesn\'t every house have an animal pen? No? Well this one does. The Animal Pen has access to the Dining Room (west).''',
                'west': 'Dining Room',
                'item' : [],
                'monster' : ['gorilla grue']
            },
            'Exit' : {
                'description' : '''This is where you leave, if the grues don\'t get you first. Need to get those keys though. The Exit has access to the Kitchen (north).''',
                'north' : 'Kitchen'
            },
            'Basement' : {
                'description' : '''The Basement. It\'s cold, dark, and for some reason is where we store the grain seeds. The Basement has access to the Beat Lab (north) and the Kitchen (east).''',
                'north' : 'Beat Lab',
                'east' : 'Kitchen',
                'item' : ['corn seeds']
            }
         }