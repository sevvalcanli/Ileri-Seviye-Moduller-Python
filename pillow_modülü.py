from PIL import Image,ImageFilter

image = Image.open("2011-smurfs-movie.jpg")

#image.show()

#image.save("sirinler.jpg") #bu isimle kaydetti aynı fotoyu

#image.rotate(180).save("sirinler2.jpg") #180 derece döndürdü ve sirinler2 diye kaydetti

#image.convert(mode = "L").save("sirinler3.jpg")

#degistir = (960,600)
#image.thumbnail(degistir)
#image.save("sirinler4.jpg")


#image.filter(ImageFilter.GaussianBlur(5)).save("sirinler5.jpg") #blulaştırdı.

kırpılacakAlan = (340,0,950,600)
image.crop(kırpılacakAlan).save("sirinlerkirpilmis.jpg")
