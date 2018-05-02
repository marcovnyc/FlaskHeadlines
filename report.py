import feedparser
from flask import Flask

app = Flask(__name__)

RSS_FEEDS = { 'ps4': 'http://feeds.ign.com/IGNPS4All',
              'xboxone': 'http://feeds.ign.com/IGNXboxOneAll',
              'reviews': 'http://feeds.ign.com/ign/reviews'
              'pc': 'http://feeds.ign.com/ign/pc-all'}

@app.route("/")
@app.route("/ps4")

