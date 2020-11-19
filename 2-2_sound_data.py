import numpy as np               # 행렬 및 벡터 데이터 관리를 위한 numpy 모듈
import matplotlib.pyplot as plt     # 소리 데이터의 그래프 표현을 위한 모듈
from scipy.io.wavfile import write  # wav 형식으로 소리 데이터를 저장하기 위한 모듈
import os                           # wav 파일을 시스템 명령어로 재생하기 위한 모듈

## Step 1) 생성할 소리 데이터의 속성과 사인함수로 생성할 데이터를 저장하기 위한 환경 변수 설정하기
# sampling rate
Fs = 44100.0        # 정보 샘플링 주파수, 1초에 44100개의 샘플링, 단위는 Hz(주파수)

# 1초 데이터 생성을 위한 환경 변수 설정
tlen = 1                        # 1초로 초기화
Ts = 1 / Fs                     # 샘플링 사이의 간격(시간) 계산
t = np.arange(0, tlen, Ts)      # 소리 데이터를 생성할 시간 성분으로 구성된 배열로
                                # 0과 1사이를 Ts(Timestamp)의 간격으로 분할하여
                                # Fs개의 데이터를 담을 수 있는 배열 t를 생성

## Step 2) 사인함수를 이용하여 임의의 소리 데이터 만들기
# 일정한 주기의 파형 모양을 가지도록 연속 데이터를 만든다. 삼각함수의 원리에 따라 -1과 1 사이의 값으로
# 일정한 파형을 형성하는 연속적인 데이터를 만들기 위해 440Hz의 주기를 갖는 사인함수를 사용한다

# 시그널 생성하기
print('t=',t)
sin_freq = 440
src = 2 * np.pi * sin_freq * t
signal = np.sin(src)

# 데이터의 시각화: 생성한 시그널 데이터를 그래프로 표현
x_range = 200
plt.plot(t[0:x_range], signal[0:x_range], color='blue')
plt.show()

# 데이터의 시각화: 시그널 데이터를 푸리에 변환하여 주파수 영역에서 시각화 함.
freq = np.fft.fftfreq(len(t), Ts)   # 주파수 영역에서의 샘플링 구간값의 배열    
signal_f = np.fft.fft(signal)       # 사인함수 값으로부터 주파수 영역에서의 정보를 나타내기 위한 푸리에 변환값을 signal_f 배열로 저장

#plt.plot(freq[0:x_range], signal_f[0:x_range])
print(signal_f)
plt.plot(freq[0:x_range], 20 * np.log10(np.abs(signal_f[0:x_range])), color='blue')
plt.show()


scaled = np.int16(signal/np.max(np.abs(signal))*32767)
write('snd_signal.wav',44100,scaled)

