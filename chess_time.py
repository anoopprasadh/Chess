
# A class named chess has been defined
class Chess():

    n = input("Enter the size of the chess board!") # n is the input used to enter the board dimension
    print("The size of the chess board is "+n+" x "+ n)
    n = int(n)                                             #being converted to integer
    bp_x = input("Enter the x coordinate of Black pawn :") #bp_x is the black pawn's x coordinate
    bp_x = int(bp_x)
    bp_y = input("Enter the y coordinate of Black pawn :") #bp_y is the black pawn's x coordinate
    bp_y = int(bp_y)
    if bp_x > n or bp_y > n:                                #checking if the coordinates are greater than that of the given dimension
        raise Exception('The Value of X and Y coordinates must be less than n')
    else:
        pass

    wp_x = input("Enter the x coordinate of white pawn :") # similarly for white pawn's position
    wp_x = int(wp_x)
    wp_y = input("Enter the y coordinate of white pawn :")
    wp_y = int(wp_y)
    if wp_x > n or wp_y > n:
        raise Exception('The Value of X and Y coordinates must be less than n')
    else:
        pass

    # bp_x = input("Enter the x coordinate of Black pawn :")
    bp = [bp_x, bp_y]               #to print them in coordinates took them in a list
    wp = [wp_x, wp_y]


    # print("Black pawn is in " + "(" + bp_x + "," + bp_y + ")")
    # print("White pawn is in " + "(" + wp_x + "," + wp_y + ")")

    print("Black pawn is in : ")
    print(bp)
    print("White pawn is in : ")
    print(wp)


    if abs(wp[0]-bp[0]) == abs(wp[1]-bp[1]):                         # if the pawns have same values or their difference in their
        print("The least number of steps for white pawn to reach black pawn is :");print(abs(wp[0]-bp[0]))#values are same then the number of steos needed is equal to the difference between them
    else:                                       #when they are not equal
        if bp_x >= bp_y:                        # we need to determine the highest number of the x and y coordinates in both coordinates
            if bp_x >= wp_x and bp_x >= wp_y:   #after that which ever is highest, it should be subtracted with the same coordinate of the other pair.
                steps = abs(bp_x - wp_x)        #example lets say there is x1 , y1 and x2 and y2 . lets say x1 is greatest of all it should be subtracted with x2
            elif bp_x >= wp_x and bp_x <= wp_y: #to arrive at the least number of steps considering the fact that the pawns can move in diagonally.
                steps = abs(wp_y - bp_y)
            elif bp_x <= wp_x and bp_x >= wp_y:
                steps = abs(wp_x - bp_x)
            elif bp_x <= wp_x and bp_x <= wp_y:
                if wp_x >= wp_y:
                    steps = abs(wp_x - bp_x)
                else:
                    steps= abs(wp_y - bp_y)
        else:
            if bp_y >= wp_x and bp_y >= wp_y:
                steps = abs(bp_y - wp_y)
            elif bp_y >= wp_x and bp_y <= wp_y:
                steps = abs(wp_y - bp_y)
            elif bp_y <= wp_x and bp_y >= wp_y:
                steps = abs(wp_x - bp_x)
            elif bp_y <= wp_x and bp_y <= wp_y:
                if wp_x >= wp_y:
                    steps = abs(wp_x - bp_x)
                else:
                    steps= abs(wp_y - bp_y)


        print("The least number of steps for white pawn to reach black pawn is :")
        print(steps)
