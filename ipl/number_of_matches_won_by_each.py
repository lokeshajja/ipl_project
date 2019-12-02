import os
import sys
from file_extraction import extract_file
from matplotlib import pyplot as plt






def plot_of_win_data(win_data):

    win_teams={}
    for year in win_data.values():
        for team in year.keys():
            if team not in win_teams:
                win_teams[team]=[]
                
    year_list=[]
    for year,win_data in win_data.items():
        year_list.append(year)
        team_list=win_teams.keys()
        team_list=list(team_list)
        for team,wins in win_data.items():
            team_list.remove(team)
            (win_teams[team]).append(wins)
        
        for team in team_list:
            (win_teams[team]).append(0)
    
    win_teams.popitem()
    all_team_names=[]
    wins_per_year=[]
    for team_name,team_wins in win_teams.items():
        all_team_names.append(team_name)
        wins_per_year.append(team_wins)

    plt.bar(year_list,wins_per_year[0])
    for serial in range(1,len(all_team_names)):
        plt.bar(year_list,wins_per_year[serial],bottom=wins_per_year[serial-1])

    plt.xlabel('Years')
    plt.ylabel('Number of Wins Per Year')
    plt.title('Wins per year per team')
    plt.show()





def matches_won_by_each(matches):
    
    winner_data={}   
    for match_data in matches:
        if match_data['winner']=='Rising Pune Supergiant':
            match_data['winner']='Rising Pune Supergiants'

        if match_data['season'] not in winner_data:
            winner_data[match_data['season']]={}

        winner_data[match_data['season']][match_data['winner']]=(winner_data[match_data['season']]).get(match_data['winner'],0)+1


    return winner_data





def compute_and_plot_of_win_data():
    matches=extract_file('matches.csv')
    win_data=matches_won_by_each(matches)
    plot_of_win_data(win_data)
    
 
