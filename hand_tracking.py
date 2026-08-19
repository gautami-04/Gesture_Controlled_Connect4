import cv2
import mediapipe as mp
import math

# MediaPipe setup
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)


def get_hand_data():

    success, frame = cap.read()

    if not success:
        return None

    # Flip frame
    frame = cv2.flip(frame, 1)

    h, w, c = frame.shape

    # Convert to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process hands
    results = hands.process(rgb_frame)

    finger_x = None
    pinch = False

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            # Index finger tip
            index_finger = hand_landmarks.landmark[8]

            # Thumb tip
            thumb = hand_landmarks.landmark[4]

            # Convert to pixels
            ix = int(index_finger.x * w)
            iy = int(index_finger.y * h)

            tx = int(thumb.x * w)
            ty = int(thumb.y * h)

            finger_x = ix

            # Distance between fingers
            distance = math.hypot(ix - tx, iy - ty)

            # Pinch detection
            pinch = distance < 20

            # Draw landmarks
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    cv2.imshow("Hand Tracking", frame)

    cv2.waitKey(1)

    if finger_x is not None:
        return finger_x, w, pinch

    return None