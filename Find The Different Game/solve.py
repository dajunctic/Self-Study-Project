import random

import cv2


def solve(img_path1, img_path2):
    img1 = cv2.imread(img_path1)
    img2 = cv2.imread(img_path2)

    img1 = cv2.resize(img1, (0, 0), fx=0.5, fy=0.5)
    img2 = cv2.resize(img2, (0, 0), fx=0.5, fy=0.5)

    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    diff = 255 - cv2.absdiff(img1, img2)
    cv2.imshow("DIFF", diff)

    ret, diff = cv2.threshold(diff, 250, 255, cv2.THRESH_TOZERO)
    diff = cv2.medianBlur(diff, 9)
    cv2.imshow("Threshold", diff)

    edged = cv2.Canny(diff, 40, 200)

    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    contours_poly = [None] * len(contours)
    boundRect = [None] * len(contours)

    for i, c in enumerate(contours):
        contours_poly[i] = cv2.approxPolyDP(c, 3, True)
        boundRect[i] = cv2.boundingRect(contours_poly[i])

    res1 = cv2.imread(img_path1)
    res1 = cv2.resize(res1, (0, 0), fx=0.5, fy=0.5)
    res2 = cv2.imread(img_path2)
    res2 = cv2.resize(res2, (0, 0), fx=0.5, fy=0.5)

    offset = 10

    for i in range(len(contours)):
        color = (0, 0, 255)
        cv2.drawContours(res2, contours_poly, i, color)
        cv2.rectangle(res2, (int(boundRect[i][0]) - offset, int(boundRect[i][1]) - offset),
                      (int(boundRect[i][0] + boundRect[i][2]) + offset * 2, int(boundRect[i][1] + boundRect[i][3])
                       + offset * 2), color, 2)

    cv2.imshow("difference", res1)
    cv2.imshow("difference", res2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # solve("assets/001-0.png", "assets/001-1.png")
    solve("assets/bar_puzzle.png", "assets/output/level-3.png")
