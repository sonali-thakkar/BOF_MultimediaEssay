# Sonali Thakkar
# Brooke Owens Fellowship
# Multimedia Essay
# Prompt: GPAs and college transcripts don’t paint a complete picture of a person.
# What else do we need to know about you?
# To experience this essay, please copy and paste this file into the main.py window of this website:




def beginAdventure():
    print('Let\'s begin!')
    print("There are two story options")
    print(" 1. A Day in the Life")
    print(" 2. My Background")

    story_num = int(input("Which story would you like to go through? (Enter 1 or 2): "))
    validate_num(1,2, story_num)

def validate_num(min, max, value):
    while (value < min or value > max):
        print(f"Sorry that choice is invalid, please enter a number- {min} or {max}")
        value = int(input("New input: "))



def print_intro():
    print("To the Brooke Owens Fellowship, ")
    print("My name is Sonali Thakkar (but you can call me Sunny)")
    print("For my Multimedia Essay I've created this python program for you to run through. Here's how it works-")
    print("Like a choose your own adventure book, this program walks you through a story, ")
    print("After reading each section, you can input your choice and see how to story continues from there!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_intro()
    beginAdventure()

