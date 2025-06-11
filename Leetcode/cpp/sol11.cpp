// https://leetcode.com/problems/container-with-most-water/


class Solution {
public:
    int calculate_area(int height, int left, int right){
        return height * (right - left);
    }

    int maxArea(vector<int>& height) {
        int max_area = 0;
        int left = 0;
        int right = height.size()-1;
        while(left < right){
            int minimum_height = min(height[left], height[right]); // choose the shorter wall, since this one determinate the area
            int curr_area = calculate_area(minimum_height, left, right); // calculate the current area
            max_area = max(curr_area, max_area); // update max_area accordingly
            if (height[left] < height[right]){ // move the shorter wall inward.
                left++;
            }else{
                right--;
            }
        }

        return max_area;
    }
};





class Solution {
public:
    int calculate_water_content(int left_height, int right_height, int distance){
        int height = min(left_height, right_height);
        return height * distance;
    }

    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int max_content = 0;
        while (left < right){
            int distance = right - left;
            int current_water_content = calculate_water_content(height[left], height[right], distance);
            max_content = max(max_content, current_water_content);
            if (height[left] <= height[right]){
                left++;
            }else{
                right--;
            }
        }

        return max_content;
    }
};