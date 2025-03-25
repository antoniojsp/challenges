class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        n_containers = n * n  # number of containers
        total_weight = n_containers * w  # total weight only containers
        if total_weight <= maxWeight:  # if total weight is less than max weight,
            # then all the containers can be shipped at the same time.
            return n_containers

        return maxWeight // w  # else, we divide the max weight and
        # the weight per container to se how many it can hold.

