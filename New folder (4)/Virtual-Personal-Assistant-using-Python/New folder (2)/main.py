import cv2
from ultralytics import YOLO
import pyttsx3
import speech_recognition as sr

# Initialize the YOLOv8 model
model = YOLO('yolov8n.pt')

# Initialize Text to Speech Engine
engine = pyttsx3.init()

# Initialize Speech Recognition
recognizer = sr.Recognizer()

def recognize_objects_in_video():
    # Open the video stream (you can also change it to open a file)
    cap = cv2.VideoCapture(0)

    # Read video properties
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Loop through the video frames
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        
        # Perform object detection
        results = model(frame)
        
        # Display the annotated frame
        annotated_frame = results.render()
        cv2.imshow('Object Detection', annotated_frame)
        
        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()

def get_user_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""

def process_command(command):
    if "detect objects" in command:
        recognize_objects_in_video()
    elif "stop" in command:
        engine.say("Goodbye!")
        engine.runAndWait()
        exit()
    else:
        engine.say("Command not recognized.")
        engine.runAndWait()

def main():
    while True:
        command = get_user_command()
        process_command(command)

if __name__ == "__main__":
    main()
