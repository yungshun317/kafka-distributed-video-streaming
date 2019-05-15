import sys, time, cv2
from kafka import KafkaProducer

topic = "testing"

def publish_video(video_file):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')

    video = cv2.VideoCapture(video_file)

    print("Publishing video...")

    while (video.isOpened()):
        success, frame = video.read()

        if not success:
            print("Bad read!")
            break

        ret, buffer = cv2.imencode(".jpg", frame)

        producer.send(topic, buffer.tobytes())
 
        time.sleep(0.2)

    video.release()
    print("Publish complete!")

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        video_path = sys.argv[1]
        publish_video(video_path)
    else:
        print("Publishing feed!")
        # publish_camera()
