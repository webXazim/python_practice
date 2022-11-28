message = input()
hell_point = []
encrypted = []
i = 0
for each_char in message:
    code_point = ord(each_char)
    hell_point.append(code_point + 1)
    encrypted.append(chr(hell_point[i]))
    i += 1

print("".join(encrypted))
