from led import RGB, LED

class ledSimple(LED):

  def __init__(self):
    super().__init__()

  def setColor(self, r, g, b):
    self._rgb = RGB(r,g,b)
    self.run()

  def _pulse(self):
    curRgb = self._rgb
    while 1:
      if curRgb.red > 0 or curRgb.green > 0 or curRgb.blue > 0
      self._rgbQ.append(curRgb)
      curRgb = 



  def run(self):
    

 #   self._rgbQ.append(self._rgb)