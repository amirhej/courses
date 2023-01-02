# Variables


## Definition:

    [Variables are used to store information to be referenced and manipulated in a computer program. They also provide a way of labeling data with a descriptive name, so our programs can be understood more clearly by the reader and ourselves. It is helpful to think of variables as containers that hold information. Their sole purpose is to label and store data in memory. This data can then be used throughout your program.](https://launchschool.com/books/ruby/read/variables)

## Creating:

    Use a assing(equal symbol) `=` operator to assign a value to it, 
    The language has no command for declaring a variable.

## Naming: 

    + names start with a letter or the underscore character

    + names cannot start with a number

    + names can only contain alpha-numeric characters plus underscores:

        - a to z, A to z, 0 to 9 , _

    + names are case-sensitive

    + names with multi words, use one of those techniques:

        - Camel case -> aMultiWordsVariableName

        - Pascal case -> AMultiWordsVariableName

        - Snake case -> a_multi_words_variable_name

## Multiple values assignment:

    use comma `,` to assign multiple values to multiple variables:
        
        ``` 
        var1, var2, var3 = 'value 1', 2, True 
        ```

## Assign single value to multiple variables:

    use multiple assign operator: 

    ```
        var1 = var2 = var3 = 'common value'
    ```
