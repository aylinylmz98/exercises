#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#merhaba python
print("merhaba python")


# In[ ]:


#isim alma 
isim=input("isminizi giriniz")


# In[ ]:


x=int(input("bir sayi giriniz:"))
y=int(input("bir sayi giriniz"))
print("sayilarin toplami",x+y)


# In[ ]:


x=int(input("bir sayi giriniz:"))
y=int(input("bir sayi giriniz:"))
ort=(x+y)/2
print("sayilarin ortalamasi",(ort))


# In[ ]:


#if yapisi kullanma
ortalama=int(input("ortalamanizi giriniz:"))
if ortalama >= 50 :
    print("gectiniz")
else:
    print("kaldiniz")


# In[ ]:


#tek sayi mi cift sayi mi
x=int(input("bir sayi giriniz"))
if x%2==0 :
    print("cift sayi ")
else:
    print("tek sayi ")


# In[ ]:


#sinifa dahil etme
boy=float(input("boyunuzu giriniz: "))
agirlik=float(input("kilonuzu giriniz: "))
VKI=agirlik/(boy*boy)
if VKI >18 and VKI <25 :
    print("normal")
elif VKI >25 and VKI <30 :
    print("kilolu")
elif VKI >30 :
    print("obez")
else:
    print("ciddi obez")


# In[ ]:


for i in range(1,20):
    print(i)


# In[ ]:


for i in range(1,20):
    if i %2==0:
        print(i)


# In[ ]:


for i in range(1,50):
    if i %3==0 and i %5==0 :
        print(i)


# In[ ]:


sayi=input('Sayıyı Gir : ')
for i in range(1,int(sayi)+1):
        print(i)


# In[ ]:


kenar1=int(input("kisa kenari giriniz:"))
kenar2=int(input("uzun kenari giriniz :"))
alan=kenar1*kenar2
cevre=(2*kenar1)+(2*kenar2)
print("alan",alan)
print("cevre",cevre)


# In[ ]:


yazi=input("metin giriniz")
sayac=0
while sayac < len(yazi):
    print(yazi[sayac])
    sayac+=1


# In[ ]:


x=int(input("ilk sayinizi giriniz:"))
y=int(input("ikinci sayinizi giriniz:"))
toplam=0;
for i in range(int(x)+1,int(y)):
    toplam+=i
print("sayilarin toplami : {}".format(x,y,toplam))


# In[ ]:


secim = input("Sinema için (1), Tiyatro için (2) tuşlayınız : ")
ogrenci = input("Öğrenci misiniz(E/H) : ")
ucret = 0
 
#indirimsiz ücret hesaplama
if secim == '1':
  ucret = 15 #sinema
elif secim == '2':
  ucret = 10 #tiyatro
 
#öğrenci indirimi
if ogrenci =='E' or ogrenci =='e':
  ucret=ucret / 2  #%50
 
print("Ödemeniz gereken ücret :{}".format(ucret))


# In[ ]:


#daire alani bulan fonksiyon olustruma
def alan(yaricap):
    alan=float(yaricap)*float(yaricap)*3.14
    print("alan",alan)
    return alan

r=int(input("yaricap"))

alan(r)


# In[ ]:


def alan(kenar1,kenar2):
    alan=kenar1*kenar2
    print("alan",alan)
    return alan

kenar1=int(input("genisligi giriniz"))
kenar2=int(input("yukseklgi giriniz"))

alan(kenar1,kenar2)


# In[ ]:


#sayi tahmin etme oyunu 
from random import randint

rand=randint(1,100)
sayac=0

while True:
    sayac+=1
    sayi=int(input("bir sayi tahmin ediniz,cikmak icin 0 basiniz:"))
    if sayi==0:
        print("cikis yapiliyor.....")
        break
    elif sayi<rand:
        print("daha yuksek deger giriniz")
        continue
    elif sayi>rand:
        print("daha dusuk deger giriniz")
        continue
    else:
        print("tahmin sayiniz: {}".format(sayac))
        print("rasgele secilen sayi".format(rand))


# In[ ]:


#metinde gecen harfi kontrol etme fonksiyonu 
def kontrol(str):
  sayac = 0
  for ch in str:
    if ch == 'a':
      sayac = sayac + 1
      return True
      break
    
 
metin=input('Metin : ')
if(kontrol(metin)==True):
      print('a karakteri metin içinde var')
else:
      print('a karakteri metin içinde yok')
 


# In[1]:


#class yapisi
class kedi:
    pati_sayisi=4
    kulak="var4tane"
    yakalanan_fare=0
    def fareyakala(self):
        self.yakalanan_fare=self.yakalanan_fare+2

yulafcuma=kedi()
yulafcuma.yakalanan_fare=5
yulafcuma.fareyakala()
print("yulafcumanin yakaladigi fareler",yulafcuma.yakalanan_fare)        


# In[ ]:




