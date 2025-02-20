#!/usr/bin/env python3
from os import system
from readline import parse_and_bind

HELPSTRING = """
==== Bloomlang esolang ====

You get an accumulator with an initial value of 0 that you can increment or decrement,
as well as a buffer that can store one value at a time.

The code is read character by character and instructions are executed one after the other.

Instruction list:
 ^    increment accumulator
 `    decrement accumulator
 !    set accumulator to 0
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

Any other character is ignored.
""".strip()

def bloomlang(code: str):
  if code.count("{") != code.count("}"):
    print("error: mismatched brackets")
    return

  code = "".join([c if c in "^`!+-*/=~#@.{}|$" else "" for c in code.strip()])

  accumulator = 0
  buffer      = 0
  pc          = 0
  stack       = []

  while pc < len(code):
    try:
      match code[pc]:
        case "^":
          accumulator = accumulator + 1 if accumulator < 255 else 0

        case "`":
          accumulator = accumulator - 1 if accumulator > 0 else 255

        case "!":
          accumulator = 0

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

def main():
  parse_and_bind("set editing-mode vi")

  print("""Welcome to the Bloomlang interpreter.
Special commands:
- help: print the manual
- exit: exit the interpreter
- \\[command]: run [command] as a system program""")

  run = True

  while run:
    try:
      cmd = input(">> ").strip()

      if cmd.startswith("\\"):
        system(cmd)
      else:
        match cmd.lower():
          case "help": print(HELPSTRING)
          case "exit": run = False
          case _:
            bloomlang(cmd)
            print("")

    except (EOFError, KeyboardInterrupt):
      run = False
      print("")

if __name__ == "__main__":
  main()
