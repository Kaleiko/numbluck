#from games import Color
from games.roulette import Roulette


class Casino():
    all_games = ['ROULETTE', 'CRAPS', 'BLACKJACK']


def play(game_name):
    game_name.single_play()

input('WELCOME TO OUR CASINO, WHERE WE SHOW YOU THAT NO MATTER HOW HARD YOU TRY OR BET, '\
      'THE CASINO STILL STACKS THE ODDS IN THEIR FAVOR AND CANNOT BE BEATEN! BUT WHY NOT TRY FOR YOURSELF? \n'\
      'Please press ENTER to continue..')   

print('\nHERE ARE THE GAMES YOU CAN PLAY: \n')
for eeach_game in Casino.all_games:
    print(eeach_game.title())

user_pick_game = input('\nWhich game would you like to play? \n')

try:
        play(eval(user_pick_game.title()))
except:
    print('Game not found')


