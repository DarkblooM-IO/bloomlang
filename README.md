```
==== Bloomlang esolang ====

You get an accumulator with an initial value of 0 that you can increment or decrement,
as well as a buffer that can store one value at a time. The code is read character by
character and instructions are executed one after the other.

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
 $    print buffer

Any other character is ignored.
```
