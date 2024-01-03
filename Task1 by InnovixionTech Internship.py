from bs4 import BeautifulSoup
import requests
import pandas as pd

def web_scrape(link):
    response=requests.get(link)
    if response.status_code==200:
        s=BeautifulSoup(response.content,"html.parser")
        world_parameter=[]
        review_modal_layer=s.find_all("span",class_="counter-item")

        for i in range(len(review_modal_layer)-50):                  # we can choose rows accordingly
            world_parameter.append(review_modal_layer[i].get_text())
        print("Scraped data in list form:\n",world_parameter)
        
        df=pd.DataFrame()
        df["WORLD PARAMETERS"]=world_parameter                       # Column name
        print(df)

    else:
        print(f"Not able to extract the data.Status Code:{response.status_code}")
        return None
    
link='https://www.worldometers.info/#google_vignette'                # change URL accordingly
web_scrape(link)
