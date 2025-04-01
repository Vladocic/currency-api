from models import Currency, CurrencyDelete, CurrencyUpdate
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse,HTMLResponse
from db_manager import get_all_currencies, create_table, get_filter_currencies, html_table, add_request_to_db, update_table, delete_multiple_currencies_from_db
from exchange import fetch_and_parse_exchange_rates



create_table()

fetch_and_parse_exchange_rates()


app = FastAPI()

@app.get("/currencies")
async def get_currencies(request:Request):
    if not request.query_params:
        return JSONResponse(
        content=get_all_currencies(),
        media_type="application/json; charset=utf-8"
    )

    codes = request.query_params.get("codes")
    if codes:
        code = codes.split(',')
        table = get_filter_currencies(code)

        if table:
            table_html = html_table(table)
            return HTMLResponse(content=table_html, media_type="text/html")

        else:
            return HTMLResponse(content=f"<h2>Валюты {', '.join(code)} не найдены.</h2>", media_type="text/html")
    else:
        return HTMLResponse(content=f"<h2>Валюты не указаны!</h2>", media_type="text/html")


# /currencies?num_code=840&char_code=USD&unit=2&name=Toncoin&name=100
# uvicorn main:app --reload
@app.post("/currencies")
def add_currency(currency: Currency):
    result = add_request_to_db(currency.num_code,currency.char_code,currency.unit,currency.name,currency.rate)
    return HTMLResponse(content=f"<h2>{result}</h2>", media_type="text/html")


@app.patch("/currencies")
def update_currency(currency:CurrencyUpdate):
    text = {i:y for i,y in currency.dict().items() if y is not None}
    update_table(text)
    response = {
        "status": "success",
        "message": "Запись успешно обновлена",
        "updated_fields": text
    }
    return JSONResponse(content=response, media_type="application/json; charset=utf-8")

    
@app.delete("/currencies")
def del_currency(currency:CurrencyDelete):
    delete_data = {i:y for i,y in currency.dict().items() if y is not None}

    if not delete_data:
        raise HTTPException(status_code=400, detail="At least one field must be provided for deletion")
    else:
        delete_multiple_currencies_from_db(delete_data)






@app.get("/currencies_html")
def get_data_html():
    currencies = get_all_currencies()
    table_html = html_table(currencies)
    return HTMLResponse(content=table_html, media_type="text/html")

    