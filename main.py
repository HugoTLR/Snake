import GameObjects
from Utils import Display
import cv2 as cv

width = 30 
height = 20
scale = 20  #Render scale factor
delay = 0   #cv.waitKey delay
di = Display.Display(delay,width,height,scale)
b = GameObjects.Board(width = width, height = height)

ui = di.draw(b)
di.show(a=[ui])

cv.destroyAllWindows()
