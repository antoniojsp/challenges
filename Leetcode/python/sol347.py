# https://leetcode.com/problems/top-k-frequent-elements/description/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count =  Counter(nums)
        freq :list[list[int]] = [[] for i in range(len(nums ) +1)]
        for num, times in count.items():
            freq[times].append(num)

        rslt :list[int] = []
        for i in freq[::-1]:
            if i:
                rslt.extend(i)

        return rslt[:k]


import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = list(Counter(nums).items())
        result = []
        for val, freq in count:
            heapq.heappush(result, (-freq, val))
        rslt = []
        for _ in range(k, 0, -1):
            rslt.append(heapq.heappop(result)[1])
        return rslt
        # if k > len(nums):
        #     return []
        # count =  list(Counter(nums).items())
        # count.sort(key=lambda x:x[1], reverse=True)
        # return [count[i][0] for i in range(k)]




