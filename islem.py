from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
from math import pi, atan, sqrt, sin, cos
from random import randrange
from PyQt5 import QtWidgets,QtGui
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
from random import randrange
import numpy as np
from qiskit import *
import os
import time
import sys


def bir():

  os.system("title MisFortune - İkinci Soru")
  os.system("cls")
  print("\n\n  MisFortune - Birinci Soru")
    
  app = QtWidgets.QApplication(sys.argv)
    
  pencere = QtWidgets.QWidget()
    
  pencere.setWindowTitle("MisFortune - ikinci Soru")
    
  etiket = QtWidgets.QLabel(pencere)
    
  etiket.setText("""
        
        MisFortune
        
         
         Kayan Noktalı Sayılar (Float)
         
           
           Kayan Noktalı sayı, real sayıların bilgisayardaki karşılığıdır.
           
           örneğin 1.0 Kayan noktalı sayıdır.
           
           Klasik Bilgisayara geçirilen bir sayı ikilik tabanda yazılır.
           
           Örneğin 10 sayısının ikilik tabana çevirilmiş hali 0101 şeklinde yazılır.

           Bunun sebebi ise klasik bilgisayarın silisyumdan yapılmasıdır.

           
    
    """)


  etiket.move(10,2)
  pencere.setGeometry(50,50,500,300)
  pencere.show()
  return(app.exec_())

def bir1(add):

  os.system("cls")
  print("\n\n  MisFortune - İkinci Soru ---{}---".format(add))
  secim = input("\n\n   a = 1.0\n   b = 0.9\n\n   a-b işleminin sonucunun ne çıkmasını beklersiniz = \n\n   a) 0.1'e eşit\n\n   b) 0.1'e eşit değil\n\n   Secim =  ")

  kontrol=-1

  if(secim=='b' or secim=='B'):
    kontrol=1

  return kontrol


def iki():

  os.system("title MisFortune")
  os.system("cls")
  print("\n\n  MisFortune")

  circ = QuantumCircuit(3)



  circ.h(0)

  circ.cx(0, 1)

  circ.cx(0, 2)

  print("\n  ")
  print(circ.draw())

  print("\n\n  Seninin için 10 kuantum bit ve 10 klasik bit ile bir kuantum devresi tasarladık. ")
  test = int(input("\n\n  bu devreyi kaç defa çalıştırmak istersin = "))

  qreg3 =  QuantumRegister(10)
  creg3 = ClassicalRegister(10)

  mycircuit3 = QuantumCircuit(qreg3,creg3)


  picked_qubits=[] 

  for i in range(10):
   
    if randrange(2) == 0:
     
      mycircuit3.x(qreg3[i])
      picked_qubits.append(i)

 
  mycircuit3.measure(qreg3,creg3)    


  mycircuit3.draw(reverse_bits=True)


  job = execute(mycircuit3,Aer.get_backend('qasm_simulator'),shots=test)

  counts = job.result().get_counts(mycircuit3)
        
  print("\n  {'ölçtüğümüz kuantum bitleri' : devreyi çalıştırma sayısı } = ",counts)


def ucz():

  os.system("title MisFortune - İkinci Soru")
  os.system("cls")
  print("\n\n  MisFortune - Birinci Soru")

  print("\n\n  |v)=(a−0.2)    ve    |u) = (1/√b) / (−1/√3) işleminin sonucunda a,b nin cevabı nedir (hesap makinesi kullanınız).")
  a = float(input("\n\n a = "))
  b = float(input("\n\n b = "))


  values = [-0.2]

  total = 0
  for i in range(len(values)):
    total += values[i]**2;

  a1 = (1-total)**0.5
  a2 = -(1-total)**0.5


  values = [-1/(3**0.5)]

  total = 0 
  for i in range(len(values)):
    total += values[i]**2; 
  
  b1 = 1/(1-total)

  kontrol = -5

  if(b==b1):
    kontrol = -1

  elif(a==a1 or a==a2):

    kontrol=kontrol+2


  return kontrol


def dort():

  os.system("cls")
  print("\n\n  MisFortune")

  print("\n\n  Tek bir qubit ile bir kuantum devresi oluşturalım.")
  print("\n\n  Bu devreyi başlatmak için rastgele bir açı [0, 2pi] belirleyelim ve souçları kontrol edelim.")
  giris = int(input("\n\n  0 ila 360 derece arasında bir sayı giriniz = "))

  theta = giris
  state = [cos(theta), sin(theta)]
  print("\n\n  Belirlediğiniz açı : {:.10f}".format(theta))
  print("\n\n  Durum başlatılıyor : ({:.10f}, {:.10f})".format(*state))

# Create a quantum circuit
  qreg = QuantumRegister(1)
  creg = ClassicalRegister(1)
  circuit = QuantumCircuit(qreg,creg)

# Initialize circuit
  circuit.initialize(state, qreg)

# Now execute this circuit
  job = execute(circuit, Aer.get_backend('statevector_simulator'))
  statevector = job.result().get_statevector(circuit)
  print("\n\n  Belirtilen vektör : ({:.10f}, {:.10f})".format(*[component.real for component in statevector]))
