#!/usr/bin/env python2

import math
import time
from array import array

# Import the PCA9685 module.
import Adafruit_PCA9685

import logging
logging.basicConfig(level=logging.DEBUG)

class Pca9685Hat:
  def __init__(self, num_channels=10, address=0x40):
    self.address = address
    self.num_channels = num_channels
    # Dictionary from channel ID to configured PWM value
    self.channels = {}
    # Initialise the PCA9685 using the default address (0x40).
    self.controller = Adafruit_PCA9685.PCA9685(address=self.address)
    # Set frequency to 60hz, good for servos.
    self.controller.set_pwm_freq(60)

  def set_pwm(self, channel, x, iteration):
    v = 0.0
    if iteration % self.num_channels == channel:
      v = math.sin(x) * 4096
    elif channel < (iteration % self.num_channels):
      if channel + 3 < (iteration % self.num_channels):
        v = 3500
      else:
        v = 4096
    pwm = int(v)
    if channels[channel] != pwm:
      self.controller.set_pwm(channel, 0, pwm)
      channels[channel] = pwm

  def illuminate(self):
    iteration = 0
    num_steps = 10
    while True:
      for step in range(0, num_steps):
        x = (math.pi / 2 ) * step / (num_steps-1)
        for channel in range(0, num_channels):
          hat.set_pwm(channel, x, iteration)
        time.sleep(0.01)
      iteration = iteration + 1
      if iteration % num_channels == 0:
        print("Cycle %d" % (iteration / num_channels))

def main():
  hat = Pca9685Hat(num_channels=12)
  num_channels = 12

if __name__ == "__main__":
  main()
