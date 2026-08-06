import cv2 as cv

# Camera resolution
WIDTH = 640
HEIGHT = 360

# Zoom settings
ZOOM_SIZE = 100
ZOOM_FACTOR = 3

# Mouse position
mouse_x = WIDTH // 2
mouse_y = HEIGHT // 2


# Open camera
cam = cv.VideoCapture(0)
cam.set(cv.CAP_PROP_FRAME_WIDTH, WIDTH)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, HEIGHT)


# Mouse callback function
def mouse_event(event, x, y, flags, params):
    global mouse_x, mouse_y

    if event == cv.EVENT_MOUSEMOVE:
        mouse_x = x
        mouse_y = y


# Create window
cv.namedWindow("Real-Time Image Zoom & Magnification")
cv.setMouseCallback(
    "Real-Time Image Zoom & Magnification",
    mouse_event
)


while True:

    success, frame = cam.read()

    if not success:
        print("Error: Cannot read camera")
        break


    h, w, _ = frame.shape


    # Define zoom area
    x1 = max(mouse_x - ZOOM_SIZE // 2, 0)
    y1 = max(mouse_y - ZOOM_SIZE // 2, 0)

    x2 = min(mouse_x + ZOOM_SIZE // 2, w)
    y2 = min(mouse_y + ZOOM_SIZE // 2, h)


    # Crop selected region
    roi = frame[y1:y2, x1:x2]


    if roi.size != 0:

        # Magnify image
        zoom_img = cv.resize(
            roi,
            None,
            fx=ZOOM_FACTOR,
            fy=ZOOM_FACTOR,
            interpolation=cv.INTER_CUBIC
        )


        # Resize zoom window
        zoom_img = cv.resize(
            zoom_img,
            (200, 200)
        )


        # Add zoom view on camera frame
        frame[10:210, 10:210] = zoom_img


    # Draw zoom selection box
    cv.rectangle(
        frame,
        (x1, y1),
        (x2, y2),
        (0, 255, 0),
        2
    )


    # Display
    cv.imshow(
        "Real-Time Image Zoom & Magnification",
        frame
    )


    # Exit with Q
    key = cv.waitKey(1) & 0xFF

    if key == ord('q'):
        break



cam.release()
cv.destroyAllWindows()
