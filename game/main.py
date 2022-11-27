import random
from ssl import Options

def choose_options():
    Options = ('piedra', 'papel', 'tijera')
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    if not user_option in Options:
        print('La opcion no es valida')
        #continue
        return None, None
    
    computer_option = random.choice(Options) #el ordenador selecciona aleatoriamente con metodo random

    print('User option => ', user_option)
    print('computer_option => ', computer_option)
    return user_option, computer_option   

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('¡Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('¡User Gano!')
            user_wins += 1
        else:
            print('papel gana a piedra')
            print('computer gano')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('User Gana')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('Computer gano')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('User Gana!')
            user_wins += 1
        else:
            print('Piedra gana a tijera')
            print('Computer Gana!')
            computer_wins += 1
    return user_wins, computer_wins

def run_game():
    rounds = 1
    computer_wins = 0
    user_wins = 0
    while True:

        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        print('computer_wins', computer_wins)
        print('user_wins', user_wins)
        rounds += 1 

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, 
        computer_option, user_wins, computer_wins)
        check_winner(user_wins, computer_wins)

def check_winner(user_wins, computer_wins):

    print(f'''
    🤖 Computer wins: {computer_wins}
    🙋 user wins: {user_wins}''')
    print('')
    
    if user_wins == 3:
        print('El ganador de la partida es user')
        exit()
    
    if computer_wins == 3:
        print('El ganador de la partida es el ordenador')
        exit()

run_game()