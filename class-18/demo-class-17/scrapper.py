import requests
from bs4 import BeautifulSoup

url = "https://testing-www.codefellows.org/course-calendar/?filters=400:%20Advanced,code-python-401"

req = requests.get(url)
# print(req.text)
markup = req.text

soup = BeautifulSoup(markup, 'html.parser')

# print(soup.find("h1"))
courses = soup.select(".calendar-event")

for course in courses:
    if 'Python' in course.h1.text:
        print(course.h1.text)
        print(course.h2.text)
