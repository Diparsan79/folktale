import random

room = 'square'
aura = 0
game_running = True

gym_done = False
cafe_done = False
alley_done = False

math_puzzles = [
  ["A kid screams 'SIX SEVEN!' at you. Okay but what is 6 x 7 actually?",
   ["a: 42", "b: 67", "c: 13", "d: 76"], "a"],
  ["You have 1000 followers and gain 250 with every video. How many followers after 4 videos?",
   ["a: 1250", "b: 1500", "c: 2000", "d: 4000"], "c"],
  ["Your aura starts at 0. Cringe dance: -50. W take: +30. Perfect rizz: +100. Final aura?",
   ["a: 180", "b: 80", "c: 120", "d: -80"], "b"],
]

# word puzzles: [scrambled, answer, hint]
word_puzzles = [
  ["dbikisi", "skibidi", "A toilet-based internet phenomenon"],
  ["gimsa", "sigma", "'Grindset' energy, according to the internet"],
  ["tornirab", "brainrot", "What too much scrolling gives you"],
]

math_puzzle = random.choice(math_puzzles)
word_puzzle = random.choice(word_puzzles)

# guess-the-number puzzle: the secret is random too
secret = random.randint(1, 20)
tries = 5

# main intro lines


print("")
print("In this town, everyone is a tiktoker\n")
print("even mayor mamdani does 4 tiktoks an hour.")
print(". A guy is aura-farming at a bus stop.")
print("")
print("And you? You don't even have the app. The town thinks you're an NPC.")
print("A kid points at you and whispers: 'Bro is cooked.'")
print("")
print("The only way to be taken seriously: collect 3 AURA, then enter the")
print("Algorithm Tower and prove you're a real main character.")
print("")

while game_running:

  if room == 'square':
    print("TOWN SQUARE: Fifty people are filming the same fountain. Nobody looks at you.")
    print("Your aura: " + str(aura) + "/3")
    print("1: The Sigma Gym (math)")
    print("2: Brainrot Cafe (word puzzle)")
    print("3: Ring Light Alley (guessing game)")
    print("4: The Algorithm Tower (needs 3 aura)")

    answer = input("1-4: ")

    if answer == "1":
      room = "gym"
    elif answer == "2":
      room = "cafe"
    elif answer == "3":
      room = "alley"
    elif answer == "4":
      room = "tower"
    else:
      print("Invalid input entered")

  elif room == "gym":
    if gym_done:
      print("The gym bros nod at you. You already earned your aura here.")
      room = "square"
    else:
      print("THE SIGMA GYM: A guy doing a pull-up while filming himself says:")
      print("'Solve this, and I'll give you aura. No cap.'")
      print("")
      print(math_puzzle[0])
      for option in math_puzzle[1]:
        print(option)

      answer = input("a-d (or 'back'): ").lower()

      if answer == math_puzzle[2]:
        print("That's correct! The gym bros chant your name. +1 aura")
        aura += 1
        gym_done = True
        room = "square"
      elif answer == "back":
        room = "square"
      elif answer == "a" or answer == "b" or answer == "c" or answer == "d":
        print("Wrong. The gym bro whispers 'L + ratio'.")
      else:
        print("Invalid input entered")

  elif room == "cafe":
    if cafe_done:
      print("The barista waves. You already got your aura spread over  here.")
      room = "square"
    else:
      print("BRAINROT CAFE: Every menu item is named after a meme. The barista")
      print("slides a stidky note across the counter. The letters are scrambled:")
      print("")
      print("   " + word_puzzle[0])
      print("   Hint: " + word_puzzle[2])

      answer = input("Type out your answer (or 'back'): ").lower()

      if answer == word_puzzle[1]:
        print("Correct! The whole cafe screams. +1 aura")
        aura += 1
        cafe_done = True
        room = "square"
      elif answer == "back":
        room = "square"
      else:
        print("Sorry, that's incorrect. The barista sighs: 'NPC behavior.'")

  elif room == "alley":
    if alley_done:
      print("The alley is empty now. You already got your aura here.")
      room = "square"
    else:
      print("RING LIGHT ALLEY: A glowing figure steps out. It's a streamer.")
      print("'I'm thinking of my view count (in millions), between 1 and 20.")
      print("You have " + str(tries) + " tries left.'")

      answer = input("Your guess (or 'back'): ").lower()

      if answer == "back":
        room = "square"
      elif answer.isdigit():
        guess = int(answer)
        tries -= 1

        if guess == secret:
          print("CORRECT! The streamer drops their phone. +1 aura")
          aura += 1
          alley_done = True
          room = "square"
        elif tries <= 0:
          print("Out of tries! The streamer ghosts you. The number was " + str(secret) + ".")
          print("He picks a new number. Try again.")
          secret = random.randint(1, 20)
          tries = 5
          room = "square"
        elif guess < secret:
          print("Too low! Aim higher.")
        else:
          print("Too high! Aim lower.")
      else:
        print("Invalid input entered")

  elif room == "tower":
    if aura >= 3:
      print("THE ALGORITHM TOWER: The doors open. A giant glowing screen speaks:")
      print("'Three aura... and you never even posted. You're the only real person")
      print("in Viralpur. Everyone else is just acting for the camera.'")
      print("")
      print("The whole town finally puts the phones down and looks at you.")
      print("A kid says: 'Bro... you're actually him.'")
      print("")
      print("YOU WIN! Your aura is legendary. (And you still don't have TikTok.)")
      game_running = False
    else:
      print("The tower door buzzes: 'Only " + str(aura) + " aura? That's mid. Come back with 3.'")
      room = "square"

  print("")