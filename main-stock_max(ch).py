# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 09:36:10 2019

@author: frank.lin
"""

import os
import yfinance as yf
from pandas_datareader import data

data_dir='\stock_data'

def download_stock(f_name):
    #date_s=add_months(date_e,-month)    
    #下載stock日資料
    try : 
        #df = web.get_data_yahoo([f_name],period='max',interval='1d')
        #df = web.get_data_yahoo([f_name],interval='d')
        df=yf.download(f_name, period='max',interval='1d')
        
        if df.empty == False:
            #5日均線、10日均線、20日均線、60日均線、120日均線、240日均線
            ll=6
            ma5=df['Close'].rolling(window=5).mean()
            ma10=df['Close'].rolling(window=10).mean()
            ma20=df['Close'].rolling(window=20).mean()
            ma60=df['Close'].rolling(window=60).mean()
            ma120=df['Close'].rolling(window=120).mean()
            ma240=df['Close'].rolling(window=240).mean()
            marketcap=data.get_quote_yahoo(f_name)['marketCap'].tolist()[0]

            df.insert(ll,column="MA5",value=ma5) 
            df.insert(ll+1,column="MA10",value=ma10) 
            df.insert(ll+2,column="MA20",value=ma20)
            df.insert(ll+3,column="MA60",value=ma60)
            df.insert(ll+4,column="MA120",value=ma120)
            df.insert(ll+5,column="MA240",value=ma240)
            #df.insert(ll+6,column="MarketCap",value=marketCap)
            df.to_csv('{}/{}_max.csv'.format(data_dir,f_name))
            close=df['Close'].tail(1).mean()
            m5=round(df['MA5'].tail(1).mean(),3)
            m10=round(df['MA10'].tail(1).mean(),3)
            m20=round(df['MA20'].tail(1).mean(),3)
            m60=round(df['MA60'].tail(1).mean(),3)
            m120=round(df['MA120'].tail(1).mean(),3)
            m240=round(df['MA240'].tail(1).mean(),3)
            if (close>m5 and close>m10 and close>m20):
                f0="三陽開泰 "
            elif (close<m5 and close<m10 and close<m20):
                f0="三聲無奈 "
            else:
                f0=""
            if (close>m5):
                f5=" 大於週線"
            else:
                f5=""
            if (close>m10):
                f10=" 大於半月線"
            else:
                f10=""
            if (close>m20):
                f20=" 大於月線"
            else:
                f20=""                
            if (close>m60):
                f60=" 大於季線"
            else:
                f60=""
            if (close>m120):
                f120=" 大於半年線"
            else:
                f120=""
            if (close>m240):
                f240=" 大於年線"
            else:
                f240=""
            fp0 = open("do_moving_stock.txt", "a") 
            if (len(f0+f5+f10+f20+f60+f120+f240)>0):
                #fp0.write(f_name+" 收盤:"+str(close)+" 週:"+str(m5)+" 半月:"+str(m10)+" 月:"+str(m20)+" 季:"+str(m60)+" 半年:"+str(m120)+" 年:"+str(m240)+f0+f5+f10+f20+f60+f120+f240+"\n")
                fp0.write(f0+f_name+" 收盤:"+str(close)+" 週線:"+str(m5)+" 市值:"+str(marketcap)+f5+f10+f20+f60+f120+f240+"\n")
            elif (close<m5):
                fp0.write(f_name+" 收盤:"+str(close)+" 週線:"+str(m5)+f5+" 市值:"+str(marketcap)+"\n")    
            fp0.close()                
            #print (f_name,"收盤:",close,"週:",m5,"半月:",m10,"月:",m20,"季:",m60,"半年:",m120,"年:",m240,f5,f10,f20,f60,f120,f240) 

        else :
            pass
    except :
        print (f_name,"error")
        pass

#read stock_list and save to csv file
def get_data(list):
    with open(list, 'r') as f:
        for line in f:
            f_name=line.strip('\n').replace(':FO','')
            print (f_name)
            download_stock(f_name)
            
def main(): 
    #rebuild new folder without old folder
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    if os.path.isfile("do_moving_stock.txt"):
        os.remove("do_moving_stock.txt")
        print ("刪除","do_moving_stock.txt")
        
    stock_check="stock_list\\list_stock_buy-us.txt"
    get_data(stock_check)  
    
if __name__ == '__main__':
    main()
