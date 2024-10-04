# -*- coding: utf-8 -*-
"""Copy of Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wBio6UHatjoV4I6ibAlyEQpWjWU54N4I
"""

drimport numpy as np
import matplotlib.pyplot as plt

def unit_sample(n):
    return np.where(n == 0, 1, 0)

x = np.arange(-10, 11)

y = unit_sample(x)

plt.stem(x, y, use_line_collection=True)
plt.title('Unit Sample Sequence')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.xlim([-10, 10])
plt.ylim([-0.5, 1.5])
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    return np.where(n >= 0, 1, 0)

x = np.arange(-10, 11)

y = unit_step(x)

plt.step(x, y, where='post', label='Unit Step Signal', linewidth=2)
plt.title('Unit Step Signal')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.xlim([-10, 10])
plt.ylim([-0.5, 1.5])
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

def unit_ramp(n):
    return np.where(n >= 0, n, 0)

x = np.arange(-10, 11)

y = unit_ramp(x)

plt.plot(x, y, label='Unit Ramp Signal', linewidth=2)
plt.title('Unit Ramp Signal')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.xlim([-10, 10])
plt.ylim([-1, 10])
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

A = 1
k = 0.5
t = np.linspace(-5, 5, 100)

def exponential_signal(t, A, k):
    return A * np.exp(k * t)

x = exponential_signal(t, A, k)

plt.plot(t, x, label='Exponential Signal', linewidth=2)
plt.title('Exponential Signal')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.grid()
plt.xlim([-5, 5])
plt.ylim([0, np.max(x) * 1.1])
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

A = 1
T = 1
t = np.linspace(0, 5, 500)

def square_wave(t, A, T):
    return A * np.sign(np.sin(2 * np.pi * t / T))

x = square_wave(t, A, T)

plt.plot(t, x, label='Square Wave Signal', linewidth=2)
plt.title('Square Wave Signal')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.grid()
plt.xlim([0, 5])
plt.ylim([-1.5, 1.5])
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

A = 1
T = 2
t = np.linspace(0, 10, 500)

def triangular_wave(t, A, T):
    return A * (2 / T) * np.abs((t % T) - T / 2) - A / 2

x = triangular_wave(t, A, T)

plt.plot(t, x, label='Triangular Signal', linewidth=2)
plt.title('Triangular Signal')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.grid()
plt.xlim([0, 10])
plt.ylim([-1.5, 1.5])
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.legend()
plt.show()