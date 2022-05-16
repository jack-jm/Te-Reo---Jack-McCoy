# Component 1: Instructions - 13/5/22 - Ask the user if they have played before and either show or don't show instructions.
show_instructions = input("Kia Ora, have you played the quiz before?\n").lower()

if show_instructions == "yes" or show_instructions == "y":
  print("Let's begin!")

elif show_instructions == "no" or show_instructions == "n":
  print("Instructions:")
  print("You will be given a word in Te Reo and you will have to match it to it's English meaning out of four options. You will type either A, B, C, or D, depending on what option you think is most likely correct. The words will start easy and will later become more difficult.")

else:
  print(end="Please answer yes or no.")

score = 0
#Lists of words based on difficulty
easy = ["Kia Ora", "Kai", "Aroha", "Iwi", "Marae", "Aotearoa", "Whānau", "Mahi", "Whenua", "Hangi"]

play_again = input("Press <enter> to play.")