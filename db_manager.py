import sqlite3
import config


def create_table():
    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS currencies (
            num_code TEXT,
            char_code TEXT,
            unit INTEGER,
            name TEXT,
            rate REAL,
            UNIQUE (num_code,char_code)               
        )
    ''')
    conn.commit()
    conn.close()


def html_table(currencies):
    table_html = """
    <table border="1">
        <tr>
            <th>Номер кода</th>
            <th>Код валюты</th>
            <th>Единица</th>
            <th>Название</th>
            <th>Курс</th>
        </tr>
    """
    for currency in currencies:
        table_html += f"""
        <tr>
            <td>{currency['num_code']}</td>
            <td>{currency['char_code']}</td>
            <td>{currency['unit']}</td>
            <td>{currency['name']}</td>
            <td>{currency['rate']}</td>
        </tr>
        """

    table_html += "</table>"
    return table_html 
        

def fill_in_table(rows):
    base = []
    for row in rows[1:]:
        cols = row.find_all("td")
        base.append([col.text.strip() for col in cols ])  

    currencies = []
    for i in base:
        currency = {
            "num_code": i[0],
            "char_code": i[1],
            "unit": i[2],
            "name": i[3],
            "rate": i[4],
            }
        currencies.append(currency)

    for i in currencies:
        add_request_to_db(i['num_code'], i['char_code'], i['unit'], i['name'], i['rate'])


def add_request_to_db(num_code,char_code,unit,name,rate):
    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT OR IGNORE INTO currencies(num_code, char_code, unit, name, rate)
        VALUES (?, ?, ?, ?, ?)''', (num_code,char_code,unit,name,rate))
    
    conn.commit()

    if cursor.rowcount == 0:
        result = f"Запись с кодом {char_code} уже существует, добавление проигнорировано."
    else:
        result = f"Запись с кодом {char_code} успешно добавлена."

    conn.close()
    return result


def update_table(update_data:dict):
    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()
    sql_text = 'UPDATE currencies SET ' + ', '.join([f'{i} =?' for i in update_data if i is not 'num_code']) + ' WHERE num_code = ?'
    value = [y for x,y in update_data.items()][1:]
    value.append(update_data['num_code'])
    cursor.execute(sql_text,value)
    conn.commit()
    conn.close()


def delete_multiple_currencies_from_db(delete_data:dict):
    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()
    sql_text= 'DELETE FROM currencies WHERE ' + ' OR '.join(  [f"{i} = ?" if len(y) == 1 else f"{i} IN ({('?, '*len(y))[:-2]})" for i,y in delete_data.items()])
    value = [i for y in delete_data.values() for i in y]
    print(sql_text,value)
    cursor.execute(sql_text,value)
    conn.commit()
    conn.close()
    

def get_all_currencies():
    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM currencies')
    table = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in table]


def get_filter_currencies(codes):
    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()
    query = f"SELECT * FROM currencies WHERE char_code IN ({','.join(['?' for i in codes])})"
    cursor.execute(query, tuple(codes))
    table = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in table]




