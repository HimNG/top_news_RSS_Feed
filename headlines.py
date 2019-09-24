import feedparser
from flask import Flask,render_template,request

app=Flask(__name__)

NUMBER_OF_TOP_NEWS=5

# Below are RSS feed links.
RSS_FEEDS = {
    'economy' : 'https://economictimes.indiatimes.com/news/economy/rssfeeds/1373380680.cms',
    'politics': 'https://economictimes.indiatimes.com/news/politics-and-nation/rssfeeds/1052732854.cms',
    'science' : 'https://economictimes.indiatimes.com/news/science/rssfeeds/39872847.cms',
    'stock'   : 'https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms',
    'ipo'     : 'https://economictimes.indiatimes.com/markets/ipos/fpos/rssfeeds/14655708.cms',
    'bond'    : 'https://economictimes.indiatimes.com/markets/bonds/rssfeeds/2146846.cms',
    'auto'    : 'https://economictimes.indiatimes.com/industry/auto/rssfeeds/13359412.cms',
    'banking' : 'https://economictimes.indiatimes.com/industry/banking/finance/rssfeeds/13358259.cms',
    'tech'    : 'https://economictimes.indiatimes.com/industry/tech/rssfeeds/56811438.cms'
}

@app.route("/")
def get_news():
    query=request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication="tech"
    else:
        publication=query.lower()

    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])

if __name__ == "__main__":
    app.run(port=5000, debug=True)