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
    attempts = 0
    story_chosen = False
    while ((story_chosen == False) ):
        if (story_num != 1 or story_num != 2 and attempts < 6):
            ++attempts
            story_num = int(input("Sorry try again. Which story would you like to go through? (Enter 1 or 2): "))
        elif (story_num == 1):
            story_chosen = True
            attempts = 6
        elif (story_num == 2):
            story_chosen = True
            attempts = 6
        elif (attempts >= 6):
            story_chosen = True



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

