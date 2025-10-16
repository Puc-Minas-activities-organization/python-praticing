import threading
import time

def walk_dog(dog_name):
    time.sleep(8)
    print(f"You finished walking {dog_name}")

def take_trash_out(trash_name, trash_second_name):
    time.sleep(2)
    print(f"You took out {trash_name} and {trash_second_name}")

def get_email():
    time.sleep(4)
    print("You got the email")

chore1 = threading.Thread(target=walk_dog, args=("Scooby",))
chore1.start()

chore2 = threading.Thread(target=take_trash_out, args=("trash1", "trash2"))
chore2.start()

chore3 = threading.Thread(target=get_email)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete")