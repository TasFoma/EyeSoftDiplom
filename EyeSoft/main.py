
import cv2  
import pyautogui  
from gaze_tracking import GazeTracking  

gaze = GazeTracking()  
webcam = cv2.VideoCapture(0)  

while True:  
    _, frame = webcam.read()  

    gaze.refresh(frame)  
    frame = gaze.annotated_frame()  
    text = "Looking center"  # Изначально устанавливаем "Looking center" как значение по умолчанию

    left_pupil = gaze.pupil_left_coords()  
    right_pupil = gaze.pupil_right_coords()  
    if left_pupil is not None and right_pupil is not None:
        left_x, left_y = left_pupil
        right_x, right_y = right_pupil  
        center_x = (left_x + right_x) / 2  
        center_y = (left_y + right_y) / 2 

        if center_x < (frame.shape[1] // 3):  
            text = "Looking left"
            pyautogui.move(-10, 0)  # Переместить курсор влево  
        elif center_x > (2 * frame.shape[1] // 3):  
            text = "Looking right"
            pyautogui.move(10, 0)  # Переместить курсор вправо

        if center_y < (frame.shape[0] // 3): 
            text = "Looking up" 
            pyautogui.move(0, -10)  # Переместить курсор вверх  
        elif center_y > (2 * frame.shape[0] // 3): 
            text = "Looking down" 
            pyautogui.move(0, 10)  # Переместить курсор вниз  

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2) 
    cv2.imshow("Demo", frame)  

    if cv2.waitKey(1) == 27:  
        break  

webcam.release()  
cv2.destroyAllWindows()
