# [x] find way to iterate through end of month dates for top level url
# example https://www.npr.org/programs/all-things-considered/archive?date=1-31-2002
# TODO for each top level url capture the html in ./data/months
# TODO for each date attempt to capture the data episode id
#  https://www.npr.org/programs/all-things-considered/2002/01/28/13020213/?showDate=2002-01-28
# for link in soup.find_all('article'):
# ...   print('data-episode-id' in repr(link))


import datetime
from datetime import timedelta
import calendar

def daterange(begin, end, delta=timedelta(1)):
    """Form a range of dates and iterate over them.

    Arguments:
    begin -- a date (or datetime) object; the beginning of the range.
    end   -- a date (or datetime) object; the end of the range.
    delta -- (optional) a timedelta object; how much to step each iteration.
             Default step is 1 day.

    Usage:

    """
    if not isinstance(delta, timedelta):
        delta = timedelta(delta)

    ZERO = timedelta(0)

    if begin < end:
        if delta <= ZERO:
            raise StopIteration
        test = end.__gt__
    else:
        if delta >= ZERO:
            raise StopIteration
        test = end.__lt__

    while test(begin):
        yield begin
        begin += delta

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
    print(f'https://www.npr.org/programs/all-things-considered/archive?date={d.month}-{d.day}-{d.year}')