import os
import sys
from file_extraction import extract_file



from file_extraction import extract_file
from matplotlib import pyplot as plt


'''
1. make a list of years
2. make a list of wins of each team per year
3.plot the graph
'''



def plot_of_win_data1(win_data):
    #print(win_data)
    win_teams={}
    for years1 in win_data.values():
        for teams in years1.keys():
            if teams not in win_teams:
                win_teams[teams]=[]

    year_list=[]
    for year2,win_data1 in win_data.items():
        year_list.append(year2)
        temp_list=win_teams.keys()
        temp_list=list(temp_list)
        for team11,wins in win_data1.items():
            #print(team11,wins)
            temp_list.remove(team11)
            (win_teams[team11]).append(wins)
        
        #print(win_teams)
        #print(temp_list)
        for team_x in temp_list:
            (win_teams[team_x]).append(0)




    win_teams.popitem()
    #print(win_teams)


    all_team_names=[]
    wins_per_year=[]
    for team_name,team_wins in win_teams.items():
        all_team_names.append(team_name)
        wins_per_year.append(team_wins)

    #print(all_team_names)
    #print(wins_per_year)



    plt.bar(year_list,wins_per_year[0])

    for num in range(1,len(all_team_names)):
        plt.bar(year_list,wins_per_year[num],bottom=wins_per_year[num-1])



    plt.xlabel('Years')
    plt.ylabel('Number of Wins Per Year')
    plt.title('Wins per year per team')
    plt.show()


def matches_won_by_each(matches):
    winner_data={}
    for match_data in matches:
        if match_data['season'] not in winner_data:
            winner_data[match_data['season']]={}
            
    #print(winner_data)
    
    for match_data1 in matches:
        if match_data1['winner']=='Rising Pune Supergiant':
            match_data1['winner']='Rising Pune Supergiants'

        if match_data1['winner']  in winner_data[match_data1['season']]:
            winner_data[match_data1['season']][match_data1['winner']]+=1

        elif match_data1['winner'] not  in winner_data[match_data1['season']]:
            winner_data[match_data1['season']][match_data1['winner']]=1

    #print(winner_data)       
    return winner_data
    


def compute_and_plot_of_win_data():
    matches=extract_file('matches.csv')
    win_data=matches_won_by_each(matches)
    plot_of_win_data1(win_data)
 
