
# https://leetcode.com/problems/slowest-key/description/

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        result = keysPressed[0]
        max_time = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            time = releaseTimes[i]-releaseTimes[i-1]
            if max_time < time or (max_time == time and result < keysPressed[i]):
                result = keysPressed[i]
                max_time = time
        return result


        # lengths = {releaseTimes[0]:[keysPressed[0]]}
        # max_time = releaseTimes[0]
        # for i in range(1, len(releaseTimes)):
        #     time = releaseTimes[i]-releaseTimes[i-1]
        #     max_time = max(time, max_time)
        #     lengths[time] = lengths.get(time, [])
        #     lengths[time].append(keysPressed[i])
        # return max(lengths[max_time])
