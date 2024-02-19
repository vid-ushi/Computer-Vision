import cv2
import numpy as np
from matplotlib import pyplot as plt

def get_pixel(img, center, x, y):
    new_value = 0
    try:
        if img[x][y] >= center:
            new_value = 1
    except:
        pass
    return new_value

def lbp_calculated_pixel(img, x, y):
    center = img[x][y]

    val_ar = []
    val_ar.append(get_pixel(img, center, x-1, y-1))    # top_left
    val_ar.append(get_pixel(img, center, x-1, y))      # top
    val_ar.append(get_pixel(img, center, x-1, y + 1))  # top_right
    val_ar.append(get_pixel(img, center, x, y + 1))    # right
    val_ar.append(get_pixel(img, center, x + 1, y + 1))# bottom_right
    val_ar.append(get_pixel(img, center, x + 1, y))    # bottom
    val_ar.append(get_pixel(img, center, x + 1, y-1))  # bottom_left
    val_ar.append(get_pixel(img, center, x, y-1))      # left

    power_val = [1, 2, 4, 8, 16, 32, 64, 128]
    val = 0

    for i in range(len(val_ar)):
        val += val_ar[i] * power_val[i]

    return val

def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += binary[i] * (2 ** (len(binary) - i - 1))
    return decimal

def lbp_img(img_gray):
    height, width = img_gray.shape
    img_lbp = np.zeros((height, width), np.uint8)

    for i in range(1, height-1):
        for j in range(1, width-1):
            img_lbp[i, j] = lbp_calculated_pixel(img_gray, i, j)

    return img_lbp

# Load input images
img_a = cv2.imread('img1.jpg', 0)  # Read image as grayscale
img_b = cv2.imread('img2.jpg', 0)

# Apply LBP to images
lbp_img_a = lbp_img(img_a)
lbp_img_b = lbp_img(img_b)

"""cv2.imshow("LBP-A",lbp_img_a )
cv2.waitKey(0)

cv2.imshow("LBP-B",lbp_img_b )
cv2.waitKey(0)"""

# Display the LBP images
plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.imshow(lbp_img_a, cmap='gray')
plt.title('LBP Image (a)')

plt.subplot(122)
plt.imshow(lbp_img_b, cmap='gray')
plt.title('LBP Image (b)')

plt.tight_layout()
plt.show()