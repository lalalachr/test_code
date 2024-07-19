import cv2


def main():
    a = 2
    b = 5
    print(a - b)
    la = cv2.imread("D:/ZE/induction plan/code/python/LicensePlate_Recognition/image/test1.png")
    # b,g,r = cv2.split(la)
    cv2.imshow("image", la)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
