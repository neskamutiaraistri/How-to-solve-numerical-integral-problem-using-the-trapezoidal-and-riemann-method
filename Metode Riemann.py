import numpy as p
import matplotlib.pyplot as plt

def func(x):
    return (x**2)*p.exp(-x)
a = float(input('Batas bawah(a) = '))   #a = 1.0
b = float(input('Batas atas (b) = '))   #b = 10.0
n = int (input('Jumlah grid (n) = '))   #n = divariasikan dimulai dari 10, 100, 1000

# Riemann
x = p.linspace(a,b,n)
dx = (x[-1]-x[0])/(n-1)

hasil = 0

for i in range (n-1):
    hasil += dx*func(x[i])
print('Hasil = ', hasil)

xp = p.linspace(a,b)
plt.plot(xp,func(xp))
for i in range(n-1):
    plt.bar(x[i],func(x[i]), align = 'edge',width=dx, color='red',edgecolor='black')
plt.show()
