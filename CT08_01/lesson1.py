import random

# Recap 1

# if material is paper, put in in the bin for paper
# else check if it is plastic, if it is, put it in the bin for plastic
# else check if it is glass, if it is, put it in the bin for glass
# else put it in the rubbish bin

material = random.randint(1,4)
if material == 1:
    print("Put it in the plastic bin.")
elif material == 2:
    print("Put it in the glass bin.")
elif material == 3:
    print("Put it in the paper bin.")
else:
    print("Put it in the general waste bin.")


# Recap 2

redPlates = 3
bluePlates = 5
greenPlates = 4

redPrice = 1
bluePrice = 2
greenPrice = 3

totalPrice = 3 * 1 + 5 * 2 + 4 * 3
print("The total price is $" + str(totalPrice))


# Recap 3

score_one = 80
score_two = 90
score_three = 75

total = score_one + score_two + score_three

average_score = total / 3

student_name = "Alex"

print("Average score for " + student_name + " is: " + str(average_score))


# Recap 4

score = random.randint(0, 100)

if score > 74:
    print("You scored a A.")
elif score > 59:
    print("You scored a B.")
elif score > 49:
    print("You scored a C.")
else:
    print("You scored a " + str(score) + ". You failed your life.")