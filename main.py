from instascrape import *

# # Instantiate the scraper objects
# google = Profile('https://www.instagram.com/google/')
# google_post = Post('https://www.instagram.com/p/CG0UU3ylXnv/')
# google_hashtag = Hashtag('https://www.instagram.com/explore/tags/google/')
#
# # Scrape their respective data
# google.scrape()
# google_post.scrape()
# google_hashtag.scrape()
#
# print(google.followers)
# print(google_post['hashtags'])
# print(google_hashtag.amount_of_posts)
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
    "cookie": "sessionid=4667996553%3APj3zguqmDVvjlZ%3A21;"
}
rashford_post = Post('https://www.instagram.com/p/CRPWb3Ysf-2/')
rashford_post.scrape(headers=headers)
comments = rashford_post.get_comments()
print(comments)
