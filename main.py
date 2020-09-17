import GameObjects
from Utils import Display
import cv2 as cv
from NN import Model
import numpy as np
width = 30 
height = 20
scale = 20  #Render scale factor
delay = 1   #cv.waitKey delay



def run_episode(debug=True):

  b = GameObjects.Board(width = width, height = height)
  if debug:
    di = Display.Display(delay,width,height,scale)
    ui = di.draw(b)
    di.show(a=[ui])

  #While not dead
  while b.snake.dead_cell is None:
    #Grab input data
    vision = b.snake.vision()
    X = np.array(vision).reshape(-1,8,3,1)
    #Predict
    predictions = b.snake.brain.predict(X)
    direction = np.argmax(predictions[0])
    #Move
    b.snake.change_direction(direction)
    b.snake.move()
    b.update()

    if debug:
      ui = di.draw(b)
      if di.show(a=[ui]):
        break

  #Update score
  b.snake.update_score()


    

  cv.destroyAllWindows()


run_episode()