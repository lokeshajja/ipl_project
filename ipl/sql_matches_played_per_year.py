from sql_config import sql
from matches_played_per_year import plot_number_of_matches_played_per_year
import logging
logging.basicConfig(filename='ipl_project.log', level=logging.INFO,
                    format='%(asctime)s:%(module)s:%(funcName)s:%(message)s')


def compute_number_of_matches_per_year():

    query = '''select season,count(season)
    from matches
    group by season'''

    number_of_matches_per_year = sql(query)

    plot_data_for_number_of_matches = {}

    for year, matches in number_of_matches_per_year:
        plot_data_for_number_of_matches[str(year)] = matches

    plot_number_of_matches_played_per_year(
        plot_data_for_number_of_matches
    )
    logging.info(plot_data_for_number_of_matches)
