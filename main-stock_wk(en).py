# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 09:36:10 2019

@author: frank.lin
"""

import os
import yfinance as yf

data_dir='.\stock_data'
list_dir='.\stock_list'

def download_stock(f_name):
    #date_s=add_months(date_e,-month)    
    #download stock weekly data
    try : 
        df=yf.download(f_name, period='max',interval='1wk')
        if df.empty == False:

            ll=6
            ma4=df['Close'].rolling(window=4).mean()
            ma8=df['Close'].rolling(window=8).mean()
            df.insert(ll,column="MA4",value=ma4) 
            df.insert(ll+1,column="MA8",value=ma8) 
            df.to_csv('{}/{}_week_max.csv'.format(data_dir,f_name))
            close=df['Close'].tail(1).mean()
            m4=round(df['MA4'].tail(1).mean(),3)
            m8=round(df['MA8'].tail(1).mean(),3)

            if (close>m4 and close>m8):
                f0=">4MA&8MA "
            elif (close<m4 and close<m8):
                f0="<4MA&8MA "
            elif (close<m4 and close>m8):
                f0="only >8MA "
            elif (close>m4 and close<m8):
                f0="only >4MA "
            else:
                f0=""
  
            fp0 = open("do_moving_stock_weekly.txt", "a") 
            if (len(f0)>0):
                fp0.write(f0+f_name+" close:"+str(close)+" 4MA:"+str(m4)+" 8MA:"+str(m8)+"\n")
            fp0.close()                

        else :
            pass
    except :
        print (f_name,"error")
        pass

#讀取清單並下載成csv檔
def get_data(list):
    with open(list, 'r') as f:
        for line in f:
            f_name=line.strip('\n').replace(':FO','')
            print (f_name)
            download_stock(f_name)

def main(): 
    #資料夾不在重建
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    if os.path.isfile("do_moving_stock_weekly.txt"):
        os.remove("do_moving_stock_weekly.txt")
        print ("delete","do_moving_stock_weekly.txt")
        
    stock_check=list_dir+"\\list_stock_buy-us.txt"
    get_data(stock_check)  

if __name__ == '__main__':
    main()
