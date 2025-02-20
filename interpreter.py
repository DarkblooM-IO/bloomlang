#!/usr/bin/env python3
from sys import argv

def bloomlang(code: str):
  if code.count("{") != code.count("}"):
    print("error: mismatched brackets")
    return

  code = "".join([c if c in "^`+-*/=~#@.{}|$" else "" for c in code.strip()])

  accumulator = 0
  buffer      = 0
  pc          = 0
  stack       = []

  while pc < len(code):
    try:
      match code[pc]:
        case "^":
          accumulator += 1

        case "`":
          accumulator -= 1

        case "+":
          accumulator += buffer

        case "-":
          accumulator -= buffer

        case "*":
          accumulator *= buffer

        case "/":
          accumulator = accumulator // buffer

        case "%":
          accumulator = accumulator % buffer

        case "=":
          buffer = accumulator

        case "~":
          accumulator = buffer

        case "#":
          print(accumulator, end="")

        case "@":
          try:
            print(chr(accumulator), end="")
          except:
            print("", end="")

        case ".":
          try:
            accumulator = int(input())
          except (ValueError, EOFError):
            accumulator = 0

        case "|":
          return

        case "{":
          stack.append(pc)
          if accumulator == 0:
            while len(stack) > 0:
              pc += 1
              if code[pc] == "}":
                del stack[-1]

        case "}":
          if accumulator != 0:
            pc = stack[-1]

        case "$":
          print(buffer, end="")

      pc += 1

    except KeyboardInterrupt:
      return

if __name__ == "__main__" and len(argv) > 1:
  bloomlang(argv[1])
