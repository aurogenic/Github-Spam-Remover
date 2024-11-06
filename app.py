


s = "hello  world a "

while "  " in s:
    s = s.replace("  ", " ")
words = s.strip().split(" ")
words.reverse()
print(''.join(w + " " for w in words)[:-1])