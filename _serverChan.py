import requests
import logging
import urllib.parse
from config import APIKEY

def alert(url):
    logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(asctime)s - %(name)s - %(message)s')
    sendMsg(url)
    
def test():
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(asctime)s - %(name)s - %(message)s')
    sendMsg('http://<test-parameter>')
    
def sendMsg(url):
    title = '[kWordSentry]'
    msg = "kWordSentry发现有关键词消失：{0}".format(url)
    msg = urllib.parse.quote_plus(msg)
    api = "https://sctapi.ftqq.com/{0}.send?title={1}&desp={2}".format(APIKEY, title, msg)
    try:
        r = requests.get(api)
    except Exception as e:
        logging.warning('Failed to connect to ServerChan: {0}'.format(e))
        return
    logging.info('Done.')

if __name__ == "__main__":
    print('TESTING...')
    test()
