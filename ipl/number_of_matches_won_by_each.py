from matplotlib import pyplot as plt


def plot_matches_won_by_each_team(winners_data):

    winning_teams = {}
    for year in winners_data.values():
        for team in year.keys():
            if team not in winning_teams:
                winning_teams[team] = []
    seasons = []
    for year, winners_data in winners_data.items():
        seasons.append(year)
        team_list = winning_teams.keys()
        team_list = list(team_list)
        for team, wins in winners_data.items():
            team_list.remove(team)
            (winning_teams[team]).append(wins)
        for team in team_list:
            (winning_teams[team]).append(0)
    winning_teams.popitem()
    all_team_names = []
    wins_per_year = []
    for team_name, team_wins in winning_teams.items():
        all_team_names.append(team_name)
        wins_per_year.append(team_wins)

    plt.bar(seasons, wins_per_year[0], label=all_team_names[0], width=0.5)

    for serial in range(1, len(all_team_names)):
        plt.bar(seasons, wins_per_year[serial], width=0.5,
                bottom=wins_per_year[serial-1], label=all_team_names[serial])
    plt.xlabel('Years')
    plt.ylabel('Number of Wins Per Year')
    plt.title('Matches Won By Each Team Over All Seasons')
    plt.show()


def matches_won_by_each_team_over_all_seasons(matches):

    number_of_wins_per_season = {}
    for match in matches:
        if match['winner'] == 'Rising Pune Supergiant':
            match['winner'] = 'Rising Pune Supergiants'

        if match['season'] not in number_of_wins_per_season:
            number_of_wins_per_season[match['season']] = {}

        number_of_wins_per_season[match['season']][match['winner']] = \
            (number_of_wins_per_season[match['season']]).get(match['winner'],
                                                             0)+1
    return number_of_wins_per_season


def compute_and_plot_matches_won_by_each_team_over_all_seasons(matches):
    matches_won_by_each_team = \
        matches_won_by_each_team_over_all_seasons(matches)
    plot_matches_won_by_each_team(matches_won_by_each_team)
