
with open('sample.txt', 'r') as texto:
    lines1 = texto.readlines()

print(str(lines1).count("-"))