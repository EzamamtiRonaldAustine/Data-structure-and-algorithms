# write a python code that implements back and forward buttons in the browser as a
# stack by designing a class named BrowserStack, implement the following methods:
# __init__). navigation(url), backward(), and forward(). Use the list, pages=
# ["www.google.com","www.github.com","www.yahoo.com","www.ucu.com","www.microsoft.com",
# "www.skype.com"] as the parameters for the navigation(url) method.

# What is the output when the following code is run?

# browser = BrowserStack()
# print([browser. navigation(page) for page in pages])
# browser.backward()
# browser.backward()
# browser.forward()
# browser.navigation("www.3wschools.com")
# browser.forward()

import webbrowser
class BrowserStack:
    def __init__(self):
        self.pages = []
        self.current_page = 0

    def navigation(self, url):
        if url not in self.pages:
            self.pages.append(url)
        self.current_page = self.pages.index(url)
        print(self.current_page)
        webbrowser.open(url)
        return self.pages[self.current_page]

    def backward(self):
        if self.current_page > 0:
            self.current_page -= 1
            webbrowser.open(self.pages[self.current_page])
            print(self.pages[self.current_page]) 
            return self.pages[self.current_page]
        else:
            return "No more pages to go back to."

    def forward(self):
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
            webbrowser.open(self.pages[self.current_page])
            print(self.pages[self.current_page])
            return self.pages[self.current_page]
        else:
            return "No more pages to go forward to."

pages = ["www.google.com","www.github.com","www.yahoo.com","www.ucu.com","www.microsoft.com","www.skype.com"]
browser = BrowserStack()
print([browser.navigation(page) for page in pages ])
browser.backward()
browser.backward()
browser.forward()
browser.navigation("www.3wschools.com")
browser.forward()