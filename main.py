import GameObjects
from Utils import Display
import cv2 as cv


width = 30 
height = 20
scale = 20  #Render scale factor
delay = 1   #cv.waitKey delay

def run_test():

  di = Display.Display(delay,width,height,scale)
  b = GameObjects.Board(width = width, height = height)

  ui = di.draw(b)
  di.show(a=[ui])
  while b.snake.dead_cell is None:

    direction = int(input())
    b.snake.change_direction(direction)
    b.snake.move()
    b.update()


    ui = di.draw(b)
    if di.show(a=[ui]):
      break

  cv.destroyAllWindows()


run_test()