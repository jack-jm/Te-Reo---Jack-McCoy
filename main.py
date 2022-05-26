import random

# Component 1: Instructions - 13/5/22 - Ask the user if they have played before and either show or don't show instructions.
show_instructions = input("Kia Ora, have you played the quiz before?\n").lower()

if show_instructions == "yes" or show_instructions == "y":
  print("Let's begin!")

elif show_instructions == "no" or show_instructions == "n":
  print("Instructions:")
  print("You will be given a word in English and you will have to match it to it's Te Reo counterpart out of four options. You will type either A, B, C, or D, depending on what option you think is most likely correct. The words will start easy and will later become more difficult. When you want to stop, type anything other than enter and you will see your final score. \nLet's begin!\n")

else:
  print("Instructions:")
  print("You will be given a word in English and you will have to match it to it's Te Reo counterpart out of four options. You will type either A, B, C, or D, depending on what option you think is most likely correct. The words will start easy and will later become more difficult. When you want to stop, type anything other than enter and you will see your final score. \nLet's begin!\n")

# Component 2: Generate Question - 17/5/22 - Generate a random English word from a list and substitute into a question. Then generate four possible Te Reo meanings with one being correct.- V1
score = 0
#Lists of words based on difficulty with Te Reo counterparts
easy_tereo = ["Kia Ora", "Kai", "Aroha", "Iwi", "Marae", "Aotearoa", "Whānau", "Mahi", "Whenua", "Taonga"]
easy_eng = ["Greetings", "Food", "Love", "Tribe", "Meeting Ground", "New Zealand", "Family", "Work", "Land", "Treasure"]

#This selects 4 random options from the list of possible Te Reo answers and one replacement answer if one of the four options is the same as the correct one.
options = random.sample(easy_tereo, 5)
easy_A = options[0]
easy_B = options[1]
easy_C = options[2]
easy_D = options[3]
replacement = options[4]

ans = dict(zip(easy_eng, easy_tereo))
x = random.randint(0,9)
easy_word = easy_eng[x]
correct_word = easy_tereo[x]

if easy_A == correct_word:
  easy_A = replacement
elif easy_B == correct_word:
  easy_B = replacement
elif easy_C == correct_word:
  easy_C = replacement
elif easy_D == correct_word:
  easy_D = replacement

play_again = input("Press <enter> to play.\n").lower()
if play_again == "":
  question_format = random.randint(1,4)
  #This randomly selects the placement of the correct answer amongst the wrong answers.
  if question_format == 1:
     q_a_input = input("What is the English word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(easy_word, correct_word, easy_B, easy_C, easy_D)).lower()
    if q_a_input == "a":
      print(correct)
      
  elif question_format == 2:
          q_b_input = input("What is the English word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(easy_word, easy_A, correct_word, easy_C, easy_D)).lower()
  elif question_format == 3:
          q_c_input = input("What is the English word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(easy_word, easy_A, easy_B, correct_word, easy_D)).lower()
  else:
          q_d_input = input("What is the English word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(easy_word, easy_A, easy_B, easy_C, correct_word)).lower()

else:
  print("Final Score: {}. Thank you for playing!".format(score))

#Component 3: Check if user's answer is correct - 27/05/22 - Check if user's input matches correct answer and the either increase or decrease score.