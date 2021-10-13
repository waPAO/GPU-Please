from bs4 import BeautifulSoup
import requests

# Create a list of all the links
gpu_link_list = []
with open('gpu_links.txt', 'r') as links:
    for link in links:
        gpu_link_list.append(link.replace('\n', ''))

#csv_file = open('price_tracker.csv', 'a')
url_headers = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
url = gpu_link_list[1]
page = requests.get(url, headers=url_headers)
soup = BeautifulSoup(page.content, 'html.parser')

item = soup.find(id='productTitle')
print(item.text.strip())