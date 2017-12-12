from settings import Settings
from binance.client import Client
import pytz
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

class mainClass():
    def __init__(self):
        self.settings=Settings()

        self.rest_client = Client(self.settings.api_key, self.settings.secret_key)
        self.rest_client.ping()

        self.tz = pytz.timezone(self.settings.timezone)
        self.scheduler = BlockingScheduler()
        self.time_now = datetime.now()