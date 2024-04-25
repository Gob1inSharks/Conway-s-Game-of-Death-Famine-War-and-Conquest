import pygame
import sys

from scripts.conway import DeathBoard
from scripts.conway import generateBoard

from scripts.utils import load_image

class Game:
        
    def __init__(self):

        pygame.init() 

        pygame.display.set_caption("Conway's Game of Death, Famine, War, and Conquest") 

        self.screen = pygame.display.set_mode()
        self.display = pygame.Surface((320,180)) 

        self.clock = pygame.time.Clock()
        self.TARGETED_FPS = 1

        self.width = 30
        self.height = 30

        self.assets = {
            "X":load_image('blue.png'),
            "O":load_image('red.png'),
            'select':load_image('purple.png')
        }

        self.blink_speed = 20

    def render_board(self,board):

        self.display.fill((0,0,0))

        for x in range(self.width):
            for y in range(self.height):

                if board[x][y][0]:

                    self.display.blit(self.assets[board[x][y][1]], (x*6+70,y*6))

        self.screen.blit(pygame.transform.scale(self.display,self.screen.get_size()), (0,0)) 

        pygame.display.update()

    def render_board_menu(self,board,current_cell):

        self.display.fill((0,0,0))

        for x in range(self.width):
            for y in range(self.height):

                if board[x][y][0]:

                    self.display.blit(self.assets[board[x][y][1]], (x*6+70,y*6))

        self.display.blit(self.assets['select'],(current_cell[0]*6+70,current_cell[1]*6))

        self.screen.blit(pygame.transform.scale(self.display,self.screen.get_size()), (0,0)) 

        pygame.display.update()

    def match(self,board):

        self.TARGETED_FPS = 1.5

        board = DeathBoard(board = board,width=self.width,height=self.height)

        no_loop = False

        while not no_loop: 

            for event in pygame.event.get(): 

                if event.type == pygame.QUIT: 

                    pygame.quit() 
                    sys.exit() 

            dt = self.clock.tick(self.TARGETED_FPS) * .001 * self.TARGETED_FPS 

            self.render_board(board.board)
        
            board.next_generation()

            #print() #for debugging

    def selection(self,total_turns):

        self.TARGETED_FPS = 60

        board = generateBoard(self.width,self.height)

        current_cell = [15,15] #using a list for better performance in changing values
        put_cell_down = False
        current_player = 'X'

        turns_played = 0

        flag = True
        flag_counter = 0

        timer = 0

        while True:

            for event in pygame.event.get(): 

                if event.type == pygame.QUIT: 

                    pygame.quit() 
                    sys.exit() 

                if event.type == pygame.KEYDOWN: 

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s: 
                        if current_cell[1] < self.height-1 : current_cell[1] += 1

                    if event.key == pygame.K_UP or event.key == pygame.K_w: 
                        if current_cell[1] > 0 : current_cell[1] -= 1

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                        if current_cell[0] < self.width-1 : current_cell[0] += 1

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a: 
                        if current_cell[0] > 0 : current_cell[0] -= 1

                    if event.key == pygame.K_RETURN:
                        put_cell_down = True

                if event.type == pygame.KEYUP: 

                    if event.key == pygame.K_RETURN:
                        put_cell_down = False

            if flag:
                self.render_board(board)
                flag_counter += 1
                if flag_counter == self.blink_speed:
                    flag = False
                    flag_counter = 0
            else:
                self.render_board_menu(board,current_cell) 
                flag_counter += 1
                if flag_counter == self.blink_speed:
                    flag = True
                    flag_counter = 0

            if put_cell_down and timer > 30:

                if not board[current_cell[0]][current_cell[1]][0]: #this statement prevents players overriding cells

                    board[current_cell[0]][current_cell[1]] = ['True',current_player,0]
                    turns_played += .5

                    if current_player == 'X':
                        current_player = 'O'
                    else:
                        current_player = 'X'

                    timer = 0

            if turns_played >= total_turns:
                break

            dt = self.clock.tick(self.TARGETED_FPS) * .001 * self.TARGETED_FPS 
            timer += dt

            print(current_cell)
              

        self.match(board)

    def test(self):

        board = generateBoard(30,30)
        board[15][14] = [True,'X',0]
        board[15][15] = [True,'O',0]
        board[15][16] = [True,'X',0]
        
        self.match(board)