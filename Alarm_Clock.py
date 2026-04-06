import time
import datetime
import winsound

def set_alarm(alarm_time):
    print(f"Alarm is set for {alarm_time}")
    sound_file = "c:\\Users\\varad\\Downloads\\alarm.wav" # Replace with your alarm sound file path

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Current Time:", current_time, end = "\r")

        if current_time == alarm_time:
            print("\n⏰! Wake up!")
            winsound.PlaySound(sound_file, winsound.SND_FILENAME)
            break

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)