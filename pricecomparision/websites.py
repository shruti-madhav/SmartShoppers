from urllib.request import urlopen

from bs4 import BeautifulSoup
import requests
from lxml import etree

print("hello from websites")

def snapdeal(product, name):
    snapdeallink = f'https://www.snapdeal.com/search?keyword={product}&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy'
    snapdealsource = requests.get(snapdeallink).text
    soup = BeautifulSoup(snapdealsource, 'lxml')
    snaplist = []
    snapdealname = soup.find('p', 'product-title').text.upper()
    if name.upper() in snapdealname:
        snapdealname = soup.find('p', 'product-title').text
        snapdealprice = soup.find('span', 'lfloat product-price').text.strip()
        snaplist.append(snapdealprice)
        snaplist.append(snapdeallink)
        return snaplist
    else:
        print("snap not found")
        snapdealprice = '0'
        snapdeallink = 'not found'
        snaplist.append(snapdealprice)
        snaplist.append(snapdeallink)
        return snaplist
# snapdeal("bean bag", "bean bag")

def ebay(product, name):
    ebaylink = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={product}&_sacat=0'
    ebaysource = requests.get(ebaylink).text
    soup = BeautifulSoup(ebaysource, 'lxml')
    ebayname = soup.find('h3', 's-item__title').text.upper()
    ebaylist = []
    if name.upper() in ebayname:
        ebayname = soup.find('h3', 's-item__title').text
        ebayprice = soup.find('span', 's-item__price').text.strip()
        print("ebay price : ", ebayprice)
        print("ebay link : ", ebaylink)
        ebaylist.append(ebayprice)
        ebaylist.append(ebaylink)
        return ebaylist
    else:
        print("not found")
        ebayprice = '0'
        ebaylink = 'not found'
        ebaylist.append(ebayprice)
        ebaylist.append(ebaylink)
        return ebaylist
# ebay("headphones", "headphones")

#
# none returning are commented
#

# flipkart has diff soup.find for electronics
def flipkart(product, name):
    flipkartlink = f'https://www.flipkart.com/search?q={product}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    flipkartsource = requests.get(flipkartlink)
    soup = BeautifulSoup(flipkartsource.text, 'html.parser')
    fliplist = []
    flipkartname = soup.find('div', '_4rR01T').text.upper()
    name = name.upper()
    if name in flipkartname:
        # flipkartname = soup.findAllNext("//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/a[1]")
        flipkartname = soup.find('div', '_4rR01T').text
        flipkartprice = soup.find('div', '_30jeq3 _1_WHN1').text.strip()
        print("flipkart name : ", flipkartname)
        print("flipkart price : ", flipkartprice)
        fliplist.append(flipkartprice)
        fliplist.append(flipkartlink)
        print("hello flip", fliplist)
        return fliplist
    else:
        print("f not found")
        flipkartprice = '0'
        flipkartlink = 'not found'
        fliplist.append(flipkartprice)
        fliplist.append(flipkartlink)
        return fliplist
# flipkart("toothbrush", "toothbrush")

"""def reliancedigital(product, name):
    reliancedigitallink = f'https://www.reliancedigital.in/search?q={product}:relevance'
    reliancedigitalsource = requests.get(reliancedigitallink).text
    soup = BeautifulSoup(reliancedigitalsource, 'lxml')
    reliancelist = []
    reliancedigitalname = soup.find('p', 'sp__name').text.upper()
    if name.upper() in reliancedigitalname:
        reliancedigitalname = soup.find('p', 'sp__name').text
        reliancedigitalprice = soup.find('span', 'sc-bxivhb dmBTBc cc_pointer').text.strip()
        print(reliancedigitalprice)
        print(reliancedigitallink)
        reliancelist.append(reliancedigitalprice)
        reliancelist.append(reliancedigitallink)
        return reliancelist
    else:
        print("r not found")
        reliancedigitalprice = '0'
        reliancedigitallink = 'not found'
        reliancelist.append(reliancedigitalprice)
        reliancelist.append(reliancedigitallink)
        return reliancelist"""
# reliancedigital("sandisk+usb","sandisk usb")

"""def shopcules(product, name):
    shopclueslink = f'https://www.shopclues.com/search?q={product}&sc_z=2222&z=0&count=10&user_id=&user_segment=default'
    shopcluessource = requests.get(shopclueslink)
    soup = BeautifulSoup(shopcluessource.text, 'lxml')
    shopculesnameupper = soup.find('h2').text.upper()
    if name.upper() in shopculesnameupper:
        try:
            shoplist = []
            shopculesname = soup.find('h2').text.upper()
            shopcluesprice = soup.find('span', 'p_price').text.strip()
            shopculesimg = soup.find('div', 'img_section', 'img', 'det_img').get('src')
            print("shopclues name : ", shopculesname)
            print("shopclues img : ", shopculesimg)
            print("shopclues price : ", shopcluesprice)
            shoplist.append(shopcluesprice)
            shoplist.append(shopclueslink)
            shoplist.append(shopculesimg)
            return shoplist
        except:
            print("not found", shopculesname)
            shopculesprice = '0'
            shopclueslink = 'not found'
            shopcluesimg = 'not found'
            return shoplist"""
# shopcules("dress", "dress")

def paytmmall(product, name):
    paytmmalllink = f'https://paytmmall.com/shop/search?q={product}&from=organic&child_site_id=6&site_id=2'
    paytmmallsource = requests.get(paytmmalllink)
    soup = BeautifulSoup(paytmmallsource.text, 'lxml')
    paylist = []
    paytmmallname = soup.find('div', 'UGUy').text.upper()
    if name.upper() in paytmmallname:
        paytmmallprice = soup.find('div', '_1kMS', 'span').text
        paytmmallname = soup.find('div', 'UGUy').text
        paylist.append(paytmmallprice)
        paylist.append(paytmmalllink)
        print("paytm mall name : ", paytmmallname)
        print("paytm mall price : ", paytmmallprice)
        return paylist
    else:
        print("not found")
        paytmmallprice = '0'
        paytmmalllink = 'nt found'
        paylist.append(paytmmallprice)
        paylist.append(paytmmalllink)
        return paylist

"""def nykaa(product, name):
    nykaalink = f'https://www.nykaa.com/search/result/?ptype=search&q={product}&root=search&sourcepage=home&searchType=Manual'
    nykaasource = requests.get(nykaalink).text
    soup = BeautifulSoup(nykaasource, 'lxml')
    try:
        nykaalist = []
        nykaaname = soup.find('div', 'm-content__product-list__title', 'h2').text.upper()
        if name.upper() in nykaaname:
            nykaaprice = soup.find('div', 'price-info', 'span', 'post-card__content-price-offer').text.strip()
            nykaaname = soup.find('div', 'm-content__product-list__title', 'h2').text
            nykaaimg = soup.find('img', 'listing-img').get('src')
            print("nykaa name : ", nykaaname)
            print("nykaa price : ", nykaaprice)
            nykaalist.append(nykaaprice)
            nykaalist.append(nykaalink)
            nykaalist.append(nykaaimg)
            return nykaalist
    except:
        print("nykaa not found")
        nykaaprice = '0'
        nykaalink = 'not fund'
        nykaaimg = 'not fund'
        nykaalist.append(nykaaprice)
        nykaalist.append(nykaalink)
        nykaalist.append(nykaaimg)
        return nykaalist

def lush(product, name):
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

def theenvybox(product, name):
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

def rediff(product, name):
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

def smartshoppers(product, name):
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
    return smartshoppersprice, smartshoppersname, smartshopperslink"""

def deltapage(product, name):
    deltapagelink = f'https://deltapage.com/index.php?route=product/search&search={product}&description=true'
    deltapagesource = requests.get(deltapagelink).text
    soup = BeautifulSoup(deltapagesource, 'lxml')
    deltapagename = soup.find().text.upper()
    deltalist = []
    if name.upper() in deltapagename:
        deltapageprice = soup.find('span', 'price-normal').text.strip()
        deltapagename = soup.find().text
        deltalist.append(deltapageprice)
        deltalist.append(deltapagelink)
        return deltalist
    else:
        print("not found")
        deltapageprice = '0'
        deltapagelink = 'not found'
        deltalist.append(deltapageprice)
        deltalist.append(deltapagelink)
        return deltalist

def mobilestoreonline(product, name):
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

def amazon(product, name):
    name1 = name.replace(" ", "-")
    amalist = []
    amazonlink = f"https://www.amazon.in/{name1}/s?k={product}"
    amazonsource = requests.get(amazonlink).text
    soup = BeautifulSoup(amazonsource, 'html.parser')
    amazonname = soup.select('.a-size-medium.a-color-base.a-text-normal')
    amazonlength = int(len(amazonname))
    for i in range(0, amazonlength):
        amazonname = soup.select('.a-size-medium.a-color-base.a-text-normal')[i].getText().strip().upper()
        print("amazonname ", amazonname)
        if name.upper() in amazonname[0:20]:
            amazonprice = soup.select('.a-price-whole')[i].getText().strip()
            amalist.append(amazonprice)
            amalist.append(amazonlink)
            return amalist
        else:
            i += 1
            i = int(i)
            if i == amazonlength:
                amazonprice = '0'
                amazonlink = 'nt found'
                amalist.append(amazonprice)
                amalist.append(amazonlink)
                return amalist

"""name = input("enter product name : ")
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

mobilestoreonlineprice = mobilestoreonline(product)
if mobilestoreonlineprice == '0':
    print("product not found")
else:
    print("mobilestoreonline price : ", mobilestoreonlineprice)

nextprice = next(product)
if nextprice == '0':
    print("product not found")
else:
    print("next) price : ", nextprice)"""
