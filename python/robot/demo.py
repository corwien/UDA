def is_move_valid_special(loc, act):
    """
    Judge wether the robot can take action act
    at location loc.

    Keyword arguments:
    loc -- tuple, robots current location
    act -- string, robots meant action
    """

    #TODO 8
    if act == 'u':
            if loc[0] - 1 >= 0:
                return True
            else:
                return False
    elif act == 'd':
         if loc[0] + 1 <= rows - 1:
             return True
         else:
             return False
    elif act == 'l':
         if loc[1] - 1 >= 0:
             return True
         else:
             return False
    elif act == 'r':
         if loc[1] + 1 <= columns -1:
             return True
         else:
             return False
    else:
         return False

print(is_move_valid_special((4,0), 'd'))
