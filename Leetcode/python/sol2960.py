#https://leetcode.com/problems/count-tested-devices-after-test-operations/description/

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested_devices = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > 0:
                tested_devices+=1
                for j in range(i+1, len(batteryPercentages)):
                    if batteryPercentages[j] > 0:
                        batteryPercentages[j]-=1

        return tested_devices

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested_devices = 0
        reduction = 0
        for i in batteryPercentages:
            if i - reduction > 0:
                tested_devices+=1
                reduction+=1
        return tested_devices