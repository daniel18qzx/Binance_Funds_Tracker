import pandas as pd

class Settings():

    def __init__(self):
        #API Key
        self.api_key = 'api_key'
        self.secret_key = 'secret_key'

        #Output formats
        self.outputPath = 'Track.xlsx'
        self.outputSheet = 'Sheet1'
        self.timezone = 'Asia/Taipei'
        self.log_t = pd.DataFrame([])
        self.round = 5
        self.roundPercentage = 2

        #Trades
        self.tradesCurrency = {

            'ETH':'USDT',
            'BCC':'USDT',
            'BNB':'USDT',
            'KNC':'ETH',
            'ETC':'ETH',
            'ADA':'ETH',
            'NEO':'ETH',
            'FUN':'ETH'
        }

        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)

        #Donate me at...
        self.donateMeAt = {

            'USDT' : '14ghxRPAPbfKWqzaqfRA48RvcJaLd89xDJ',
            'ETH' : '0x4bcb4c89557fae210fe47d8f50b191936318c27d',
            'BTC' : '1DRoMGRkTZA5Rz6vX3p3Wxa4ZPQocQHvc8'
        }
