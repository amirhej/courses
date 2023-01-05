print('Strings')

name = 'John Due' # single quote
print(name)

sentence = "Welcome to new world" # double quotes
print(sentence)

multiline_string =  '''
    Lorem ipsum dolor sit amet,
    consectetur adipiscing elit, 
    sed do eiusmod tempor incididunt 
    ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, 
    quis nostrud exercitation ullamco 
    laboris nisi ut aliquip ex ea 
    commodo consequat. 
'''  # single quote
print(multiline_string)

multiline_string_double = """
Duis aute irure dolor in 
reprehenderit in voluptate 
velit esse cillum dolore 
eu fugiat nulla pariatur. 
Excepteur sint occaecat 
cupidatat non proident, 
sunt in culpa qui officia 
deserunt mollit anim id
est laborum.
""" # double quote
print(multiline_string_double)

print('Strings are arrays')

print('First character of ', name, ' = ', name[0])
print('Third character of ', name, ' = ', name[3])
print('Fifth character of ', name, ' = ', name[5])

print('Strings length')
print('The length of ', name , ' is ', len(name))   