#!/usr/bin/env python3

# OS import to allow console to be cleared
import os

#lists that contain the information for each project type and ratings
animeProjects = ["What anime should you watch next?", "Which Anime character are you based on your favorite foods?", "Anime trivia", "Anime character matchmaker"]
fantasyProjects = ["What DnD character type are you?", "12 reasons why everyone is secretly a Bard", "How many dragons will you own based on shoe size and height", "Which Game of Thrones Character are you?", "Tell you what season of Game of Thrones you would die in!"]
foodProjects = ["What type of pizza are you?", "Which potato would win in a battle royal?", "Recipe Maker", "Why pizza is actually a vegetable"]
historyProjects = ["Which founding father was the most zaney?", "Could you beat George Washington at Halo?", "Facts about specific time periods", "Which old buildings are the pointiest"]
vidgamesProjects = ["What videogame character are you?", "What game should you play next?", "How bad are you at First Person shooters?", "Is (insert game here) actually just Call of Duty?", "Can we guess what game you are thinking of?"]
generalProjects = ["Rock, paper scissors", "Guess the number", "20 questions", "What color am I thinking of"]
ratings = ["1 = Not even if I was getting paid", "2 = I mean if I really HAD to", "3 = Enjoy it from time to time", "4 = Enjoy it quite a bit", "5 = OMG I LOVE IT SO MUCH I COULD DIE!!!!!"]

# clears console when called
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# prints ratings for user to see when rating their interests in a topic
def interestValues():
    for rating in ratings:
        print(rating)
    print()

# prints project suggestions in the anime list
def animeInterest():
    for project in animeProjects:
        print(project)
    print()

# prints project suggestions in the food list    
def foodInterest():
    for project in foodProjects:
        print(project)
    print()

# prints project suggestions in the fantasy list
def fantasyInterest():
    for project in fantasyProjects:
        print(project)
    print()

# prints project suggestions in the history list
def historyInterest():
    for project in historyProjects:
        print(project)
    print()

# prints project suggestions in the videogames list
def vidgamesInterest():
    for project in vidgamesProjects:
        print(project)
    print()

# prints project suggestions in the general list
def generalProjectIdeas():
    for project in generalProjects:
        print(project)
    print("We hope this list helps you out! If not...well we tried. Guess you should try google...")

#prints all lists contents and the users rating of each interests when total interest level is above 23
def highInterestResult(animeInterestLevel, fantasyInterestLevel, foodInterestLevel, historyInterestLevel, vidgamesInterestLevel):
        print("Wow, you are interested in a lot of stuff! Guess we'll show you all the options and let you decide. Your level of interest is displayed as well to try and help narrow it down a bit\n")
       
        print(f"Anime interest rating: {str(animeInterestLevel)}")
        animeInterest()
        print()

        print(f"Fantasy interest rating: {str(fantasyInterestLevel)}")
        fantasyInterest()
        print()

        print(f"Food interest rating: {str(foodInterestLevel)}")
        foodInterest()
        print()

        print(f"History interest rating: {str(historyInterestLevel)}")
        historyInterest()
        print()

        print(f"Videogames interest rating: {str(vidgamesInterestLevel)}")
        vidgamesInterest()
        print()

        print("We hope this list helps you out! If not...well we tried. Guess you should try google...")

# function to handle user input outside of 1-5 rating system, either above 5 or lower than 1
def ratingOutOfBounds():
    while True:
        newRating = int(input("Rating can only be between 1 and 5\n>"))
        if newRating > 0 and newRating <= 5:
            return newRating

# function to handle user input when anything other than "yes" or "no" is entered when deciding to print project list
def checkYesNo():
    while True:
        choice = input("To show the list of projects type 'yes', otherwise type 'no'\n>")
        if choice.lower() == "yes" or choice.lower() == "no":
            return choice
        else:
            print("Come on dude, YES or NO. Now let's try this again.")

# asks the user the questions in regards to how interested they are in anime, fantasy, food, history, or videogames
# prompts user input based on how they rated their interests in each topic
def interestQuestions():
    noInterests = 10
    allInterests = 23
    minSingleInterest = 3
    
    interestValues()
    fantasyInterestLevel = int(input("Question 1: Rate your interest in the fantasy genre\n>"))
    if (fantasyInterestLevel < 1 or fantasyInterestLevel > 5):
        fantasyInterestLevel = ratingOutOfBounds()
    cls()

    interestValues()
    animeInterestLevel = int(input("Question 2: Rate your interest in anime\n>"))
    if (animeInterestLevel < 1 or animeInterestLevel > 5):
        animeInterestLevel = ratingOutOfBounds()
    cls()

    interestValues()
    vidgamesInterestLevel = int(input("Question 3: Rate your interest in videogames\n>"))
    if (vidgamesInterestLevel < 1 or vidgamesInterestLevel > 5):
        vidgamesInterestLevel = ratingOutOfBounds()
    cls()

    interestValues()
    historyInterestLevel = int(input("Question 4: Rate your interest in history\n>"))
    if (historyInterestLevel < 1 or historyInterestLevel > 5):
        historyInterestLevel = ratingOutOfBounds()
    cls()

    interestValues()
    foodInterestLevel = int(input("Question 5: Rate your interest in food\n>"))
    if (foodInterestLevel < 1 or foodInterestLevel > 5):
        foodInterestLevel = ratingOutOfBounds()
    cls()

    totalInterestLevel = (fantasyInterestLevel + animeInterestLevel + vidgamesInterestLevel + historyInterestLevel
            + foodInterestLevel)
    
    # runs when total interest is above 23 
    if totalInterestLevel >= allInterests:
        highInterestResult(animeInterestLevel, fantasyInterestLevel, foodInterestLevel, historyInterestLevel, vidgamesInterestLevel)
    
    #runs when total interest is at or below 10
    if totalInterestLevel <= noInterests:
        print("Guess you aren't that interested in the topics provided. Here are some general suggestions so you aren't leaving empty handed.")
        generalProjectIdeas()
    
    # runs when anime interest is 3 or above and the total interest is less than 23
    # gives user the choice to print topic project suggestions
    if animeInterestLevel >= minSingleInterest and totalInterestLevel < allInterests:
        print("Based on your answers it seems like you may enjoy projects relating to anime. Would you like to see some suggested projects?")
        choice = checkYesNo()
        print()
        if choice.lower() == "yes":
            animeInterest()
            print()
        elif choice.lower() == "no":
            print("Nani?!?!?!?!\n")
    
    # runs when fantasy interest is 3 or above and the total interest is less than 23
    # gives user the choice to print topic project suggestions
    if fantasyInterestLevel >= minSingleInterest and totalInterestLevel < allInterests:
        print("Based on your answers it seems like you may enjoy projects relating to the fantasy genre. Would you like to see some suggested projects?")
        choice = checkYesNo()
        print()
        if choice.lower() == "yes":
            fantasyInterest()
            print()
        elif choice.lower() == "no":
                print("Not into the fantasy genre, you shall pass\n")
    
    # runs when food interest is 3 or above and the total interest is less than 23
    # gives user the choice to print topic project suggestions
    if foodInterestLevel >= minSingleInterest and totalInterestLevel < allInterests:
        print("Based on your answers it seems like you may enjoy projects relating to food. Would you like to see some suggested projects?")
        choice = checkYesNo()
        print()
        if choice.lower() == "yes":
            foodInterest()
            print()
        elif choice.lower() == "no":
            print("Not a foodie, we get it\n")

    # runs when history interest is 3 or above and the total interest is less than 23
    # gives user the choice to print topic project suggestions
    if historyInterestLevel >= minSingleInterest and totalInterestLevel < allInterests:
        print("Based on your answers it seems like you may enjoy projects relating to history. Would you like to see some suggested projects?")
        choice = checkYesNo()
        print()
        if choice.lower() == "yes":
            historyInterest()
            print()
        elif choice.lower() == "no":
            print("Not a history buff, telegraph received\n")
    
    # runs when videogame  interest is 3 or above and the total interest is less than 23
    # gives user the choice to print topic project suggestions
    if vidgamesInterestLevel >= minSingleInterest and totalInterestLevel < allInterests:
        print("Based on your answers it seems like you may enjoy projects relating to videogames. Would you like to see some suggested projects?")
        choice = checkYesNo()
        print()
        if choice.lower() == "yes":
            vidgamesInterest()
            print()
        elif choice.lower() == "no":
            print("No vidya games, message recieved\n")
      
# prompts for users name of choice
name = input("Enter what you would like to be called for this session.\n>")
cls()

# greets user
print(f"Welcome to the Project Decider app, {name}!\n")

# loop to allow the user to begin the app or exit before answering questions
while True:    

    # prompts user to answer whether they are a python student looking for a project idea
    student = input("Are you a python student being forced by an omnipotent instructor to create code that tests your python skills but you have no idea what to do? (this is where you type 'yes' or 'no')\n>")
    print()
    
    # if student answers yes to above prompt the app starts
    if student.lower() == "yes":
        print(f"Well you are in luck, {name}! In just 5 questions we will find you some projects that will knock the socks off your classmates!")
        interestQuestions()
        break
    # if student answers no the app ends
    elif student.lower() == "no":
        print(f"Well then what the heck are you doing here, {name}? You dont have to go home but you can't stay here...")
        break  
    
    # hanldes input that isn't yes or no
    else:
        print(f"Come on {name}, the only options are 'yes' or 'no'! You either didn't pick one of those options or you typed gibberish. Either way I ask again...")
