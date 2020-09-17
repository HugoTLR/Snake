import sys
import math
import random

class Board:
  cell = {  0 : {"typ":"EMPTY","rpr":' '}, \
            1 : {"typ":"WALL","rpr":'X'}, \
            2 : {"typ":"BODY","rpr":'.'}, \
            3 : {"typ":"HEAD","rpr":'*'}, \
            4 : {"typ":"FOOD","rpr":'o'}, \
            5 : {"typ":"DEAD","rpr":'W'}}

  def __str__(self):
    ret = ""
    for row in self.board:
      ret = ret + ''.join([Board.cell[c]['rpr'] for c in row]) + '\n'
    return ret

  def __init__(self,width,height):
    self.W = width
    self.H = height
    self.board = [[1 if self.is_border(j,i) else 0 for i in range(self.W)] for j in range(self.H)]
    self.snake = Snake(self)

    self.food = self.generate_food()
    self.done = False #Is the game done ? snake dead or perfect snake
    self.update()

  def is_border(self,j,i): return j == 0 or j == self.H - 1 or i == 0 or i == self.W -1

  def update(self):
    for j in range(1, self.H - 1, 1):
      for i in range(1, self.W - 1, 1):
        if (j,i) in self.snake.body:
          if (j,i) == self.snake.body[0]:   self.board[j][i] = 3
          else:                             self.board[j][i] = 2
        elif (j,i) == self.food:            self.board[j][i] = 4
        elif (j,i) == self.snake.dead_cell: self.board[j][i] = 5
        else:                               self.board[j][i] = 0

  def generate_food(self):
    avaiable_cells = [ [(j,i) for i in range(self.W) if self.board[j][i] == 0] for j in range(self.H)]
    avaiable_cells = [x for l in avaiable_cells for x in l] #Flatten list of list
    assert len(avaiable_cells) > 0, "The full map is complete, we created the perfect snake"
    return random.choice(avaiable_cells)


class Snake:
  def __init__(self,parent):
    self.parent = parent

    self.dead_cell = None
    self.body = self.init_body()

  def init_body(self):
    w2 = int(self.parent.W/2)
    h2 = int(self.parent.H/2)
    return [(h2,w2),(h2+1,w2),(h2+2,w2)]