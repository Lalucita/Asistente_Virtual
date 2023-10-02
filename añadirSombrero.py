import cv2
import tkinter as tk
from threading import Thread
import time
from video_player import run_window

RECORDING = False
FRAME_TO_SAVE = None
STOP_VIDEO = False
FRAMES_BUFFER = []
FACE_CASCADE = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
HAT_IMG = cv2.imread("image/sombrero.png", -1)


def overlay_hat_on_face(frame, face_coords):
    x, y, w, h = face_coords
    hat_resized = cv2.resize(HAT_IMG, (int(w * 1.2), int(h * 1.1)))

    for i in range(hat_resized.shape[0]):
        for j in range(hat_resized.shape[1]):
            if (
                0 <= y + i - int(h // 1.8) < frame.shape[0]
                and 0 <= x + j - 20 < frame.shape[1]
            ):
                if (
                    hat_resized[i, j][3] != 0
                ):  # Asegurando que el pixel no sea transparente
                    frame[y + i - int(h // 1.8), x + j - 20] = hat_resized[i, j, 0:3]


def process_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = FACE_CASCADE.detectMultiScale(gray, 1.3, 5)
    for face_coords in faces:
        overlay_hat_on_face(frame, face_coords)


def start_video():
    global RECORDING, FRAME_TO_SAVE, STOP_VIDEO, FRAMES_BUFFER
    cap = cv2.VideoCapture(0)

    # Configurar VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # out = cv2.VideoWriter('person_recorder.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
    fps = cap.get(cv2.CAP_PROP_FPS)
    out = cv2.VideoWriter(
        "Outputs/person.avi", fourcc, 4, (int(cap.get(3)), int(cap.get(4)))
    )  # Usar el FPS obtenido
    while True:
        ret, frame = cap.read()
        if not ret or STOP_VIDEO:
            break

        process_frame(frame)
        cv2.imshow("Video con sombrero", frame)

        # Si estamos grabando, guardar el frame
        if RECORDING:
            FRAMES_BUFFER.append(frame.copy())
            if FRAME_TO_SAVE is None:
                FRAME_TO_SAVE = frame.copy()

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    for frame in FRAMES_BUFFER:
        out.write(frame)
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def record_video():
    global RECORDING, FRAME_TO_SAVE, STOP_VIDEO
    RECORDING = True
    time.sleep(5)  # Grabamos durante 2 segundos
    RECORDING = False
    if FRAME_TO_SAVE is not None:
        cv2.imwrite(
            "Outputs/person_picture.png", FRAME_TO_SAVE
        )  # Guardamos una imagen del frame, como ejemplo
    STOP_VIDEO = True
    root.destroy()
    time.sleep(3)
    run_window()

# Crear GUI con tkinter
root = tk.Tk()
root.title("Video Recorder with Hat")

btn_start = tk.Button(
    root, text="Iniciar Video", command=lambda: Thread(target=start_video).start()
)
btn_start.pack(pady=20)

btn_record = tk.Button(root, text="Grabar Video", command=record_video)
btn_record.pack(pady=20)

root.mainloop()
