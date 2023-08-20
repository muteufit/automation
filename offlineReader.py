import os
import requests
from bs4 import BeautifulSoup
from ebooklib import epub

def create_ebook(title, articles):
    book = epub.EpubBook()
    book.set_title(title)
    book.set_language('en')

    for idx, article in enumerate(articles):
        title = article['title']
        content = article['content']

        chapter = epub.EpubHtml(title=title, file_name=f'chap_{idx + 1}.xhtml', lang='en')
        chapter.content = f'<h1>{title}</h1>{content}'

        book.add_item(chapter)
        book.spine.append(chapter)

    epub.write_epub(f'{title}.epub', book, {})

def fetch_articles(urls):
    articles = []

    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string if soup.title else 'Untitled Article'
            content = str(soup)
            articles.append({'title': title, 'content': content})
    
    return articles

if __name__ == "__main__":
    article_urls = [
        'https://example.com/article1',
        'https://example.com/article2',
        # Add more article URLs here
    ]

    ebook_title = input("Enter the title for the e-book: ")
    
    articles = fetch_articles(article_urls)
    if articles:
        create_ebook(ebook_title, articles)
        print(f"E-book '{ebook_title}.epub' created successfully!")
    else:
        print("No articles fetched or there was an issue with fetching articles.")
