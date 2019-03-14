#coding:utf-8
from datetime import datetime


class Client:
    def __init__(self):
        pass
        
    def getGreeting(self):
        now_time = int(datetime.now().strftime('%H'))
        if 0 <= now_time < 12:
            return 'Good morning'
        elif 12 <= now_time < 18:
            return 'Good afternoon'
        elif 18 <= now_time < 24:
            return 'Good evening'
    


