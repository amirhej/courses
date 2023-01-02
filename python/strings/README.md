# Strings


## Definition:

Strings in python are surrounded by either single quotation marks, or double quotation marks.[#](https://www.w3schools.com/python/python_strings.asp)

```
print("Life")
print('life')
```
## :cat: Single line & Multiline string
use """ [string] """ & ''' [string] ''' to assign a multiline string to a variable, so the LINE BREAKS are nserted at the same position as in the code.

use " [string] " & ' [string] ' to assign a single line string to a variable.

## :hamster: Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

```
myVar = "Live good"
print( myVar[1] )
```

The first character has index `0`.

## :frog: String length

use the `len()` function

## :bear: Check String

use the keyword `in` & `not in`

## :cow: Slicing

You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

```
myVar = "John Due"
print( myVar[1:4] )
```

### :monkey: Slice from the start

just leaving out the start index

```
myVar = "John Due"
print( myVar[:4] )
```

### :camel: Slice to the end

just leaving out the ** end ** index

```
myVar = "John Due"
print( myVar[5:])
```

### :panda_face: Negative indexing
start the slice from the end of the string

```
myVar = "John Due"
print( myVar[-6: -2] )
```

## :baby_chick: Upper case

use the `upper()` function

## :chicken: Lower case

use the `lower()` function

## :snake: Remove whitespace

use the `strip()` function

## :sheep: Replace string

use the `replace()` function, with 2 argument

## :horse: Split string

use the `split()` function, with a argument that is the separator, the function will return a list

## :boar: String concatenation

use the `+` operator

## :koala: String format

By default we cannot combine strings and numbers with the `+` operator.
We can combine strings and numbers by using the `format()` method.

```
year = 2023
sentence = 'Happy {} to everyone'
print( sentence.format(year) )
```

Plus those, we can use index numbers `{0}` to be sure the arguments are placed in the correct placeholders. 

## :pig: Escape characters

`\```` -> single quote

`\\` -> backslash

`\n` -> new line

`\r` -> carriage return

`\t` -> tab

`\b` -> backspace

`\f` -> form feed

`\ooo` -> octal value

`\xhh` -> hex value


