import numpy as np
import matplotlib.pyplot as plt

# Frecuencia de muestreo y duración
fs = 1000  # Hz
t = np.arange(-1, 1, 1/fs)  # 2 segundos centrados en t=0

# 1) Pulso rectangular
# Definición: pulso de amplitud 1, duración 0.2 s
pulse = np.where(np.abs(t) <= 0.1, 1.0, 0.0)

# 2) Función escalón
# Definición: escalón unitario que cambia en t=0
step = np.where(t >= 0, 1.0, 0.0)

# 3) Función senoidal
freq = 5  # Hz
sine = np.sin(2 * np.pi * freq * t)

# Gráficas de las señales en el dominio del tiempo
plt.figure(figsize=(12, 8))
plt.subplot(3, 2, 1)
plt.plot(t, pulse)
plt.title("Pulso rectangular en el tiempo")
plt.xlabel("Tiempo [s]")
plt.grid()

plt.subplot(3, 2, 3)
plt.plot(t, step)
plt.title("Escalón en el tiempo")
plt.xlabel("Tiempo [s]")
plt.grid()

plt.subplot(3, 2, 5)
plt.plot(t, sine)
plt.title("Senoidal en el tiempo")
plt.xlabel("Tiempo [s]")
plt.grid()

# Calcular la Transformada de Fourier con np.fft.fft
n = len(t)
freqs = np.fft.fftfreq(n, d=1/fs)
# fftshift para centrar el cero en el espectro
freqs_shifted = np.fft.fftshift(freqs)

pulse_fft = np.fft.fftshift(np.fft.fft(pulse))
step_fft = np.fft.fftshift(np.fft.fft(step))
sine_fft = np.fft.fftshift(np.fft.fft(sine))

# Magnitud de cada espectro
plt.subplot(3, 2, 2)
plt.plot(freqs_shifted, np.abs(pulse_fft))
plt.title("Magnitud del pulso rectangular")
plt.xlabel("Frecuencia [Hz]")
plt.grid()

plt.subplot(3, 2, 4)
plt.plot(freqs_shifted, np.abs(step_fft))
plt.title("Magnitud del escalón")
plt.xlabel("Frecuencia [Hz]")
plt.grid()

plt.subplot(3, 2, 6)
plt.plot(freqs_shifted, np.abs(sine_fft))
plt.title("Magnitud de la senoidal")
plt.xlabel("Frecuencia [Hz]")
plt.grid()

plt.tight_layout()
plt.show()

# Análisis de propiedades:
# - Linealidad: combinación lineal de señales
combined_signal = 0.5 * pulse + 0.5 * sine
combined_fft = np.fft.fftshift(np.fft.fft(combined_signal))

plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(t, combined_signal)
plt.title("Combinación lineal: 0.5*pulse + 0.5*sine")
plt.xlabel("Tiempo [s]")
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(freqs_shifted, np.abs(combined_fft))
plt.title("Magnitud de la FFT de la combinación lineal")
plt.xlabel("Frecuencia [Hz]")
plt.grid()

plt.tight_layout()
plt.show()

# Desplazamiento en el tiempo
delay = 0.2  # segundos
pulse_delayed = np.where(np.abs(t - delay) <= 0.1, 1.0, 0.0)
pulse_delayed_fft = np.fft.fftshift(np.fft.fft(pulse_delayed))

plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(t, pulse_delayed)
plt.title(f"Pulso rectangular desplazado {delay}s")
plt.xlabel("Tiempo [s]")
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(freqs_shifted, np.abs(pulse_delayed_fft))
plt.title("Magnitud de la FFT del pulso desplazado")
plt.xlabel("Frecuencia [Hz]")
plt.grid()

plt.tight_layout()
plt.show()
