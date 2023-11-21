import time
import sys
import random

#The more interactions, the more "real" the responses and reactions from the rock. 


# Slow typing effect function
def slow_type(text, delay=0.05, end="\n"):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)  # Control the end character (newline by default)
    sys.stdout.flush()

class PetRock:
    def __init__(self, name):
        self.name = name

    def feed(self, interactions):
        if interactions <= 1:
            slow_type(f"You try to feed {self.name}, ", end="")
            time.sleep(.5)  
            slow_type("but it's a rock. ", end="")
            time.sleep(1)  
            slow_type("It doesn't eat.")
        elif interactions <= 2:
            slow_type(f"You try to feed {self.name}. ", end="")
            time.sleep(.5)  
            slow_type(f"It seems {self.name} is not hungry right now. ")
        else:             
            slow_type(f"You try to feed {self.name}. ", end="")
            time.sleep(.5)  
            slow_type("It seems to be very slowly absorbing the food's nutrients.")
        time.sleep(1)  
        
    def play(self, interactions):
        choices = ["rock", "paper", "scissors"]
        user_choice = random.choice(choices)
        slow_type(f"You play rock-paper-scissors. ", end="")
        time.sleep(1)  
        slow_type(f"You choose {user_choice}. ", end="")
        time.sleep(1)  
        slow_type(f"{self.name} chooses rock ", end="")
        time.sleep(.5)  
        slow_type(f"(Obviously).")
        time.sleep(1)  

        #if interactions <=1 replace play_responses

        # Determine the winner
        if user_choice == "rock":
            slow_type("It's a tie. ", end="")
            time.sleep(1)
            slow_type("An expected outcome against a rock.")
        elif user_choice == "paper":
            slow_type("You won. ", end="")
            time.sleep(1)
            play_responses = [
                f"{self.name}'s mood remains unfazed.",
                f"{self.name} seems indifferent to defeat.",
            ]
            slow_type(random.choice(play_responses))
        else:
            slow_type(f"Somehow, {self.name} wins. ", end="")
            time.sleep(1)
            slow_type("This rock must be a genius.")
        time.sleep(1)  

    def talk(self, interactions):
        talk_responses = [
            "The rock stares back silently.",
            "It seems the rock has a lot to say about geology.",
            f"{self.name} is fast asleep(it seems like).",
            "The rock remains stoic and unresponsive."
        ]
        slow_type(random.choice(talk_responses))
        time.sleep(1)  

    def check_mood(self, interactions):
        moods = ["neutral", "unmoved", "stoic"]
        slow_type(f"{self.name}'s mood is {random.choice(moods)}. ", end="") 
        time.sleep(.5) 
        slow_type("As expected from a rock.")
        time.sleep(1)  

# Interaction function
def interact_with_pet_rock():
    global interactions
    slow_type("What do you want to name your pet rock? ")
    name = input()
    my_pet_rock = PetRock(name)

    while True:
        interactions += 1
        slow_type(f"What do you want to do with {name}? ", end="") 
        print("(feed/play/talk/check mood/exit):")
        choice = input().lower()
        if choice == "feed":
            my_pet_rock.feed(interactions)
        elif choice == "play":
            my_pet_rock.play(interactions)
        elif choice == "talk":
            my_pet_rock.talk(interactions)
        elif choice == "check mood":
            my_pet_rock.check_mood(interactions)
        elif choice == "exit":
            slow_type("Goodbye!")
            break
        else:
            slow_type("Invalid choice. Please choose again.")

# Start the interaction
interactions = 0
interact_with_pet_rock()
