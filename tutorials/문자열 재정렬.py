S = input()

num = 0
chars = []

for char in S:
    if char.isdigit():
        num += int(char)
    else:
        chars.append(char)

chars.sort()
num = str(num)

answer = ''.join(chars) + num
print(answer)
