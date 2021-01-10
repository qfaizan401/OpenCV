#read image from a file

import cv2
import numpy as np
img = cv2.imread(filename='lena.jpg', flags=0)
# 1 for coloured img
# 0 for grayscale img
# -1 for unchange img
print(img) # print the matrics of img
cv2.imshow(winname='lena', mat=img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f'\nThe shape of image Lena is {np.shape(img)}')

#write an img to a file

cv2.imwrite(filename='copy_of_lena.png',img=img)
