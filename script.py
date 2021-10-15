# Import libraries
import requests
import datetime as dt
from bs4 import BeautifulSoup

# Creates and Returns a list of all the links and checks if inputed file exists
def create_links(url_file: str) -> list:
    # Sets empty list where urls will be appended to
    gpu_url_list = []

    # Tries to open file, if able to then it will append urls on each line to gpu_url_list
    try:
        with open(url_file, 'r') as links:
            for link in links:
                gpu_url_list.append(link.replace('\n', ''))
        print('Your data has been collected. Please wait for your data to process...')
        return gpu_url_list
    # If file can't be opened, will print statement below 
    except IOError:
        print('File entered is not accessible. Please enter a valid file and rerun the script.')


# Creates and Returns a list of lists containing the extracted information from each URL Ex: [[Name, Price, Availability, Link]]
def extract_data(file_urls: list) -> list:
    # Follows the assertion of create_links(), addressing the user that entered file does not exist
    assert type(file_urls) == list, 'The ".txt" file you entered does not exist. Please enter a valid file and rerun the script.'
    # Checks if the entered file contains no information
    assert len(file_urls) > 0, 'The ".txt" file you are accessing contains no content. Please enter a valid file and rerun the script.'
    
    # Sets count for printing updates on url completion
    count = 1
    
    # HEADERS based on operating system and search engine **Refer to README.md to learn how to change**
    url_headers = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    
    # Creates a list where lists of data will organized into after each iteration 
    data_list = []

    # Iterates through each url in the file_urls list
    for url in file_urls:
        # Sends HTTP request for the current url
        page = requests.get(url, headers=url_headers)
        assert page.status_code < 400, f'The url on line {count}: {url} is not a valid url. Please edit your ".txt" and rerun the script.'
        # Creates soup object from BeautifulSoup
        soup = BeautifulSoup(page.content, 'html.parser')

        # Finds item name
        item = soup.find(id='productTitle')
        # Finds item price
        price = soup.find(id='priceblock_ourprice')
        # Finds item availability
        availability = soup.find(id='availability')

        # Checks each item string for empty spaces and removes them
        item_name = item.text.strip().replace(',', '')
        item_price = price.text.strip().replace(',', '')
        item_availability = availability.text.strip()

        # Checks each item if it exists and if not, then will replace it's attribute with "NA"
        if len(item_price) == 0:
            item_price = 'NA'

        if len(item_availability) == 0:
            item_availability = 'NA'

        # Creates list that will store item, price, availability, and link inside of data_list initiated above (changes each iteration)
        current_data = [item_name, item_price, item_availability, url]
        # Appends current_data to data_list initiated above ^^
        data_list.append(current_data)
       
        # Prints updates onto the terminal of each link getting processed
        if count == 1:
            print('1 link  processed...')
            count += 1
        else:
            print(f'{count} links processed...')
            count += 1

    return data_list
    

def sort_and_append_data(extracted_data: list) -> None:
    # Creates a ".csv" file called "price_tracker.csv" if not already existing and appends to the file through each iteration
    csv_file = open('price_tracker.csv', 'a')

    # Initiates datetime object in the format: day-of-the-week month day(number) time year
    date_and_time = dt.datetime.now().strftime("%c")

    # Appends the headers to the .csv file
    csv_file.write(f'{date_and_time},ITEM,PRICE,AVAILABILITY,LINK\n')

    # Sorts the extracted data based on price (1st index of each list)from least to greatest
    sorted_data = sorted(extracted_data, key=lambda x: float(x[1].replace('$', '')))

    # Writes the name, price, availability, and link in csv format to the file
    for data in sorted_data:
        csv_file.write(f',{data[0]},{data[1]},{data[2]},{data[3]}\n')

    # Closes file when done
    csv_file.close()


# Main function to execute code and gather user input
def main():
    print('\n                                          Hello! Welcome to GPU Please!')
    print('          The following program is able to keep track of all your dream gpu prices and accessibilty on amazon!\n')
    file = input('Please enter the name of your ".txt" file: ')
    print()
    links = create_links(file)
    data = extract_data(links)
    sort_and_append_data(data)
    print('...Your data has been fully processed and organized into the "price_tracker.csv" file. Check the file to see the results!\n')


# Executes script
if __name__ == '__main__':
    main()