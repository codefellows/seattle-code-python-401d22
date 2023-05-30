import requests
from page_parser import parse


url = "https://testing-www.codefellows.org/course-calendar/?filters=400:%20Advanced,code-python-401"
response = requests.get(url)
results = parse(response.text)

with open("courses.txt","w") as f:
    f.write(results)
