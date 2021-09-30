from bs4 import BeautifulSoup
import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
'''
source = requests.get('https://getbootstrap.com/').text
soup = BeautifulSoup(source, 'lxml')

# with open('https://getbootstrap.com/') as html_file:
    # soup = BeautifulSoup(html_file, 'lxml')

headline = soup.find('h1', class_='mb-3').text
sumary = soup.find('p', class_='lead').text.strip()
a = soup.find('div', class_='container-xl').a['href']

print(a)
# print(soup.prettify())
# print(soup.prettify())'''

"""name = input("enter name : ")
product = name.replace(" ", "+")
flipkartlink = f'https://www.flipkart.com/search?q={product}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
flipkartsource = requests.get(flipkartlink)
soup = BeautifulSoup(flipkartsource.text, 'lxml')
flipkartprice = soup.find('div', class_='_30jeq3').text.strip()
print("flipkart price: ", flipkartprice)

snapdeallink = f'https://www.snapdeal.com/search?keyword={product}&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy'
snapdealsource = requests.get(snapdeallink)
soup = BeautifulSoup(snapdealsource.text, 'lxml')
snapdealname = soup.find('p', 'product-title')
snapdealprice = soup.find('span', class_='lfloat product-price').text.strip()
print("snapdeal price: ", snapdealprice)
print("snapdeal name: ", snapdealname)

ebaylink = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={product}&_sacat=0'
ebaysource = requests.get(ebaylink)
soup = BeautifulSoup(ebaysource.text, 'lxml')
ebayprice = soup.find('span', class_='s-item__price').text.strip()
print("ebay price: ", ebayprice)

reliancedigitallink = f'https://www.reliancedigital.in/search?q={product}:relevance'
reliancedigitalsource = requests.get(reliancedigitallink).text
soup = BeautifulSoup(reliancedigitalsource, 'lxml')
reliancedigitalprice = soup.find('span', class_='sc-bxivhb cHwYJ').text.strip()
print("reliance digital price: ", reliancedigitalprice)

shopclueslink = f'https://www.shopclues.com/search?q={product}&sc_z=2222&z=0&count=10&user_id=&user_segment=default'
shopcluessource = requests.get(shopclueslink)
soup = BeautifulSoup(shopcluessource.text, 'lxml')
shopcluesprice = soup.find('span', 'p_price').text.strip()
print("shopclues price", shopcluesprice)

paytmmalllink = f'https://paytmmall.com/shop/search?q={product}&from=organic&child_site_id=6&site_id=2'
paytmmallsource = requests.get(paytmmalllink)
soup = BeautifulSoup(paytmmallsource.text, 'lxml')
paytmmallprice= soup.find('div', '_1kMS', 'span').text
print("paytm mall price: ",paytmmallprice)

nykaalink = f'https://www.nykaa.com/search/result/?ptype=search&q={product}&root=search&sourcepage=home&searchType=Manual'
nykaasource = requests.get(nykaalink).text
soup = BeautifulSoup(nykaasource, 'lxml')
nykaaprice = soup.find('span', 'post-card__content-price-offer').text.strip()
print("nykaa price ", nykaaprice)

lushlink = f'https://uk.lush.com/search/site/{product}'
lushsource = requests.get(lushlink).text
soup = BeautifulSoup(lushsource, 'lxml')
lushprice = soup.find('div', 'product-module-price').div.text.strip()
print("lush price", lushprice)

theenvyboxlink = f'https://www.myenvybox.com/?fuseaction=store.search&searchTxt={product}'
theenvyboxsource = requests.get(theenvyboxlink).text
soup = BeautifulSoup(theenvyboxsource, 'lxml')
theenvyboxprice = soup.find('div', 'price').text.strip()
print("the envy box price ", theenvyboxprice)


redifflink = f'https://shopping.rediff.com/#!{product}'
rediffsource = requests.get(redifflink).text
soup = BeautifulSoup(rediffsource, 'lxml')
rediffprice = soup.find('span', 'f14 bold')
print(rediffprice)

# uses string with "-" redmi-y2
vijaysaleslink = f'https://www.vijaysales.com/search/{product}'
print(vijaysaleslink)
vijaysalessource = requests.get(vijaysaleslink).text
print(vijaysalessource)

smartshopperslink = f'https://www.smartshoppers.in/index.php?route=product/search&search={product}'
smartshopperssource = requests.get(smartshopperslink).text
soup = BeautifulSoup(smartshopperssource, 'lxml')
price = soup.find_all('div', 'price')[5]
smartshoppersprice = price.find('span', 'price-new').text.strip()
print("smartshoppers price ", smartshoppersprice)

deltapagelink = f'https://deltapage.com/index.php?route=product/search&search={product}&description=true'
deltapagesource = requests.get(deltapagelink).text
soup = BeautifulSoup(deltapagesource, 'lxml')
deltapageprice = soup.find('span', 'price-normal').text.strip()
print("deltapage price ", deltapageprice)

mobilestoreonlinelink = f'https://mobilestoreonline.com/?s={product}&post_type=product'
mobilestoreonlinesource = requests.get(mobilestoreonlinelink).text
soup = BeautifulSoup(mobilestoreonlinesource, 'lxml')
mobilestoreonlineprice = soup.find('bdi').text
print("mobilestoreonline price :", mobilestoreonlineprice)

nextlink = f'https://www.next.co.uk/search?w={product}&isort=score&af='
nextsource = requests.get(nextlink).text
soup = BeautifulSoup(nextsource, 'lxml')
nprice = soup.find('div', 'Info')
nextprice = ntprice.find('div', 'Price').a.text.strip()
print(nextprice)"""

'''
giving price 0
primeabgblink = f'https://www.primeabgb.com/?post_type=product&s={product}'
primeabgbsource = requests.get(primeabgblink).text
soup = BeautifulSoup(primeabgbsource, 'lxml')
primeabgbprice = soup.find('span', 'amount')
print(primeabgbprice)
'''

"""
flipkart = ''
def flipkart(name):
    global flipkart
    name1 = name.replace(" ","+")
    flipkart = f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    res = requests.get(f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off', headers=headers)

    print("Searching in flipkart...")
    soup = BeautifulSoup(res.text,'html.parser')
    flipkart_name = soup.select('._3wU53n')[0].getText().strip()
    flipkart_name = flipkart_name.upper()
    if name.upper() in flipkart_name:
        flipkart_name = soup.select('._3wU53n')[0].getText().stript()
        flipkart_price = soup.select('._2rQ-NK')[0].getText().stript()
        print("flipkart: ",flipkart_name)
        print("flipkart: ",flipkart_price)
    else:
        print("not found")
        flipkart_price='0'
    return flipkart_name

name = input("enter name: ")
flipkart_price = flipkart(name)
if flipkart_price == '0':
    print("no product found")
else:
    print("flipkart price : ",flipkart_price)
    
    def convert(a):
        b = a.replace(" ", '')
        c = b.replace("INR", '')
        d = c.replace(",", '')
        f = d.replace("rs", '')
        g = int(float(f))
        return g"""
    
    
    
def snapdeal(product):
    snapdeallink = f'https://www.snapdeal.com/search?keyword={product}&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy'
    snapdealsource = requests.get(snapdeallink).text
    soup = BeautifulSoup(snapdealsource, 'lxml')
    snapdealname = soup.find('p', 'product-title').text.upper()
    if name.upper() in snapdealname:
        snapdealname = soup.find('p', 'product-title').text
        snapdealprice = soup.find('span', class_='lfloat product-price').text.strip()
        print("snapdeal name : ", snapdealname)
        print("snapdeal price : ", snapdealprice)
    else:
        print("not found")
        snapdealprice = '0'
    return snapdealprice, snapdealname, snapdeallink

def ebay(product):
    ebaylink = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={product}&_sacat=0'
    ebaysource = requests.get(ebaylink).text
    soup = BeautifulSoup(ebaysource, 'lxml')
    ebayname = soup.find('h3', 's-item__title').text.upper()
    if name.upper() in ebayname:
        ebayname = soup.find('h3', 's-item__title').text
        ebayprice = soup.find('span', class_='s-item__price').text.strip()
        print("ebay name : ", ebayname)
        print("ebay price : ", ebayprice)
    else:
        print("not found")
        ebayprice = '0'
    return ebayprice, ebayname, ebaylink

def flipkart(product):
    flipkartlink = f'https://www.flipkart.com/search?q={product}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    flipkartsource = requests.get(flipkartlink)
    soup = BeautifulSoup(flipkartsource.text, 'lxml')
    flipkartname = soup.find('a', 's1Q9rs').text.upper()
    if name.upper() in flipkartname:
        flipkartname = soup.find('a', 's1Q9rs').text
        flipkartprice = soup.find('div', '_30jeq3').text.strip()
        print("flipkart name : ", flipkartname)
        print("flipkart price : ", flipkartprice)
    else:
        print("not found")
        flipkartprice = '0'
    return flipkartprice, flipkartname, flipkartlink

def reliancedigital(product):
    reliancedigitallink = f'https://www.reliancedigital.in/search?q={product}:relevance'
    reliancedigitalsource = requests.get(reliancedigitallink).text
    soup = BeautifulSoup(reliancedigitalsource, 'lxml')
    reliancedigitalname = soup.find('div', 'slider-text').text.upper()
    if name.upper() in reliancedigitalname:
        reliancedigitalname = soup.find('div', 'slider-text').text
        reliancedigitalprice = soup.find('span', 'sc-bxivhb cHwYJ').text.strip()
        print("reliance digital name : ", reliancedigitalname)
        print("reliance digital price : ", reliancedigitalprice)
    else:
        print("not found")
        reliancedigitalprice = '0'
    return reliancedigitalprice, reliancedigitalname, reliancedigitallink

def shopcules(product):
    shopclueslink = f'https://www.shopclues.com/search?q={product}&sc_z=2222&z=0&count=10&user_id=&user_segment=default'
    shopcluessource = requests.get(shopclueslink)
    soup = BeautifulSoup(shopcluessource.text, 'lxml')
    shopculesname = soup.find().text.upper()
    if name.upper() in shopculesname:
        shopculesname = soup.find().text
        shopcluesprice = soup.find('span', 'p_price').text.strip()
        print("shopclues name : ", shopculesname)
        print("shopclues price : ", shopcluesprice)
    else:
        print("not found")
        shopculesprice = '0'
    return shopculesprice, shopculesname, shopclueslink

def paytmmall(product):
    paytmmalllink = f'https://paytmmall.com/shop/search?q={product}&from=organic&child_site_id=6&site_id=2'
    paytmmallsource = requests.get(paytmmalllink)
    soup = BeautifulSoup(paytmmallsource.text, 'lxml')
    paytmmallname = soup.find().text.upper()
    if name.upper() in paytmmallname:
        paytmmallprice = soup.find('div', '_1kMS', 'span').text
        paytmmallname = soup.find().text
        print("paytm mall name : ", paytmmallname)
        print("paytm mall price : ", paytmmallprice)
    else:
        print("not found")
        paytmmallprice = '0'
    return paytmmallprice, paytmmallname, paytmmalllink

def nykaa(product):
    nykaalink = f'https://www.nykaa.com/search/result/?ptype=search&q={product}&root=search&sourcepage=home&searchType=Manual'
    nykaasource = requests.get(nykaalink).text
    soup = BeautifulSoup(nykaasource, 'lxml')
    nykaaname = soup.find().text.upper()
    if name.upper() in nykaaname:
        nykaaprice = soup.find('span', 'post-card__content-price-offer').text.strip()
        nykaaname = soup.find().text
        print("nykaa name : ", nykaaname)
        print("nykaa price : ", nykaaprice)
    else:
        print("not found")
        nykaaprice = '0'
    return nykaaprice, nykaaname, nykaalink

def lush(product):
    lushlink = f'https://uk.lush.com/search/site/{product}'
    lushsource = requests.get(lushlink).text
    soup = BeautifulSoup(lushsource, 'lxml')
    lushname = soup.find().text.upper()
    if name.upper() in lushname:
        lushprice = soup.find('div', 'product-module-price').div.text.strip()
        lushname = soup.find().text
        print("lush name : ", lushname)
        print("lush price : ", lushprice)
    else:
        print("not found")
        lushprice = '0'
    return lushprice, lushname, lushlink

def theenvybox(product):
    theenvyboxlink = f'https://www.myenvybox.com/?fuseaction=store.search&searchTxt={product}'
    theenvyboxsource = requests.get(theenvyboxlink).text
    soup = BeautifulSoup(theenvyboxsource, 'lxml')
    theenvyboxname = soup.find().text.upper()
    if name.upper() in theenvyboxname:
        theenvyboxprice = soup.find('div', 'price').text.strip()
        theenvyboxname = soup.find().text
        print("the envy box name : ", theenvyboxname)
        print("the envy box price : ", theenvyboxprice)
    else:
        print("not found")
        theenvyboxprice = '0'
    return theenvyboxprice, theenvyboxname, theenvyboxlink

def rediff(product):
    redifflink = f'https://shopping.rediff.com/#!{product}'
    rediffsource = requests.get(redifflink).text
    soup = BeautifulSoup(rediffsource, 'lxml')
    rediffname = soup.find().text.upper()
    if name.upper() in rediffname:
        rediffprice = soup.find('span', 'f14 bold')
        rediffname = soup.find().text
        print("rediff name : ", rediffname)
        print("rediff price : ", rediffprice)
    else:
        print("not found")
        rediffprice = '0'
    return rediffprice, rediffname, redifflink

def smartshoppers(product):
    smartshopperslink = f'https://www.smartshoppers.in/index.php?route=product/search&search={product}'
    smartshopperssource = requests.get(smartshopperslink).text
    soup = BeautifulSoup(smartshopperssource, 'lxml')
    smartshoppersname = soup.find().text.upper()
    if name.upper() in smartshoppersname:
        price = soup.find_all('div', 'price')[5]
        smartshoppersprice = price.find('span', 'price-new').text.strip()
        smartshoppersname = soup.find().text
        print("smartshoppers name : ", smartshoppersname)
        print("smartshoppers price : ", smartshoppersprice)
    else:
        print("not found")
        smartshoppersprice = '0'
    return smartshoppersprice, smartshoppersname, smartshopperslink

def deltapage(product):
    deltapagelink = f'https://deltapage.com/index.php?route=product/search&search={product}&description=true'
    deltapagesource = requests.get(deltapagelink).text
    soup = BeautifulSoup(deltapagesource, 'lxml')
    deltapagename = soup.find().text.upper()
    if name.upper() in deltapagename:
        deltapageprice = soup.find('span', 'price-normal').text.strip()
        deltapagename = soup.find().text
        print("deltapage name : ", deltapagename)
        print("deltapage price : ", deltapageprice)
    else:
        print("not found")
        deltapageprice = '0'
    return deltapageprice, deltapagename, deltapagelink

def mobilestoreonline(product):
    mobilestoreonlinelink = f'https://mobilestoreonline.com/?s={product}&post_type=product'
    mobilestoreonlinesource = requests.get(mobilestoreonlinelink).text
    soup = BeautifulSoup(mobilestoreonlinesource, 'lxml')
    mobilestoreonlinename = soup.find().text.upper()
    if name.upper() in mobilestoreonlinename:
        mobilestoreonlineprice = soup.find('bdi').text
        mobilestoreonlinename = soup.find().text
        print("mobilestoreonline name : ", mobilestoreonlinename)
        print("mobilestoreonline price :", mobilestoreonlineprice)
    else:
        print("not found")
        mobilestoreonlineprice = '0'
    return mobilestoreonlineprice, mobilestoreonlinename, mobilestoreonlinelink

def next(product):
    nextlink = f'https://www.next.co.uk/search?w={product}&isort=score&af='
    nextsource = requests.get(nextlink).text
    soup = BeautifulSoup(nextsource, 'lxml')
    nextname = soup.find().text.upper()
    if name.upper() in nextname:
        nprice = soup.find('div', 'Info')
        nextprice = nprice.find('div', 'Price').a.text.strip()
        nextname = soup.find().text
        print("next name : ", nextname)
        print("next price :", nextprice)
    else:
        print("not found")
        nextprice = '0'
    return nextprice, nextname, nextlink




name = input("enter product name : ")
product = name.replace(" ", "+")

snapdealprice = snapdeal(product)
if snapdealprice == '0':
    print("product not found")
else:
    print("snapdeal price : ", snapdealprice)

ebayprice = ebay(product)
if ebayprice == '0':
    print("product not found")
else:
    print("ebay price : ", ebayprice)

flipkartprice = flipkart(product)
if flipkartprice == '0':
    print("product not found")
else:
    print("flipkart price : ", flipkartprice)

reliancedigitalprice = reliancedigital(product)
if reliancedigitalprice == '0':
    print("product not found")
else:
    print("reliancedigital price : ", reliancedigitalprice)

shopculesprice = shopcules(product)
if shopculesprice == '0':
    print("product not found")
else:
    print("shopcules price : ", shopculesprice)

paytmmallprice = paytmmall(product)
if paytmmallprice == '0':
    print("product not found")
else:
    print("paytmmall price : ", paytmmallprice)

nykaaprice = nykaa(product)
if nykaaprice == '0':
    print("product not found")
else:
    print("nykaa price : ", nykaaprice)

lushprice = lush(product)
if lushprice == '0':
    print("product not found")
else:
    print("lush price : ", lushprice)

theenvyboxprice = theenvybox(product)
if theenvyboxprice == '0':
    print("product not found")
else:
    print("the envy box price : ", theenvyboxprice)

rediffprice = rediff(product)
if rediffprice == '0':
    print("product not found")
else:
    print("rediff price : ", rediffprice)

smartshoppersprice = smartshoppers(product)
if smartshoppersprice == '0':
    print("product not found")
else:
    print("smartshoppers price : ", smartshoppersprice)

deltapageprice = deltapage(product)
if deltapageprice == '0':
    print("product not found")
else:
    print("deltapage price : ", deltapageprice)

mobilestoreonlineprice =mobilestoreonline(product)
if mobilestoreonlineprice == '0':
    print("product not found")
else:
    print("mobilestoreonline price : ", mobilestoreonlineprice)

nextprice =next(product)
if nextprice == '0':
    print("product not found")
else:
    print("next) price : ", nextprice)
