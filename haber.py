import feedparser

rss_url = "https://www.cnnturk.com/feed/rss/ekonomi/news"

feed = feedparser.parse(rss_url)


for entry in feed.entries:
    print(entry.title)
    print(entry.published)
    print(entry.link)
    print("\n")
