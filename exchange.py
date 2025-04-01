import requests
from config import url,header
from bs4 import BeautifulSoup
from db_manager import fill_in_table,add_request_to_db



def fetch_and_parse_exchange_rates():
    response = requests.get(url, headers=header)
    response.encoding = 'utf-8' 
    html = response.text
    soup = BeautifulSoup(html, "lxml")

    table = soup.find('table', class_="data")
    rows = table.find_all("tr")
    
    fill_in_table(rows)