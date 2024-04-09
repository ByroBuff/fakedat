import random
import datetime

def main(format="%B %d, %Y", start="1970-01-01", end="2000-01-01"):
    start = datetime.datetime.strptime(start, "%Y-%m-%d")
    end = datetime.datetime.strptime(end, "%Y-%m-%d")
    return (start + (end - start) * random.random()).strftime(format)