from led import RGB, LED

class ledSimple(LED):

  def __init__(self):
    super().__init__()

  def setColor(self, r, g, b):
    self._rgb = RGB(r,g,b)
    self.on()

  def on(self):
    self.rPin.value = self._rgb.red
    self.gPin.value = self._rgb.green
    self.bPin.value = self._rgb.blue

  def off(self):
    self.rPin.off()
    self.gPin.off()
    self.bPin.off()
