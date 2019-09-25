# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

nbk_url = 'https://english.mubasher.info/markets/BK/stocks/NBK/profile'
hcc_url = 'https://english.mubasher.info/markets/BK/stocks/HCC/profile'
wins_url = 'https://english.mubasher.info/markets/BK/stocks/WINS/profile'

companies = ['NBK','HCC','WINS']


def get_stock_value (option , url):

	page = urlopen(url).read()

	soup = BeautifulSoup(page, 'html.parser')

	closing_price_box = soup.find('div' , attrs={'class':'market-summary__last-price'})

	closing_price  = closing_price_box.text

	volume_box = soup.find('div' , attrs= {'class':'market-summary__total'}).find('div' , attrs= {'class':'market-summary__block-row'}).find('span' , attrs={'class':'market-summary__block-number'})

	volume = volume_box.text

	turnover_box= soup.find('div' , attrs= {'class':'market-summary__total'}).find_all(attrs= {'class':'market-summary__block-row'})

	turnover_box  = turnover_box[1]. find('span',attrs={'class':'market-summary__block-number'})

	turnover = turnover_box.text

	print ('\n%s  Stocks : \n\tClosing Price : %s\n\tVolume : %s\n\tTurnover : %s\n' %(companies[option-1],closing_price,volume,turnover))



print ('\nChoose a company from the list:')
for i,n in enumerate(companies) : 
	print('\t%s- %s'%(i+1,n))

option = int(input())

if option == 1 :
	get_stock_value(option,nbk_url)
elif option == 2 :
	get_stock_value(option,hcc_url)
elif option == 3 :
	get_stock_value(option,wins_url)

else :
	print ('\nINVALID OPTION\n')

