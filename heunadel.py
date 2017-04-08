import sys
import getopt
import requests
import random
import datetime
import time
from bs4 import BeautifulSoup

from helper import getexternallinks, getextension, disclaimer

wordlist = ['rainbow', 'stack', 'answer', 'overflow', 'list', 'rocks', 'sun', 'earth', 'test', 'king', 'doctor',
            'galaxy', 'titanic', 'support', 'silver', 'hulk']

duckduckurl = 'https://duckduckgo.com/html/'
yahoourl = 'http://search.yahoo.com/search?p='

# Pseudo RAND
random.seed(datetime.datetime.now())

timeout = 10

extensions = ['.jpg', '.pdf', '.gif', '.pdf', '.ps', '.gz', '.tar', '.tgz', '.zip', '.ppt', '.txt', '.doc', '.mp3',
              '.wav', '.mpg', '.mov', '.avi', '.exe', '.qt', '.jar', '.Z', '.mat', '.wrl']

switch = False

# Filled with unused URLs. These URLs get used before duckduckgo/yahoo to prevent reaching query limits.
backup_urllist = []


def getrandurl(url):
    try:
        res = requests.get(url, timeout=timeout)
        soup = BeautifulSoup(res.content, "lxml")
        ext = getexternallinks(soup, url)
    except:
        return None

    if len(ext) == 0:
        return None
    else:
        if len(backup_urllist) < 1000:
            backup_urllist.extend(ext)
        rand = random.randint(0, len(ext) - 1)
        newurl = ext[rand]
        if getextension(newurl) not in extensions:
            print newurl
            return newurl
        else:
            return None


def geturlyahoo():
    word = random.choice(wordlist)

    print "yahoo: " + word

    starturl = yahoourl + word

    try:
        res = requests.get(starturl, timeout=timeout)
        print res
        soup = BeautifulSoup(res.content, "lxml")
        ext = getexternallinks(soup, starturl)
    except:
        return None

    if len(ext) == 0:
        return None
    else:
        if len(backup_urllist) < 1000:
            backup_urllist.extend(ext)
        rand = random.randint(0, len(ext) - 1)
        newurl = ext[rand]
        print word, newurl
        return newurl


def geturlduckduck():
    word = random.choice(wordlist)

    params = {
        'q': word,
    }

    print "duckduckgo: " + word

    try:
        res = requests.post(duckduckurl, data=params)
        print res
        soup = BeautifulSoup(res.content, "lxml")
        ext = getexternallinks(soup, duckduckurl)
    except:
        return None

    if len(ext) == 0:
        return None
    else:
        if len(backup_urllist) < 1000:
            backup_urllist.extend(ext)
        rand = random.randint(0, len(ext) - 1)
        newurl = ext[rand]
        print word, newurl
        return newurl


def getstarturl():
    global switch

    if len(backup_urllist) > 0:
        rand = random.randint(0, len(backup_urllist) - 1)
        newurl = backup_urllist.pop(rand)
        print "backup URL"
        return newurl

    if switch == False:
        switch = True
        return geturlduckduck()
    else:
        switch = False
        return geturlyahoo()


def start():
    version()

    newurl = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:t:u:", ["help", "timeout", "url"])
    except getopt.GetoptError:
        help()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help()
            sys.exit()
        elif opt in ("-t", "--timeout"):
            global timeout
            timeout = arg
        elif opt in ("-u", "--url"):
            newurl = arg
            print arg
        else:
            newurl = getstarturl()

    while True:
        if newurl == None:
            newurl = getstarturl()
        newurl = getrandurl(newurl)
        time.sleep(0.2)


def version():
    sys.stdout.write("\nProject HeuNadel 0.1\n")
    sys.stdout.write("\n")
    sys.stdout.write("Author: Johannes Schroeter - www.devwerks.net\n\n")
    sys.stdout.write(disclaimer)
    sys.stdout.write("\n\n")

def help():
    sys.stdout.write("heunadel.py -t/--timeout -u/--url\n")
    sys.stdout.write("Example: heunadel.py -t 5\n")
    sys.stdout.write("Example: heunadel.py -u https://devwerks.net/\n")
    sys.stdout.write("\n")


def main():
    start()
    sys.exit()


if __name__ == "__main__":
    main()
