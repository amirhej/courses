# Basic

## Syntax

1. Header files add functionality to C programs, that (almost) always appears in your program.( like `#include <stdio.h>`)

2. C ignores white space. But we use it to make the code more readable.

3. Another thing that always appear in a C program, is `main()`. This is called a function. Any code inside its curly brackets `{}` will be executed. Do not forget to add the closing curly bracket `}` to actually end the main function.

4. Every C statement ends with a semicolon `;`

5. return `0` ends the `main()` function.

## Output

To output values or print text in C, you can use the `printf()` function.

### Escape sequence

+ `\n` ,it forces the cursor to change its position to the beginning of the next line on the screen. This results in a new line.

+ `\t` , it creates a horizontal tab.

+ `\\` , it inserts a backslash character (\\)

+ `\"` , it inserts a double quote character.

## Comments

Comments can be used to explain code, and to make it more readable. It can also be used to prevent execution when testing alternative code.
Comments can be singled-lined or multi-lined.

### Single-line Comments

Single-line comments start with two forward slashes (`//`).

Any text between `//` and the end of the line is ignored by the compiler (will not be executed).

### Multi-line Comments

Multi-line comments start with `/*` and ends with `*/`.

Any text between `/*` and `*/` will be ignored by the compiler.

