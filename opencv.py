import cv2

def show_img_from_path(path, time, text="Demo"):
    """
    Reads an image from path and displays it. The image with automatically close after time millseconds
    """
    src = cv2.imread(cv2.samples.findFile(path))
    cv2.imshow(text, src)
    c = cv2.waitKey(time)
    cv2.destroyAllWindows()

    if c >= 0:
        return -1
    return 0

def show_img(src, time, text="Demo"):
    """
    Displays an image whose input is a numpy ndarray. The image with automatically close after time millseconds
    """
    cv2.imshow(text, src)
    c = cv2.waitKey(time)
    cv2.destroyAllWindows()

    if c >= 0:
        return -1
    return 0