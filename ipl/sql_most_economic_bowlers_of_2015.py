from sql_config import sql

from most_econ_bowlers_2015 import \
    plot_top_economy_data

import logging
logging.basicConfig(filename='ipl_project.log', level=logging.INFO,
                    format='%(asctime)s:%(module)s:%(funcName)s:%(message)s')


def sql_most_economic_bowlers_2015():
    query = '''select bowler,
                sum(total_runs)/(count(bowler)/6)as economy
                from matches m
                join deliveries d
                on m.id = d.match_id
                where m.season = 2015
                group by bowler
                order by economy
                limit 10'''

    most_economic_bowlers = sql(query)
    plot_top_economy_data(most_economic_bowlers)
    logging.info(most_economic_bowlers)
