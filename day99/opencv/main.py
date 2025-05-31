import cv2 as cv
# print(cv2.getBuildInformation())

# path = 'image/img1.jpg'
# img = cv.imread(path)

# print(img.shape)
# img = cv.resize(img,(800,600))
# # print(img)
# # print(img.ndim)
# print(img.shape)
# # type(img)
# # type(img.ndim)

# cv.imshow("photo",img)
# cv.waitKey(delay=10000)
# cv.imwrite("img1_resize.jpg",img)

# import cv2 as cv
# import sys
img = cv.imread(cv.samples.findFile("image/img1.jpg"))

 
if img is None:
    sys.exit("Could not read the image.")
else:
    print("found")
    

# cv.imshow("Display window", img)
# k = cv.waitKey(0)
 
# if k == ord("s"):
#     cv.imwrite("starry_night.png", img)

