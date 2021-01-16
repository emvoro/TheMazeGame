import pygame as pg
import game


def on_execute(stars, crystals, is_won, points):
    pg.init()
    sc = pg.display.set_mode((1200, 800))
    sc.fill((55, 55, 55))
    time = game.Game.result_time
    score = " Stars : " + str(stars) + " Crystals : " + str(crystals) + " Time : " + str(time)
    result = ""
    if is_won:
        result += "WIN "
        result += score + " Points : " + str(int(points))
    else:
        result += "LOSS "
        result += score + " Points : 0"
    font = pg.font.Font(None, 72)
    text = font.render(result, True, (255, 255, 255))
    place = text.get_rect(center=(580, 250))
    sc.blit(text, place)
    pg.display.update()

    while 1:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                return

        sc.fill((55, 55, 55))
        sc.blit(text, place)

        pg.display.update()
