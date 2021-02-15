'''
Tournament Winner from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def tournamentWinner(competitions, results):
    '''    
    There's an algorithms tournament taking place in which 
    teams of programmers compete against each other to solve 
    algorithmic problems as fast as possible. Teams compete 
    in a round robin, where each team faces off against all other
    teams. Only two teams compete against each other at a time, 
    and for eachc ompetition, one team is designated the home team, 
    while the other team is the away team. In each competition there's 
    always one winner and one loser; there are no ties. A team receives 
    3 points if it wins and 0 points if it loses. The winner of the 
    tournament is the team that receives the most amount of points. 
        
    Given an array of pairs representing the teams that have competed 
    against each other and an array containing the results of each 
    competition, write a function that returns the winner of the 
    tournament. The input arrays are named 'competitions' and 'results'
    respectively. The competitions array has elements in the form of
    [homeTeam, awayTeam], where each team is a string of at most 30
    characters representing the name of the team. The results array
    contains information about the winner of each corresponding competition
    in the competition array. Specifically, results[i] denotes the winner
    of competitions[i], where a 1 in the result array means that the home
    team in the corresponding competition won and a 0 means that the away team
    won.

    It's guaranteed that exactly one team will win the tournament and that
    each team will copete against all other reams exactly once. It's also 
    guaranteed that the tournament will always have at least two teams.
    '''

    teams = {}
    # O(n) time where n is num of competitions | O(k) space where k is num of teams
    for battle, result in zip(competitions, results):
        # O(1) time (only 2 teams fights) 
        for team in battle:
            if team not in teams:
                teams[team] = 0
        if result == 0:
            teams[battle[1]] += 3
        if result == 1:
            teams[battle[0]] += 3

    return max(teams, key=teams.get)

    # Total complexity
    # Time O(n) | space O(k)