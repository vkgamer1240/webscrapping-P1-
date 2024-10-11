# webscrapping-P1-
my first webscraping project(ipl auction 2024)
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.iplt20.com/auction'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

teams = []
funds_remaining_list = []
overseas_players_list = []
total_players_list = []

main_div = soup.find('div', class_='auction-grid-view mt-3')

team_names = main_div.find_all('div', class_='agv-team-name')
for team in team_names:
    teams.append(team.text.strip())

fund_divs = main_div.find_all('div', class_='avg-bottom')

for fund_div in fund_divs:
    # Funds Remaining
    funds_remaining = fund_div.find('span', class_='fr-fund').text.strip()
    funds_remaining_list.append(funds_remaining)
    
    # Overseas Players and Total Players
    ul_tag = fund_div.find('ul', class_='mb-0 px-1')
    li_tags = ul_tag.find_all('li')
    
    overseas_players = li_tags[0].find('span', class_='fr-fund').text.strip()
    total_players = li_tags[1].find('span', class_='fr-fund').text.strip()
    
    overseas_players_list.append(overseas_players)
    total_players_list.append(total_players)

df = pd.DataFrame({
    'Team Name': teams,
    'Funds Remaining': funds_remaining_list,
    'Overseas Players': overseas_players_list,
    'Total Players': total_players_list
})
df.to_excel("overview.xlsx", index=False)

print(df)
