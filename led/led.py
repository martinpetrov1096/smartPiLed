from abc import ABC, abstractmethod
from gpiozero import PWMLED
from time import sleep
import threading


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
    self._rgbQ = []
    self.pulse = .1

  @abstractmethod
  def run(self):
    pass

  @property
  def rgbQ(self) -> []:
    return self._rgbQ

  @rgbQ.setter
  def rgbQ(self, rgbQ) -> None:
    self._rgbQ = rgbQ


class ledContext():

  def __init__(self, rPin: int, gPin: int, bPin: int, led: LED) -> None:
    self._brightness = 1
    self._mode = led
    self._q = []
    self._mode.rgbQ = self._q

    self.rPin = PWMLED(rPin)
    self.gPin = PWMLED(gPin)
    self.bPin = PWMLED(bPin)

  ## PUBLIC METHODS ##
  def on(self) -> None:
    self._isOn = True
    self._mode.run()
    self.updateT = threading.Thread(target=self._updateLED, args=()) 
    self.updateT.start()

  def off(self) -> None:
    self._isOn = False
    self.updateT.join()
    self.rPin.off()
    self.gPin.off()
    self.bPin.off()

  def _updateLED(self) -> None:
    while self._isOn:
      if self._q:
        rgb = self._q.pop()
        self.rPin.value = rgb.red * self._brightness
        self.gPin.value = rgb.green * self._brightness
        self.bPin.value = rgb.blue * self._brightness

      sleep(self._mode.pulse)

  ## PUBLIC DATA MEMBERS ##
  @property
  def mode(self) -> LED:
    return self._mode

  @mode.setter
  def mode(self, led: LED) -> None:
    self._mode = led
    self._mode.rgbQ = self._q

  @property
  def brightness(self):
    return self._brightness

  @brightness.setter
  def brightness(self, brightness) -> None:
    self._brightness = brightness
    self._q.append(RGB(self.rPin.value, self.gPin.value, self.bPin.value))
    
