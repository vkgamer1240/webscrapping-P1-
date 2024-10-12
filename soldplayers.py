import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction"  

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

tables = soup.find_all("table")

all_data = []

if len(tables) >= 11:
    for i in range(2, 11):
        table = tables[i]
        
        for row in table.find_all("tr"):
            columns = row.find_all("td")
            if columns:
                player_name = columns[0].text.strip()
                nationality = columns[1].text.strip()
                player_type = columns[2].text.strip()
                price_paid = columns[3].text.strip().replace(",", "")
                all_data.append([player_name, nationality, player_type, price_paid, f"Table {i+1}"])  # Add table number
    
    df = pd.DataFrame(all_data, columns=['Player', 'Nationality', 'Type', 'Price Paid', 'Source Table'])
    
    
    print(df)
else:
    print("Less than ten tables found on the webpage.")
