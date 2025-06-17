class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        n_boxes = 0
        for boxes, units in boxTypes:
            if truckSize-boxes >= 0:
                n_boxes+=units*boxes
                truckSize-=boxes
            elif truckSize-boxes < 0:
                n_boxes+= (truckSize)*units
                break

        return n_boxes



