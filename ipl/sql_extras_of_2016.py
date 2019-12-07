from sql_config import sql

from extras_of_year_2016 import \
    plot_extra_runs_given_by_each_team

import logging
logging.basicConfig(filename='ipl_project.log', level=logging.INFO,
                    format='%(asctime)s:%(module)s:%(funcName)s:%(message)s')


def compue_and_plot_extras_of_2016():
    query = ''' select bowling_team, sum(extra_runs)
                from matches m
                join deliveries d
                on m.id = d.match_id
                where m.season = 2016
                group by bowling_team'''
    extras_of_2016 = dict(sql(query))
    logging.info(extras_of_2016)
    plot_extra_runs_given_by_each_team(extras_of_2016)
