import feedparser
from flask import Flask,render_template

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
def index():
    return render_template('index.html')


@app.route("/<publication>")
def get_news(publication="bbc"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    my_string=''
    for i in range(NUMBER_OF_TOP_NEWS):
        first_article = feed['entries'][i]
        # print(type(feed))
        # print(feed)
        my_string += """
                    <a href={0}><b>{1}</b></a> <br />
                    <i>{2}</i> <br />
                    <p>{3}</p> <br /><br />
                <hr>
                """.format(first_article.get("link"), first_article["title"],
                           first_article.get("published"),
                           first_article.get("summary"))


    print(my_string)

    return """<html>
            <body>
            """ + my_string + """
            </body>
            </html>
        """


if __name__ == "__main__":
    app.run(port=5000, debug=True)