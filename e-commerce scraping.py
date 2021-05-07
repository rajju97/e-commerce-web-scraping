from bs4 import BeautifulSoup
import requests
from pandas import *
from tkinter import *

def phone():
    if ch1.get()=='phone':
        shop_list = []
        for page in range(1,10):
            html_text=requests.get('https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&sort=recency_desc&page='+str(page)).text
            #print(html_text)
            soup=BeautifulSoup(html_text, 'lxml')#lxml is a parser
            mob_products=soup.find_all('div', class_='_2kHMtA')
            #print(mob_products)

            for prod in mob_products:
                prod_name=prod.find('div', class_='_4rR01T').text
                #print(f"product name:{prod_name.strip()}")
                specs=prod.find_all('li',class_='rgWa7D')
                #print(specs)
                #print("specifications:")
                sp_list=[]
                for sp in specs:
                    specific=sp.text

                    #print(f'>>{specific.strip()}')
                    spl=[specific]
                    sp_list.append(spl)
                price=prod.find('div',class_="_30jeq3 _1_WHN1").text
                #print(f"price:{price.strip()}")
                rating=prod.find('div',class_='_3LWZlK').text
                #print(f"rating:{rating.strip()}")
                buy=prod.a['href']
                link=(f'https://www.flipkart.com{buy.strip()}')
                list=[prod_name,sp_list,price,rating,link]
                shop_list.append(list)
                #print("\n\n")

        #print(shop_list)
        dataset=DataFrame(shop_list)
        dataset.columns=['product_name','specifications','price','rating','link']
        print(dataset)
        dataset.to_csv("flipkart.csv",index=False)

    if ch1.get()=='smart_tv':
        shop_list = []
        for page in range(1, 10):
            html_text = requests.get('https://www.flipkart.com/search?q=smart+tv&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_4_5_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_5_na_na_na&as-pos=4&as-type=RECENT&suggestionId=smart+tv&requestId=258d8f77-0542-4183-8d82-782f11e27058&as-searchtext=smart&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&sort=recency_desc&page='+str(page)).text
            # print(html_text)
            soup = BeautifulSoup(html_text,'lxml')  # lxml is a parser
            smart_tv=soup.find_all('div', class_='_2kHMtA')
            #print(smart_tv)
            for tv in smart_tv:
                tv_name=tv.find('div',class_='_4rR01T').text
                #print(f'prod_name: {tv_name.strip()}')
                specs = tv.find_all('li', class_='rgWa7D')
                # print(specs)
                # print("specifications:")
                sp_list = []
                for sp in specs:
                    specific = sp.text

                    #print(f'>>{specific.strip()}')
                    spl = [specific]
                    sp_list.append(spl)
                price = tv.find('div', class_="_30jeq3 _1_WHN1").text
                # print(f"price:{price.strip()}")
                rating = tv.find('div', class_='_3LWZlK').text
                # print(f"rating:{rating.strip()}")
                buy = tv.a['href']
                link = (f'https://www.flipkart.com{buy.strip()}')
                list = [tv_name, sp_list, price, rating, link]
                shop_list.append(list)
                # print("\n\n")

                # print(shop_list)
            dataset = DataFrame(shop_list)
            dataset.columns = ['product_name', 'specifications', 'price', 'rating', 'link']
            print(dataset)
            dataset.to_csv("flipkart1.csv", index=False)


win=Tk()
win.title("web scrapping")
#creating frame and grid to hold the content
fram=Frame(win)
fram.grid(column=0,row=0,sticky=(N,W,E,S))
fram.columnconfigure(0,weight=1)
fram.rowconfigure(0,weight=1)
fram.pack(pady=100,padx=100)
ch={'phone','smart_tv'}
ch1=StringVar(win)
ch1.set('phone')
lanmenu1=OptionMenu(fram,ch1,*ch,)
Label(fram,text="select categories",fg="blue").grid(row=0,column=1)
lanmenu1.grid(row=1,column=1)

b=Button(fram,text="scrape",command=phone,bd=7,activebackground="yellow").grid(row=1,column=3,columnspan=3)

win.mainloop()