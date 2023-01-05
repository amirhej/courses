print("Life") # -> double quotation
print('life')
sentence = """Lorem ipsum is typically a
 corrupted version of De finibus
bonorum et malorum, a 1st-century
 BC text by the Roman statesman 
 and philosopher Cicero, with words altered, added, and removed to make it nonsensical and improper Latin."""
print(sentence)

sentence2 = '''
2 Lorem ipsum is typically 
a corrupted version of De finibus 
bonorum et malorum, a 1st-century 
BC text by the Roman statesman and philosopher Cicero, with words altered, added, and removed to make it nonsensical and improper Latin.
'''
print(sentence2)

name = 'John' # Strings are Arrays
print(name) # -> 'John'

print(name[0]) # -> 'J'
print(name[1]) # -> 'o'
print(name[2]) # -> 'h'
print(name[3]) # -> 'n'
# print(name[4]) # -> IndexError

print(sentence[4])
print(sentence[6])
print(sentence[30])
print("Length of sentence is ", len(sentence)) # len -> length
print( sentence[ len(sentence) - 1 ] )