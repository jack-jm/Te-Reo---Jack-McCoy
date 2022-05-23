import random

# Component 1: Instructions - 13/5/22 - Ask the user if they have played before and either show or don't show instructions.
show_instructions = input("Kia Ora, have you played the quiz before?\n").lower()

if show_instructions == "yes" or show_instructions == "y":
  print("Let's begin!")

elif show_instructions == "no" or show_instructions == "n":
  print("Instructions:")
  print("You will be given a word in Te Reo and you will have to match it to it's English meaning out of four options. You will type either A, B, C, or D, depending on what option you think is most likely correct. The words will start easy and will later become more difficult.\nLet's begin!\n")

else:
  print("Please answer yes or no.")
  exit()

# Component 2: Generate Question - 17/5/22 - Generate a random Te Reo word from a list and substitute into a question. Then generate four possible English meanings with one being correct.- V1
score = 0
#Lists of words based on difficulty with English counterparts
easy_tereo = ["Kia Ora", "Kai", "Aroha", "Iwi", "Marae", "Aotearoa", "Whānau", "Mahi", "Whenua", "Taonga"]
easy_eng = ["Greetings", "Food", "Love", "Tribe", "Meeting Ground", "New Zealand", "Family", "Work", "Land", "Treasure"]
easy_word = random.choice(easy_tereo)
easy_A = random.choice(easy_eng)
easy_B = random.choice(easy_eng)
easy_C = random.choice(easy_eng)
easy_D = random.choice(easy_eng)

ans = dict(zip(easy_tereo, easy_eng))

play_again = input("Press <enter> to play.").lower()
if play_again == "":
  input("What is the English word for {}?\nA: {}\nB: {}\nC: {}\nD: {}\n".format(easy_word, easy_A, easy_B, easy_C, easy_D)).lower()