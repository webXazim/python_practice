text = input()
snake_foot = '_'
snake_case = ''
for letter in text:
    if letter.islower():
        snake_case += letter
    else:
        snake_case += snake_foot + letter
print(snake_case.lower())