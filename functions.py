import pandas as pd
from openpyxl import load_workbook
from pathlib import Path
from tabulate import tabulate

def track(mainClass):
	account = mainClass.rest_client.get_account()
	prices = mainClass.rest_client.get_all_tickers()

	log_t = mainClass.settings.log_t
	MktValue_track = pd.DataFrame([])
	MktValueTot = 0

	for price in prices:
		if price['symbol'] == 'BTCUSDT':
			BTCUSDT_price = float(price['price'])

	for balance in account['balances']:
		symbol_price = 0
		if (float(balance['free'])+float(balance['locked']) == 0):
			continue
		else:
			if balance['asset'] == 'USDT':
				log = pd.DataFrame([balance['asset'],round(float(balance['free'])+float(balance['locked']),mainClass.settings.round),(float(balance['free'])+float(balance['locked'])),0,"",""])
			else:
				tp = balance['asset']+'BTC'
				for price in prices:
					if price['symbol'] == tp:
						symbol_price = float(price['price'])
						symbol_price = symbol_price * BTCUSDT_price
				
				for price in prices:
					if price['symbol'] == balance['asset']+mainClass.settings.tradesCurrency[balance['asset']]:
						current_price = float(price['price'])
						
				accuV = 0
				accuQ = 0
				for trade in mainClass.rest_client.get_my_trades(symbol=balance['asset']+mainClass.settings.tradesCurrency[balance['asset']]):
					if trade['isBuyer'] == True:
						accuV = accuV + float(trade['price']) * float(trade['qty'])
						accuQ = accuQ + float(trade['qty'])
					elif trade['isBuyer'] == False:
						accuV = accuV - float(trade['price']) * float(trade['qty'])
						accuQ = accuQ - float(trade['qty'])
				log = pd.DataFrame([balance['asset'],round(float(balance['free'])+float(balance['locked']),mainClass.settings.round),round((float(balance['free'])+float(balance['locked']))*symbol_price,mainClass.settings.round),0,str(round(accuV/accuQ,mainClass.settings.round))+" "+mainClass.settings.tradesCurrency[balance['asset']],str(round(current_price,mainClass.settings.round))+" "+mainClass.settings.tradesCurrency[balance['asset']]])
		MktValueTot = MktValueTot+log.iloc[2,0]
		log = log.transpose()
		log.columns = ['Asset','Total Balance','Market Value in USDT','%','Cost','Current Price']
		log_t = log_t.append(log)

	log_t = log_t.sort_values(by='Market Value in USDT', ascending=False)
	log_t.reset_index()
	log_t['%']=round(log_t.iloc[:,2].astype(float)/MktValueTot,mainClass.settings.roundPercentage+2)*100

	print(mainClass.time_now.strftime('%Y-%m-%d %H:%M:%S'))
	print("Total Market Value in USDT: "+str(MktValueTot))
	print("")
	print(tabulate(log_t, headers='keys', tablefmt='psql',numalign="right",stralign='right'))
	print("")
	
	log_v = pd.DataFrame([mainClass.time_now.strftime('%Y-%m-%d %H:%M:%S'),MktValueTot])
	log_v = log_v.transpose()
	log_v.columns = ['Time','Market Value in USDT']
	MktValue_track = MktValue_track.append(log_v)
	return MktValue_track,log_t

def write_xls(DataFrameData,settings):
	my_file = Path(settings.outputPath)
	writer = pd.ExcelWriter('Track.xlsx')
	DataFrameData.to_excel(writer, settings.outputSheet,startrow=1)
	writer.save()

def sche(Sec,func):
	scheduler.add_job(func, 'interval', seconds=Sec, id='track')
	scheduler.start()