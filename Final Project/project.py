"""
    Script Name: ETL for Bovespa Index Composition
    Author: Kevyn A. Marcelino
    Date Created: 2024-12-31
    Last Modified: 
    Version: 1.0

    Description:
        Python script for downloading, processing, and saving the Bovespa Index (IBOV) daily composition data & saving in an Excel file.

    Contact:
        - Email: kevyn.marcelino@usp.br / kevyn.lino@gmail.com
        - GitHub: [https://github.com/k-marcelino]
"""
### IMPORTS ###
import json
import requests
import pandas as pd


def main():
    # Retrieves daily information from Bovespa's Index composition using the URL provided by B3 and exports it to an Excel file.
    URL = 'https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay/eyJpbmRleCI6IklCT1YiLCJsYW5ndWFnZSI6InB0LWJyIn0='

    r = request_data(URL)
    data, date = transform(r)
    export(data, date)


def request_data(url):
    """
    Requests data from url provided.

    :param url: Constant from B3 website
    :return: response content from the url
    """
    session = requests.Session()
    response = session.get(url, verify=False)
    response.raise_for_status()
    
    return response


def transform(response):
    """
    Transforms data into final output.
        Reads json from content and normalizes it into a DataFrame.
        Drops unnecessary columns and transforms 'part' and 'theoricalQty' columns.
        Transforms numerical columns
    :param content: Content from the request
    :return: DataFrame with transformed data
    """
    # Transforming Data
    comp_ibov = pd.json_normalize(json.loads(response.content), record_path=['results'])
    comp_ibov.drop(columns=['segment', 'partAcum'], inplace=True)
    comp_ibov['part'] = comp_ibov['part'].apply(lambda x: float(x.replace(',', '.'))/100)
    comp_ibov['theoricalQty'] = comp_ibov['theoricalQty'].apply(lambda x: int(x.replace('.', '')))
    comp_ibov = comp_ibov.sort_values(by=['part'], ascending=False).reset_index(drop=True)

    # Transforming Date
    date = pd.json_normalize(json.loads(response.content))
    date = pd.to_datetime(date['header.date'], format='%d/%m/%y').dt.strftime('%Y%m%d').values[0]

    return comp_ibov, date


def export(data, date):
    """
    Export data to excel file.

    :param data: Ibovespa Composition
    :param date: Date of the composition
    :return: None
    """
    data.to_excel(f'outputs/{date}_comp_ibov.xlsx', index=False)


if __name__ == "__main__":
    main()