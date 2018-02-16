from cpu import CPU
import time
to = set()
cpu = CPU()
file = open("test.py", "r")
code = ""
for line in file.read():
	code += line
cpu.run_code(code)