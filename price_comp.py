from bs4 import BeautifulSoup
import requests
import time
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

flipkart=''
ebay=''
croma=''
amazon=''
olx=''

def flipkart(name):
    try:
        global flipkart
        name1 = name.replace(" ","+")   #iphone x  -> iphone+x
        flipkart=f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
        res = requests.get(f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',headers=headers)


        print("\nSearching in flipkart....")
        soup = BeautifulSoup(res.text,'html.parser')
        flipkart_name = soup.select('._3wU53n')[0].getText().strip()
        flipkart_name = flipkart_name.upper()
        if name.upper() in flipkart_name:
            flipkart_price = soup.select('._2rQ-NK')[0].getText().strip()
            flipkart_name = soup.select('._3wU53n')[0].getText().strip()
            print("Flipkart:")
            print(flipkart_name)
            print(flipkart_price)
            print("-----------------------")
        else:
            print("Flipkart:No product found!")
            print("-----------------------")
            flipkart_price='0'
        return flipkart_price 
    except:
        print("Flipkart:No product found!")  
        print("-----------------------")
        flipkart_price= '0'
    return flipkart_price 
def ebay(name):
    try:
        global ebay
        name1 = name.replace(" ","+")
        ebay=f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={name1}&_sacat=0'
        res = requests.get(f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={name1}&_sacat=0',headers=headers)
        print("\nSearching in ebay.....")
        soup = BeautifulSoup(res.text,'html.parser')
        length = soup.select('.s-item__price')
        ebay_page_length=int(len(length))
        for i in range (0,ebay_page_length):
            info = soup.select('.SECONDARY_INFO')[i].getText().strip()
            info = info.upper()
            if info=='BRAND NEW':
                ebay_name = soup.select('.s-item__title')[i].getText().strip()
                name=name.upper()
                ebay_name=ebay_name.upper()
                if name in ebay_name[:25]:
                    ebay_price = soup.select('.s-item__price')[i].getText().strip()
                    ebay_name = soup.select('.s-item__title')[i].getText().strip()
                    print("Ebay:")
                    print(ebay_name)
                    print(ebay_price.replace("INR","₹"))
                    print(info)
                    print("-----------------------")
                    ebay_price=ebay_price[0:14]
                    break
                else:
                    i+=1
                    i=int(i)
                    if i==ebay_page_length:
                        print("Ebay: No product Found!")
                        print("-----------------------")
                        ebay_price = '0'
                        break

        return ebay_price
    except:
        print("Ebay: No product Found!")
        print("-----------------------")
        ebay_price = '0'
    return ebay_price

def croma(name):
    try:
        global croma
        name1 = name.replace(" ","+")
        croma=f'https://www.croma.com/search/?text={name1}'
        res = requests.get(f'https://www.croma.com/search/?text={name1}',headers=headers)
        print("\nSearching in croma.....")
        soup = BeautifulSoup(res.text,'html.parser')
        croma_name = soup.select('h3')

        croma_page_length = int( len(croma_name))
        for i in range (0,croma_page_length):
            name = name.upper()
            croma_name = soup.select('h3')[i].getText().strip().upper()
            if name in croma_name.upper()[:25]:
                croma_name = soup.select('h3')[i].getText().strip().upper()
                croma_price = soup.select('.pdpPrice')[i].getText().strip()
                print(croma_name)
                print(croma_price)
                print("-----------------------")
                break
            else:
                i+=1
                i=int(i)
                if i==croma_page_length:
                    print("Croma: No product Found!")
                    print("-----------------------")
                    croma_price = '0'
                    break
        ##print(croma_price)
        return croma_price
    except:
        print("Croma: No product Found!")
        print("-----------------------")
        croma_price = '0'
    return croma_price

def amazon(name):
    try:
        global amazon
        name1 = name.replace(" ","-")
        name2 = name.replace(" ","+")
        amazon=f'https://www.amazon.in/{name1}/s?k={name2}'
        res = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}',headers=headers)
        print("\nSearching in amazon:")
        soup = BeautifulSoup(res.text,'html.parser')
        amazon_page = soup.select('.a-color-base.a-text-normal')
        amazon_page_length = int(len(amazon_page))
        for i in range(0,amazon_page_length):
            name = name.upper()
            amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
            if name in amazon_name[0:20]:
                amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
                amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()
                print("Amazon:")
                print(amazon_name)
                print("₹"+amazon_price)
                print("-----------------------")
                break
            else:
                i+=1
                i=int(i)
                if i==amazon_page_length:
                    print("amazon : No product found!")
                    print("-----------------------")
                    amazon_price = '0'
                    break
        return amazon_price
    except:
        print("amazon: No product found!")
        print("-----------------------")
        amazon_price = '0'
    return amazon_price


def olx(name):
    try:
        global olx
        name1 = name.replace(" ","-")
        olx=f'https://www.olx.in/items/q-{name1}?isSearchCall=true'
        res = requests.get(f'https://www.olx.in/items/q-{name1}?isSearchCall=true',headers=headers)
        print("\nSearching in OLX......")
        soup = BeautifulSoup(res.text,'html.parser')
        olx_name = soup.select('._2tW1I')
        olx_page_length = len(olx_name)
        for i in range(0,olx_page_length):
            olx_name = soup.select('._2tW1I')[i].getText().strip()
            name = name.upper()
            olx_name = olx_name.upper()
            if name in olx_name:
                olx_price = soup.select('._89yzn')[i].getText().strip()
                olx_name = soup.select('._2tW1I')[i].getText().strip()
                olx_loc = soup.select('.tjgMj')[i].getText().strip()
                try:
                    label = soup.select('._2Vp0i span')[i].getText().strip()
                except:
                    label = "OLD"
                
                print("Olx:")
                print(label)
                print(olx_name)
                print(olx_price)
                print(olx_loc)
                print("-----------------------")
                break
            else:
                i+=1
                i=int(i)
                if i==olx_page_length:
                    print("Olx: No product Found!")
                    print("-----------------------")
                    olx_price = '0'
                    break
        return olx_price
    except:
        print("Olx: No product found!")
        print("-----------------------")
        olx_price = '0'
    return olx_price

def convert(a):
    b=a.replace(" ",'')
    c=b.replace("INR",'')
    d=c.replace(",",'')
    f=d.replace("₹",'')
    g=int(float(f))
    return g

###
name=input("product name:\n")
ebay_price=ebay(name)
flipkart_price=flipkart(name)
amazon_price=amazon(name)
croma_price=croma(name)
olx_price = olx(name)
print("----------------------------------")
if ebay_price== '0':
    print("No Product found!")
    ebay_price = int(ebay_price)
else:
    print("Ebay price:",ebay_price)
    ebay_price = convert(ebay_price)
if flipkart_price=='0':
    print("No product found!")
    flipkart_price = int(ebay_price)
else:
    print("\nFLipkart Price:",flipkart_price)
    flipkart_price=convert(flipkart_price)
if amazon_price=='0':
    print("No Product found!")
    amazon_price = int(amazon_price)
else:
    print("\namazon price: ₹",amazon_price)
    amazon_price=convert(amazon_price)
   
if croma_price=='0':
    print("No product found!")
    croma_price = int(croma_price)
else:
    print("\nCroma Price:",croma_price)
    croma_price=convert(croma_price)
if olx_price =='0':
    print("No product found!")
    olx_price = int(olx_price)
else:
    print("\nOlx Price:",olx_price)
    olx_price=convert(olx_price)

time.sleep(2)

#print(f"{type(ebay_price)} , {type(flipkart_price)} , {type(amazon_price)} , {type(croma_price)} , {type(olx_price)} ")


lst = [ebay_price,flipkart_price,amazon_price,croma_price,olx_price]
lst2=[]
for j in range(0,len(lst)):
    if lst[j]>0:
        lst2.append(lst[j])
min_price=min(lst2)

print("_______________________________")
print("\nMinimun Price: ₹",min_price)
price = {
    f'{ebay_price}':f"{ebay}",
    f'{amazon_price}':f'{amazon}',
    f'{olx_price}':f"{olx}",
    f'{flipkart_price}':f'{flipkart}',
    f'{croma_price}':f'{croma}'
}
for key, value in price.items():
    if int(key)==min_price:
        print ('\nurl:', price[key])
print("\nUrls:\n")
print("-----------------------------------------------------------------------")
print(ebay)
print(amazon)
print(olx)
print(flipkart)
print(croma)
print("------------------------------------------------------------------------")
