

test = [1, 7, 3, 7, 5, 7, 3]

def max_freq(nums):
    max_freq = 0
    val = nums[0]

    for i in range(1, len(nums)):
        if nums[i] == val:
            max_freq+=1
        else:
            if max_freq == 0:
                max_freq = 1
                val = nums[i]
            else:
                max_freq -=1
                # max_freq = max(max_freq, nums[i])

    return val, max_freq

print(max_freq(test))