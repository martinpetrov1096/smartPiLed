from led import RGB, LED

class ledSimple(LED):

  def __init__(self):
    super().__init__()

  def setColor(self, r, g, b):
    self._rgb = RGB(r,g,b)
    self.run()

  def run(self):
    self._rgbQ.append(self._rgb)

