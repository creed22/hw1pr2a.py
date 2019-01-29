# coding: utf-8
#
# hw1pr2b.py
#


import time

delay = 2.0          
username = input("Please enter your name: ")

print()
print("Unfortunatley", username, " you've lost an important homework assignment while exploring LA with your friends.")
print()

print("Your quest: To correctly retrace your steps and retrieve the assignment.")
print()
burger = input("Before heading to LA you and your friends went to (arguably) the most popular burger chain in California. Which was it? ")

if burger == "in-n-out" :
  print("Yes In-N-Out! Let's see if it's there!")
  time.sleep(delay)
  print("It's not there...")
elif burger == "jack in the box" :
  print ("Yes! Jack In The Box! Let's see if it's there...")
  time.sleep(delay)
  print("It's not there...")
else:
  print ("You just remembered you didn't get out of the car at the restaurant so it couldn't be there.")    
time.sleep(delay)
print ("After " , burger , " you guys bought tickets to get into the Getty Museum. You went to three exihibits: Modern Fashion, Greek Sculptures, and African Art.")
print("You only have time to revisit one before the Museum closes!")
art = input("Which exihibit?")

if art == "modern fashion" :
  print ("You scour the exihibit, searching under benches and behind curtains. The Museum is just about to close when you get a text from your friend saying he remembers seeing it peeking out of your backpack when you guys were getting back in the car. So it couldn't be still in the Getty.")
elif art == "greek sculptures" :
  print ("You run around frantically looking for the stapled paper. You almost knock over a statue when you get a text from your friend saying he remembers seeing it peeking out of your backpack when you guys were getting back in the car. So it couldn't be still in the Getty.")
elif art == "african art":
  print ("You rush into the exihibit and think you spot your assignment near a display. Unfortunately it's just a discarded pamphlet. The Museum is just about to close when you get a text from your friend saying he remembers seeing it peeking out of your backpack when you guys were getting back in the car. So it couldn't be still in the Getty. ")
else:
  print("The Museum is closed when you get there so you pray you didn't leave it there and move on to the next spot.")

time.sleep(delay)
print("Next, you all drove to the beach so you make your way there.")
time.sleep(delay)
beach = input("You remember setting your backpack down to play beach volleyball! Do you want to go check?") 

if beach == 'yes':
  print ("You make the trek to the volleyball net and still don't see it.")
else:
  print("You recall leaving your bag in the car so it couldn't be here.")

time.sleep(delay)

print("After leaving the beach the first time, you remember your vegan friend was hungry so you guys drove to a vegan taco restaurant.") 
print("You pull up to the restaurant and see that it's closed but there's an employee sweeping the floor.")
taco = input("Do you want to knock on the door to see if he will let you in to look around?")

if taco == "yes":
  print("You knock on the glass and startle the employee. He gestures that the restaurant is closed. You mouth that you left something here and beg him to let you in. He finally lets you in.")
elif taco == "no":
  print("You're about to drive away when you see a paper hanging off the edge of the table inside. You jump out of the car and knock loudly on the glass, startling the employee. He gestures that the restaurant is closed. You mouth that you left something here and beg him to let you in. He finally lets you in.")

print ("You tell him that you think that paper you see on one of the tables is yours. He goes to grab it, looks at assignment, and asks you if your name is" , username , ".")

name = input("Do you confirm that's your name?")

if name == "yes":
  print("Finally! You take your assignment and head back to campus.")
