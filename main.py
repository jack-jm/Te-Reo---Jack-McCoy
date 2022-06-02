import random

# Component 1: Instructions - 13/5/22 - Ask the user if they have played before and either show or don't show instructions.
show_instructions = input("Kia Ora, have you played the quiz before?\n").lower()

if show_instructions == "yes" or show_instructions == "y":
  print("Let's begin! Remember to answer with only the letter, not the word.\n")

else:
  print("Instructions:")
  print("You will be given a word in English and you will have to match it to it's Te Reo counterpart out of four options. You will type either A, B, C, or D, depending on what option you think is most likely correct. The words will start easy and will later become more difficult. When you want to stop, type anything other than enter and you will see your final score. \nLet's begin!\n")

# Component 2: Generate Question - 17/5/22 - Generate a random English word from a list and substitute into a question. Then generate four possible Te Reo meanings with one being correct.- V1
score = 0
question_number = 0
#Lists of words based on difficulty with Te Reo counterparts
easy_tereo = ["Kia Ora", "Kai", "Aroha", "Iwi", "Marae", "Aotearoa", "Whānau", "Mahi", "Whenua", "Taonga"]
easy_eng = ["Greetings", "Food", "Love", "Tribe", "Meeting Ground", "New Zealand", "Family", "Work", "Land", "Treasure"]
med_tereo = ["Karakia", "Maunga", "Moana", "Tamariki", "Waka", "Awa", "Hīkoi", "Tāne", "Wahine", "Waiata"]
med_eng = ["Prayer", "Mountain", "Ocean", "Children", "Canoe", "River", "Walk", "Man", "Woman", "Song"]
hard_tereo = ["Hui", "Whakapapa", "Motu", ]
hard_eng = ["Gathering", "Genealogy", "Island"]

play_again = input("Press <enter> to play or type anything else to quit.\n").lower()
while play_again == "":
  question_number = question_number + 1
  #This selects 4 random options from the list of possible Te Reo answers and one replacement answer if one of the four options is the same as the correct one.
  if score >= 0 and score < 4:
    easy_options = random.sample(easy_tereo, 5)
    easy_A = easy_options[0]
    easy_B = easy_options[1]
    easy_C = easy_options[2]
    easy_D = easy_options[3]
    easy_replacement = easy_options[4]
  
    ans_easy = dict(zip(easy_eng, easy_tereo))
    x = random.randint(0,9)
    easy_word = easy_eng[x]
    easy_correct_word = easy_tereo[x]
  
    if easy_A == easy_correct_word:
      easy_A = easy_replacement
    elif easy_B == easy_correct_word:
      easy_B = easy_replacement
    elif easy_C == easy_correct_word:
      easy_C = easy_replacement
    elif easy_D == easy_correct_word:
      easy_D = easy_replacement
    easy_question_format = random.randint(1,4)
    #This randomly selects the placement of the correct answer amongst the wrong answers.
    if easy_question_format == 1:
      easy_a_input = input("- Question {} -\nWhat is the English word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, easy_word, easy_correct_word, easy_B, easy_C, easy_D)).lower()    
      #Component 3: Check if user's answer is correct - 27/05/22 - Check if user's input matches correct answer and the either increase or decrease score.
      if easy_a_input == "a":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       #Component 4: Multiple Questions - 31/05/22 - Ask user if they want to continue and either ask another question or tell them their final score and end program.
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(easy_correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()

    elif easy_question_format == 2:
      easy_b_input = input("- Question {} -\nWhat is the English word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, easy_word, easy_A, easy_correct_word, easy_C, easy_D)).lower()
      if easy_b_input == "b":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(easy_correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
        
    elif easy_question_format == 3:
      easy_c_input = input("- Question {} -\nWhat is the English word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, easy_word, easy_A, easy_B, easy_correct_word, easy_D)).lower()
      if easy_c_input == "c":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1 
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(easy_correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
        
    else:
      easy_d_input = input("- Question {} -\nWhat is the English word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, easy_word, easy_A, easy_B, easy_C, easy_correct_word)).lower()
      if easy_d_input == "d":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(easy_correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
  
  elif score >= 4 and score < 8:
    print("\n\nCongratulations! You have leveled up to medium difficulty. The words will be slightly harder now.\n\n")
    med_options = random.sample(med_tereo, 5)
    med_A = med_options[0]
    med_B = med_options[1]
    med_C = med_options[2]
    med_D = med_options[3]
    med_replacement = med_options[4]
    
    ans_med = dict(zip(med_eng, med_tereo))
    x = random.randint(0,9)
    med_word = med_eng[x]
    med_correct_word = med_tereo[x]

    if med_A == med_correct_word:
      med_A = med_replacement
    elif med_B == med_correct_word:
      med_B = med_replacement
    elif med_C == med_correct_word:
      med_C = med_replacement
    elif med_D == med_correct_word:
      med_D = med_replacement
    med_question_format = random.randint(1,4)\

    if med_question_format == 1:
      med_a_input = input("- Question {} -\nWhat is the English word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, med_word, med_correct_word, med_B, med_C, med_D)).lower()    
      if med_a_input == "a":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(med_correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()

    elif med_question_format == 2:
      med_b_input = input("- Question {} -\nWhat is the English word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, med_word, med_A, med_correct_word, med_C, med_D)).lower()
      if med_b_input == "b":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(med_correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()

    elif med_question_format == 3:
      med_c_input = input("- Question {} -\nWhat is the English word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, med_word, med_A, med_B, med_correct_word, med_D)).lower()
      if med_c_input == "c":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1 
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(med_correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()

    else:
      med_d_input = input("- Question {} -\nWhat is the English word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(question_number, med_word, med_A, med_B, med_C, med_correct_word)).lower()
      if med_d_input == "d":
       score = score + 1
       print("That is correct! You gained one point and your score is {}.\n".format(score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()
      else:
       score = score - 1
       print("Sorry, that is incorrect. The correct answer was {}. You lost one point and your score is {}.\n".format(med_correct_word, score))
       play_again = input("Press <enter> to keep playing or type anything else to quit.\n").lower()

else:
  print("Thank you for playing! Your final score is {}.".format(score))