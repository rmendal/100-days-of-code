"""Write a function called friends_teams that takes a list of friends, a team_size int (default=2) and order_does_matter
boolean (default False). Return all possible teams. Hint: if order matters (order_does_matter=True) the number of teams
would be greater. See the tests for more details. Enjoy :)"""

def friends_teams():













####### TESTS #######################################################################################################
"""friends = 'Bob Dante Julian Martin'.split()


def test_friends_teams():
    combos = list(friends_teams(friends, team_size=2, order_does_matter=False))
    assert len(combos) == 6
    assert ('Bob', 'Julian') in combos
    assert ('Julian', 'Bob') not in combos

    combos = list(friends_teams(friends, team_size=2, order_does_matter=True))
    assert len(combos) == 12
    assert ('Bob', 'Julian') in combos
    assert ('Julian', 'Bob') in combos

    combos = list(friends_teams(friends, team_size=3, order_does_matter=False))
    assert len(combos) == 4
    assert ('Bob', 'Julian', 'Martin') in combos
    assert ('Martin', 'Julian', 'Bob') not in combos

    combos = list(friends_teams(friends, team_size=3, order_does_matter=True))
    assert len(combos) == 24
    assert ('Bob', 'Julian', 'Martin') in combos
    assert ('Martin', 'Julian', 'Bob') in combos"""