"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    decision = None

    if power_pellet_active == True and touching_ghost == True:
        decision = True
    else:
        decision = False
    
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    Parameters:
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Can a ghost be eaten?

    """

    return decision

def score(touching_power_pellet, touching_dot):
    decision = None
    if touching_power_pellet == True or touching_dot == True:
        decision = True
    else:
        decision = False
        
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    Parameters:
        touching_power_pellet (bool): Is the player touching a power pellet?
        touching_dot (bool): Is the player touching a dot?

    Returns:
        bool: Has the player scored or not?

    """
    return decision


def lose(power_pellet_active, touching_ghost):
    decision = None
    if power_pellet_active == False and touching_ghost == True:
        decision = True
    else:
        decision = False
        
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    Parameters:
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Has the player lost the game?
    """
    return decision

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    decision = None
    if has_eaten_all_dots == True and lose(power_pellet_active, touching_ghost) == False:
        decision = True
    else:
        decision = False
        
    """Trigger the victory event when all dots have been eaten.

    Parameters:
        has_eaten_all_dots (bool): Has the player "eaten" all the dots?
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Has the player won the game?
    """
    return decision
