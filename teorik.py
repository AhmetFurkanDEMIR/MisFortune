import sys
from PyQt5 import QtWidgets,QtGui
import os
import time


def bir():

	os.system("title MisFortune")
	os.system("cls")
	print("\n\n  MisFortune")

	print("\n\n  Klasik bilgisayarlarda bilgi bitlerle temsil edilirken,\n  kuantum bilgisayarlar bilgisayar bellek birimi için kuantum bitlerini yani .... kullanır.")
	cevap = input("\n\n  '....' yerine gelecek kelime (küçük büyük harf duyarlılığı yoktur) = ")
	cevap = cevap.lower()

	kontrol = -1

	if(cevap=="qubit" or cevap=="kübit"):
		kontrol=1

	return kontrol

def iki():

  os.system("title MisFortune")
  os.system("cls")
  print("\n\n  MisFortune")
    
  app = QtWidgets.QApplication(sys.argv)
    
  pencere = QtWidgets.QWidget()
    
  pencere.setWindowTitle("MisFortune")

  etiket2 = QtWidgets.QLabel(pencere)
  etiket2.setPixmap(QtGui.QPixmap("images.jpg"))
  etiket2.move(100,200)
    
  etiket = QtWidgets.QLabel(pencere)
    
  etiket.setText("""
        
        MisFortune
        
         
        Klasik bilgisayarlarda veri işleme,

        NOT, AND ve OR gibi mantıksal operatörler tarafından gerçekleştirilirken

Quantum bilgisayarlarda veri işleme, kuantum operatöriler tarafından gerçekleştirilir.

           
    
    """)


  etiket.move(10,2)
  pencere.setGeometry(50,50,500,400)
  pencere.show()
  return(app.exec_())
	
	
def iki1():

	cevap = input("  Aşağıdaki boşluğu uygun şekilde doldurunuz.\n\n  ...... bilgisayarlarda veri işleme mantıksal operatörlerle gerçekleştirilir = ")
	cevap = cevap.lower()

	kontrol = -1

	if(cevap=="klasik"):
		kontrol=1

	return kontrol



def uc():

  os.system("title MisFortune")
  os.system("cls")
  print("\n\n  MisFortune")

  os.system("title MisFortune")
  os.system("cls")
  print("\n\n  MisFortune")
    
  app = QtWidgets.QApplication(sys.argv)
    
  pencere = QtWidgets.QWidget()
    
  pencere.setWindowTitle("MisFortune")

  etiket2 = QtWidgets.QLabel(pencere)
  etiket2.setPixmap(QtGui.QPixmap("indir.jpg"))
  etiket2.move(100,200)
    
  etiket = QtWidgets.QLabel(pencere)
    
  etiket.setText("""
        
        MisFortune
        
         
  Kuantum kriptografi tekniği mesajın iletilmesinden çok
		
  mesajın şifrelenmesinde ve şifrelenmiş mesajın çözülmesinde
		
  kullanılan anahtarın güvenilir bir biçimde alıcı ve verici arasında değişimi ile ilgilenir.

           
    
    """)


  etiket.move(10,2)
  pencere.setGeometry(50,50,500,400)
  pencere.show()
  return(app.exec_())

def uc1():

	cevap = input("\n\n  Bu açıklamada kuantum kriptografi tekniği hangi ilkeye dayandırılmıştır? = ")
	cevap = cevap.lower()

	kontrol = -1

	if(cevap=="belirsizlik ilkesi" or "belirsizlik"):
		kontrol=1

	return kontrol



def dort():

	os.system("title MisFortune")
	os.system("cls")
	print("\n\n  MisFortune - Dördüncü Soru")

	print("\n\n  Quantum programlamayı normal programlama gibi yapmak mümkün değil")
	print("  Bunun için bize yardımcı olan bir kaç tane özelleşmiş diller mevcuttur.")

	cevap = input("\n\n  Quantum programlama yapmak için gerekli olan dillerden birinin ismini yazınız = ")
	cevap = cevap.lower()

	kontrol = -1

	if(cevap== "forest" or cevap == "qiskit" or cevap == "qrojectq" or cevap == "quantum development kit"):
		kontrol=1

	return kontrol


def bes():

  os.system("title MisFortune")
  os.system("cls")
  print("\n\n  MisFortune")

  os.system("title MisFortune")
  os.system("cls")
  print("\n\n  MisFortune")
    
  app = QtWidgets.QApplication(sys.argv)
    
  pencere = QtWidgets.QWidget()
    
  pencere.setWindowTitle("MisFortune")

  etiket2 = QtWidgets.QLabel(pencere)
  etiket2.setPixmap(QtGui.QPixmap("aqwe.jpg"))
  etiket2.move(90,130)
    
  etiket = QtWidgets.QLabel(pencere)
    
  etiket.setText("""
        
        MisFortune
        
        Kuantum bilgisayarları bir çok işlemi günümüzdeki bilgisayarlara göre 

        Çok daha hızlı bir şekilde yapabilmekte,
        
        Bunun sebebi de süperposizyon (superposition) ve kuantum dolanıklığı (entanglement)dır.
    
    """)


  etiket.move(10,2)
  pencere.setGeometry(50,50,500,450)
  pencere.show()
  return(app.exec_())

def bes1():

  os.system("cls")
	
  print("\n\n  MisFortune")

  cevap = input("\n\n  ............., Google'nin çıkarmış olduğu kuantum bilgisayardır = ")
  cevap = cevap.lower()

  kontrol = -1

  if(cevap=="supremacy"):
    kontrol=1

  return kontrol
