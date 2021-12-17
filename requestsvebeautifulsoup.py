import requests
from bs4 import BeautifulSoup

url =  "https://www.n11.com/giyim-ayakkabi" # Site linkimiz
response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.

#print(soup.prettify()) # Daha güzel bir görüntü için prettify() fonksiyonunu kullanıyoruz.


#print(soup.find_all("a")) # Bize tüm <a> etiketlerini liste şeklinde dönüyor.


#for i in soup.find_all("a"):
 #   print(i.get("href")) #a nin içindeki href özelliğini almak istiyorum diyoruz.


#for i in soup.find_all("a"):
 #   print(i.text) #yazıları aldık.


# Bu kullanımın anlamı div etiketlerinden class'ı yp-poi-box-2 yi al anlamına geliyor.
for i in soup.find_all("div",{"class":"breadcrumb"}):
    print(i)

