binary = "1011011"
print("By two")
for idx in range(len(binary)):
    print(int(binary[0:len(binary)-idx],2))
print("\nDouble")
for idx in range(len(binary)):
    print(int(binary[0:idx+1],2))