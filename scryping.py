import requests
from bs4 import BeautifulSoup
import json

# Словник для збереження інформації про авторів
authors_dict = {}

# Список для збереження всіх quotes
quotes = []

# Функція для отримання даних зі сторінки
def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quote_elements = soup.find_all('div', class_='quote')
    for quote_element in quote_elements:
        quote_text = quote_element.find('span', class_='text').text.replace('\u201c', '').replace('\u201d', '')
        author_name = quote_element.find('small', class_='author').text
        author_link = quote_element.find('a', href=True)['href']
        tags = [tag.text for tag in quote_element.find_all('a', class_='tag')]
        # Записуємо дані про quote
        quotes.append({
            'tags': tags,
            'author': author_name,
            'quote': quote_text
        })
        # Перевіряємо чи автор вже доданий до словника
        if author_name not in authors_dict:
            author_info = scrape_author_info(author_link)
            authors_dict[author_name] = author_info

# Функція для отримання інформації про автора
def scrape_author_info(author_link):
    response = requests.get(f"http://quotes.toscrape.com{author_link}")
    soup = BeautifulSoup(response.text, 'html.parser')
    fullname = soup.find('h3', class_='author-title').text.strip()
    born_date = soup.find('span', class_='author-born-date').text.strip()
    born_location = soup.find('span', class_='author-born-location').text.strip()
    description = soup.find('div', class_='author-description').text.strip()
    author_info = {
        'fullname': fullname,
        'born_date': born_date,
        'born_location': born_location,
        'description': description
    }
    return author_info

# Функція для скрапінга всіх сторінок
def scrape_all_pages(base_url):
    page_number = 1
    while True:
        url = f"{base_url}/page/{page_number}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        scrape_page(url)
        next_button = soup.find('li', class_='next')
        if next_button:
            page_number += 1
        else:
            break

# Основна функція для скрапінга
def main():
    base_url = "http://quotes.toscrape.com"
    scrape_all_pages(base_url)

    # Зберігаємо дані у файли JSON
    with open('quotes.json', 'w', encoding='utf-8') as quotes_file:
        json.dump(quotes, quotes_file, ensure_ascii=False, indent=4)
    
    with open('authors.json', 'w', encoding='utf-8') as authors_file:
        # Зберігамо значення словника (інформацію про авторів без дублювання ) 
        json.dump(list(authors_dict.values()), authors_file, ensure_ascii=False, indent=4)


    
if __name__ == "__main__":
    main()