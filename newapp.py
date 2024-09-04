import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("https://webscraper.io/test-sites/tables/tables-semantically-correct")


def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    info = []

    names = soup.find_all("table", {'class': 'table table-bordered'})
    def get_info(names):

        title_info = names.contents[1].find('tr').text.strip()

        num_of_rows = len(names.contents[3].find_all('tr'))

        for i in range(num_of_rows):   
            body_info = names.contents[3].find_all('tr')[i].text.strip()

        info.append({
            "#" : title_info,
            "First Name" : body_info.split("\n")[1],
            "Last Name": body_info.split("\n")[2],
            "Username" : body_info.split("\n")[3] 
            })
        
    get_info(names[0])


    keys = info[0].keys()

    with open('C:\\Users\\moham\\OneDrive\\Desktop\\flask playground\\matches-info.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(info)
        print("creating file is Done!")

main(page)