import random

print('Can you beat me at rock paper scissors?')

loop = 0
while loop < 10:
        user = input('Choose your weapon(rock(R), paper(P) or scissors(S)): ')
        print(f'You chose {user}')
        choices = ['R', 'P', 'S']
        my_choice = random.choice(choices)
        print(f'I chose {my_choice}')

        if user == my_choice:
                print('scoreless, try again')

        if (user == 'R' and my_choice == 'S') or (user == 'S' and my_choice == 'P') or (user == 'P' and my_choice == 'R'):
                print('You win, brother!')

        if (user =='R' and my_choice == 'P') or (user == 'S' and my_choice == 'R') or (user == 'P' and my_choice == 'S'):
                print('I win, loseeer')
        loop = loop + 1
        print('Do you want to play again?')


