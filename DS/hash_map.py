
def hashed(key:str):
    h = 0
    for c in key:
        h = h * 31 + ord(c)

    return h


class HashMap:
    def  __init__(self):
        init_size = 100
        hash_table = [[] for i in range(init_size)]
        num_elements = 0

