from matches_played_per_year import compute_and_plot_matches_played_per_year
from number_of_matches_won_by_each import compute_and_plot_of_win_data
from extras_of_year_2016 import extra_runs_conceived_by_each_team_in_2016
from extras_of_year_2016 import plot_of_extra_runs_given_by_each_team_in_2016
from most_econ_bowlers_2015 import\
    compute_and_plot_most_economic_bowlers_of_2015
from max_centuries import compute_centuries_data_over_all_years
from file_extraction import extract_file


def main():
    matches = extract_file('matches.csv')
    deliveries = extract_file('deliveries.csv')
    compute_and_plot_matches_played_per_year(matches)

    compute_and_plot_of_win_data(matches)

    extras_given_by_each_team = \
        extra_runs_conceived_by_each_team_in_2016(matches, deliveries)
    plot_of_extra_runs_given_by_each_team_in_2016(extras_given_by_each_team)

    compute_and_plot_most_economic_bowlers_of_2015(matches, deliveries)

    compute_centuries_data_over_all_years(matches, deliveries)


if __name__ == "__main__":
    main()
