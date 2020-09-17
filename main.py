import GameObjects
from Utils import Display
import cv2 as cv


width = 30 
height = 20
scale = 20  #Render scale factor
delay = 0   #cv.waitKey delay

def run_test():

  di = Display.Display(delay,width,height,scale)
  b = GameObjects.Board(width = width, height = height)
  while b.snake.dead_cell is None:

    b.snake.move()
    b.update()


    ui = di.draw(b)
    # print(b)
    if di.show(a=[ui]):
      break

  cv.destroyAllWindows()


run_test()