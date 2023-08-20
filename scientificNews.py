import requests
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

# NewsAPI configuration
NEWSAPI_KEY = 'your_newsapi_key'
NEWSAPI_ENDPOINT = 'https://newsapi.org/v2/top-headlines'
SCIENCE_KEYWORD = 'science'
NUM_ARTICLES = 5

def fetch_science_news():
    params = {
        'apiKey': NEWSAPI_KEY,
        'q': SCIENCE_KEYWORD,
        'language': 'en',
        'pageSize': NUM_ARTICLES,
    }
    response = requests.get(NEWSAPI_ENDPOINT, params=params)
    data = response.json()

    if response.status_code == 200 and data['status'] == 'ok':
        articles = data['articles']
        return articles
    else:
        return None

def summarize_article(article):
    parser = PlaintextParser.from_string(article['title'] + " " + article['description'], Tokenizer("english"))
    summarizer = LsaSummarizer(Stemmer("english"))
    summarizer.stop_words = get_stop_words("english")

    summary = summarizer(parser.document, 3)  # You can adjust the number of sentences in the summary
    return " ".join([str(sentence) for sentence in summary])

if __name__ == "__main__":
    articles = fetch_science_news()

    if articles:
        print("Scientific News Daily Briefing:")
        for idx, article in enumerate(articles):
            print(f"\nArticle {idx + 1}:")
            print("Title:", article['title'])
            print("Source:", article['source']['name'])
            print("Description:", article['description'])
            print("Summary:", summarize_article(article))
    else:
        print("Failed to fetch science news. Please check your API key.")
