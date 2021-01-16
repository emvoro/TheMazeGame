import pygame
import pygame_menu
import game
import time
import json
import score
import operator

pygame.init()
surface = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('The Maze by Emilia Voronova')
# def set_difficulty(value, difficulty):
#    pass

def start_the_game():
    the_app = game.Game()
    start_time = time.time()
    the_app.on_execute()
    game.Game.result_time = (time.time() - start_time).__floor__()
    data = {}
    data['game'] = []
    with open('data.txt') as json_file:
        data = json.load(json_file)
    if the_app.player.isWon:
        id = int(data['game'][len(data['game']) - 1]['id'])
        next_id = id + 1
        points = int(the_app.player.stars * 2 + the_app.player.crystals * 6 + (100 - game.Game.result_time))
        data['game'].append({
            'id': next_id,
            'stars': the_app.player.stars,
            'lives': the_app.player.lives,
            'crystals': the_app.player.crystals,
            'time': game.Game.result_time,
            'points': points
    })
        score.on_execute(the_app.player.stars, the_app.player.crystals, True, points)
    else:
        score.on_execute(the_app.player.stars, the_app.player.crystals, False, 0)
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)


def on_execute():
    menu.mainloop(surface)

menu = pygame_menu.Menu(600, 800, 'Main menu', theme=pygame_menu.themes.THEME_DARK)

# menu.add_text_input('Name : ', default='John Doe')
# menu.add_selector('Level :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add_button('Play', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)

