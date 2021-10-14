# Import libraries
import requests
from bs4 import BeautifulSoup

# Creates a list of all the links and checks if inputed file exists
def create_links(url_file):
    gpu_url_list = []
    try:
        with open(url_file, 'r') as links:
            for link in links:
                gpu_url_list.append(link.replace('\n', ''))
        print('Your data has been collected. Please wait for your data to process...\n')
        return gpu_url_list
    except IOError:
        print('File entered is not accessible. Please enter a valid file and rerun the script.')

# 
def organize_data(file_urls: list):
    # Creates a .csv file called "price_tracker.csv" and appends to the file through each iteration
    csv_file = open('price_tracker.csv', 'a')
    # Appends the headers to the .csv file
    csv_file.write('ITEM,PRICE,AVAILABILITY,LINK\n')

    url_headers = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    # Iterates through each url in the file_urls list
    for url in file_urls:
        # Sends HTTP request for the current url
        page = requests.get(url, headers=url_headers)
        # Creates soup object from BeautifulSoup
        soup = BeautifulSoup(page.content, 'html.parser')

        # Finds item name
        item = soup.find(id='productTitle')
        # Finds item price
        price = soup.find(id='priceblock_ourprice')
        # Finds item availability
        availability = soup.find(id='availability')

        # Refines each item
        item_name = item.text.strip().replace(',', '')
        item_price = price.text.strip().replace(',', '')
        if len(item_price) == 0:
            item_price = 'NA'
        item_availability = availability.text.strip()
        if len(item_availability) == 0:
            item_availability = 'NA'

        # Writes the name, price, availability, and link in csv format to the file
        csv_file.write(f'{item_name},{item_price},{item_availability},{url}\n')

    csv_file.close()

if __name__ == '__main__':
    print('\n                                          Hello! Welcome to GPU Please!')
    print('          The following program is able to keep track of all your dream gpu prices and accessibilty on amazon!\n\n')
    file = input('Please enter the file name of your ".txt": ')
    links = create_links(file)
    organize_data(links)
    print('...Your data has been organized into the "price_tracker.csv" file. Check the file to see the results.')
    