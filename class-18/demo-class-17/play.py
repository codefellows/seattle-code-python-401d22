from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=3000)
        page = browser.new_page()
        page.goto("https://testing-www.codefellows.org/")

        page.get_by_text("Course Calendar").click()

        page.click("//label[text()='400: Advanced']")

        courses = {
            "java": "Code 401: Java",
            "javascript": "Code 401: JavaScript",
            ".net": "Code 401: ASP.NET",
            "python": "Code 401: Python",
            "cybersecurity": "Ops 401: Cybersecurity",
        }

        for course in courses:
            if course != 'python':
                course_label = courses[course]
                page.click(f"//label[text()= '{course_label}']")


        browser.close()


if __name__ == '__main__':
    main()
