import random
import keyboard

print("="*24)
print(" Lotto Number Generator")
print("   Press R to Reset")
print("   Press Q to Quit") 
print("="*24)

def Generator():
    num_list = random.sample(range(1,46),6)

    for i in num_list:
        print(i,end=" ")
    print()

Generator()

while True:
    event = keyboard.read_event()

    if event.name == 'r' and event.event_type == 'down':
        Generator()
    
    elif event.name == 'q' and event.event_type == 'down':
        break




