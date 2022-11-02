import cv2
import numpy as np
from matplotlib import pyplot as plt
foto = cv2.imread('lena_color.bmp',0)
[h,w] = foto.shape # resmin en boy pixel bilgilerini shape ile alıyoruz
foto_2 = np.zeros([h,w], dtype=np.uint8)
for i in range(h):
    for j in range(w): foto_2[i,j] = 255 - foto[i,j]
print(foto_2[i,j])
cv2.imshow("Goruntunun Ters Hali: ",foto_2)
cv2.waitKey()