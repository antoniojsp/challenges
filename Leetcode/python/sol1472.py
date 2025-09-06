# https://leetcode.com/problems/design-browser-history/?envType=problem-list-v2&envId=linked-list
class Link:
    def __init__(self, page="", next=None, back=None):
        self.page = page
        self.next = next
        self.back = back

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Link(page=homepage)

    def visit(self, url: str) -> None:
        self.current.next = None
        self.current.next = Link(page=url, back=self.current)
        self.current = self.current.next

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.back:
                self.current = self.current.back
            else:
                break
        return self.current.page

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.next:
                self.current = self.current.next
            else:
                break
        return self.current.page



    # Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)