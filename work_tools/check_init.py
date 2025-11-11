with open('sample.txt', 'r',  encoding="utf-8") as texto:
    lines = texto.read()
lines = lines.split(" ")
print(lines)
rslt = []
for idx, i in enumerate(lines):
    if i:
        rslt.append(i[0][0])

# print(rslt)
for i in range(0, len(rslt)-8):
    # print(len(set(rslt[i:i+7])) )
    if len(set(rslt[i:i+3])) == 1:
        print("Here", rslt[i:i+7], i)