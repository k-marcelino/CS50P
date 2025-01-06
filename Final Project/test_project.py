import os
from project import request_data, transform, export

URL = 'https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay/eyJpbmRleCI6IklCT1YiLCJsYW5ndWFnZSI6InB0LWJyIn0='

r = request_data(URL)
data, date = transform(r)
export(data, date)

def test_request_data():
    # Testing Connection
    assert(r.status_code == 200)
    # Testing Content Type
    assert(r.headers['Content-Type'] == 'application/json; charset=utf-8')


def test_transform():
    assert(len(data) > 0)
    # Testing date format
    assert(len(date) == 8)
    assert(data['part'].sum() == 1)



def test_export():
    # Testing Export
    assert(export(data, date) == None)
    # Testing if file exists
    assert(os.path.isfile(f'outputs/{date}_comp_ibov.xlsx'))
