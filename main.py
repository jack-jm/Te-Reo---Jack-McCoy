# Component 1: Instructions - 13/5/22 - Ask the user if they have played before and either show or don't show instructions.
show_instructions = input("Kia Ora, have you played the quiz before?\n").lower()

if show_instructions == "yes" or show_instructions == "y":
  print("Quiz starts")

elif show_instructions == "no" or show_instructions == "n":
  print("Here are the instructions")

else:
  print("Please answer yes or no.")