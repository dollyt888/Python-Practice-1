print ('''

  .,               _ '    `_      _______                               ( )
--+-[---------.---(-)-----(@)----|-------|--.-----|-------------.-------|~--
  | ]         |   |~      |~ (@) _          |     |          |} |       |
--+-[-----|---+---|-------|--|--(@)---------+-----|----------|}-+---|---|---
  |/      |   |   |       |  |  |~  (@)  _  | |  _| ..       |  |   |   |
--Y-------|---+---|-------|--|--|---|---(@)-+-|>( )------|---|--+---|-------
 /|_     _|   |           `=_|  |   |   |~  |    ~       |>(@)  |  _|
|-@-)---(@)---+-----------------|---|---|---+-------------------+-(@)-------
\_|/     ~    |                     |   |   |                   |  ~
--+-----------"-------------------------|---"-------------------"-----------
  |
._}    --jw''')
race = 0
city_of_origin = 0
occupation = 0
player_name = 0

player_name = input("Welcome to One More Word, a fanciful, thrilling choose-your-own adventure game! Please type in your player name. ")
race = input ("Hi " + player_name + "! Let's begin. Choose your character's race: 1. Robot 2. Cyborg 3. Human 4. Mage. Simply type any number 1-4 to choose.")
if race == "1" :
    race = "robot"
elif race == "2" : 
    race = "cyborg"
elif race == "3" : 
    race = "human"
elif race == "4" : 
    race = "mage"

city_of_origin = input("Next, choose your city of origin: \n1. The Ruined City 2. Paradise 3. Crossover Bridge 4. The Overcity\nSimply type the number of your choice, from 1-4.\n")

if city_of_origin == "1" : 
    city_of_origin = "The Ruined City"
    occupation = input("The Ruined City is a tangled web of metal and glass left over from a massive earthquake. Choose your occupation: 1. Cleaner 2. Runner 3. Smuggler")
elif city_of_origin == "2" and race == "mage": 
    city_of_origin = "Paradise"
    occupation = input("Paradise is the most vibrant and rich city in the world. Wealthy socialites, celebrities, and politicians make their homes behind its glittering walls. Choose your occupation: 1. Spy 2. Politician 3. Singer")
elif city_of_origin == "2" and race != "mage": 
    city_of_origin = "Paradise"
    occupation = input("Paradise is the most vibrant and rich city in the world. Wealthy socialites, celebrities, and politicians make their homes behind its glittering walls. Choose your occupation: 1. Spy 2. Politician ")