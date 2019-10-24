import requests
from bs4 import BeautifulSoup



r = requests.get('https://www.80txt.la/sort17/1.html')


c = r.text


soup = BeautifulSoup(c,'html.parser')
page_div = soup.find('div',{'id':'foot_pages'})
page = page_div.find_all('a')[-1].text
books=[]
for i in range(2, 11):
    url='https://www.80txt.la/sort17/'+str(i)+'.html'
    p_r=requests.get(url)
    p_c=p_r.text
    p_soup=BeautifulSoup(p_c,'html.parser')
    all_img_list=p_soup.find_all('div',{'id':'slist'})
       
    for book in all_img_list:
        bookDic={}
        bookDic['picurl']=book.find('div',{'id':'list_art_2013'}).find('div',{'class':'book_pic'}).find('img')['src']
        bookDic['name']=book.find('div',{'class':'book_bg'}).find('a').text
        bookDic['info']=book.find('div',{'class':'book_jj'}).text
        books.append(bookDic)
print(books)