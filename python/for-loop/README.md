# For Loop

## Definition [^1]

Python For loop is used for sequential traversal i.e. it is used for iterating over an iterable like String, Tuple, List, Set or Dictionary.

__Note:__ In Python, for loops only implements the collection-based iteration.

## Syntax
```
for var in iterable:
    # statements
```
## Continue Statement

Python continue Statement returns the control to the beginning of the loop.

## Break Statement

Python break statement brings control out of the loop.

## Pass Statement

The pass statement to write empty loops. Pass is also used for empty control statements, functions, and classes.

## For loop in Python with else

In most programming languages (C/C++, Java, etc), the use of else statements has been restricted with the if conditional statements. But Python also allows us to use the else condition with for loops. 

__Note__: The else block just after for/while is executed only when the loop is NOT terminated by a break statement

## `Range()` function

The Python `range()` function returns a sequence of numbers, in a given range. The most common use of it is to iterate sequence on a sequence of numbers using Python loops.

### Syntax

`range(start, stop, step)`

### Parameter

+ __start__: [ optional ] start value of the sequence
+ __stop__: next value after the end value of the sequence
+ __step__: [ optional ] integer value, denoting the difference between any two numbers in the sequence.

### Return

Returns a range type object

Reference: 
[^1]: [geeksforgeeks](https://www.geeksforgeeks.org/python-for-loops)