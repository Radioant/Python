

import random # 利用内部的radomint函数生成一个随机的整数。

def hangman(word):
    wrong=0
    stages=['',
        '                       ',
        '___________            ',
        '|         |            ',
        '|         |           ',
        '|         O           ',
        '|        /|\          ',
        '|        / \          ',
        '|                      '
        ]
    rletters=list(word)
    board=['_'] * len(word)
    win=False
    print('Welcome to Hangman')
    while wrong < len(stages)-1:
        print('\n')
        msg='Guess a letter: '
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
        else:
            print('You guess wrong!')
            wrong+=1
        print((' '.join(board))
        e=wrong+1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('You win')
            print(' '.join(board))
            win=True
            break

    if not win:
        print('\n'.join(stages[0:wrong]))
        print('You lose ! It was {}.'.format(word))


chr=['Davy','Mary','Carl','Crag','Albert']
n=random.randint(0,4)
hangman(chr[n])
	
