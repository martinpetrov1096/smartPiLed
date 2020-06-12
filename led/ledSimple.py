from rgbBase import rgbBase
from gpiozero import PWMLED
from time import sleep

class ledSimple(LED):

  def __init__(self, rPin, gPin, bPin):
    super().__init__(rPin, gPin, bPin)
    self.brightness = 1
    self.red = 0
    self.green = 0
    self.blue = 0

  def off(self):
    self.rPin.off()
    self.gPin.off()
    self.bPin.off()
    print(self.rPin.is_lit)

  def on(self):
    self.__update()

  def setBrightness(self, brightness):
    self.brightness = brightness

  def setColor(self, r, g, b):
    self.red = r
    self.green = g
    self.blue = b

  def __update(self):
    self.rPin.value = self.red * self.brightness
    self.gPin.value = self.green * self.brightness
    self.bPin.value = self.blue * self.brightness



def main():
  x = ledSimple(17,18,27)
  x.setColor(1,1,1)
  x.on()

  sleep(2)

  x.off()
  sleep(2)

if __name__ == "__main__":
    
  main()



