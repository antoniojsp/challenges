# # https://leetcode.com/problems/repeated-substring-pattern/
# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         if len(s) <= 1:
#             return False
#
#         for length in range(1, len(s )// 2 +1):
#             if len(s ) %length != 0:
#                 continue
#             check = set()
#             for i in range(0, len(s), length):
#                 check.add(s[i: i +length])
#                 if len(check) > 1:
#                     break
#             if len(check) == 1:
#                 return True
#
#         return False


import requests
from bs4 import BeautifulSoup

URL = "https://rec.uoregon.edu/"
resp = requests.get(URL)

# Parse the HTML
soup = BeautifulSoup(resp.text, "html.parser")

# Example 1: Find the first <h1> tag
h1_tag = soup.find("h3")
print("First <h1>:", h1_tag.text if h1_tag else "Not found")

# Example 2: Find all <a> tags
# links = soup.find_all("a")
# print("\nNumber of <a> tags:", len(links))
# print("First 5 links:")
# for link in links[:5]:
#     print(link.get("href"))
#
# # Example 3: Find by class name
# article_title = soup.find("div", class_="article-title")
# if article_title:
#     print("\nArticle Title:", article_title.text.strip())
