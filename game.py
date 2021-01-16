from pygame.locals import *
import pygame
import player
import maze
import time
from random import randint


class Game:
    windowWidth = 1200
    windowHeight = 800
    result_time = time.time()

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._player_surf = None
        self._block_surf = None
        self._door_surf = None
        self._key_surf = None
        self._exit_surf = None
        self._star_surf = None
        self._bomb_surf = None
        self._shield_surf = None
        self._crystal_surf = None
        self._potion_surf = None
        self._life_surf = None
        self.player = player.Player()
        self.maze = maze.Maze()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('The Maze by Emilia Voronova')
        self._running = True
        self._player_surf = pygame.image.load("img/player2.png").convert()
        self._block_surf = pygame.image.load("img/block.png").convert()
        self._door_surf = pygame.image.load("img/door.png").convert()
        self._key_surf = pygame.image.load("img/key.png").convert()
        self._exit_surf = pygame.image.load("img/exit.png").convert()
        self._star_surf = pygame.image.load("img/star.png").convert()
        self._bomb_surf = pygame.image.load("img/bomb.png").convert()
        self._shield_surf = pygame.image.load("img/shield.png").convert()
        self._crystal_surf = pygame.image.load("img/crystal.png").convert()
        self._potion_surf = pygame.image.load("img/potion5.png").convert()
        self._life_surf = pygame.image.load("img/life.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        sc = pygame.display.set_mode((1200, 800))
        self._display_surf.fill((0, 0, 0))
        self.maze.draw(self._display_surf, self._block_surf, self._door_surf, self._key_surf, self._exit_surf, self._star_surf, self._bomb_surf, self._shield_surf, self._crystal_surf, self._potion_surf, self._life_surf)
        self._display_surf.blit(self._player_surf, (self.player.x, self.player.y))
        font = pygame.font.Font(None, 36)
        text1 = font.render("Lives : " + str(self.player.lives), True, (255, 255, 255))
        place1 = text1.get_rect(center=(930, 40))
        sc.blit(text1, place1)
        text2 = font.render("Shields : " + str(self.player.shields), True, (255, 255, 255))
        place2 = text2.get_rect(center=(930, 90))
        sc.blit(text2, place2)
        text3 = font.render("Crystals : " + str(self.player.crystals), True,(255, 255, 255))
        place3 = text3.get_rect(center=(930, 140))
        sc.blit(text3, place3)
        text4 = font.render("Time : " + str((time.time() - self.result_time).__floor__()), True, (255, 255, 255))
        place4 = text4.get_rect(center=(930, 190))
        sc.blit(text4, place4)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    zeros_indexes = []

    def rand_bomb(self):
        for x_index in range(0, len(self.maze.maze) - 1):
            if self.maze.maze[x_index] == 0:
                self.zeros_indexes.append(x_index)
        random_number = randint(0, len(self.zeros_indexes) - 1)
        return random_number

    bomb = 0

    def on_execute(self):
        ind = -1
        if self.on_init() == False:
            self._running = False

        while self._running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[K_RIGHT]:
                ind = self.player.move_right()

            if keys[K_LEFT]:
                ind = self.player.move_left()

            if keys[K_UP]:
                ind = self.player.move_up()

            if keys[K_DOWN]:
                ind = self.player.move_down()

            if keys[K_ESCAPE]:
                self._running = False

            if (time.time() - self.result_time).__floor__() % 40 == 0 and (time.time() - self.result_time).__floor__() != 0:
                self.maze.maze[17] = 9

            if (time.time() - self.result_time).__floor__() == 20:
                self.maze.maze[241] = 'C'

            if (time.time() - self.result_time).__floor__() % 55 == 0:
                while self.bomb == 0:
                    self.maze.maze[self.zeros_indexes[self.rand_bomb()]] = 5
                    self.bomb = 1

            if type(self.maze.maze[ind]) is not int and not str(self.maze.maze[ind]).isupper():
                self.player.key = self.maze.maze[ind]
                self.maze.maze[ind] = 0
            elif self.maze.maze[ind] == 4:
                self.player.stars += 1
                self.maze.maze[ind] = 0
            elif self.maze.maze[ind] == 5:
                if self.player.shields > 0:
                    self.player.shields -= 1
                else:
                    self.player.lives -= 1
                self.maze.maze[ind] = 0
                if self.player.lives < 1:
                    self.player.game_over = True
            elif self.maze.maze[ind] == 6:
                self.player.shields += 1
                self.maze.maze[ind] = 0
            elif self.maze.maze[ind] == 7:
                self.player.crystals += 1
                self.maze.maze[ind] = 0
            elif self.maze.maze[ind] == 8:
                self.player.delta *= 3
                self.maze.maze[ind] = 0
            elif self.maze.maze[ind] == 9:
                self.player.lives += 1
                self.maze.maze[ind] = 0
            elif self.maze.maze[ind] == -1:
                if self.player.crystals > 1:
                    self.player.isWon = True
                self.player.game_over = True

            if self.player.key is not None:
                search = self.maze.maze.index(self.player.key.upper(), 0, len(self.maze.maze) - 1)
                if self.maze.maze.__contains__(self.maze.maze[search]):
                    if self.maze.maze[search] == 'C':
                        self.maze.maze[search] = -1
                    else:
                        self.maze.maze[search] = 4
                    self.player.key = None

            if self.player.game_over:
                return

            self.on_render()

        self.on_cleanup()
