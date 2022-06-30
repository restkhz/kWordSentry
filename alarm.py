from config import ALARM
import importlib

def trigger(url):
    if isinstance(ALARM,list):
        for a in ALARM:
            alarm = importlib.import_module(a)
            alarm.alert(url)
    else:
        alarm = importlib.import_module(ALARM)
        alarm.alert(url)
