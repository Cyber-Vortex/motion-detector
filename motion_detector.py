import cv2

def main():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        raise SystemExit("Could not open webcam. Check permissions or try VideoCapture(1).")

    background = None
    print("Motion detector started. Press 'q' in the video window to quit.")

    while True:
        ok, frame = camera.read()
        if not ok:
            print("Could not read frame from webcam.")
            break

        frame = cv2.resize(frame, (800, 450))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if background is None:
            background = gray.astype("float")
            cv2.imshow("Python Motion Detector", frame)
            if cv2.waitKey(30) & 0xFF == ord("q"):
                break
            continue

        cv2.accumulateWeighted(gray, background, 0.03)
        delta = cv2.absdiff(gray, cv2.convertScaleAbs(background))
        thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motion_found = False
        for contour in contours:
            if cv2.contourArea(contour) < 1200:
                continue
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 220, 255), 2)
            motion_found = True

        status = "MOTION DETECTED" if motion_found else "No motion"
        cv2.putText(frame, status, (18, 35), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 220, 255), 2, cv2.LINE_AA)
        cv2.imshow("Python Motion Detector", frame)

        if cv2.waitKey(30) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
