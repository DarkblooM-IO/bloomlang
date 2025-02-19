#!/usr/bin/env python3

"""
==== Bloomlang esolang ====

You get an accumulator with an initial value of 0 that you can increment or decrement, as well as
a buffer that can store one value at a time. The code is read character by character and instructions
are executed one after the other.

Instruction list:
 ^    increment accumulator
 `    decrement accumulator
 +    add buffer to accumulator
 -    substract buffer from accumulator
 *    multiply accumulator by buffer
 /    divide accumulator by buffer and store the result (floor division)
 %    divide accumulator by buffer and store the remainder (modulo)
 =    set buffer to accumulator
 ~    set accumulator to buffer
 #    print accumulator
 @    print accumulator as ASCII
 .    set accumulator to user input
 {}   repeatedly run the code inside while accumulator is not 0
 |    halt the program
 $    (optional, for debugging) print buffer

Any other character is ignored
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
