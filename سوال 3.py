
f= open ("output.txt",'w')
import cv2
import os

image_path = "c:\\Users\\NS\\Desktop\\p1\\img.jpg"

if os.path.exists(image_path):
    image = cv2.imread(image_path)
    
    if image is not None:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, 100, 200)

        cv2.imshow('Original Image', image)
        cv2.imshow('Edge Detection', edges)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Could not read the image.")
else:
    print("Image file does not exist.")

print( cv2.imshow('Original Image', image),file=f)
print( cv2.imshow('Edge Detection', edges),file=f)
f.write(cv2.imshow('Original Image', image))
f.write(cv2.imshow('Edge Detection', edges))
f.close()