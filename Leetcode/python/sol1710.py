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



class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        items = 0
        boxes_curr = 0
        for box, items_per_box in boxTypes:
            if boxes_curr + box < truckSize:
                boxes_curr += box
                items += (box*items_per_box)
            else:
                space_left = truckSize - boxes_curr
                items += items_per_box*space_left
                break
        return items

