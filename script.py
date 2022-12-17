from tkinter import N
import matplotlib.pyplot as plt
import csv
import tkinter
import seaborn as sns
import plotly.express as px

from numpy import average

numero_n = [400000000, 600000000, 800000000, 1000000000, 1200000000]
medidasSinOptimizar = []
medidasOptimizadas = []
mediasNormal = []
mediasOptimizada = []

with open('salida_p2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    counter = 0
    for row in csv_reader:
        counter += 1
        if counter % 10 != 0:
            medidasSinOptimizar.append(float(row[0]))
        else:
            mediasNormal.append(average(medidasSinOptimizar))
            counter = 0
            medidasSinOptimizar = []

with open('salida_p2op.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        counter += 1
        if counter % 10 != 0:
            medidasSinOptimizar.append(float(row[0]))
        else:
            mediasOptimizada.append(average(medidasSinOptimizar))
            counter = 0
            medidasSinOptimizar = []

print(mediasNormal)
print(mediasOptimizada)

plt.plot(numero_n, mediasNormal)
plt.plot(numero_n, mediasOptimizada)
plt.xlabel('N')
plt.ylabel('Tiempo (s)')
plt.legend(["Medidas originales", "Medidas optimizadas"])
plt.show()
plt.close()