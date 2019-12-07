from sql_matches_played_per_year import \
    compute_and_plot_number_of_matches_per_year
from sql_number_of_matches_won import \
    compute_and_plot_number_of_matches_per_season_of_all_teams
from sql_extras_of_2016 import compue_and_plot_extras_of_2016


def main():

    compute_and_plot_number_of_matches_per_year()

    compute_and_plot_number_of_matches_per_season_of_all_teams()

    compue_and_plot_extras_of_2016()


if __name__ == "__main__":
    main()
