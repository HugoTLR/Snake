from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.models import Sequential

class Model:
  @staticmethod
  def build(width,height,depth,classes):
    model = Sequential()
    input_shape = (width,height,depth)

    model.add(Flatten(input_shape=input_shape))
    model.add(Dense(8))
    model.add(Activation("relu"))
    model.add(Dropout(0.5))


    # softmax classifier
    model.add(Dense(classes))
    model.add(Activation("softmax"))
    print(model.summary())
    return model


  