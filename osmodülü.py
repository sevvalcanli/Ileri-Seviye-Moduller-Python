import os
from datetime import datetime

for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("C:/Users/ASUS/Desktop"):
    for i in dosya_isimleri:
        if(i.endswith(".txt")):
            print(i)
    #print("Klasör Yolu: ",klasör_yolu)
    #print("Klasör İsimleri: ", klasör_isimleri)
    #print("Dosya İsimleri: ", dosya_isimleri)
#print(os.getcwd())

#print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime)) #dosyanın değişme zamanını yazdırıyor.
#print(os.stat("test2.txt")) #bilgisayarda bulunan dosyanın tüm özellikleri

#os.rename("test.txt","test2.txt") #ismini değiştiriyor.

#os.rmdir("Deneme2/Deneme3")
#os.mkdir("Deneme2/Deneme3")
#os.removedirs("Deneme2/Deneme3") #ikisinide sildi
#os.makedirs("Deneme2/Deneme3")#iç içe oluşturdu.
#os.mkdir("Deneme1") #Deneme1 olusturdu.
#os.chdir("C:/Users/ASUS/Desktop")
#print(os.listdir())
#for i in os.listdir():
 #   print(i)