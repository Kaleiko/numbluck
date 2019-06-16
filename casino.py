from roulette import Roulette

from enums import Game, Color


class Casino():
    all_games = ['ROULETTE']


def play(game_name):
    game_name.single_play()

print('WELCOME TO OUR CASINO, WHERE WE SHOW YOU THAT NO MATTER HOW HARD YOU TRY OR BET, THE CASINO STILL ', 
      'STACKS THE ODDS IN THEIR FAVOR AND CANNOT BE BEATEN! BUT WHY NOT TRY FOR YOURSELF? \n')   

print('HERE ARE THE GAMES YOU CAN PLAY: \n')
print([game.value for game in Game], '\n')
user_pick_game = input('WHICH GAME WOULD YOU LIKE TO PLAY? \n')
try:
    eval(Game[user_pick_game])
    print('Success')
    play(eval(user_pick_game))
except KeyError:
    print('Game not found')
