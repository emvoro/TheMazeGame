from pygame.locals import *
import pygame
import player
import maze


class Game:
    windowWidth = 1200
    windowHeight = 800
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._player_surf = None
        self._block_surf = None
        self._door_surf = None
        self._key_surf = None
        self.player = player.Player()
        self.maze = maze.Maze()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._player_surf = pygame.image.load("player.png").convert()
        self._block_surf = pygame.image.load("block.png").convert()
        self._door_surf = pygame.image.load("door.png").convert()
        self._key_surf = pygame.image.load("key.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self.maze.draw(self._display_surf, self._block_surf, self._door_surf, self._key_surf)
        self._display_surf.blit(self._player_surf, (self.player.x, self.player.y))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit();  # sys.exit() if sys is imported
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.player.move_right()
                    if event.key == pygame.K_LEFT:
                        self.player.move_left()
                    if event.key == pygame.K_UP:
                        self.player.move_up()
                    if event.key == pygame.K_DOWN:
                        self.player.move_down()
            """
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[K_RIGHT]:
                # print("->")
                self.player.move_right()

            if keys[K_LEFT]:
                # print("<-")
                self.player.move_left()

            if keys[K_UP]:
                # print("^")
                self.player.move_up()

            if keys[K_DOWN]:
                # print("v")
                self.player.move_down()

            if keys[K_ESCAPE]:
                self._running = False

            # self.on_loop()
            self.on_render()

        self.on_cleanup()
