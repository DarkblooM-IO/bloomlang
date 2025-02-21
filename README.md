```
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
```
