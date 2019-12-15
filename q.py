import os
import time
import random
import teorik
import islem

toplam = 10

os.system("cls")
os.system("title MisFortune")
print("\n\n  MisFortune")
os.system("color b0")
add = input("\n\n    Adınız = ")

def kaydet(toplam,add):

	file = open("quantum.demir","a") # a kipinde dosyayı tekrar açtık
	file.write("\n")
	file.write(add)
	file.write(",")
	file.write(str(toplam))
	


def satirlar(satir,knt):

	satir=satir[:-1] #pythonda print input gibi fonksiyonlarda otomatik olarak "\n" vardır, ve bunu kaldırıyoruz (javada system out println() de bu özellik vardır)
	liste= satir.split(",") # virgül gördüğü yerden parçalara ayırıp listeye atıyoruz.
	isim=liste[0] # parçaları ait oldukları yeni listelere dağıtıyoruz.
	skor=liste[1]

	if(knt==0):
		print("\n\n  MisFortune --skorlar--")
		os.system("color b0")
		print("\n  ",isim)
		print(" = ",skor)
		

def servera():

	try:

		file = open("quantum.demir","r+",encoding="utf-8") # "utf-8" Türkçe karekter isimli öğrenciler için kullandim, r+ kipinde dosyayı açtık

	except FileNotFoundError: # try except blokları sayesinde "DEMIR Not (giris).txt" adlı dosyayı bulamazsa, kullanıcıya yenisini olustur seklinde mesaj gönderdim
			
		os.system("CLS")
		os.system("color c7")
		print("\n\n  'DEMIR Not (giris).txt' adlı dosaya ya silinmiş yada hasar görmüştür. lütfen var ise silip yenisini oluşturunuz...\a")
		input("\n\n   Çıkmak için Enter'e basınız. \n\n")
		quit()

	file = open("quantum.demir","a") # a kipinde dosyayı tekrar açtık
	file.write(",") # En son satırın en sonuna "," virgül koyduk, sebebi ise son satırdaki kişiyi virgül görmediğinden dolayı parça olarak saymıyordu
	file = open("quantum.demir","r+",encoding="utf-8") # "utf-8" Türkçe karekter isimli öğrenciler için kullandim, r+ kipinde dosyayı tekrardan açtık

	for i in file: #for döngüsü pythonda, listelerin dosyalarin demetlerin sözlüklerin içinde gezinmek için kullanılır
			
		satirlar(i,-5) #dosya içindeki notları ve öğrencileri, alt alta satirlar() isimli fonksiyona gönderdim

def serverb():

	try:

		file = open("quantum.demir","r+",encoding="utf-8") # "utf-8" Türkçe karekter isimli öğrenciler için kullandim, r+ kipinde dosyayı açtık

	except FileNotFoundError: # try except blokları sayesinde "DEMIR Not (giris).txt" adlı dosyayı bulamazsa, kullanıcıya yenisini olustur seklinde mesaj gönderdim
			
		os.system("CLS")
		os.system("color c7")
		print("\n\n  'DEMIR Not (giris).txt' adlı dosaya ya silinmiş yada hasar görmüştür. lütfen var ise silip yenisini oluşturunuz...\a")
		input("\n\n   Çıkmak için Enter'e basınız. \n\n")
		quit()

	file = open("quantum.demir","a") # a kipinde dosyayı tekrar açtık
	file.write(",") # En son satırın en sonuna "," virgül koyduk, sebebi ise son satırdaki kişiyi virgül görmediğinden dolayı parça olarak saymıyordu
	file = open("quantum.demir","r+",encoding="utf-8") # "utf-8" Türkçe karekter isimli öğrenciler için kullandim, r+ kipinde dosyayı tekrardan açtık

	for i in file: #for döngüsü pythonda, listelerin dosyalarin demetlerin sözlüklerin içinde gezinmek için kullanılır
			
		satirlar(i,0) #dosya içindeki notları ve öğrencileri, alt alta satirlar() isimli fonksiyona gönderdim

servera()

def basla(add,toplam):

	os.system("cls")
	print("\n\n  MisFortune")

	print("\n\n  Merhaba {} ben qübit.".format(add)) 
	print("\n  Gezegenimden çok uzaktayım ve yardımına ihtiyacım var!")
	print("  Uzay gemimin yakıtı bitti, her istasyonda sana sorulan sorulara\n  doğru cevap vererek yakıt kazanabiliriz\n  ancak her yanlış cevabında da yakıtımızı kaybedeceğiz.")
	print("  Gezegenime ulaşmam senin elinde.. Hazır mısın benimle bu maceraya?\n\n  'Devam etmek icin Enter'e basınız' ")
	input()

	os.system("cls")
	print("\n\n  MisFortune")
	print("\n\n   İlk istasyon gezegenimiz Demir gezegeni {}.\n\n   Yolumuza devam etmek ve aynı zamanda yakıt kazanabilmek için bu soruyu doğru cevapla !".format(add))
	input("\n\n  Devam etmek icin Enter'e basınız ")


	
	kontrol1 = teorik.bir()

	if(kontrol1==-1):
		os.system("cls")
		os.system("color 47")
		os.system("title MisFortune")
		toplam=toplam-4
		print("\n\n  MisFortune")
		print("\n\n  Cevap = qübit veya kübit olacaktı.\n\n  Normal bilgisayarlarda bit kavramı kullanırken, quantum bilgisayarlarda qubit/kübit kavramını kullanırız.\n  Yakıtımız = {}".format(toplam))
		
		i=0
		print("\n")

		input("\n\n  Devam etmek icin Enter'e basınız ")


		
		
	else:
		toplam=toplam+4
		
		os.system("cls")
		print("\n\n  MisFortune")

		print("\n\n   Tebrikler {} soruyu doğru bildik ve yolumuza devam ediyoruz :)\n\n   Yakıtımız = {}".format(add,toplam))

		i=0
		print("\n")

		input("\n\n  Devam etmek icin Enter'e basınız ")

	os.system("color b0")
	os.system("cls")
	print("\n\n  MisFortune")
	print("\n\n  Merhaba {}, şimdi ise Stealth gezegenindeyiz. Bu gezegende sayılar bizim en iyi dostumuz :)  ".format(add))
	input("\n\n  Devam etmek icin Enter'e basınız ")

	

	islem.bir()
	kontrol = islem.bir1(add)

	if(kontrol==-1):
		os.system("cls")
		os.system("color 47")
		os.system("title MisFortune")
		print("\n\n  MisFortune")
		print("\n\n  cevap = 0.1'e eşit değildir. Bu bilgisayarın Hammadesi olan Silisyumdan dolayı kaynaklanıyor.\n\n  Bu hatayı quantum bilgisayarlarda alamazsınız çünkü onların çalışma mekaniği biraz daha farklıdır :)")
		print("\n\n  Yaktımız = {}".format(toplam))

		i=0
		print("\n")

		input("\n\n  Devam etmek icin Enter'e basınız ")
		toplam=toplam-3

	else:
		toplam=toplam+4
		
		os.system("cls")
		print("\n\n  MisFortune")

		print("\n\n   Tebrikler {} soruyu doğru bildik ve yolumuza devam ediyoruz :)\n\n   Yakıtımız = {}".format(add,toplam))

		i=0
		print("\n")

		input("\n\n  Devam etmek icin Enter'e basınız ")

	os.system("cls")
	os.system("color b0")
	os.system("title MisFortune")
	print("\n\n  MisFortune")
	print("\n\n   qiskit gezegenine geldik. Bu gezegenin özelliğini pythonda quantum bilgisayarı simüle etmek için kullanıyoruz.")
	input("\n\n  Devam etmek icin Enter'e basınız ")

	teorik.iki()
	kontrol = teorik.iki1()

	if(kontrol==-1):

		os.system("cls")
		os.system("color 47")
		os.system("title MisFortune")
		print("\n\n  MisFortune")
		toplam=toplam-6
		print("\n\n  cevap = Klasik bilgisayardır. yakıtımız = {} ".format(toplam))

		if(toplam<0):

			os.system("cls")
			print("\n\n  MisFortune")
			print("\n\n  Malesef yakıtımız bitti. iyi oyundu {} :) ".format(add))
			kaydet(str(toplam*-1),add)
			input("\n\n  Ana menüye dönmek icin Enter'e basınız ")
			return

		input("\n\n  Devam etmek icin Enter'e basınız ")
		

	else:

		os.system("cls")
		os.system("title MisFortune")
		print("\n\n  MisFortune")
		toplam=toplam+2
		print("\n\n   Tebrikler {}, bu soruyu doğru cevapladın ve yakıtımız = {}".format(add,toplam))

		i=0
		print("\n")

		input("\n\n  Devam etmek icin Enter'e basınız ")

	os.system("cls")
	os.system("color b0")
	os.system("title MisFortune")
	print("\n\n  MisFortune")

	print("\n\n  Şimdi seni çok güzel bir gezegene götüreceğim!\n  Bu gezegeni görmeden evine gitmeni istemiyorum!\n\n  Bu gezegende quantum bir devre göreceğiz. Heyecanın dindiyse devam edelim :) ")
	input("\n\n  Devam etmek icin Enter'e basınız ")

	islem.iki()
	input("\n\n  Muhteşem değil mi? :)\n\n  Devam etmek icin Enter'e basınız ")

	os.system("cls")
	print("\n\n  MisFortune")
	print("\n\n   Evet şimdi ise sayılar gezegenindeyiz, işin zor {} hesap makinelerini hazırla:)".format(add))
	input("\n\n  Devam etmek icin Enter'e basınız ")



	kontrol = islem.ucz()

	if(kontrol<0):

		os.system("cls")
		os.system("color 47")
		os.system("title MisFortune")
		print("\n\n  MisFortune")
		toplam=toplam-2

		if(toplam<0):

			os.system("cls")
			print("\n\n  MisFortune")
			print("\n\n  Malesef yakıtımız bitti. iyi oyundu {} :) ".format(add))
			kaydet(str(toplam*-1),add)
			input("\n\n  Ana menüye dönmek icin Enter'e basınız ")
			return

		print("\n\n  cevap => \n\n  a = 0.9797958971132712 veya -0.9797958971132712\n\n  b = 1.5000000000000004\n\n  yakıtımız = {} ".format(toplam))

		i=0
		print("\n")

		input("\n\n  Devam etmek icin Enter'e basınız ")

	else:

		os.system("cls")
		os.system("title MisFortune")
		print("\n\n  MisFortune")
		toplam=toplam+4
		print("\n\n   Tebrikler {}, bu soruyu doğru cevapladın ve yakıtımız = {}".format(add,toplam))

		i=0
		print("\n")

		input("\n\n  Devam etmek icin Enter'e basınız ")


	os.system("cls")
	os.system("color b0")
	os.system("title MisFortune")
	print("\n\n  MisFortune")
	print("\n\n  artık evime yaklaşıyoruz. sabret az kaldı.")
	input("\n\n  Devam etmek icin Enter'e basınız ")
	
	teorik.uc()

	kontrol = teorik.uc1()
	
	if(kontrol == -1):

		os.system("cls")
		os.system("color 47")
		os.system("title MisFortune")
		print("\n\n  MisFortune")
		toplam=toplam-3

		if(toplam<0):
			os.system("cls")
			print("\n\n  MisFortune")
			print("\n\n  malesef yakıtımız bitti. iyi oyundu {} :) ".format(add))
			kaydet(str(toplam*-1),add)
			input("\n\n  Ana menüye dönmek icin Enter'e basınız ")
			return

		print("\n\n  cevap = Kuantum kriptografi tekniği temel bir fizik kanunu olan Heisenberg’in belirsizlik ilkesine dayanmaktadır.")
		print("  Bu ilkeye göre kuantum mekaniğinin temel öğesi olan bir foton’un aynı anda iki özelliği bilinemez.")
		print("  Bu da iletişim kanalında ki bir fotonun kopyalanmasını imkansız hale getirmektedir. yakıtımız = {}".format(toplam))

		i=0
		print("\n")

		input("\n\n  Devam etmek icin Enter'e basınız ")

	else:

		os.system("cls")
		os.system("title MisFortune")
		print("\n\n  MisFortune")
		toplam=toplam+4
		print("\n\n   Tebrikler {}, bu soruyu doğru cevapladın ve yakıtımız = {}".format(add,toplam))

		i=0
		print("\n")

		input("\n\n  Devam etmek icin Enter'e basınız ")

	os.system("cls")
	os.system("color b0")
	os.system("title MisFortune")
	print("\n\n  MisFortune")

	kontrol = teorik.dort()

	if(kontrol==-1):

		os.system("cls")
		os.system("color 47")
		os.system("title MisFortune")
		print("\n\n  MisFortune")
		toplam=toplam-6

		if(toplam<0):

			os.system("cls")
			print("\n\n  MisFortune")
			print("\n\n  malesef yakıtımız bitti. iyi oyundu {} :) ".format(add))
			kaydet(str(toplam*-1),add)
			input("\n\n  Ana menüye dönmek icin Enter'e basınız ")
			return

		print("\n\n  cevap = Quantum bilgisayara normal bilgisayarlara ulaştığımız gibi ulaşamayız.")
		print("  Bu bilgisayarları kullanmak için aracı bir dile ihtiyacımız vardır.")
		print("  Bu dillerden bazıları ise Forest, qistik, qrojectq ve quantum development kit 'dir.\n  Yakıtımız={}".format(toplam))

		i=0
		print("\n")

		input("\n\n  Devam etmek icin Enter'e basınız ")

	else:

		os.system("cls")
		os.system("title MisFortune")
		print("\n\n  MisFortune")
		toplam=toplam+4
		print("\n\n   Tebrikler {}, bu soruyu doğru cevapladın ve yakıtımız = {}".format(add,toplam))

		i=0
		print("\n")

		input("\n\n  Devam etmek icin Enter'e basınız ")


	os.system("cls")
	os.system("color b0")
	os.system("title MisFortune")
	print("\n\n  MisFortune")
	print("\n\n  merhaba {}, sana yeni öğrendiğim bir şeyi göstermek istiyorum.\n\n  Biliyorsunki artık gezegenine yaklaştık, Sana gitmeden birşeyler öğretmek istiyorum :)".format(add))
	input("\n\n  Devam etmek icin Enter'e basınız ")
	os.system("cls")
	islem.dort()
	input("\n\n  Devam etmek icin Enter'e basınız ")

	os.system("cls")
	teorik.bes()
	os.system("cls")
	kontrol = teorik.bes1()


	if(kontrol==-1):
		os.system("cls")
		os.system("color 47")
		os.system("title MisFortune")
		print("\n\n  MisFortune")
		toplam=toplam36
		print("Doğru cevap Supremacy olmalıydı!\n\n Google'ın da son teknoloji olan quantum bilgisayarının adı da kendisi kadar havalı.\n  Yakıtımız:".format(toplam))

		if(toplam<0):
			os.system("cls")
			print("\n\n  MisFortune")
			print("\n\n  malesef yakıtımız bitti. iyi oyundu {} :) ".format(add))
			kaydet(str(toplam*-1),add)
			input("\n\n  Ana menüye dönmek icin Enter'e basınız ")
			return

		print("\n\n  cevap = Quantum bilgisayara normal bilgisayarlara ulaştığımız gibi ulaşamayız.")
		print("  Bu bilgisayarları kullanmak için aracı bir dile ihtiyacımız vardır.")
		print("  Bu dillerden bazıları ise Forest, qistik, qrojectq ve quantum development kit 'dir.\n  Yakıtımız={}".format(toplam))

		i=0
		print("\n")


		input("\n\n  Devam etmek icin Enter'e basınız ")

	else:

		os.system("cls")
		os.system("title MisFortune")
		print("\n\n  MisFortune")
		toplam=toplam+6
		print("\n\n   Tebrikler {}, bu soruyu doğru cevapladın ve yakıtımız = {}".format(add,toplam))

		i=0
		print("\n")

		input("\n\n  Devam etmek icin Enter'e basınız ")


	os.system("cls")
	os.system("color b0")
	os.system("title MisFortune")
	print("\n\n  MisFortune")
	print("\n\n   Teşekkür ederim beni gezegenime ulaştırdığın için.\n\n   bir başka mecarada görüşmek dileyiyle hoscakal....")
	print("\n\n   Skorun = {}".format(toplam*4))
	kaydet(str(toplam*4),add)

	while(i<toplam*4/3):
			print("         ","------")
			i=i+1

	input("\n\n  Devam etmek icin Enter'e basınız ")


def oyun_oynanis():
	
	os.system("cls")

	print("\n\n  MisFortune")

	print(""" 

  Oyun Nasıl Oynanır?
   
   1-"Oyuna başla" ya tıklayınız.
   2-Ekrana gelen bilgi kutucuğunu dikkatlice okuyarak sonrasında gelen sorulara doğru cevap vermeye çalışın.
   3-Her doğru cevabınızda qübite yakıt kazandırırken , her yanlış cevapta yakıt kaybettireceksiniz.
   4-Oyun sonunda qübit sayenizde gezegenine ulaşacak ya da sonsuza kadar uzayda kaybolacaktır.
   5-qübiti kurtarmak sizin elinizde , başarılar..

		""")
	print("\n  Ana menüye dönmek dönmek için herhangi bir tuşa basınız =  ")
	input("")




menu= """
	
   MisFortune'a Hoş Geldin  ---{}---

	1) Oyuna Başla

	2) Oyun nasıl oynanır ?

	3) Geçmiş skorlar

	Q) Çıkış

"""





while True:

	os.system("cls")
	os.system("title MisFortune")
	os.system("color b0")

	print(menu.format(add))
	
	secim = input("\n   Secim = ")

	if(secim=='1'):

		basla(add,toplam)

	elif(secim=='2'):

		oyun_oynanis()

	elif(secim=='3'):
		os.system("cls")
		serverb()
		input("\n\n  Devam etmek icin Enter'e basınız ")

		

	elif(secim=='q' or secim=='Q'):

		os.system("cls")
		print("\n\n  MisFortune\n\n    Quantum bizimle daha güzel...")

		quit()

