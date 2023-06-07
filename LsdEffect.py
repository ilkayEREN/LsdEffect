import cv2
import numpy as np
import random

# Görüntü boyutları
width, height = 800, 800

# Siyah bir arka plan oluşturma
image = np.zeros((height, width, 3), dtype=np.uint8)

# Halka merkezi ve yarıçapı
circle_center_x = width // 2
circle_center_y = height // 2
radius = 300

# Halka sayısı
num_circles = 100

# Halka efekti hızı
speed = 15

# Halka kalınlığı
thickness = 4

# Halkalar arasındaki boşluk
gap = 4 

# Renklerin listesi
colors = []

# Başlangıç yönü
direction = 1  # 1: Sağa doğru, -1: Sola doğru

# Halkalara renk atama
for i in range(num_circles):
    colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

# Sonsuz döngüde halkaları çizme
while True:
    # Halkaları çizme
    image = np.zeros((height, width, 3), dtype=np.uint8)  # Siyah bir arka plan
    for i in range(num_circles):
        current_radius = i * (thickness + gap) 
        cv2.circle(image, (circle_center_x, circle_center_y), current_radius, colors[i], thickness=thickness)

    # Ekrana gösterme
    cv2.imshow("LSD effect by ilkay eren", image)
    cv2.waitKey(1)

    # Yön değiştirme
    if circle_center_x >= width - radius:
        direction = -1  # Sola doğru yönlendir
    elif circle_center_x <= radius:
        direction = 1  # Sağa doğru yönlendir

    # Merkezi güncelleme
    circle_center_x += direction * speed

    # Renk aktarımı
    colors.insert(0, colors.pop())

    # Eğer 'q' tuşuna basılırsa döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Pencereyi kapatma
cv2.destroyAllWindows()
