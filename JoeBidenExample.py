from selenium.webdriver import Chrome
from instascrape import Profile, scrape_posts

webdriver = Chrome("./chromedriver.exe")
headers = {
    "user-agent": "Chrome/87.0.4280.88",
    "cookie": "sessionid=4667996553%3APj3zguqmDVvjlZ%3A21;"
}
joe = Profile("joebiden")
joe.scrape(headers=headers)
posts = joe.get_posts(webdriver=webdriver, login_first=True)


