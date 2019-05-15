import sys, time, cv2
from kafka import KafkaProducer

topic = "testing"

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        video_path = sys.argv[1]
        publish_video(video_path)
    else:
        print("Publishing feed!")
        publish_camera()
