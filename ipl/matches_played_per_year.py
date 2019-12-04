from matplotlib import pyplot as plt


def plot_number_of_matches_played_per_year(matches_per_year):
    match_data = matches_per_year
    years = list(match_data.keys())
    matches = list(match_data.values())
    plt.bar(years, matches)
    plt.title('Matches Played Per Year')

    plt.show()


def compute_number_of_matches_played_per_year(matches):
    matches_played_per_year = {}
    for match in matches:
        matches_played_per_year[match['season']] = \
            matches_played_per_year.get(match['season'], 0) + 1
    ordered_matches_played_per_year = {}
    for year in sorted(matches_played_per_year.keys()):
        ordered_matches_played_per_year[year] = matches_played_per_year[year]

    return ordered_matches_played_per_year


def compute_and_plot_number_of_matches_played_per_year(matches):

    matches_played_per_year = \
        compute_number_of_matches_played_per_year(matches)

    plot_number_of_matches_played_per_year(matches_played_per_year)
