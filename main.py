import random

#TESTING

# Component 1: Instructions - 13/5/22 - Ask the user if they have played before and either show or don't show instructions.
show_instructions = input("Kia Ora, have you played the quiz before?\n").lower()

if show_instructions == "yes" or show_instructions == "y":
  print("Let's begin! Remember to answer with only the letter, not the word.\n")

else:
  print("Instructions:\nYou will be given a word in English and you will have to match it to it's Te Reo counterpart out of four options. You will type either A, B, C, or D, depending on what option you think is most likely correct. The words will start easy and will later become more difficult. If you lose enough points so that you fall below the level up point, you will go down a level. When you want to stop, type anything other than enter and you will see your final score. \nLet's begin!\n")

# Component 2: Generate Question - 17/5/22 - Generate a random English word from a list and substitute into a question. Then generate four possible Te Reo meanings with one being correct.- V1
#Score Variable - increases by one when answered correctly, decreases by one when answered incorrectly.
score = 0
#Question No. Variable - Increases every question, prints number before asking the question.
question_number = 0
#Lists of words based on difficulty with Te Reo counterparts
easy_tereo = ["Kia Ora", "Kai", "Aroha", "Iwi", "Marae", "Aotearoa", "Whānau", "Mahi", "Whenua", "Taonga"]
easy_eng = ["Greetings", "Food", "Love", "Tribe", "Meeting Ground", "New Zealand", "Family", "Work", "Land", "Treasure"]
med_tereo = ["Tangi", "Maunga", "Moana", "Tamariki", "Waka", "Awa", "Hīkoi", "Tāne", "Wahine", "Waiata", "Whare"]
med_eng = ["Funeral", "Mountain", "Ocean", "Children", "Canoe", "River", "Walk", "Man", "Woman", "Song", "House"]
hard_tereo = ["Hui", "Whakapapa", "Motu", "Koha", "Roto", "Mana", "Karakia", "Puku", "Kaumātua", "Kura"]
hard_eng = ["Gathering", "Genealogy", "Island", "Gift", "Lake", "Prestige", "Prayer", "Stomach", "Elder", "School"]

#Play Again Variable - If user types <enter>, it asks a question, if anything else is entered, the program ends.
play_again = input("Press <enter> to play or type anything else to quit.\n").lower()
while play_again == "":
  question_number = question_number + 1
  #This selects 4 random options from the list of possible Te Reo answers and one replacement answer if one of the four options is the same as the correct one.
  #If score is between 0 and 4, the question generated is easy diffculty.
  
  #Component 5: Difficulty Levels - 01/06/2022
  if score < 4:
    options = random.sample(easy_tereo, 5)
    A = options[0]
    B = options[1]
    C = options[2]
    D = options[3]
    replacement = options[4]
  
    ans = dict(zip(easy_eng, easy_tereo))
    x = random.randint(0,9)
    question_word = easy_eng[x]
    correct_word = easy_tereo[x]

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
    #This randomly selects the placement of the correct answer amongst the wrong answers.
    if question_format == 1:
      a_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, correct_word, B, C, D)).lower()    
      #Component 3: Check if user's answer is correct - 27/05/22 - Check if user's input matches correct answer and the either increase or decrease score.
      if a_input == "a":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       #Component 4: Multiple Questions - 31/05/22 - Ask user if they want to continue and either ask another question or tell them their final score and end program.
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()

    elif question_format == 2:
      b_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, A, correct_word, C, D)).lower()
      if b_input == "b":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
        
    elif question_format == 3:
      c_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, A, B, correct_word, D)).lower()
      if c_input == "c":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1 
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
        
    else:
      d_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, A, B, C, correct_word)).lower()
      if d_input == "d":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()

  elif score == 4:
    print("\n\nYou are now at medium difficulty.\n\n")
    options = random.sample(med_tereo, 5)
    A = options[0]
    B = options[1]
    C = options[2]
    D = options[3]
    replacement = options[4]
    
    ans_med = dict(zip(med_eng, med_tereo))
    x = random.randint(0,9)
    question_word = med_eng[x]
    correct_word = med_tereo[x]

    if A == correct_word:
      A = replacement
    elif B == correct_word:
      B = replacement
    elif C == correct_word:
      C = replacement
    elif D == correct_word:
      D = replacement
    question_format = random.randint(1,4)

    if question_format == 1:
      a_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, correct_word, B, C, D)).lower()    
      if a_input == "a":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()

    elif question_format == 2:
      b_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, A, correct_word, C, D)).lower()
      if b_input == "b":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()

    elif question_format == 3:
      c_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, A, B, correct_word, D)).lower()
      if c_input == "c":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1 
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()

    else:
      d_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, A, B, C, correct_word)).lower()
      if d_input == "d":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
        
  #If score is between 4 and 8, the question generated is medium diffculty. Everything is the same except the words are harder in difficulty.
  elif score >= 4 and score < 8:
    options = random.sample(med_tereo, 5)
    A = options[0]
    B = options[1]
    C = options[2]
    D = options[3]
    replacement = options[4]
    
    ans_med = dict(zip(med_eng, med_tereo))
    x = random.randint(0,9)
    question_word = med_eng[x]
    correct_word = med_tereo[x]

    if A == correct_word:
      A = replacement
    elif B == correct_word:
      B = replacement
    elif C == correct_word:
      C = replacement
    elif D == correct_word:
      D = replacement
    question_format = random.randint(1,4)\

    if question_format == 1:
      a_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, correct_word, B, C, D)).lower()
      if a_input == "a":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()

    elif question_format == 2:
      b_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, A, correct_word, C, D)).lower()
      if b_input == "b":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()

    elif question_format == 3:
      c_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, A, B, correct_word, D)).lower()
      if c_input == "c":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1 
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()

    else:
      d_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, A, B, C, correct_word)).lower()
      if d_input == "d":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()

  elif score == 8:
    print("\n\nYou are now at hard difficulty. This is the final difficulty level. Feel free to keep playing for as long as you want or quit when you are finished.\n\n")
    options = random.sample(hard_tereo, 5)
    A = options[0]
    B = options[1]
    C = options[2]
    D = options[3]
    replacement = options[4]
  
    ans_hard = dict(zip(hard_eng, hard_tereo))
    x = random.randint(0,9)
    question_word = hard_eng[x]
    correct_word = hard_tereo[x]

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
    #This randomly selects the placement of the correct answer amongst the wrong answers.
    if question_format == 1:
      a_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, correct_word, B, C, D)).lower()    
      if a_input == "a":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()

    elif question_format == 2:
      b_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, A, correct_word, C, D)).lower()
      if b_input == "b":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
        
    elif question_format == 3:
      c_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, A, B, correct_word, D)).lower()
      if c_input == "c":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1 
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
        
    else:
      d_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, A, B, C, correct_word)).lower()
      if d_input == "d":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
  #If score is greater than 8, question diffculty goes up to hard - only thing that changes is again the words.
  elif score >= 8:
    options = random.sample(hard_tereo, 5)
    A = options[0]
    B = options[1]
    C = options[2]
    D = options[3]
    replacement = options[4]
  
    ans_hard = dict(zip(hard_eng, hard_tereo))
    x = random.randint(0,9)
    question_word = hard_eng[x]
    correct_word = hard_tereo[x]

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
    #This randomly selects the placement of the correct answer amongst the wrong answers.
    if question_format == 1:
      a_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, correct_word, B, C, D)).lower()    
      if a_input == "a":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()

    elif question_format == 2:
      b_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, A, correct_word, C, D)).lower()
      if b_input == "b":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
        
    elif question_format == 3:
      c_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, A, B, correct_word, D)).lower()
      if c_input == "c":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1 
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
        
    else:
      d_input = input("- Question {} -\nWhat is the Te Reo word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, question_word, A, B, C, correct_word)).lower()
      if d_input == "d":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
        
else:
  print("Thank you for playing! Your final score is {}.".format(score))