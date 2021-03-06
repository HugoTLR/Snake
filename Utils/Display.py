import cv2 as cv
import numpy as np 

class Display:
  colors = {"BLACK" : (0,0,0), \
            "WHITE" : (255,255,255), \
            "GRAY"  : (100,100,100), \
            "BLUE"  : (255,0,0), \
            "RED"   : (0,0,255), \
            "GREEN" : (0,255,0)}
  mapping = {0:"BLACK", \
              1:"GRAY", \
              2:"WHITE", \
              3:"BLUE", \
              4:"GREEN", \
              5:"RED"}

  def __init__(self,delay,w,h,scale):
    self.delay = delay
    self.W = w
    self.H = h
    self.SCALE = scale

  def show(self, **kwargs):
    for i,stack in enumerate(kwargs.values()):
      if not stack: continue
      cv.imshow(f"Stack {i}",np.hstack(stack))
    return cv.waitKey(self.delay) == ord('q') & 0xFF

  def draw(self,board):
    im = np.zeros((self.H,self.W,3),dtype=np.uint8)
    for j,row in enumerate(board.board):
      for i,col in enumerate(row):
        im[j][i] = Display.colors[Display.mapping[col]]
    return cv.resize(im,(0,0),fx=self.SCALE,fy=self.SCALE,interpolation=cv.INTER_AREA)