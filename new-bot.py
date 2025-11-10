import os
import time
import random
import logging
import tweepy
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# 1) Load API Keys & Tokens
API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# 2) Authenticate Tweepy Client
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# 3) Logging Setup
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()

# 4) Predefined Tweets and Retweet Targets
TWEET_PHRASES = [
    "Embrace the chaos.",
    "Another random thought from my mind.",
    "Coding is like magic, except your spells have syntax errors.",
    "Stay humble.",
    "Hello World."
]

RETWEET_TARGETS = [
    1986215386224992320,
    1986400282461548863,
    1986593526059311604
]

# 5) Functions
def random_delay(min_seconds=10, max_seconds=20):
    delay = random.uniform(min_seconds, max_seconds)
    logger.info(f"Sleeping for {delay:.2f} seconds.")
    time.sleep(delay)


def tweet_random_phrase():
    phrase = random.choice(TWEET_PHRASES)
    try:
        client.create_tweet(text=phrase)
        logger.info(f"Tweeted: {phrase}")
        print(f"Tweeted: {phrase}")
    except Exception as e:
        logger.error(f"Error tweeting: {e}")
        print(f"Error tweeting: {e}")


def retweet_random_post():
    if not RETWEET_TARGETS:
        logger.warning("No retweet targets configured.")
        print("No retweet targets configured.")
        return

    tweet_id = random.choice(RETWEET_TARGETS)
    try:
        client.retweet(tweet_id=tweet_id)
        logger.info(f"Retweeted: {tweet_id}")
        print(f"Retweeted: {tweet_id}")
    except Exception as e:
        logger.error(f"Error retweeting: {e}")
        print(f"Error retweeting: {e}")


# 6) Main Bot Execution
if __name__ == "__main__":
    print("Twitter Bot Started. Press Ctrl + C to stop.")
    logger.info("Twitter bot started.")

    try:
        while True:
            chance = random.random()

            if chance < 0.5:
                tweet_random_phrase()
            else:
                retweet_random_post()

            random_delay()

    except KeyboardInterrupt:
        print("Bot stopped manually.")
        logger.info("Bot stopped manually by the user.")
        print("Check bot.log for activity history.")
