from sql_config import sql

import logging
logging.basicConfig(filename='ipl_project.log', level=logging.INFO,
                    format='%(asctime)s:%(module)s:%(funcName)s:%(message)s')


def centuries_by_season():
    query = '''select season,batsman, count(batsman)
                from (select season,batsman
                from matches m
                join deliveries d
                on m.id = d.match_id
                group by season, match_id, batsman
                having sum(batsman_runs) >= 100) as c
                group by season,batsman
                order by season'''
    centuries_by_year = sql(query)
    grouped_centuries_per_year = {}
    for year, batsman, century in centuries_by_year:

        grouped_centuries_per_year[year] = \
            grouped_centuries_per_year.get(year, {})
        grouped_centuries_per_year[year][batsman] =\
            century
    logging.info(grouped_centuries_per_year)
