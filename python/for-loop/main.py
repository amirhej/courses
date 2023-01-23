name = 'Alex Wanger'

for letter in name:
    print(letter)

print('=' * 10)

for i in range(10):
    print(i)

print('=' * 10)

for age in range(12, 30, 2):
    if age < 18:
        continue
    print(age)

print('=' * 10)
letters = 'abcdefg'
forbidden = 'g'
for letter in letters:
    if letter in forbidden:
        break
    print(letter)

print('=' * 10)

for letter in letters:
    print(letter)
else:
    print('no Break')