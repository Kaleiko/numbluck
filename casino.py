from games import Color
from games.roulette import Roulette


class Casino():
    all_games = ['ROULETTE']


def play(game_name):
    game_name.single_play()

input('WELCOME TO OUR CASINO, WHERE WE SHOW YOU THAT NO MATTER HOW HARD YOU TRY OR BET, '\
      'THE CASINO STILL \n STACKS THE ODDS IN THEIR FAVOR AND CANNOT BE BEATEN! BUT WHY NOT TRY FOR YOURSELF? \n'\
      'Please press Enter to continue..')   

user_pick_game = input('HERE ARE THE GAMES YOU CAN PLAY: \n'\
      'Roulette \n'\
      'Craps \n'\
      'BlackJack \n'\
      'Which game would you like to play? \n')

try:
    play(eval(user_pick_game))
except KeyError:
    print('Game not found')
