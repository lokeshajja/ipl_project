from matplotlib import pyplot as plt
from collections import OrderedDict


def plot_number_of_matches_per_year(matches_per_year):

    plot_data = matches_per_year
    years = list(plot_data.keys())
    matches = list(plot_data.values())
    plt.bar(years, matches)
    plt.title('Matches Played Per Year')
    plt.show()


def compute_number_of_matches_per_year(matches):
    match_per_year = OrderedDict()
    for match in matches:
        match_per_year[match['season']] = \
            match_per_year.get(match['season'], 0) + 1
    matches_per_year = {}
    for year in sorted(match_per_year.keys()):
        matches_per_year[year] = match_per_year[year]
    print('matches played per year are ')
    print(matches_per_year)
    return matches_per_year


def compute_and_plot_matches_played_per_year(matches):

    matches_per_year = compute_number_of_matches_per_year(matches)
    plot_number_of_matches_per_year(matches_per_year)
