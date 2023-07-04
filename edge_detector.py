import cv2 as cv

window_name = 'Edge Map'

def CannyThreshold(val, src):
    low_threshold = val
    kernel_size = 3
    ratio = 3

    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    img_blur = cv.blur(src_gray, (3,3))
    detected_edges = cv.Canny(img_blur, low_threshold, low_threshold*ratio, kernel_size)
    mask = detected_edges != 0
    dst = src * (mask[:,:,None].astype(src.dtype))
    cv.imshow(window_name, dst)

def edge_detect(path):
    title_trackbar = 'Min Threshold:'
    max_lowThreshold = 100
    
    print(f"Detecting edges in input: {path}.")
    src = cv.imread(cv.samples.findFile(path))

    if src is None:
        print('Could not open or find the image: ', path)
        exit(0)
    
    cv.namedWindow(window_name)
    cv.createTrackbar(title_trackbar, window_name , 0, max_lowThreshold, CannyThreshold)
    CannyThreshold(0, src)
    cv.waitKey(10000)
    cv.destroyAllWindows()

    # example path on Windows: C:/users/kunal/coding/000000_JPG_jpg.rf.b136c76488ef2ebcad9d0bdb32a3c48d.jpg