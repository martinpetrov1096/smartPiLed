from ledPulse import *
from led import *
from time import sleep


def main():
  print("hello world")
  ledState = ledPulse()
  ledState.setColor(0,0,1)
  led = ledContext(17,18,27, ledState)
  led.on()
  sleep(4)
  ledState.setColor(1,0,1)
  led.off()
  led.on()
  sleep(2)




if __name__ == "__main__":    
  main()


