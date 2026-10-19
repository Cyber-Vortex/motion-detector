# Webcam Motion Detector

Uses OpenCV to detect movement in a webcam view and draw a bounding box around the changed area.

## Setup
```bash
pip install -r requirements.txt
python motion_detector.py
```

Press `q` in the video window to quit. Allow camera access if prompted.

## Notes
- This detects changes/motion, not identities.
- Performance depends on lighting and camera quality.
- If your webcam is not camera 0, change `VideoCapture(0)` to another index.
