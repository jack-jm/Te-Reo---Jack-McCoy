# Import the random library
import random

# Functions go here
def generate_question(score, question_format, question_number, question_word, correct_word,A, B, C, D):
   #This randomly selects the placement of the correct answer amongst the wrong answers.
    if question_format == 1:
      a_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, correct_word, B, C, D)).lower()    
      #Component 3: Check if user's answer is correct - 27/05/22 - Check if user's input matches correct answer and the either increase or decrease score.
      if a_input == "a":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       #Component 4: Multiple Questions - 31/05/22 - Ask user if they want to continue and either ask another question or tell them their final score and end program.

      else:
       print("Sorry, that is incorrect. The correct answer was {}. Your score did not change and is still {}.\n".format(correct_word, score))


    elif question_format == 2:
      b_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, A, correct_word, C, D)).lower()
      if b_input == "b":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))

      else:
       print("Sorry, that is incorrect. The correct answer was {}. Your score did not change and is still {}.\n".format(correct_word, score))

        
    elif question_format == 3:
      c_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, A, B, correct_word, D)).lower()
      if c_input == "c":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))

      else:
       print("Sorry, that is incorrect. The correct answer was {}. Your score did not change and is still {}.\n".format(correct_word, score))

        
    else:
      d_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, A, B, C, correct_word)).lower()
      if d_input == "d":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))

      else:
       print("Sorry, that is incorrect. The correct answer was {}. Your score did not change and is still {}.\n".format(correct_word, score))
    return score

# Main routine goes here
# Component 1: Instructions - 13/5/22 - Ask the user if they have played before and either show or don't show instructions.
show_instructions = input("Kia Ora, have you played the quiz before?\n").lower()

if show_instructions == "yes" or show_instructions == "y":
  print("Let's begin! Remember to answer with only the letter, not the word.\n")

else:
    print("Instructions:\nYou will be given a word in English and you will have to match it to it's Te Reo counterpart out of four options. You will type either A, B, C, or D, depending on what option you think is most likely correct. There are ten questions and you will be given your final score when you reach the end. If you want to quit, type anything other than enter and you will see your final score. \nLet's begin!\n")

# Component 2: Generate Question - 17/5/22 - Generate a random English word from a list and substitute into a question. Then generate four possible Te Reo meanings with one being correct.- V1
  
#Score Variable - increases by one when answered correctly, decreases by one when answered incorrectly.
score = 0
#Question No. Variable - Increases every question, prints number before asking the question.
question_number = 0
#Lists of words based on difficulty with Te Reo counterparts
tereo_list = ["Kia Ora", "Kai", "Aroha", "Iwi", "Marae", "Aotearoa", "Whānau", "Mahi", "Whenua", "Taonga", "Tangi", "Maunga", "Moana", "Tamariki", "Waka", "Awa", "Hīkoi", "Tāne", "Wahine", "Waiata", "Whare", "Hui", "Whakapapa", "Motu", "Koha", "Roto", "Mana", "Karakia", "Puku", "Kaumātua", "Kura"]
eng_list = ["Greetings", "Food", "Love", "Tribe", "Meeting Ground", "New Zealand", "Family", "Work", "Land", "Treasure", "Funeral", "Mountain", "Ocean", "Children", "Canoe", "River", "Walk", "Man", "Woman", "Song", "House", "Gathering", "Genealogy", "Island", "Gift", "Lake", "Prestige", "Prayer", "Stomach", "Elder", "School"]

#Play Again Variable - If user types <enter>, it asks a question, if anything else is entered, the program ends.
play_again = input("Press <enter> to play or type anything else to quit.\n").lower()
while play_again == "":
  question_number = question_number + 1
  #This selects 4 random options from the list of possible Te Reo answers and one replacement answer if one of the four options is the same as the correct one.
  #If score is between 0 and 4, the question generated is easy diffculty.
  
  #Component 5: Difficulty Levels - 01/06/2022
  if question_number <= 10:
    options = random.sample(tereo_list, 5)
    A = options[0]
    B = options[1]
    C = options[2]
    D = options[3]
    replacement = options[4]
  
    ans = dict(zip(eng_list, tereo_list))
    x = random.randint(0,29)
    question_word = eng_list[x]
    correct_word = tereo_list[x]
  
    #If any option is the same as the correct one a replacement is generated to fill in.
    if A == correct_word:
      A = replacement
    elif B == correct_word:
      B = replacement
    elif C == correct_word:
      C = replacement
    elif D == correct_word:
      D = replacement
    question_format = random.randint(1,4)

    score = generate_question(score, question_format, question_number, question_word, correct_word,A, B, C, D)
    play_again = input("Press <enter> to play or type anything else to quit.\n").lower()

  if question_number == 10:
    if score >= 5:
      print("Congratulations! You have finished the quiz and answered half or more of the questions correctly! Your final score was {}.".format(score))
    else:
      print("Congratulations! You have finished the quiz but unfortunately you answered less than half of the questions correctly. Your final score was {}.".format(score))
  
    #This randomly selects the placement of the correct answer amongst the wrong answers.
    
print("Your final score is {}".format(score))