"""Write a function called friends_teams that takes a list of friends, a team_size int (default=2) and order_does_matter
boolean (default False). Return all possible teams. Hint: if order matters (order_does_matter=True) the number of teams
would be greater. See the tests for more details. Enjoy :)"""

from itertools import combinations, permutations

friends = 'Bob Dante Julian Martin'.split()

def friends_teams(friends, team_size = 2, order_does_matter = False):
    if order_does_matter == False:
        combo_false = list(combinations(friends, team_size)) # Order doesn't matter in combinations
        return combo_false
    else:
        combo_true = list(permutations(friends, team_size)) # Order does matter in permutations
        return combo_true
