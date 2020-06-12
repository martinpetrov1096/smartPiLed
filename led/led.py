class ledContext():

  def __init__(self, led: LED, rPin, gPin, bPin) -> None:
    self._mode = led
    self.rPin = PWMLED(rPin)
    self.gPin = PWMLED(gPin)
    self.bPin = PWMLED(bPin)

  @property
  def mode(self) -> LED:
    return self._mode

  @mode.setter
  def mode(self, led: LED) -> None:
    self._mode = led

  @property
  def brightness(self):
    return 


# Interface for the LED strips. 

from abc import ABC, abstractmethod
from gpiozero import PWMLED
from time import sleep
import threading

class LED(ABC):

  @abstractmethod
  def on(self):
    pass

  @abstractmethod
  def off(self):
    pass

  @abstractmethod
  def setColor(self, r, g, b):
    pass

  @abstractmethod
  def setBrightness(self, brightness):
    pass