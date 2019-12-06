from sql_config import sql
from number_of_matches_won_by_each import \
    plot_matches_won_by_each_team


import logging
logging.basicConfig(filename='ipl_project.log', level=logging.INFO,
                    format='%(asctime)s:%(module)s:%(funcName)s:%(message)s')


def compute_and_plot_number_of_matches_per_season_of_all_teams():
    query = ''' select season,winner,count(winner)
                from matches
                group by season,winner'''

    number_of_matches_won_per_season_per_team = sql(query)
    matches_won_per_season = {}
    for year, team, wins in \
            number_of_matches_won_per_season_per_team:
        year = str(year)
        matches_won_per_season[year] = \
            matches_won_per_season.get(year, {})
        matches_won_per_season[year][team] = wins

    logging.info(matches_won_per_season)
    plot_matches_won_by_each_team(matches_won_per_season)
