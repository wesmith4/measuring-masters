import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

DATA_URL = "https://www.golfstats.com/search/?player=&yr=1936&tour=Majors&tournament=Masters&box=&submit=go"

def getTableByYear(year):
    DATA_URL = "https://www.golfstats.com/search/?player=&yr={}&tour=Majors&tournament=Masters&box=&submit=go".format(year)

    soup = BeautifulSoup(urlopen(DATA_URL), "html.parser")
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table),header=1)
    df[0].to_csv('./data/{}data.csv'.format(year))
    return df[0]

for year in range(1934,2020):
    getTableByYear(year)
getTableByYear(2021)
