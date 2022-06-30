import requests
import logging
from time import sleep
import re
import config as cfg
from urllist import urllist
import alarm

FOUND_LIST='foundList.txt'

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(asctime)s - %(name)s - %(message)s')

def getContent(url):
    try:
        r = requests.get(url, headers=cfg.HEADER)
        r.raise_for_status()
        return r.text
    except Exception as e:
        logging.warning('Something went wrong: {0}'.format(e))
        return ''
        
def checkContent(url, content, kWords):
    if content == '':
        return
    if re.search(r'{}'.format(kWords), content) == None:
        logging.info('!!!kWord not found, page might be changed!!!')
        logging.info("!!!@URL: %s" % (url,))
        if not checkAlreadyFound(url):
            logging.info("!!!Calling alarm module...")
            alarm.trigger(url)
        else:
            logging.info("!!!Has been found already")

def checkAlreadyFound(url):
    fRead = open(FOUND_LIST,'r')
    foundList = fRead.readlines()
    for i in foundList:
        if i==url:
            return True
    fWrite = open(FOUND_LIST,'w+')
    fWrite.write(url)
    fWrite.close()
    fRead.close()
    return False

        
def loop():
    while True:
        logging.info('Checking...Starting a loop')
        for url in urllist:
            content = getContent(url)
            checkContent(url, content, urllist[url])
        logging.info("Done. Goto sleep for %ssec." % (cfg.DURATION))
        sleep(cfg.DURATION)
    

if __name__ == "__main__":
    print('''
  _   __        __            _ ____             _              
 | | _\ \      / /__  _ __ __| / ___|  ___ _ __ | |_ _ __ _   _ 
 | |/ /\ \ /\ / / _ \| '__/ _` \___ \ / _ \ '_ \| __| '__| | | |
 |   <  \ V  V / (_) | | | (_| |___) |  __/ | | | |_| |  | |_| |
 |_|\_\  \_/\_/ \___/|_|  \__,_|____/ \___|_| |_|\__|_|   \__, |
                                                          |___/ 
        ''')
    logging.info('Starting sentry duty...')
    f = open(FOUND_LIST,'w')
    f.close()
    loop()
