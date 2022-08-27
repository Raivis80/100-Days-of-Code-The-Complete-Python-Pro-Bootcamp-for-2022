# Make Treasure Island simple game

#          __________
#         /\____;;___\
#        | /         /
#        `. ())oo() .
#         |\(%()*^^()^\
#        %| |-%-------|
#       % \ | %  ))   |
#       %  \|%________|
# ejm97  %%%%

#        {}           {}
#          \  _---_  /
#           \/     \/
#            |() ()|
#             \ + /
# ejm 96     / HHH  \
#           /  \_/   \
#         {}          {}
#                            ___________
#                 ___________)%{}%%%%%%/
#                /{}%%%%%%%%/%%/%%%%%%/
#               /%%\% _---_/ \/%%%%%%/
#              /%%%%\/    /()|%%%%%%/
#             /%%%%%|()  /+ /%%%%%%/
#            /%%%%%%%\ +/HH%%\%%%%/
#           /%%%%%%/%HH/_/%%%\%%%/
#  ejm97   /%%%%%%/%%\/%%%%%%{}%/
#         /%%%%%{}%%%/
#        /
#       /
#      /
#     /
#    /

print("Welcome to the Treasure Island Treasure Hunter!\n Your mission is to find the treasure.")

direction = input("you are at crossroads, do you want to go left or right? ").upper()

if direction== 'LEFT':
    print("You have chosen to go left.")
    boat = input("You have found a small boat, do you want to go in? Y or N ").upper()
    if boat== 'Y':
        print("You have chosen to go in boat sank .\n Game over.")
        exit()
    elif boat== 'N':
        doors = input("You found house with 3 dors one red, green and blue. which one do you choose? ").upper()
        if doors== 'RED':
            print("You have chosen red door.\n Game over.")
            exit()
        elif doors== 'GREEN':
            print("You have chosen green door.\n Game over.")
            exit()
        elif doors== 'BLUE':
            
            print("You have chosen blue door.\n *********You win!!**********")
            exit()
        else:
            print("Invalid input.")
    else:
        print("Invalid input.")
elif direction== 'RIGHT':
    print("You have chosen to go right.\n Game over.")
    exit()
else:
    print("Invalid input.")


        