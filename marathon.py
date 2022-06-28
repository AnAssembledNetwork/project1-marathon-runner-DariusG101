# """
#  *****************************************************************************
#    FILE:        marathon.py
#
#    AUTHOR:      {Your Name Here}
#
#    ASSIGNMENT: A marathon calculator to determine if a U.S. participant can
#    run in the Tokyo Marathon. 
#
#    DATE:         {Today's Date}
#
#    DESCRIPTION: {Your Description Here}
#
#  *****************************************************************************

# $1 = 134.28¥
JAPANESE_YEN = 134.28

# 1 mi = 1609.34 meters
METERS_IN_MILE = 1609.34 

# Insert Code Below
def fitness():

    # This ignores our code so that we do not get an error Remove 'pass' when you want to start testing code.
    
    print("Tokyo Marathon Qualifier")
  name = input("what is your name: ")
  mile_every_minute = float(input("How many miles can you run in 10 minutes?"))
  money_saved = input("How much U.S.$ do you have saved for the marathon? ")
  money_saved = float(money_saved)
  yen_saved = money_saved * JAPENESE_YEN
  km_in_one_minute_pace = mile_every_minute/10 * METERS_IN_MILE / 1000
  space_index = name.find(" ")
  name = name[space_index +1:]
  print(f"Dear {name}, you have a pace of {km_in_one_minute_pace:,.2f} km/min.\nAdditionally, you only have       {yen_saved:,.2f}¥ to spend ")

    

# This invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    fitness()