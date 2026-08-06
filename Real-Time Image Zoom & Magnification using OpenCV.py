import cv2 as cv
import numpy as np

WIDTH = 640
HEIGHT = 360

cam = cv.VideoCapture(0)

cam.set(cv.CAP_PROP_FRAME_WIDTH, WIDTH)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, HEIGHT)

# مكان الـ Zoom
zoom_size = 100
zoom_factor = 3

while True:
    success, img = cam.read()

    if not success:
        print("Error: Failed to grab frame.")
        break

    # تحديد مكان الزوم (منتصف الصورة)
    h, w, _ = img.shape
    x = w//2 - zoom_size//2
    y = h//2 - zoom_size//2

    # أخذ جزء من الصورة
    zoom_area = img[y:y+zoom_size, x:x+zoom_size]

    # تكبير الجزء
    zoom_img = cv.resize(
        zoom_area,
        None,
        fx=zoom_factor,
        fy=zoom_factor,
        interpolation=cv.INTER_LINEAR
    )

    # رسم مربع يوضح مكان الزوم على الفريم الأساسي
    cv.rectangle(
        img,
        (x, y),
        (x+zoom_size, y+zoom_size),
        (0, 255, 0),
        2
    )

    # جعل حجم الزوم نفس حجم الصورة الصغيرة
    zoom_img = cv.resize(zoom_img, (200, 200))

    # إضافة فريم الزوم فوق الكاميرا
    img[10:210, 10:210] = zoom_img

    cv.imshow("Camera + Zoom", img)

    key = cv.waitKey(1) & 0xFF

    if key == ord('q'):
        break

cam.release()
cv.destroyAllWindows()