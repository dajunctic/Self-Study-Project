import random
import cv2
import numpy

img = cv2.imread("assets/bar_puzzle.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 40, 200)

contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

gray = numpy.zeros((img.shape[0], img.shape[1], 3), dtype="uint8")
for x in contours:
    cv2.fillPoly(gray, pts=[x], color=[255, 255, 255])

cv2.imshow("Before Blur", gray)
cv2.waitKey(0)

preprocessing = cv2.medianBlur(gray, 9)

cv2.imshow("After Blur", preprocessing)
cv2.waitKey(0)

edged = cv2.Canny(preprocessing, 40, 200)
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.imshow("Edge after preprocessing", edged)
cv2.waitKey(0)

LEVEL = 5

limit = [10000, 2000, 1000, 500, 200, 100]
num_diff = [5, 5, 5, 5, 10]

for level in range(1, LEVEL + 1):

    paint = numpy.zeros((img.shape[0], img.shape[1], 3), dtype="uint8")
    result = img.copy()
    choice = []

    for x in contours:
        area = cv2.contourArea(x)

        if limit[level] <= area <= limit[level - 1]:
            choice.append(x)

    choice = random.sample(choice, min(num_diff[level - 1], len(choice)))

    for x in choice:
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        cv2.fillPoly(paint, pts=[x], color=[r, g, b])
        cv2.fillPoly(result, pts=[x], color=[r, g, b])

    cv2.imshow('Paint', paint)
    cv2.imshow('Result', result)
    cv2.imwrite(f"assets/output/level-{level}.png", result)
    cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
