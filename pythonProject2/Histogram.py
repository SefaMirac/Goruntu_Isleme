# 02210201513 Sefa Miraç DURGUN
import cv2
import numpy as np
from matplotlib import pyplot as plt
foto = cv2.imread("lena_color.bmp",0) # renksiz (gri) goruntu alma
cv2.imshow("lena_color",foto)
cv2.waitKey()
print(foto.shape) # yükseklik, genişlik ve kanal sayısı
Hist = zeros(256)
[w,h,i] = shape(foto)
for v in range(0, u<h):
for u in range (0, u<w):
i= foto(u,v)
Hist[i]=Hist[i]+1
plt.plot(Hist[i])
plt.show()
