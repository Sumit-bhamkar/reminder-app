import schedule
import time
from plyer import notification

# Function to send reminders
def send_reminder(task):
    notification.notify(
        title="Reminder",
        message=f"Task: {task}",
        timeout=10
    )

# Add reminders
def schedule_task(task, time_to_remind):
    schedule.every().day.at(time_to_remind).do(send_reminder, task)

# Main Function
def main():
    print("Welcome to the Reminder App!")
    while True:
        print("\n1. Add a Reminder\n2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            time_to_remind = input("Enter time (HH:MM in 24-hour format): ")
            try:
                schedule_task(task, time_to_remind)
                print(f"Reminder set for {task} at {time_to_remind}.")
            except ValueError:
                print("Invalid time format. Try again.")
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

        # Run scheduled tasks
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()
