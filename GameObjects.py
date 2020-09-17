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
    for j in range(self.H):
      for i in range(self.W):
        if (j,i) == self.snake.dead_cell: self.board[j][i] = 5
        elif self.is_border(j,i):         self.board[j][i] = 1
        elif (j,i) in self.snake.body:
          if (j,i) == self.snake.body[0]:   self.board[j][i] = 3
          else:                             self.board[j][i] = 2
        elif (j,i) == self.food:            self.board[j][i] = 4
        else:                               self.board[j][i] = 0

  def generate_food(self):
    avaiable_cells = [ [(j,i) for i in range(self.W) if self.board[j][i] == 0] for j in range(self.H)]
    avaiable_cells = [x for l in avaiable_cells for x in l] #Flatten list of list
    assert len(avaiable_cells) > 0, "The full map is complete, we created the perfect snake"
    return random.choice(avaiable_cells)


class Snake:
  MOVE_COST = 1
  FOOD_REWARD = 10
  def __init__(self,parent,timeleft = 150):
    self.parent = parent
    self.body = self.init_body()

    self.dead_cell = None

    self.direction = random.randint(0,3) #4 directions possible

    self.timeleft = 150 #How many moves we can do without eating food

    self.livetime = 0 #How many step we've done



  def init_body(self):
    w2 = int(self.parent.W/2)
    h2 = int(self.parent.H/2)
    return [(h2,w2),(h2+1,w2),(h2+2,w2)]

  def move(self):
    #get_head
    cur_head = self.body[0]

    if self.direction == 0:   self.body.insert(0,(cur_head[0], cur_head[1] - 1 )) #Moving left
    elif self.direction == 1: self.body.insert(0,(cur_head[0] - 1, cur_head[1] )) #Moving Up
    elif self.direction == 2: self.body.insert(0,(cur_head[0], cur_head[1] + 1)) #Moving Right
    else:               self.body.insert(0,(cur_head[0] + 1, cur_head[1])) #Moving Down


    n_head = self.body[0]
    self.livetime += 1
    if n_head != self.parent.food:
      self.body.pop()
      self.timeleft -= Snake.MOVE_COST
    else:
      self.timeleft += Snake.FOOD_REWARD
      self.parent.food = self.parent.generate_food()



    #Handle end game
    if self.body.count(n_head) > 1 or self.parent.is_border(n_head[0],n_head[1]): #We run into ourself or the border
      self.dead_cell = n_head
      self.timeleft = 0

  def change_dir(self,direction):
    self.direction = direction

