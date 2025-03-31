import cv2
import numpy as np

# Load image
im = cv2.imread('/Users/tinaabdalla/Desktop/IMG_2180.JPG')
img = cv2.resize(im, (0, 0), fx=1.0, fy=1.0)  
original_img = img.copy()


# Define filter functions
def apply_filter(filter_type):
    global img
    img = original_img.copy()
    
    if filter_type == 'normal':
        pass  
    elif filter_type == 'blur':
        img = cv2.GaussianBlur(img, (35, 35), 0)
    elif filter_type == 'sharpen':
        kernel = np.array([[0, -1, 0], [-1, 6, -1], [0, -1, 0]])
        img = cv2.filter2D(img, -1, kernel)
    elif filter_type == 'edge':
        img = cv2.Canny(img, 50, 150)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    elif filter_type == 'inverse':
        img = cv2.bitwise_not(img)
    elif filter_type == 'rotateL':
        img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    elif filter_type == 'rotateR':
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    elif filter_type == 'turn_blue':
        img[:, :, 1] = 0  
        img[:, :, 2] = 0  
    elif filter_type == 'turn_green':
        img[:, :, 0] = 0  
        img[:, :, 2] = 0  
    elif filter_type == 'turn_red':
        img[:, :, 0] = 0
        img[:, :, 1] = 0 
    
    draw_menus()

def draw_menus():
    img_with_menu = img.copy()
    cv2.rectangle(img_with_menu, (0, 0), (img.shape[1], 50), (0, 0, 0), -1)
    cv2.rectangle(img_with_menu, (0, img.shape[0] - 50), (img.shape[1], img.shape[0]), (0, 0, 0), -1)

    menu_items = ["Normal (0)", "Blur (1)", "Sharpen (2)", "Edge (3)", "Inverse (4)", "Rotate L (5)", "Rotate R (6)", "Turn Blue (7)", "Turn Green (8)", "Turn Red (9)"]
    spacing = img.shape[1] // len(menu_items)

    for i, item in enumerate(menu_items):
        x_pos = 10 + i * spacing
        cv2.putText(img_with_menu, item, (x_pos, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 1)
        cv2.putText(img_with_menu, item, (x_pos, img.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 1)

    cv2.imshow("image", img_with_menu)

# Handle key events
def key_event(key):
    if key == ord('0'):
        apply_filter('normal')
    elif key == ord('1'):
        apply_filter('blur')
    elif key == ord('2'):
        apply_filter('sharpen')
    elif key == ord('3'):
        apply_filter('edge')
    elif key == ord('4'):
        apply_filter('inverse')
    elif key == ord('5'):
        apply_filter('rotateL')
    elif key == ord('6'):
        apply_filter('rotateR')
    elif key == ord('7'):
        apply_filter('turn_blue')
    elif key == ord('8'):
        apply_filter('turn_green')
    elif key == ord('9'):
        apply_filter('turn_red')

# Handle mouse clicks on menu
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        menu_items = ["Normal (0)", "Blur (1)", "Sharpen (2)", "Edge (3)", "Inverse (4)", "Rotate L (5)", "Rotate R (6)", "Turn Blue (7)", "Turn Green (8)", "Turn Red (9)"]
        spacing = img.shape[1] // len(menu_items)

        for i in range(len(menu_items)):
            x_start = i * spacing
            x_end = (i + 1) * spacing
            if (0 < y < 50 or img.shape[0] - 50 < y < img.shape[0]) and x_start < x < x_end:
                key_event(ord(str(i)))
                break

draw_menus()
cv2.setMouseCallback("image", click_event)

while True:
    key = cv2.waitKey(0) & 0xFF
    if key == 27:
        break
    key_event(key)

cv2.destroyAllWindows()
