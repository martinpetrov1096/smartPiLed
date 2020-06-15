from abc import ABC, abstractmethod
from gpiozero import PWMLED

# Helper struct
class RGB:
  def __init__(self,r,g,b):
    self.red = r
    self.green = g
    self.blue = b
  
# Interface for the LED strips. 
class LED(ABC):
  def __init__(self): 
    self._rgb = RGB(1,1,1)
    self._power = False

  def setPins(self,  rPin, gPin, bPin):
    self.rPin = rPin
    self.gPin = gPin
    self.bPin = bPin

  @abstractmethod
  def on(self): 
    pass

  @abstractmethod
  def off(self):
    pass


class ledContext():

  def __init__(self, rPin: int, gPin: int, bPin: int, led: LED) -> None:
    self._brightness = 1
    self.rPin = PWMLED(rPin)
    self.gPin = PWMLED(gPin)
    self.bPin = PWMLED(bPin)
    self.mode = led


  ## PUBLIC METHODS ##
  def on(self) -> None:
    self.mode.on()

  def off(self) -> None:
    self.mode.off()

  ## PUBLIC DATA MEMBERS ##
  @property
  def mode(self) -> LED:
    return self._mode

  @mode.setter
  def mode(self, led: LED) -> None:
    self._mode = led
    self.mode.setPins(self.rPin, self.gPin, self.bPin)
