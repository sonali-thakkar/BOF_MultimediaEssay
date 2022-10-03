# Sonali Thakkar
# Brooke Owens Fellowship
# Multimedia Essay
# Prompt: GPAs and college transcripts don’t paint a complete picture of a person.
# What else do we need to know about you?
# To experience this essay, please copy and paste this file into the main.py window of this website:

# Instructions:
# Go to this website:
# https://codesandbox.io/p/github/sonali-thakkar/BOF_MultimediaEssay/draft/eager-hypatia?file=%2Fmain.py&selection=%5B%7B%22endColumn%22%3A1%2C%22endLineNumber%22%3A8%2C%22startColumn%22%3A1%2C%22startLineNumber%22%3A8%7D%5D&workspace=%257B%2522activeFileId%2522%253A%2522cl8swgt0l0008lui98wst4dri%2522%252C%2522openFiles%2522%253A%255B%2522%252Fmain.py%2522%255D%252C%2522sidebarPanel%2522%253A%2522EXPLORER%2522%252C%2522gitSidebarPanel%2522%253A%2522COMMIT%2522%252C%2522sidekickItems%2522%253A%255B%255D%257D
# You should be able to see the code in the right or center pane and the

story1 = {
    "start": "For this adventure, you can get a sense of what it's like for me as a senior at UVM working a full time internship and the my daily activites."
             " \n Unlike a regular day in the life, however, you can choose amongst my activities throughout the week instead of just one particular day, \n "
             "How would you like to start? \n   1. Wake up and start working at my internship \n   2. Wake up and go to class",
    "step1": ""
}
story2 = {}

working_story = story1
step_count = 0


def begin_adventure():
    global working_story
    print('Let\'s begin!')
    print("There are two story options")
    print(" 1. A Day in the Life")
    print(" 2. My Background")

    story_num = int(input("Which story would you like to go through? (Enter 1 or 2): "))
    story_num = validate_num(1, 2, story_num)
    if story_num == 1:
        working_story = story1
    else:
        working_story = story2


def adventure_time():
    global working_story

    # begin the story by printing start
    print(working_story.get("start"))

    # get input for what the next step should be and validate it
    next_step = int(input("(Enter 1 or 2): "))
    next_step = validate_num(1,2,next_step)

    # call next_step function
    play_next_step(next_step)

def play_next_step(step_num):
    global working_story
    global step_count

    # get the corresponding step number for the place in the working_story dictionary
    step_count += step_num

    # print that step in the dictionary
    print(working_story.get("story"+str(step_count)))

    # get input for what the next step should be and validate it
    next_step = int(input("(Enter 1 or 2): "))
    next_step = validate_num(1, 2, next_step)

    # recursively call play_next_step to continue through
    play_next_step(next_step)


def validate_num(min, max, value):
    # check if provided value is either 1 or 2, and if not ask again until input is either 1 or 2
    while value < min or value > max:
        print(f"Sorry that choice is invalid, please enter a number- {min} or {max}")
        value = int(input("New input: "))
    return value


def print_intro():
    print("To the Brooke Owens Fellowship, ")
    print("My name is Sonali Thakkar (but you can call me Sunny)")
    print("For my Multimedia Essay I've created this python program for you to run through. Here's how it works-")
    print("Like a choose your own adventure book, this program walks you through a \"story\", ")
    print("after reading each section, you will be given a choice and you can see how the \"story\" continues from there!")

if __name__ == '__main__':
    print_intro()
    begin_adventure()
    adventure_time()
