#!/usr/bin/env python3

"""
TODO:
- loops
"""

def bloomlang(code: str):
  if code.count("{") != code.count("}"):
    print("error: mismatched brackets")
    return

  code = "".join([c if c in "^`+-*/=~#@.{}|" else "" for c in code.strip()])

  accumulator = 0
  buffer      = 0
  pc          = 0
  stack       = []

  while pc < len(code):
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
        print(chr(accumulator), end="")

      case ".":
        try:
          accumulator = int(input())
        except ValueError:
          accumulator = 0

      case "|":
        return

    pc += 1

if __name__ == "__main__":
  code = """

  """
  bloomlang(code)
