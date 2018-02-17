from cpu import CPU
import time

#Use a random CPU
with open("test.py", "r") as r:
	lines = r.readlines()
	for line in lines:
		cpu = CPU()
		cpu.run_code(line)

#Use a dedicated CPU
with open("test.py", "r") as r:
	lines = r.readlines()
	for line in lines:
		cpu = CPU(1)
		cpu.run_code(line)
