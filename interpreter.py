#!/usr/bin/env python3
from os import system, path
from sys import argv
from readline import parse_and_bind

HELPSTRING = """
==== Bloomlang esolang ====

You get a value x with an initial value of 0 that you can increment or decrement,
as well as a value y that can store one value at a time. The code is read character by
character and instructions are executed one after the other.

Instruction list:
 ^    x += 1
 `    x -= 1
 !    x = 0
 +    x += y
 -    x -= y
 *    x *= y
 /    x /= y
 %    x %= y
 =    y = x
 ~    x = y
 #    print x
 @    print chr x
 .    x = input
 {}   while x != 0 { ... }
 |    exit
 $    print y

Any other character is ignored.
""".strip()

MOTD = """
Welcome to the Bloomlang interpreter.
Special commands:
- help: print the manual
- exit: exit the interpreter
- \\[command]: run [command] as a system program
""".strip()

def bloomlang(code: str):
  # check for mismatched brackets
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
        case "^": # increment accumulator
          accumulator += 1

        case "`": # decrement accumulator
          accumulator -= 1

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
          print(chr(accumulator), end="")

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
            loop = 1
            while loop > 0: # advance until matching loop end
              pc += 1
              match code[pc]:
                case "{": loop += 1
                case "}": loop -= 1

        case "}":
          if accumulator != 0:
            pc = stack[-1] # jump back to matching loop start
          else:
            stack.pop() # discard last stack entry

        case "$": # print buffer
          print(buffer, end="")

      accumulator %= 256 # keep accumulator in range 0-255
      buffer%= 256 # same for buffer

      pc += 1 # advance to next instruction

    except KeyboardInterrupt:
      return

def main():
  if len(argv) > 1 and path.isfile(argv[1]):
    code = ""

    with open(argv[1], "r") as file:
      for line in file:
        code = code+line.strip()

    bloomlang(code)

  else:
    parse_and_bind("set editing-mode vi")

    print(MOTD)

    run = True
    while run:
      try:
        cmd = input(">> ").strip()

        if cmd.startswith("\\"):
          system(cmd[1:])
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
