import cv2

# Paths
video_path = "sample video.mp4"          # Input video
output_path = "sample_video_with_captions.mp4"  # Output video

# Open the video
cap = cv2.VideoCapture(video_path)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Example dummy caption: show second count at bottom
    second = frame_count // fps
    text = f"Caption at second {second+1}"
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, (50, height-50), font, 1, (255, 255, 255), 2)

    out.write(frame)
    frame_count += 1

cap.release()
out.release()
print(f"Video with captions saved as '{output_path}'")
