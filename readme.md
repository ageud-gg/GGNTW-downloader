# GGNTW Bulk Downloader #

This code is written in python and it basically uses ggntw api to download the mods of choice.

## Requirements (all built in) ##
* webbrowser
* random
* requests
* time

## How to use ##
1. Put all your links in list.txt
2. Put proxies in proxies.txt [(proxyscrape)](https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=ipport&format=text)
3. Run ggntw.py
   
Successful links will be put in success.txt.

If the downloader cant download one file, download it manually but make sure to stop the code so it can write to success.txt (and also remove previously downloaded mods from list.txt).

###### protected by MIT license you are granted permission to use, modify, and distribute the software, with the condition that the original copyright notice and the license text are retained in the redistributed software. ######
