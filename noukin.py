# Noukin v1.0
# Brainfuck with Japanese culture

import sys
import random

pointer = 0
mem = [0 for i in range(32768)]
pos = 0

path = sys.argv[1]

with open(path) as f:  # open file
    code = f.read()
    while pos < len(code):
        if code[pos] == "進":
            pointer += 1
        elif code[pos] == "戻":
            pointer -= 1
        elif code[pos] == "足":
            mem[pointer] += 1
        elif code[pos] == "引":
            mem[pointer] -= 1
        elif code[pos] == "出":
            print(chr(mem[pointer]), end="")
        elif code[pos] == "入":
            mem[pointer] = int(input())
        elif code[pos] == "始":
            if mem[pointer] == 0:
                nest = 0
                while True:
                    pos += 1
                    if code[pos] == "始":
                        nest += 1
                    elif code[pos] == "終" and nest == 0:
                        break
                    elif code[pos] == "終":
                        nest -= 1
        elif code[pos] == "終":
            if mem[pointer] != 0:
                nest = 0
                while True:
                    pos -= 1
                    if code[pos] == "終":
                        nest += 1
                    elif code[pos] == "始" and nest == 0:
                        break
                    elif code[pos] == "始":
                        nest -= 1
        elif code[pos] == "乱":
            code[pos] = random.randint(0, 255)
        pos += 1
