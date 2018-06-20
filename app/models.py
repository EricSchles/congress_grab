from app import db

class CongressTwitter(db.Model):
    """
    This model stores the tweets and other information relating to congress members.
    parameters:
    @timestamp - when the tweet was written
    @name - name of the tweeter
    @tweet - the text of the tweet
    @hashtag_of_interest - hashtags of interest are present
    @twitter_handle - the twitter handle of the tweeter
    """

    __tablename__ = 'congress_twitter'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    name = db.Column(db.String)
    tweet = db.Column(db.String)
    hashtag_of_interest = db.Column(db.Boolean)
    twitter_handle = db.Column(db.String)
    
    def __init__(
            self, timestamp,
            name, tweet,
            hashtag_of_interest,
            twitter_handle
    ):
        self.timestamp = timestamp
        self.name = name
        self.tweet = tweet
        self.hashtag_of_interest = hashtag_of_interest
        self.twitter_handle = twitter_handle
