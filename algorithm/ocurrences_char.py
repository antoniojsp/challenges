


def occurrence(string:str, seek:str, index:int = 0):
    if len(string) == index:
        return 0
    count = 1 if string[index] == seek else 0
    return count + occurrence(string, seek, index+1)

print(occurrence("ana", 'a'))