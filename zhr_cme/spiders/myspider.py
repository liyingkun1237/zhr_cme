# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 14:25:56 2016

@author: yingkun.li
"""

import scrapy
from zhr_cme.items import ZhrCmeItem



'''
#agricultural
a='http://www.cmegroup.com/trading/agricultural/'
b='_product_calendar_futures.html'
contract_name_list=['grain-and-oilseed/soybean-oil','grain-and-oilseed/corn',
                    'grain-and-oilseed/mini-sized-corn',
                    'grain-and-oilseed/oats','grain-and-oilseed/soybean',
                    'grain-and-oilseed/mini-sized-soybean',
                    'grain-and-oilseed/soybean-meal',
                    'grain-and-oilseed/wheat',
                    'grain-and-oilseed/mini-sized-wheat',
                    'grain-and-oilseed/rough-rice',
                    'livestock/feeder-cattle','livestock/live-cattle',
                    'livestock/lean-hogs']
'''


'''

#Fx
a='http://www.cmegroup.com/trading/fx/'
b='_product_calendar_futures.html'
contract_name_list=['g10/australian-dollar','g10/british-pound','g10/canadian-dollar',
                    'g10/euro-currency','g10/japanese-yen','g10/new-zealand-dollar',
                    'g10/swiss-franc','e-micros/e-micro-australian-dollar',
                    'e-micros/e-micro-euro','e-micros/e-micro-british-pound']

'''

'''
#metal
a='http://www.cmegroup.com/trading/metals/precious/'
b='_product_calendar_futures.html'
contract_name_list=['gold','copper','silver','palladium','platinum']
'''


#energy
a='http://www.cmegroup.com/trading/energy/'
b='_product_calendar_futures.html'
contract_name_list=['crude-oil/light-sweet-crude',
                    'crude-oil/emini-crude-oil',
                    'refined-products/heating-oil',
                    'natural-gas/natural-gas',
                    'natural-gas/emini-natural-gas',
                    'refined-products/rbob-gasoline',
                    'crude-oil/brent-crude-oil-last-day']


'''
#equity index
a='http://www.cmegroup.com/trading/equity-index/'
b='_product_calendar_futures.html'
contract_name_list=['us-index/e-mini-dow','us-index/e-mini-nasdaq-100',
                    'us-index/sandp-500','us-index/e-mini-sandp500',
                    'international-index/nikkei-225-yen',
                    'international-index/e-mini-ftse-china-50-index']
'''

'''
#interest-rates
a='http://www.cmegroup.com/trading/interest-rates/'
b='_product_calendar_futures.html'
contract_name_list=['us-treasury/5-year-us-treasury-note',
                    'us-treasury/10-year-us-treasury-note',
                    'us-treasury/30-year-us-treasury-bond',
                    'stir/eurodollar']

'''

'''
#option
a='http://www.cmegroup.com/trading/'
b='_product_calendar_futures.html'
contract_name_list=['energy/crude-oil/light-sweet-crude',
                    'equity-index/us-index/e-mini-sandp500']
'''



urls=[]
for c in contract_name_list:
    urls.append(a+c+b)


class CmeSpider(scrapy.Spider):
    name = 'zhr_cme'
    

    start_urls=urls
    
    def parse(self, response):
        pattern3='//*[@id="calendarFuturesProductTable1"]/tbody/tr'
        pattern1='//*[@id="productName"]/text()'
        
        print '<=============================='

#        for name_elm in response.xpath('//*[@id="productName"]/text()'):
#            product_names=name_elm.extract().__str__().strip()
       
        
        for elm in response.xpath(pattern3):
            product_names=response.xpath(pattern1).extract().__str__().strip()
            product_codes=elm.xpath('./td[1]/text()').extract().__str__().strip()
            contract_months=elm.xpath('./th/text()').extract()            
            first_notices=elm.xpath('./td[6]/text()[1]').extract()
            last_trades=elm.xpath('./td[2]/text()[2]').extract()
                        
            
            yield ZhrCmeItem(product_name=product_names,
                                 product_code=product_codes,
                                 contract_month=contract_months,
                                 first_notice=first_notices,
                                 last_trade=last_trades)
                            
            
        print '======================================>'





        
