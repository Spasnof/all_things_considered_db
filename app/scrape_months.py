import datetime
import calendar
import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.npr.org/programs/all-things-considered/archive'

def monthendrange(begin, end):
    if begin < end:
        test = end.__gt__
    else:
        test = end.__lt__

    while test(begin):
        monthEndDate = calendar.monthrange(begin.year, begin.month)[1]
        begin = begin.replace(day=monthEndDate)
        yield begin
        begin += datetime.timedelta(1)

start = datetime.date(2002,1,1)
end = datetime.date(2005,1,1)

for d in monthendrange(start,end):
    r = requests.get(f'{baseurl}?date={d.month}-{d.day}-{d.year}')
    file = open(f'../data/months/archive_page{d.month}_{d.day}_{d.year}.txt','w')
    file.write(str(r.content))
    file.close()