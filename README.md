# Project HeuNadel
> *"Die Nadel im Heuhaufen suchen" / "find a needle in a haystack"*
> German phrase


### What does Project HeuNadel do?
It queries DuckDuckGo/Yahoo for random words and picks one of the results. 
Then retrieves that page and looks for further URLs there, picks another random one and retrieves that, and so long. 


### Why?:
An average user doesn't generate that many unique connections. By using Project HeuNadel this changes drastically. 
The user surfing won't be the only observable connections coming from the computer. 
There will much rather be many connections originating from the computer. 
This way it is very hard to tell which connections are actually made by the user thus generating plausible deniability.


### Usage:
```
heunadel.py -t/--timeout -u/--url

Example: heunadel.py -t 5

Example: heunadel.py -u https://devwerks.net/
```

### Contact:
If you run into issues, feel free to get on touch on Twitter, check the current issues or create a new one. 
Patches are also welcome.

http://devwerks.net
