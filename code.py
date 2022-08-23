
from re import L
import string
import requests
import webbrowser
import math
import streamlit as st
from bs4 import BeautifulSoup


def price_text_to_string(price):
    prc = ""
    for i in range(0, len(price)):
        if (price[i] >= '0' and price[i] <= '9'):
            prc += price[i]
        elif (price[i] == '.'):
            break

    n = len(prc)
    a = 0
    for i in range(0, n):
        a += (int(prc[i])*(pow(10, n-i-1)))

    return a
    # utility_function


def func(i):
    price_class = 'grid-product__price-amount'
    price = books_set_lis[i].find('div', {'class': price_class})

    link_class = 'grid-product__image'

    linkk = books_set_lis[i].find('a', {'class': link_class})

    book_title_class = 'grid-product__image'
    book_title = books_set_lis[i].find('a', {'class': book_title_class})

    # print("title : " , book_title['title'])
    # print("price: " ,"₹" + price.text)
    # print("rating : ",rating.text)
    # print("link :", linkk['href'] )
    price = price_text_to_string(price.text)

    ls.append([price, book_title['title'], linkk['href'],
              "pushtkosh", "no rating available"])

    # utility function


def func1(i):
    price_class = '_30jeq3'
    price = books_set_lisflp[i].find('div', {'class': price_class})
    rating_class = '_3LWZlK'

    rating = books_set_lisflp[i].find('div', {'class': rating_class})

    link_class = 's1Q9rs'

    linkk = books_set_lisflp[i].find('a', {'class': link_class})

    book_title_class = 's1Q9rs'
    book_title = books_set_lisflp[i].find('a', {'class': book_title_class})

    # print("title : " , book_title['title'])
    # print("price: " ,price.text)
    # print("rating : ",rating.text)
    # print("link :", mn_url+linkk['href'] )

    price = price_text_to_string(price.text)
    ls.append([price, book_title['title'], mn_url +
              linkk['href'], "flipkart", rating.text])


product = ''
header = st.container()
inpu = st.container()
search_results = st.container()


with header:
    st.title('Welcome to costObest')
with inpu:
    title = st.text_input('Search for product', 'HC verma')
    product = title
    st.write('The current product is', product)


with search_results:
    str = product
    mn_url = "https://pustakkosh.com/rent_or_buy_books.php"
    url = "https://pustakkosh.com/rent_or_buy_books.php?s="

    # url1="&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


def price_text_to_string(price):
    prc = ""
    for i in range(0, len(price)):
        if (price[i] >= '0' and price[i] <= '9'):
            prc += price[i]
        elif (price[i] == '.'):
            break

    n = len(prc)
    a = 0
    for i in range(0, n):
        a += (int(prc[i]) * (pow(10, n - i - 1)))
    return a


print("output :")

n = len(str)

for i in range(0, n):
    if (str[i] == ' '):
        url += "+"
    else:
        url += str[i]

# url+=url1
print(url)

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

book_classes = 'grid-product__wrap-inner'

books_set_lis = soup.find_all('div', {'class': book_classes})
pstsize = int(len(books_set_lis))
print(pstsize)
# books_data=  BeautifulSoup(books_set_lis[0],'html.parser')
ls = []


def func(i):
    price_class = 'grid-product__price-amount'
    price = books_set_lis[i].find('div', {'class': price_class})
    link_class = 'grid-product__image'
    grid_img_class = 'grid-product__image-wrap'
    grid_img_src = books_set_lis[i].find('div', {'class': grid_img_class})
    img_src = grid_img_src.find('img')
    linkk = books_set_lis[i].find('a', {'class': link_class})

    book_title_class = 'grid-product__image'
    book_title = books_set_lis[i].find('a', {'class': book_title_class})

    # print("title : " , book_title['title'])
    # print("price: " ,"₹" + price.text)
    # print("rating : ",rating.text)
    # print("link :", linkk['href'] )
    price = price_text_to_string(price.text)

    ls.append([price, book_title['title'], linkk['href'],
              "pushtkosh", img_src['src'], "no rating available"])


mn_urlflp = "https://www.flipkart.com"
urlflp = "https://www.flipkart.com/search?q="
url1flp = "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

# print("output :")

# n=len(str)

for i in range(0, n):
    if (str[i] == ' '):
        urlflp += "%20"
    else:
        urlflp += str[i]

urlflp += url1flp
print(urlflp)

pageflp = requests.get(urlflp)

soupflp = BeautifulSoup(pageflp.text, 'html.parser')

# page_classflp='_1YokD2 _3Mn1Gg'

# pgeflp=soupflp.find_all('div',{'class' : page_classflp})

book_classesflp = '_4ddWXP'

books_set_lisflp = soupflp.find_all('div', {'class': book_classesflp})

# books_dataflp=  BeautifulSoup(books_set_lisflp[0],'html.parser')
flipsize = int(len(books_set_lisflp))
print("flip", flipsize)


def func1(i):
    price_class = '_30jeq3'
    price = books_set_lisflp[i].find('div', {'class': price_class})

    rating_class = '_3LWZlK'
    rating = books_set_lisflp[i].find('div', {'class': rating_class})
    rat = ""
    if (rating == None):
        rat = "no rating available"
    else:
        rat = rating.text

    link_class = 's1Q9rs'

    linkk = books_set_lisflp[i].find('a', {'class': link_class})

    book_title_class = 's1Q9rs'
    book_title = books_set_lisflp[i].find('a', {'class': book_title_class})
    img_class = '_396cs4 _3exPp9'
    img_src = books_set_lisflp[i].find('img', {'class': img_class})

    # print("title : " , book_title['title'])
    # print("price: " ,price.text)
    # print("rating : ",rating.text)
    # print("link :", mn_url+linkk['href'] )

    price = price_text_to_string(price.text)
    ls.append([price, book_title['title'], mn_urlflp +
              linkk['href'], "flipkart", img_src['src'], rat])


# now adding booksswagon.com
# https://www.bookswagon.com/search-books/concept-of-physics-hc-verma

url_booksswagon = "https://www.bookswagon.com/search-books/"

for i in range(0, n):
    if (str[i] == ' '):
        url_booksswagon += "-"
    else:
        url_booksswagon += str[i]

print(url_booksswagon)

page_bookswagon = requests.get(url_booksswagon)

soup_bookswagon = BeautifulSoup(page_bookswagon.text, 'html.parser')

book_classes_bookswagon = 'list-view-books'

books_set_lis_bookswagon = soup_bookswagon.find_all(
    'div', {'class': book_classes_bookswagon})

int_total_no_of_books = int(len(books_set_lis_bookswagon))
print("book swagon", int_total_no_of_books)


def func2(i):
    price_class = 'sell'
    price = books_set_lis_bookswagon[i].find('div', {'class': price_class})
    # rating_class='_3LWZlK'
    # rating=books_set_lisflp[i].find('div',{'class': rating_class})

    bookswagon_name_link_class = 'title'

    linkk = books_set_lis_bookswagon[i].find(
        'div', {'class': bookswagon_name_link_class})

    # book_title_class=''
    book_title = linkk.find('a')

    img_src = books_set_lis_bookswagon[i].find('img')

    # print("title : " , book_title['title'])
    # print("price: " ,price.text)
    # print("rating : ",rating.text)
    # print("link :", mn_url+linkk['href'] )
    price = price_text_to_string(price.text)
    ls.append([price, book_title.text, book_title['href'],
              "bookswagon", img_src['src'], "no rating available"])


# sapna
url_sapna_main = "https://www.sapnaonline.com"
url_sapna = "https://www.sapnaonline.com/search?keyword="

for i in range(0, n):
    if (str[i] == ' '):
        url_sapna += "%20"
    else:
        url_sapna += str[i]

print(url_sapna)

page_sapna = requests.get(url_sapna)

soup_sapna = BeautifulSoup(page_sapna.text, 'html.parser')

book_classes_sapna = 'sc-AxirZ CategoryTabInner__ProductBox-qaa80s-0 jZjvfA'

books_set_lis_sapna = soup_sapna.find_all('div', {'class': book_classes_sapna})

int_total_no_of_books_sapna = int(len(books_set_lis_sapna))
print("sapna", int_total_no_of_books_sapna)


def func3(i):
    price_class = 'ProductCard__PrcieText-sc-10n3822-7 hnbQgS'
    price = books_set_lis_sapna[i].find('h3', {'class': price_class})
    # rating_class='_3LWZlK'

    # rating=books_set_lisflp[i].find('div',{'class': rating_class})

    sapna_name_link_class = 'ProductCard__AboutText-sc-10n3822-2 kOZyab link'

    book_title = books_set_lis_sapna[i].find(
        'h2', {'class': sapna_name_link_class})

    # book_title_class=''
    # book_title=linkk.find('a')
    linkk = books_set_lis_sapna[i].find('a')
    img_class = 'bookImage'
    img_src = books_set_lis_sapna[i].find('img')
    # print("title : " , book_title['title'])
    # print("price: " ,price.text)
    # print("rating : ",rating.text)
    # print("link :", mn_url+linkk['href'] )

    price = price_text_to_string(price.text)
    ls.append([price, book_title.text, url_sapna_main + linkk['href'],
              "sapna", img_src['src'], "no rating available"])


mn_url_amazon = "https://www.amazon.in"
url_amazon = "https://www.amazon.in/s?k="
# str=input()
for i in range(0, len(str)):
    if (str[i] == ' '):
        url_amazon += "+"
    else:
        url_amazon += str[i]

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


# Making the HTTP Request
webpage_amazon = requests.get(url_amazon, headers=HEADERS)

# Creating the Soup Object containing all data
soup_amazon = BeautifulSoup(webpage_amazon.content, "lxml")

print(url_amazon)

# print(soup)


book_set_Class_amazon = 's-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'
book_set_list_amazon = soup_amazon.find_all(
    'div', {'class': book_set_Class_amazon})

amazon_size = len(book_set_list_amazon)
print(amazon_size)


def func5(i):

    book_price_class = 'a-price-whole'
    book_price = book_set_list_amazon[i].find(
        'span', {'class': book_price_class})
    if (book_price == None):
        return
    # print(book_price.text)
    book_rate = price_text_to_string(book_price.text)
    book_title_class = 'a-size-medium a-color-base a-text-normal'
    book_title = book_set_list_amazon[i].find(
        'span', {'class': book_title_class})
    # print(book_title.text)
    link_class = 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'
    link = book_set_list_amazon[i].find('a', {'class': link_class})
    # print(mn_url_amazon+link['href'])
    img_class = 's-image'
    img_link = book_set_list_amazon[i].find('img', {'class': img_class})
    # print(img_link['src'])

    book_rating_class = "a-row a-size-small"
    book_rating_div = book_set_list_amazon[i].find(
        'div', {'class': book_rating_class})
    book_rating = book_rating_div.find('span')
    ls.append([book_rate, book_title.text, mn_url_amazon+link['href'],
              "amazon", img_link['src'], book_rating['aria-label']])


val1 = min(flipsize, 10)
val2 = min(2, pstsize)
val3 = min(2, int_total_no_of_books)
val4 = min(2, int_total_no_of_books_sapna)
val5 = min(10, amazon_size)
# val5=min(5,int_total_no_of_books_snapdeal)

if ((val1 + val2 + val3 + val4) == 0):
    print("SORRY! NO ITEM FOUND")
for i in range(0, val1):
    print(len(ls))
    # print("serial no ",i)
    func1(i)
for i in range(0, val4):
    print(len(ls))
    # print("serial no ",i)
    func3(i)

# print("pushtakosh")


# val3=0
for i in range(0, val3):
    func2(i)

for i in range(0, val5):
    func5(i)

    # for i in range(0,val5):
    #     func4(i)

ls.sort()


list_book_serial_no = []
list_book_L_no = []
list_book_price = []
list_book_name = []
list_book_link = []
list_book_website_name = []
list_book_rating = []

c = 1
val = "L"
val = val+(string(c))
ls_prc = ls[0][0]
list_book_L_no.append(val)


for i in range(0, len(ls)):
    list_book_serial_no.append(i+1)
    list_book_price.append(ls[i][0])
    list_book_name.append(ls[i][1])
    list_book_link.append(ls[i][2])
    list_book_website_name.append(ls[i][3])
    list_book_rating.append(ls[i][5])
    if (i >= 1):
        if (ls_prc != ls[i][0]):
            c += 1
            ls_prc = ls[i][0]
        val = "L"
        val = val+(string(c))
        list_book_L_no.append(val)


for i in range(0, len(ls)):
    item = st.container()
    with item:
        st.markdown("""---""")
        st.write("serial no ", i)
        for j in range(0, len(ls[i])):
            if (j == 0):
                converted_num = "{}".format(ls[i][j])
                st.write("₹"+converted_num)
            elif j == 4:
                st.image(ls[i][j])
            elif j != 4 and j != 3:
                st.write(ls[i][j])
            st.write("")
