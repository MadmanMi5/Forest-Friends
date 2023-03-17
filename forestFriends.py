import sys, subprocess
import time
from time import sleep

class AdventureGame: # class to hold the game 

  def __init__(self):
    self.startIntro = False     # setting dialog and clue into boolean, changing depending on the conditions
    self.arriveRoad = False
    self.arriveWoods = False
    self.foundHorse = False
    self.meetFarmer = False
    self.getQlue = False
    self.directions = ["right", "left", "back"]     # to be conpared with the user's answer
    self.options = ["1", "2", "3"]
    self.question = ["y", "n"]

    self.typeThis = ("type inside")     # to be used in the type method
    
    self.wind = False       # weather system boolean, the changing weather conditions that affect other conditions or methods
    self.rain = False
    self.storm = False

    self.wind_time = 40     # weather timer, setting each weather to given timer till end
    self.rain_time = 90
    self.night_time = 170
    self.time_limit = 300
    self.start_time = time.time()   # Gathers the current time, setting it as variable, the value does not change
   


  def intro(self):
    # initializes the instance variable `typeThis` to an empty string
    self.typeThis = ("")
    self.clear_screen()
    # prints a welcome message
    print("Welcome to the Adventure Game!")
    # asks for the player's name and saves it as an instance variable `name`
    self.name = input("Please type in your name? ")
    # clears the screen (implementation not shown)
    self.clear_screen()
    # sets the instance variable `typeThis` to a string containing a welcome message with the player's name
    self.typeThis = (f"Welcome {self.name.capitalize()} to")
    # displays the `typeThis` string letter by letter, creating a typing effect
    self.typeWriter()
    # waits for three seconds
    time.sleep(1)
    # displays ASCII art for the game title
    art.game_title()
    # waits for three seconds
    time.sleep(3)
    # calls the `ogreHome()` method to start the game
    self.ogreHome()



  def ogreHome(self):
    self.clear_screen()
    self.typeThis =("") # initializes the instance variable `typeThis` to an empty string
    art.ogreHome()    # displays ASCII art for the ogre's home
    if self.startIntro == False:    # if this is the first time calling this method (`startIntro` is initially set to `False`), the method sets up the scene where the ogre's donkey is missing
      self.startIntro = True
      self.typeThis = self.typeThis + (
        "It was a calm evening in a small wooden home, the Ogre slept calmly and peacefully till a gust of wind rattled the window with a faint sound of thunder the Ogre awoken by the sudden noise to see a storm was on the horizon. ‘Donkey, Donkey’ he shouted, but his pet Donkey has not arrived from his trip out in the woods."
      )
    else:   # displays a message asking the player if they want to go out and look for the donkey or stay at home
      self.typeThis = self.typeThis + ("The Ogre returns to his home and patiently waits. ")
    self.typeThis = self.typeThis + ("Worried he asks, ‘should I go out and look for him?’ ")
    self.typeWriter()

    print("""
    1) Stay at home and wait for Donkey to arrive
    2) Go out and look for him""")

    userInput = ""
    while userInput not in self.options:
      
      userInput = input("Would you like to continue? (1/2) ").replace(" ", "")  # if the player chooses to stay at home or the time limit is exceeded, the method displays the outcome of finding the donkey dead in the morning
      if userInput == "1" or (time.time()-self.start_time) > self.time_limit:
        self.typeThis = (
          "It is morning and the storm has past, the Ogre looks around in dreed and concern for his pet the Donkey, only to find him still and lifeless in a small pool of water. "
        )
        self.typeWriter()
        if self.foundHorse == True:
          self.typeThis = ("Later that day the Ogre was able to find and return the horse back to its owner. ")
          self.typeWriter()
          exit()
      elif userInput == "2":
        theWeather.weatherNow()    
        self.forkedRoad()   # Once passing through and returning from the other methods, moves on with the story
      else:
        print("Please enter a valid option (1/2).")
      

  def forkedRoad(self):
    # Clear the console screen (not defined in this code snippet)
    self.clear_screen()   
    self.typeThis =("") # clearing the variable, to be later be filled and used in the method
    # Display some ASCII art of a road or landscape (not defined in this code snippet)
    art.road()
    # Check if the Ogre has been to the fork before
    if self.arriveRoad == False:    # If not, add some text to the typeThis string about following the Donkey's trail
      self.typeThis = self.typeThis + (
        "The Ogre puts on his cloak and goes out, following the Donkey’s trail he arrives at a fork in the path and sees below small hove prints heading into the woods, instead of his normal path to the open field. "
      )
    else:   # If yes, add some different text to the typeThis string
      self.typeThis = self.typeThis + ("The Ogre returns to the fork path and wonders where he should go. ")
    # Type out the contents of the typeThis string letter by letter (not defined in this code snippet)
    self.typeWriter()
    # Display a menu of three options for the user to choose from
    print("""
    Which direction should he go? 
    1) Go into the woods (right) 
    2) Go into the open field (left)
    3) Go back the Ogre’s home (back)""")
    # Set the arriveRoad variable to True, indicating the Ogre has been to the fork
    self.arriveRoad = True
    # Ask the user to enter a direction
    print("Where do you want to go? ")
    userInput = ""
    # Keep asking until a valid direction is entered
    while userInput not in self.directions:
      print("Options (no spaces): right / left / back ")
      userInput= input().lower().replace(" ", "")
    # Call different methods depending on the chosen direction
    if userInput == "right":
      # Display the current weather (not defined in this code snippet)
      theWeather.weatherNow()
      # Go to the farmHouse method
      self.farmHouse()
    elif userInput == "left":
      # Ask the user if the Ogre should go left
      print("""
      The Ogre turns right to discover donkey’s hair and questions himself. 
      ‘Should I go left?’ 
      Yes / No""")
      userInput= input("").lower().replace(" ", "")
      if userInput == "yes":
        # Display the current weather (not defined in this code snippet)
        theWeather.weatherNow()
        # Go to the farmfield method
        self.farmfield()
      else:
        # Display the current weather (not defined in this code snippet)
        theWeather.weatherNow()
        # Go back to the forkedRoad method
        self.forkedRoad()
    elif userInput == "back":
      # Display the current weather (not defined in this code snippet)
      theWeather.weatherNow()
      # Go back to the ogreHome method
      self.ogreHome()
    else:
      # Display an error message if an invalid direction is entered
      print("Please enter a valid option.")

  def farmHouse(self):
    self.clear_screen()   
    self.typeThis =("") 
    userInput = ""
    art.farmHouse()
    # if the weather is rainy or rain boolean variable is true then the farmer would go inside and these additional dialogs and options will be hidden
    if self.meetFarmer == False and self.rain == False:
      self.typeThis = (
        "The Ogre heads towards the right path and goes forth into the woods. Where footprints can be found. However, Ogre notices the footprints were fading away as he continued."
        )
      self.typeWriter()
      while userInput not in self.question:
        userInput = input("Should he continue on his current path? Answer: 'y', 'n' ").lower().replace(" ", "")
        if userInput.lower() == "y":
          self.typeThis = ("The Ogre continues on his current path, leading him towards an old farmer's home. There he meets the farmer and asks, ‘Hello there, have you seen my donkey?’. Scratching his beard, he replies ‘your donkey hm, he should have gone to his usual path towards in that open farm field no, I did see something move by here rather quick, but I don’t know what, it headed straight into the dark woods’")
          self.meetFarmer = True
        elif userInput.lower() == "n":
          self.typeThis = ("The Ogre turns back and goes to his home, hoping his Donkey will be waiting for him.")
          self.typeWriter()
          time.sleep(0.5)
          # wait for a certain amount of time till it calls on the methods for the weather and the ogre's home
          theWeather.weatherNow()
          self.ogreHome()
          return
        else:
          print("Please enter a valid option.")
    elif self.meetFarmer == False and self.rain == True:
      self.typeThis = ("The Ogre continues on his current path, leading him near the old farmer's home, looking at direction of the trail it seems as though it is heading towards the woods. ")
    else:
      self.typeThis = ("The Ogre arrives back at the old farmer’s home. ")
    self.typeWriter()

    # show certain answers or clues depending on the boolean variable
    if self.meetFarmer == True:
      print("\n1) Follow the path of a fast being running into the woods, seen by the farmer.")
    else:
      print("\n1) Follow the path of the trail deeper into the woods.")
    print("2) Go back.")
    if self.getQlue == False and self.rain == False:
      print("3) Further question the old farmer. ")
    userInput = ""
    while userInput not in self.options:
      userInput = input("What should the ogre do?  Enter a number: ").lower().replace(" ", "")
      if userInput == "1":
        theWeather.weatherNow()

        self.theWoods()
        return
      elif userInput == "2":
        theWeather.weatherNow()
        # Go back to the forkedRoad method
        self.forkedRoad()
        return
      elif userInput == "3" and self.getQlue == False and self.rain == False:
        # the boolean attribute set to true as user gathers the clue in this option
        self.getQlue = True
        self.typeThis = ("‘Not long ago a man came running through here, yelling. I don’t know what he was yelling, but I do know he was chasing after what I saw earlier into the dark woods, sorry but I'm heading back home before the storm arrives, you should do the same’ ")
        self.typeWriter()
        time.sleep(0.5)
        theWeather.weatherNow()
        # repeat the farmHouse method again to change the conditions and with it he dialog
        self.farmHouse()
        return
      else:
        print("Please enter a valid option.")

  def theWoods(self):
    self.clear_screen()   
    self.typeThis =("")
    art.theWoods()
    if self.arriveWoods == False:
      self.typeThis = (
        "The Ogre heads deeper and deeper into the woods fearful and concerned, he asks himself ‘why on earth would Donkey be out here in the middle of the woods?’. Then up ahead he sees a something moving past the trees and bushes, it was not his pet donkey but a horse. ‘A storm is coming you don’t want to be out here’, as he grabs the horse's rain. "
      )
      # if by approaching this section of the game the boolean is set to True so this would enable up addition dialog in other sections
      self.arriveWoods = True
      self.foundHorse = True
    else:
      self.typeThis = ("The Ogre returns to the woods. ")

    self.typeWriter()
    print("""
    1) Go back
    2) Go further into the woods to look for donkey """)
    userInput = ""
    while userInput not in self.options:
      userInput = input("What do you want to do?  (1/2) ").replace(" ", "")
      if userInput == "1":
        theWeather.weatherNow()
        self.farmHouse()
      elif userInput == "2":
        art.gameOver()
        self.typeThis = ("The Ogre and the horse went further into the woods, they have never been seen since. Game over, Try agian ")
        self.typeWriter()
        quit()
      else:
        print("Please enter a valid option (1/2).")

  def farmfield(self):
    self.clear_screen()   
    self.typeThis =("")
    art.farmField()
    self.typeThis = (
      "The Ogre heads towards the open farm field where he finds piece of matching his pet donkey. But the weather is starting to get bad and the Ogre wonders if he should find shelter soon before it gets worse. "
    )
    self.typeWriter()
    print("""
          1) Head further into the fields 
          2) Head back 
          3)Take shelter in the small nearby barn  """)
    userInput = ""
    while userInput not in self.options:
      userInput = input("What do you want to do?  (1/2/3) ").lower().replace(" ", "")
      if userInput == "1":
        self.clear_screen()
        art.gameOver()
        print(
          "‘I have to find Donkey’ he says to himself, shielding his face from the sharp rainfall, slowly walking into the field. Morning arose and an old farmer arrived in his field, looking and inspecting any harm that may have accrued, but to his shock it was not his field that was harmed it was instead the Ogre as the storm had tragically taken his life. "
        )
      elif userInput == "2":
        theWeather.weatherNow()
        self.forkedRoad()
      elif userInput == "3":
        self.clear_screen()
        # displays ASCII art of the donkey found
        art.donkeyEnding()
        self.typeThis = (
          "The Ogre quickly runs towards the nearby barn as it begins to hail, entering the barn and quickly closing the door he breaths a sign of relief ‘I'm so sorry Donkey’. But then ‘HEE-HAAW’, the Ogre turns around and to his surprise as he yells ‘Donkey’, as donkey too has also taken shelter in the old farmer’s barn. There both the Ogre and the donkey wait out through stormy night, opening the barn doors in the morning of a new day, ‘what a beautiful clear blue day, shall we go home Donkey’, ‘HEE-HAAW’ "
        )
        self.typeWriter() 
        # additional dialog displayed due to the following conidtion 
        if self.foundHorse == True:
          self.typeThis = (
            "Later that day the Ogre was able to find and return the horse back to its owner."
            )
          self.typeWriter()
      else:
        print("Please enter a valid option (1/2/3).")
     
   

  def clear_screen(self):       # Method to clear the terminal screen
    subprocess.run("cls", shell=True)   # Using the clear feature, this feature only work windows operating system
    return
  
  def typeWriter(self):           # Method to allow the each character in the string to be typed one at a time in a certain speed
    for char in self.typeThis:
      print(char, sep='', end='', flush=True)
      sleep(0.05)   # speed of each character should be diplayed
    else:
      return
  
  
class gameWeather:   # Class holding all the methods for the weather
  def weatherNow(self):      # List of cascading methods, after passing through these methods it returns to the method calling it 
    self.windy()
    self.rainy()
    self.night()
    self.game_over()
    return
  
  def windy(self):
    game.clear_screen()
    if (time.time()-game.start_time) > game.wind_time and game.wind == False:
      art.wind()
      print("The wind begins to howl, louder and louder, blowing leaves and moving branches, the storm is drawing near. ")
      time.sleep(2)
      game.wind = True    # To make sure this method does not repeat itself, only appearing once
    return

  def rainy(self):
    game.clear_screen()
    if (time.time()-game.start_time) > game.rain_time and game.rain == False:
      art.rain()
      print("A small water droplet falls nearby, then another and another as it slowly gets darker, ‘oh no’ the Ogre says with worry ‘the storm is here’ ")
      time.sleep(2)
      game.rain = True
    return

  def night(self):   
    game.clear_screen()
    if (time.time()-game.start_time) > game.night_time and game.storm == False:
      art.storm()
      print("Night approaches, as the wind begins to raw and the rain pours ferociously, the concerned Ogre wonders to himself if he should find his pet donkey or if he should get away from this storm.  ")
      time.sleep(2)
      game.storm = True
    return

  def game_over(self):    # When the timer has reached its limit, if the Ogre is still outside this ending will appear
    game.clear_screen()
    if (time.time()-game.start_time) > game.time_limit and game.storm == True:
       art.gameOver()
       print("The Ogre tried to battle through the storm to find his pet donkey, not only failing to find donkey but also finding shelter for himself and tragically succumb to the storm. ")
       exit()
    

class gameArt: # Class holding all the AASCI art
  def game_title(self):
    print("""

        *************************************************************************************
        *                                                                                   *
        *                   ______ ____  _____  ______  _____ _______                       *
        *                  |  ____/ __ \|  __ \|  ____|/ ____|__   __|                      *
        *                  | |__ | |  | | |__) | |__  | (___    | |                         *
        *                  |  __|| |  | |  _  /|  __|  \___ \   | |                         *
        *                  | |   | |__| | | \ \| |____ ____) |  | |                         *
        *                  |_|    \____/|_|  \_\______|_____/   |_|                         *
        *                   ______ _____  _____ ______ _   _ _____   _____                  *
        *                  |  ____|  __ \|_   _|  ____| \ | |  __ \ / ____|                 *
        *                  | |__  | |__) | | | | |__  |  \| | |  | | (___                   *
        *                  |  __| |  _  /  | | |  __| | . ` | |  | |\___ \                  *
        *                  | |    | | \ \ _| |_| |____| |\  | |__| |____) |                 *
        *                  |_|    |_|  \_\_____|______|_| \_|_____/|_____/                  *
        *                                                                                   *
        *                                                                                   *
        *************************************************************************************

    """)
    return
  def ogreHome(self):
    print("""
                  
                                                -=[ Orges House ]=- 

                                                    _____________
                                          |==|____/_____________\___
                                          |==/UUUU|.---.---.---.|UUU\:
                                          |=/UUUUU||___|___|___||UUUU\:
                                          |/UUUUUU||___|___|___||UUUUU\:
                                          /UUUUUUU"============="UUUUUU\:
                                          /UUUUUUUUUUUUUUUUUUUUUUUUUUUUUU\:
                                          |______________________________|
                                          |== ===  = =  ==   ==  == =  ==|-
                                          |= _______________ =  _______ =|=
                                          |=|:::|:::|:::|:::| =|.-----.|=|-
                                          |=|^^^|^^^|^^^|^^^|1O|||_|_|||=|=
                                          |=|---+---+---+---| =|||_|_|||=|=
                                          |=|   |   |   |   | =||     ||=|-
                                          |=|___|___|___|___| =|| == O||=|=
                                          |=                  "||     ||=|-
                                          |= =.o%&hjw8@&o.== ==||_____||=|-
                                              |__________|     |/_____\|
    """)    
    return


  def road(self):
    print("""
                                                -=[ Choose Path ]=- 
                                  ___                          
                                _/XXX |
                  _             /XXXXXX \                                    __
                  X\__    __   /X XXXX XX\                          _       /XX\__      ___
                      \__/  \_/__       \ \                       _/X\__   /XX XXX\____/XXX
                    \  ___   \/  \_      \ \               __   _/      \_/  _/  -   __  -  \__/
                  ___/   \__/   \ \__      \_           /  \_//  _ _ \  \     __  /  \____//
                  /  __    \  /     \ \_   _//_\___     _/    //           \___/  \/     __/
                  __/_______\________\__\_/________\_ _/_____/_____________/_______\____/_______

                                  <Fields|                           |Woods>
                                      | |                              | |
                        ______________| |______________________________| |________________


                            
                        _____________________                    _________________________
                                            /                   /
                                           /                   /
                                          /                   /
                                         /                   /
                                                (you)
                            
    """)
    return
  def farmField(self):
    print("""
                                                -=[ Open Field ]=- 


                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    .,__,.-=~'`^`'~=-., __,.-=~'`^  \/      ..--  .   .  .._   \/ .  .\/ '~=-
                    \/         \/ \/    \/     / -                     \.   --._
                      .   \/    _..\/-...--..         '~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^                   
                            .  \/                                                            .
                    . \/             .   \/     ~-.__ - - - -              - - - - -__.-~  . \/
                      __...--..__..__       .  \/   ~~~--..____- - - - -____..--~~~    \/_..--..
                    \/  .   .    \/     \/    __..--... \/      ~~~~~~~~~     \/ . \/  .
                    _
                    ~`'^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^

    """)
    return
  def farmHouse(self):
    print("""
                                              -=[ Farm House ]=- 
                      
                                                                                  ,-- 
                  --.                                                            -'    
                    \                                                            ,---  
                    --.                                                         /      
                        ).          __,-O<                                      ,--      
                  ----'  `.          `\)                                  ,--(      ,;:. 
                          _)          /                                  (_        .:;:;.
                          |          |                                             :;';.;:'
                        _|_        _|_                                             ';\||' 
                  ______/=\|\______/=\|\_____                                          :|  
                  '-'-'-[=]/'-'-'-[=]/'-'-'-/'.=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=
                  -'-'-'-'-'-'-'-'-'-'-'-'-/   '.                                       |
                  '-'-'-'-'-'-'-'-'-'-'-'-/    .-'                                    |/|
                  -'-'-'-'-'-'-'-'-'-'-'-/ _.-'.-:                                 |/|/ 
                        ___       ___   |' _.'\ :|--|--|- .;_;'   ';_;. --|--|--|/|/   
                  |]   [|_|_|]   [|_|_|] | |\ | \:|--|--| ; ;'       '; ; -|--|--|/     
                  |]   [|_|_|]   [|_|_|] | | \|--'                     
                  _______________________| |.-'         
                                      |/|                         
                      ____.-".      |/|/               
                    ;( ,__.)/='   |/|/                           
                    ; |/  \|    |/|/               
                      \    |  |/|/                      
                        `   `|/|/             
                  |--|--|--|/|/               
                  |--|--|--|/                   
      
    """)
    return
  def theWoods(self):
    print("""
                                              -=[ the Woods ]=- 
                    
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⢠⢤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠔⠒⠒⠲⠎⠀⠀⢹⡃⢀⣀⠀⠑⠃⠀⠈⢀⠔⠒⢢⠀⠀⠀⡖⠉⠉⠉⠒⢤⡀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠚⠙⠒⠒⠒⠤⡎⠀⠀⠀⠀⢀⣠⣴⣦⠀⠈⠘⣦⠑⠢⡀⠀⢰⠁⠀⠀⠀⠑⠰⠋⠁⠀⠀⠀⠀⠀⠈⢦⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⢰⠃⠀⣀⣀⡠⣞⣉⡀⡜⡟⣷⢟⠟⡀⣀⡸⠀⡎⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣻⠀⠀⠀⠀
                    ⢰⠂⠀⠀⠀⠀⠀⠀⠀⣗⠀⠀⢀⣀⣀⣀⣀⣀⣓⡞⢽⡚⣑⣛⡇⢸⣷⠓⢻⣟⡿⠻⣝⢢⠀⢇⣀⡀⠀⠀⠀⢈⠗⠒⢶⣶⣶⡾⠋⠉⠀⠀⠀⠀⠀
                    ⠈⠉⠀⠀⠀⠀⠀⢀⠀⠈⠒⠊⠻⣷⣿⣚⡽⠃⠉⠀⠀⠙⠿⣌⠳⣼⡇⠀⣸⣟⡑⢄⠘⢸⢀⣾⠾⠥⣀⠤⠖⠁⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢀⠀⠀
                    ⠀⠀⠀⢰⢆⠀⢀⠏⡇⠀⡀⠀⠀⠀⣿⠉⠀⠀⠀⠀⠀⠀⠀⠈⢧⣸⡇⢐⡟⠀⠙⢎⢣⣿⣾⡷⠊⠉⠙⠢⠀⠀⠀⠀⠀⢸⡇⢀⠀⠀⠀⠀⠈⠣⡀
                    ⠀⠀⠀⠘⡌⢣⣸⠀⣧⢺⢃⡤⢶⠆⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣟⠋⢀⠔⣒⣚⡋⠉⣡⠔⠋⠉⢰⡤⣇⠀⠀⠀⠀⢸⡇⡇⠀⠀⠀⠀⠀⠀⠸
                    ⠀⠀⠀⠀⠑⢄⢹⡆⠁⠛⣁⠔⠁⠀⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⣿⢠⡷⠋⠁⠀⠈⣿⡇⠀⠀⠀⠈⡇⠉⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠑⣦⡔⠋⠁⠀⠀⠀⣿⠀⠀⢠⡀⢰⣼⡇⠀⡀⠀⠀⣿⠀⠁⠀⠀⠀⠀⣿⣷⠀⠀⠀⠀⡇⠀⠀⢴⣤⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⢰⣿⡇⠀⠀⠀⠀⠀⣿⡀⠀⢨⣧⡿⠋⠀⠘⠛⠀⠀⣿⠀⠀⢀⠀⠀⠀⣿⣿⠀⠀⠀⠀⢲⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⢸⡧⡄⠀⠹⣇⡆⠀⠀⠀⠀⠀⣿⠀⢰⣏⠀⣿⣸⣿⣿⠀⠀⠀⠀⣼⠀⠀⠰⠗⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⢸⡇⣷⣛⣦⣿⢀⠈⠑⠀⢠⡆⣿⠐⢠⣟⠁⢸⠸⣿⣿⢱⣤⢀⠀⣼⠀⠀⢀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⢀⠀⠀⠀⢸⡇⠘⠫⣟⡇⠊⣣⠘⠛⣾⡆⢿⠀⠙⣿⢀⣘⡃⣿⣿⡏⠉⠒⠂⡿⠀⠰⣾⡄⠀⢸⡟⣽⣀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠸⣿⡇⠀⠘⣾⠀⠀⢸⡇⢸⣇⡙⠣⠀⣹⣇⠀⠈⠧⢀⣀⣀⡏⣸⣿⣇⢹⣿⡇⢴⣴⣄⣀⡀⢰⣿⡇⠀⢸⣇⢿⡿⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠓⠁⠈⠻⢷⠾⠦⠤⠬⣅⣹⣿⣖⣶⣲⣈⡥⠤⠶⡖⠛⠒⠛⠁⠉⠛⠮⠐⢛⡓⠒⢛⠚⠒⠒⠒⠛⣚⣫⡼⠿⠿⣯⠛⠤⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⡉⠉⠁⠀⠀⠘⠓⠀⠀⠀⠀⠀⣀⣞⡿⡉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀
    
    """)
    return
 
  def gameOver(self):
    print("""

                                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                                    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
                                    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
                                    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
                                    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
                                    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
                                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                                    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
                                    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
                                    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
                                    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
                                    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
                                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                                    ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
                                    ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
                                    ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
                                    ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
                                    ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
                                    ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
                                    ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
                                    ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
                                    ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
                                    ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
                                    ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
                                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼

             
    """)
    return
  def donkeyEnding(self):
    print("""
                   

                                                                  _
                              ,,;;;,,,,   _.---.._                \`-._
                            `';;;;;;;;;;;;;,      `'.           .--'-._';,
                                ,;;';;''/            `;_       `';;;;'    `'.
                                        |  .            '-._   ,;;:'   /  '<a'.
                                        |  ;        \       '.,;;'     |       .
                                        \  \       |                  ;._. ,-'`.
                                      /`'-`;.`'._   /                  /   `-.\_/
                                      ; .-._ .-'  .'                  |
                                    / /    '\ .-'`.                _/
                                _.-' /       \ \   '-._            /
                                (_/_.'     __.) /       `;--.._/   (
                                          (_/__/          \   `,   |
                                                            \ \  `\ |
                                                            \ \   \ |
                                                              \_\   \ |
                                                              )-`\  \_|
                                                              `==`   )-`|
                                                                      `==`
                                                            
                                          -=[ Found Donkey ]=- 
             
    """)
    return

  def wind(self):
    print("""
                          
                 
                                      ___
                                    (`    ).                   _ _          
                                  (       ).               .:(`    )`.       
                      )           _(         '`.           :(   .       )      
                              .=(`(       .   )     .--   `.  (      ) )      
                            ((    (..__.:'-'   .+(       )   ` _`     ) )                 
                      `.     `(       ) )       (    .     )     (    )  ._   
                        )      ` __.:'   )     (   (       ))     `-'.-(`    ) 
                      )  )  ( )       --'       `- __.')        :(           )) 
                      .-'  (_.'          .')                    `(         )  ))
                                        (_  )                     ` __.:'        
                                                  _.--..-._.-a:f--.
                      --..,___.--,--'`
                                        .--..-._.-a:f--.
                                                            ,,..._.--..-._.-a:


                                       -=[ Windy Conditions ]=- 

            
    """)
    return
  def rain(self):
    print("""

                              
                              .-.                                    ,-.
                            .-(    )-.                           ,-(   )-.
                          (      __) )-.                   ,-(_      __)
                        `-( _         __)                 ( (_    )   __)-'
                              `(____)-',                     `-(____)-'
                            |     |  |                           |   |   |
                              |    |       |                   |       |        
                            |  |     |                            |
                                      |                      _|       |
                                |                           >')
                                        _   /              (\)\         (W)
                                        =') //               = \     -. `|'
                                        ))////)             = ,-      \(| ,-
                                        ( (///))           ( |/  _______\|/____
                          ~~~~~~~~~~~~~~~`~~~~'~~~~~~~~~~~~~\|,-'::::::::::::::
                                      _                 ,----':::::::::::::::::
                                  {><_'c   _      _.--':MJP:::::::::::::::::::
                          __,'`----._,-. {><_'c  _-':::::::::::::::::::::::::::
                          :.:.:.:.:.:.:.\_    ,-'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:
                          .:.:.:.:.:.:.:.:`--'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.
                          .....................................................

                                          -=[ Raining ]=- 
                             
    """)
    return
  def storm(self):
    print("""          
                        
                                          ______
                                  ,--,,--'       '-------,_
                                  (        ---              ',
                                  .'          '-     ,__  ,_)
                                (      "          _     __)
                                  '--`"----.~.-`--` `---`
                                          / /   \   \   \  \ 
                                         / /  \   \    \    \      
                                        / /   \     \  \   \       
                                        //       \  \  \    \   
                                       //    \  \  \      \  \   
                             *        //  \   \         \     \     
                            **       /    \     \    \  \     \         
                          __##_______     \      \    \       \                
                        /   ##        \**      \   \      \    \         
                       /              \***               \     \  X   
                      /                \****     \         \     XXX      
                     /_________________***    \     \           XXXXX
                        |             |****               \    XXXXXXX   X
                        | ___         |            \       \  XXXXXXXX  XXX
                        | | |   ___   |      \               XXXXXXXXXXXXXXX
                        | |_|   | |  ****             \           X   XXXXXXX
                    *********** | | *******      \         \      X      X
                  **********************************************************

                                      -=[ Heavy Storm ]=- 
    """)
    return


theWeather = gameWeather() # Assigning all the classes to a variable
art = gameArt()
game = AdventureGame()    
game.intro() # Starting the game / Starting or activating this method