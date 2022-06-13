import random

while True:
    options = ['R', 'P', 'S']
    computer = random.choice(options)
    user = input('pick between R,P,S :')
    player = user.upper()
    print(f'''Player:{player} 
Computer:{computer}
        ''')
    if player == computer:
        print('its a tie')
        continue
    elif player == 'R':
        if computer == 'P':
            print('you lose')
        elif computer == 'S':
            print('you win!')
    elif player == 'P':
        if computer == 'S':
            print('you lose')
        elif computer == 'R':
            print('you win!')
    elif player == 'S':
        if computer == 'R':
            print('you lose')
        elif computer == 'p':
            print('you win')
    play_again = input('Do you wish to play again? y/n:')
    if play_again.lower() != 'y':
        print('Thanks for playing')
        break

