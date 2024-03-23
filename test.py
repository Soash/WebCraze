import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

proxy_host = "190.110.226.162"
proxy_port = '80'


# Initialize Chrome webdriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument(f"--proxy-server=https://{proxy_host}:{proxy_port}")
# options.add_argument('--headless')
# driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome(service=service)


url = 'https://www.amazon.com/Best-Sellers-Audible-Books-Originals-Biographies-Memoirs/zgbs/audible/18571951011/ref=zg_bs_nav_audible_1'
driver.get(url)

# Waiting for the page to load properly (adjust the sleep time as needed)
time.sleep(15)



# Creating BeautifulSoup object from the page source of the category
soup = BeautifulSoup(driver.page_source, 'html.parser')

books = []
authors = []
ratings = []
num_reviews = []
prices = []
images = []

# Finding all h2 elements with class 'elementor-heading-title'

div_list = soup.find_all('div', {'id':'gridItemRoot'})

# for data in div_list:
#     book = data.find('div', class_='_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y').text.strip()
#     books.append(book)
#     author = data.find('span', class_='a-color-base').text.strip()
#     authors.append(author)
#     rating = data.find('span', class_='a-icon-alt').text.strip()
#     ratings.append(rating)

#     rating_elements = data.find('div', class_="a-icon-row").find_all('span', class_='a-size-small')
#     rating_count = rating_elements[-1].text.strip()
#     num_reviews.append(rating_count)

#     price = data.find('span', class_='p13n-sc-price').text.strip()
#     prices.append(price)
    
#     img = data.find('img', class_='a-dynamic-image p13n-sc-dynamic-image p13n-product-image')['src']
#     images.append(img)

for data in div_list:
    book_element = data.find('div', class_='_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y')
    author_element = data.find('span', class_='a-color-base')
    rating_element = data.find('span', class_='a-icon-alt')
    price_element = data.find('span', class_='p13n-sc-price')

    # Check if any of the elements are None
    if None in (book_element, author_element, rating_element, price_element):
        continue  # Skip this iteration if any element is missing

    book = book_element.text.strip()
    books.append(book)
    author = author_element.text.strip()
    authors.append(author)
    rating = rating_element.text.strip()
    ratings.append(rating)

    rating_elements = data.find('div', class_="a-icon-row").find_all('span', class_='a-size-small')
    rating_count = rating_elements[-1].text.strip()
    num_reviews.append(rating_count)

    price = price_element.text.strip()
    prices.append(price)
    
    img = data.find('img', class_='a-dynamic-image p13n-sc-dynamic-image p13n-product-image')['src']
    images.append(img)

name = 'test'
print(f'parsing: {name} done')

data = pd.DataFrame({'book':books, 'author':authors,'rating':ratings, 'num_reviews':num_reviews, 'price':prices, 'img':images})
data.to_csv(f'{name}.csv')
driver.quit()
