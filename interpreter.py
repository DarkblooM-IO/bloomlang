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
  # check for incomplete loop scopes
  if code.count("{") != code.count("}"):
    print("error: mismatched brackets")
    return

  # sanitize code
  code = "".join([c if c in "^`!+-*/%=~#@.{}|$" else "" for c in code.strip()])

  accumulator = 0
  buffer      = 0
  pc          = 0  # program counter
  stack       = [] # to store loop checkpoints

  # iterate over whole code
  while pc < len(code):
    try:
      match code[pc]:
        case "^": # increment accumulator if less than 255, else loop back around to 0
          accumulator = accumulator + 1 if accumulator < 255 else 0

        case "`": # decrement accumulator if greater than 0, else loop back around to 255
          accumulator = accumulator - 1 if accumulator > 0 else 255

        case "!": # set accumulator to 0
          accumulator = 0

        case "+": # add buffer to accumulator
          accumulator += buffer

        case "-": # substract buffer from accumulator
          accumulator -= buffer

        case "*": # multiply accumulator by buffer
          accumulator *= buffer

        case "/": # floor divide accumulator by buffer
          accumulator = accumulator // buffer

        case "%": # mod accumulator by buffer
          accumulator = accumulator % buffer

        case "=": # set buffer to accumulator
          buffer = accumulator

        case "~": # set accumulator to buffer
          accumulator = buffer

        case "#": # print accumulator
          print(accumulator, end="")

        case "@": # print ASCII char from accumulator or nothing if exception
          try:
            print(chr(accumulator), end="")
          except:
            print("", end="")

        case ".": # prompt user for value, default to 0 on exception
          try:
            accumulator = int(input())
          except (ValueError, EOFError):
            accumulator = 0

        case "|": # terminate function
          return

        case "{":
          stack.append(pc) # add loop start to stack
          if accumulator == 0:
            while len(stack) > 0: # advance until matching loop end
              pc += 1
              match code[pc]:
                case "{": stack.append(pc)
                case "}": del stack[-1] # delete last entry in stack

        case "}":
          if accumulator != 0:
            pc = stack[-1] # jump back to matching loop start

        case "$": # print buffer
          print(buffer, end="")

      pc += 1 # advance to next instruction

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
