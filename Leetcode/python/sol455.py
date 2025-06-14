#  https://leetcode.com/problems/assign-cookies/description/
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(), s.sort()
        children = cookies = 0
        while cookies < len(s) and children < len(g):
            '''
            If statement check if the cookie is big enough to satisfy a kid
            if it's big enough, count the kid and move on to match the next cookie.
            '''
            if s[cookies ]> =g[children]:
                childre n+ =1
            cookie s+ =1
        return children

