#!/usr/bin/env python3
import glob

for sensor in glob.glob("/sys/bus/w1/devices/28-*/w1_slave"):
  id = sensor.split("/")[5].split("-")[1]
  f = open(sensor, "r")
  data = f.read()
  f.close()
  if "YES" in data:
    partitioned = data.partition(' t=')
    temp = float(partitioned[2]) / 1000.0
    print("sensors,sensor_id={:s} temperature={:.3f}".format(id, temp))