import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'currency.db')

url = "https://www.cbr.ru/currency_base/daily/" 
header = {"User-Agent": "Mozilla/5.0"}
