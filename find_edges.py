import cv2
import numpy as np
def auto_canny(image, sigma=0.3):
    v = np.median(image)
    print(np.array(image).max())
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))

    return cv2.Canny(image, 254, 255)

def add_contrast(img, contrast_level=8):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(contrast_level, contrast_level))
    cl = clahe.apply(l)

    limg = cv2.merge((cl, a, b))

    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

    return final
def perspective_transform(image, source_points):
    dest_points = np.float32([[0, 0], [500, 0], [500, 300], [0, 300]])
    M = cv2.getPerspectiveTransform(source_points, dest_points)
    dst = cv2.warpPerspective(image, M, (500, 300))

    return dst
# ------------------------------------------ #
# FIND EDGES
# ------------------------------------------ #
# img_path = "/Users/macbookpro/Desktop/Projects/Machine_Learning_Projects/ID_Card_Info_Extractor/Sample Data/Natioanal ID/3.jpg"
# img = cv2.imread(img_path)
# #  img = add_contrast(img=img, contrast_level=8)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray", gray)

# kernel_size = 5
# blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

# edges = auto_canny(image=blur_gray) 
# # for lines in edges:
# #     for line in lines:
# #         if line > 0:
# #             print(line)
# cv2.imshow("canny",edges)
# count = 0
# points = np.argwhere(edges==255)
# points = np.fliplr(points)
# print(points)
# x, y, w, h = cv2.boundingRect(points) # create a rectangle around those points
# print(x, y, w, h)
# x, y, w, h = x-10, y-10, w+20, h+20 # make the box a little bigger
# crop = gray[y:y+h, x:x+w]
# # lines = cv2.HoughLines(edges, 1, np.pi/90, 50)

# # for line in lines:
# #     rho,theta = line[0]
# #     print("rho:",rho)
# #     a = np.cos(theta)
# #     b = np.sin(theta)
# #     x0 = a*rho
# #     y0 = b*rho
# #     x1 = int(x0 + 10000*(-b))
# #     y1 = int(y0 + 10000*(a))
# #     x2 = int(x0 - 10000*(-b))
# #     y2 = int(y0 - 10000*(a))
# #     # print("initial points: ",x0,y0)
# #     # print("start point: ",x1,y1)
# #     # print("end point: ",x2,y2)
# #     cv2.line(img,(x1,y1),(x2,y2),(0,255,0),1)

# # Show images for testing
# # get the thresholded crop
# # retval, thresh_crop = cv2.threshold(crop, thresh=200, maxval=255, type=cv2.THRESH_BINARY)

# # display
# print("size of crop img: ",crop.shape)
# print("size of img: ",img.shape)
# cv2.imshow("Cropped and thresholded image", crop) 
# # cv2.imshow('edges', crop)
# cv2.waitKey(0)
# cv2.destroyAllWindows()