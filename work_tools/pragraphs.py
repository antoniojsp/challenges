
with open('sample.txt', 'r') as texto:
    lines1 = texto.readlines()

ans = str(lines1).split('\n\n')
for i in ans:
    print(i)