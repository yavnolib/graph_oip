import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

#################### СЧИТЫВАНИЕ ДАННЫХ #################################
voltage = []
data = np.loadtxt('data.txt', dtype = int)
voltage = [i / 256 *3.3 for i in data] 
with open('settings.txt', mode = 'r') as settings:
    frequency = float(settings.read().split('\n')[0])

x = np.linspace(0, len(voltage)*frequency, len(voltage))
voltage = np.array(voltage)
max_elem_id = np.argmax(voltage)
zaryad = frequency * (max_elem_id + 1)
razryad = frequency * (len(voltage) - 1 - max_elem_id)
time = frequency * len(voltage)
################## НАСТРОЙКА ОТОБРАЖЕНИЯ ГРАФИКА ########################
title = 'Процеcc зарядки и разрядки конденсатора в RC-цепи'

fig, ax = plt.subplots()
ax.plot(x, voltage, 'g.-', label = 'V (t)')
ax.text(0.75 * time, 2, f'Время заряда = {zaryad} c.',
        fontsize = 11,
        color = 'r')
ax.text(0.75 * time , 1.5, f'Время разряда = {razryad} c.',
        fontsize = 11,
        color = 'r')
ax.minorticks_on()
ax.grid(which = 'major',
        color = 'k',
        linewidth = 1)
ax.grid(which = 'minor',
        color = 'k',
        linestyle = ':')
ax.set(xlim = (x.min(), x.max()), ylim = (voltage.min(), voltage.max()))
plt.title('\n'.join(wrap(title,60)), fontsize=14)
fig.set_figwidth(12)
fig.set_figheight(8)
plt.xlabel('Время,с ')
plt.ylabel('Показания ADC, Вольт')
plt.legend()
plt.show()
fig.savefig('graph.svg')
fig.savefig('graph.png')