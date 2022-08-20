import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
        |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
    |   |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
   /|   |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
   /|\  |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
        ==========''','''

    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
        ==========''','''
''']

WORDS = [ 
    'lavadora',
    'secadora',
    'sofa',
    'computadora',
    'teclado',
    'celular',
    'guitarra'
]

def random_word():
    indice = random.randint(0,len(WORDS) - 1)
    return WORDS[indice]


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- *')



def  run(): 
    word = random_word()
    print(word)
    hidden_word = ['_'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = input('Escribe una letra: ')

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries+=1;

            if tries == len(IMAGES) -1:
                print('PERDISTE! La palabra era {}'.format(word))
                break;
        else:
            for inx in letter_indexes:
                hidden_word[inx] = current_letter

            letter_indexes = []

        try:
            hidden_word.index('_')  #Si se usa index o indexof python regresa un error por eso usamos try
        except ValueError: 
            print('')
            print('Ganaste!!')
            break


if __name__ == '__main__':
    print("Bienvenidos a Ahorcado")
    run()