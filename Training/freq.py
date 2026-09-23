

arr = [1, 2, 2, 3, 3, 3]

def freq(nums):
    res = {}

    for i in nums:
        res[i] = res.get(i, 0) + 1

    return max(res.items(), key=lambda x:x[1])[1]


# print(max(a.items(), key=lambda x:x[1]))
print(freq(arr))