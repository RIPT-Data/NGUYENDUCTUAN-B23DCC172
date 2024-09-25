import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin, urlparse
def crawl_page(url, visited):
    if url in visited:
        return []  
    visited.add(url) 
    try:
        response = requests.get(url)
        response.raise_for_status()  
    except requests.RequestException as e:
        print(f"Có lỗi xảy ra với {url}: {e}")
        return []
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    for article in soup.find_all('article'):
        title_element = article.find('h1')
        content_element = article.find(class_='article-content')

        title = title_element.text.strip() if title_element else "Tiêu đề không tìm thấy"
        content = content_element.text.strip() if content_element else "Nội dung không tìm thấy"

        article_data = {
            "title": title,
            "content": content,
            "url": url
        }
        articles.append(article_data)
    for link in soup.find_all('a', href=True):
        next_url = urljoin(url, link['href'])
        if urlparse(next_url).netloc == urlparse(url).netloc:
            articles += crawl_page(next_url, visited)
    return articles
start_urls = [
    "https://dantri.com.vn/the-gioi/chien-su-ukraine-219-hai-canh-quan-nga-kep-chat-10-lu-doan-kiev-o-kursk-20240921112300699.html",
    "https://www.youtube.com/", 
    "https://tuoitre.vn/" 
]
visited_urls = set()  
all_articles = []
for start_url in start_urls:
    all_articles += crawl_page(start_url, visited_urls)
with open('all_articles_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_articles, json_file, ensure_ascii=False, indent=4)

with open('titles.js', 'w', encoding='utf-8') as js_file:
    js_file.write("const titles = [\n")
    for article in all_articles:
        js_file.write(f"    '{article['title']}',\n")
    js_file.write("];\n")

print("Dữ liệu đã được lưu vào file JSON và tiêu đề vào file JavaScript")
