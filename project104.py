import cv2
img = cv2.imread("C:\\Users\\Shinj_28\\OneDrive\\Desktop\\python\\solar-system.jpg")
headtext = "THE SOLAR SYSTEM:"
text =" SUN!"
text2 ="Mercury"
text3 = "Venus"
text4 = "Earth"
text5 = "Mars"
text6 = "Jupiter"
text7 = "Saturn"
text8 = "Uranus"
text9 = "Neptune"

cv2.putText(img, headtext,(50,40),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=2.5,color=(0,255,255))

cv2.putText(img, text,(70,100),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=2,color=(0,0,225))
cv2.putText(img, text2,(150,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.3,color=(225,225,225))
cv2.putText(img, text3,(220,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5,color=(225,225,225))
cv2.putText(img, text4,(320,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5,color=(225,225,225))
cv2.putText(img, text5,(410,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5,color=(225,225,225))
cv2.putText(img, text6,(650,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5,color=(225,225,225))
cv2.putText(img, text7,(850,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5,color=(225,225,225))
cv2.putText(img, text8,(1000,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5,color=(0,0,0))
cv2.putText(img, text9,(1180,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5,color=(225,225,225))


cv2.imshow("Here is the img" , img)
cv2.imwrite("new.jpg",img)
cv2.waitKey(0)
