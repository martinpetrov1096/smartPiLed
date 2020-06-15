from ledSimple import *
from led import *


def main():
  print("hello world")
  ledState = ledSimple()
  led = ledContext(17,18,27, ledState)
  ledState.setColor(0,0,1)
  led.on()
  sleep(2)
  led.brightness = .5
  sleep(2)
  led.off()
  sleep(1)




if __name__ == "__main__":    
  main()


