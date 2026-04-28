print("Welcome to the sorting Hat Simulator!")
print ("Please anwser the folowing Questione.")
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

question1 = int(input("Q1) Do you like Dawn or Dusk?\n" 
                      "1) Dawn\n" 
                      "2) Dusk \n"))

if question1 == 1:
  gryffindor = gryffindor + 1
  ravenclaw = ravenclaw + 1
elif question1 == 2:
  hufflepuff = hufflepuff + 1
  slytherin = slytherin + 1
else:
  print ("Wrong input")

question2 = int(input("Q2) When I’m dead, I want people to remember me as:\n" 
                      "1) The Good\n" 
                      "2) The Great\n" 
                      "3) The Wise\n" 
                      "4) The Bold\n"))

if question2 == 1:
  hufflepuff = hufflepuff + 2
elif question2 == 2:
  slytherin = slytherin + 2
elif question2 == 3:
  ravenclaw = ravenclaw + 2
elif question2 == 4:
  gryffindor = gryffindor + 2
else:
  print("Wrong input")

questione3 = int(input("Q3) Which kind of instrument most pleases your ear?\n" 
                       "1) The violin\n" 
                       "2) The trumpet\n" 
                       "3) The piano\n" 
                       "4) The drum \n"))

if questione3 == 1:
  slytherin = slytherin + 4
elif questione3 == 2:
  hufflepuff = hufflepuff + 4
elif questione3 == 3:
  ravenclaw = ravenclaw + 4
elif questione3 == 4:
  gryffindor = gryffindor + 4
else:
  print("Wrong Input")

print("Griffyndor: ", gryffindor)
print("Hufflepuff: ", hufflepuff)
print("Ravenclaw: ", ravenclaw)
print("Slytherin: ", slytherin)