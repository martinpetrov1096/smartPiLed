from led import RGB, LED
import threading 
from time import sleep

class ledPulse(LED):

  def __init__(self):
    super().__init__()

  def setColor(self, r, g, b):
    self._rgb = RGB(r,g,b)

  def on(self):
    self._power = True
    self._thread = threading.Thread(target=self.run, args=())
    self._thread.start()

  def off(self):
    self._power = False
    self._thread.join()
    self.rPin.off()
    self.gPin.off()
    self.bPin.off()

  def run(self):
    increment = True
    print(self.bPin.value)
    while self._power:
      if increment:
        self.bPin.value+= .1
      else:
        self.bPin.value-= .1

      if self.bPin.value > self._rgb.blue:
        increment = False
      elif self.bPin.value < .1:
        increment = True
      sleep(.5)
    