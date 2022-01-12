import numpy as np
import cv2 as cv

video = cv.VideoCapture(0)

while True:

    ret, img = video.read()

    #cv.imshow("Imagen", img)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    #cv.imshow("Gris", gray)

    gauss = cv.GaussianBlur(gray, (5,5), 0)

    #cv.imshow("Blur", gauss)

    circles = cv.HoughCircles(gauss, cv.HOUGH_GRADIENT, 1, 100, param1=50, param2=40, minRadius=40, maxRadius=100)

    total = 0
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for x, y, r in circles[0, :]:
            cv.circle(img, (x, y), r, (0, 255, 0), 2)
            cv.circle(img, (x, y), 2, (0, 0, 255), 3)
            if r > 50:
                total += 10
                lbl = "$10"
            else:
                total += 1
                lbl = "$1"

            cv.putText(img, lbl, (x-r//2, y-r), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv.LINE_AA)

        cv.putText(img, "El total es ${}".format(total), (20, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv.LINE_AA)
    cv.imshow("Video", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()