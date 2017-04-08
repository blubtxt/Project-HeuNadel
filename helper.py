import os
import re

disclaimer = """[!] legal disclaimer: It is the end user's responsibility to obey all applicable local, state and federal laws.
Developers assume no liability and are not responsible for any misuse or damage caused by this program"""

def getexternallinks(bsobj, excludeurl):
    externallinks = []
    for link in bsobj.findAll("a", href=re.compile("^(http|www)((?!"+excludeurl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externallinks:
                externallinks.append(link.attrs['href'])
    return externallinks


def getextension(filename):
    (base, ext) = os.path.splitext(filename)
    return ext
