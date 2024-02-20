from flask import Flask, request
import requests
import re
from bs4 import BeautifulSoup

app = Flask(__name__)


def extract_price(price_string):
    numbers = re.findall(r'\d+\.\d+|\d+', price_string.replace(',', ''))
    
    if numbers:
        return round(float(numbers[0])) if '.' in numbers[0] else int(numbers[0])
    else:
        return {"error":"Failed to fetch data, please try again later"}

def validateUrl(url):
    
    flipkart_pattern =re.compile(r'^https://(www\.|dl\.)?flipkart\.com/.*$')
    amazon_pattern = re.compile(r'^https?://(www\.)?amazon\.(com|in|co\.uk|de|fr|es|it|jp|ca|cn|br|mx|au)/.*$')
    try:    
        if flipkart_pattern.match(url):
           return get_soup(url,"flipkart")
        elif amazon_pattern.match(url):
           return get_soup(url,"amazon")
        else:
            return {"error":"Invalid Url"}

    except Exception as e:
        return {"error":"Failed to fetch data, please try again later"}
def get_soup(url,company):    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    req= requests.get(url,headers=headers)
    soup = BeautifulSoup(req._content, 'html.parser')
    if(company=="flipkart"):
        title = soup.find('span', {"class":"B_NuCI"}).get_text(strip=True)
        img= soup.find('img', {"class":"q6DClP"}).get('src')
        img=img.replace('128','832')
    
        ratingDiv = soup.find_all("span", {"id":["productRating_LSTACCGC4GN5SQR7ZCZYKXWJM_ACCGC4GN5SQR7ZCZ_","productRating_LSTWATFFDFZHZAVGZHJWL2XH4_WATFFDFZHZAVGZHJ_"]})
        if(len(ratingDiv)==0):
            rating=0
        else:
            ratingDiv = soup.find_all("span", {"id":["productRating_LSTACCGC4GN5SQR7ZCZYKXWJM_ACCGC4GN5SQR7ZCZ_","productRating_LSTWATFFDFZHZAVGZHJWL2XH4_WATFFDFZHZAVGZHJ_"]})[0]
            rating=float(ratingDiv.find("div").getText(strip=True))
        price = soup.find('div', {"class":"_30jeq3 _16Jk6d"}).get_text(strip=True)
        price = extract_price(price)
        data=dict(currentPrice=price,url=url,company=company,title=title,img=img,rating=rating)
        return data
    else:
        title = soup.find("span",{"id":"productTitle"}).get_text(strip=True)
        img= soup.find("img", {"id":"landingImage"}).get('src')
        ratingDiv = soup.find("div", {"id":"averageCustomerReviews"})
        rating= float(ratingDiv.find_all("span", {"class": "a-size-base a-color-base"})[0].get_text(strip=True))
        price= soup.find("span", {"class":"a-price-whole"}).get_text(strip=True)
        price= extract_price(price)
        data=dict(currentPrice=price,url=url,company=company,title=title,img=img,rating=rating)
        return data

@app.route('/', methods=['POST','GET'])
def fetchData():
    if request.method == 'GET':
        url= request.args.get("url")
        return validateUrl(url)
    if request.method == 'POST':
        url= request.get_json()['url']
        return validateUrl(url)


if __name__ == '__main__':
    app.run()