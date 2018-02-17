import sys
import os

with open("REQUIREMENTS.txt", "r") as r:
  for line in r.readlines():
    os.system("pip install "+line)
