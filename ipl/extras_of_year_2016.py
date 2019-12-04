from matplotlib import pyplot as plt


def year_and_id_data(matches, season):
    matches_of_2016 = []
    for match in matches:
        if match['season'] == season:
            matches_of_2016.append(match['id'])

    return matches_of_2016


def compute_extra_runs(matches_of_2016, deliveries_data):

    ids = matches_of_2016
    teams_and_extra_runs = {}

    for ball in deliveries_data:
        if ball['match_id'] in ids:
            teams_and_extra_runs[ball['bowling_team']] = \
                teams_and_extra_runs.get(ball['bowling_team'], 0) +\
                int(ball['extra_runs'])

    return teams_and_extra_runs


def plot_extra_runs_given_by_each_team(extra_runs_data):

    x = extra_runs_data.keys()
    y = extra_runs_data.values()
    plt.bar(x, y)
    plt.title('Extra Runs Given By Each Team In 2016')
    plt.xlabel('Teams')
    plt.ylabel('Extra Runs')
    plt.setp(plt.gca().get_xticklabels(), rotation=30,
             horizontalalignment='right')
    plt.show()


def compute_and_plot_extra_runs_given_by_each_team(matches, deliveries_data):
    season = '2016'
    matches_of_2016 = year_and_id_data(matches, season)
    extra_runs_data = compute_extra_runs(matches_of_2016, deliveries_data)
    plot_extra_runs_given_by_each_team(extra_runs_data)
