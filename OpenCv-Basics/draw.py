import cv2
import numpy as np

# Create a blank white image
img = np.ones((600, 800, 3), dtype=np.uint8) * 255

# Draw a blue rectangle (top-left corner, bottom-right corner)
cv2.rectangle(img, (50, 50), (250, 200), (255, 0, 0), thickness=3)

# Draw a green circle (center, radius)
cv2.circle(img, (400, 150), 75, (0, 255, 0), thickness=5)

# Draw a red line (start point, end point)
cv2.line(img, (50, 300), (750, 300), (0, 0, 255), thickness=2)

# Draw a polygon (e.g., triangle)
pts = np.array([[300, 400], [400, 350], [500, 400]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], isClosed=True, color=(255, 0, 255), thickness=3)

# Draw a filled yellow ellipse
cv2.ellipse(img, (650, 450), (100, 50), 0, 0, 360, (0, 255, 255), thickness=2)

# Draw text
cv2.putText(img, "OpenCV Drawing", (250, 550), cv2.QT_FONT_BLACK, 1, (0, 0, 0), thickness=2)

# Show the image
cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
