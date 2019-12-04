def compute_years_and_matches(matches):

    ids_yearwise = {}
    for id_data in matches:
        if id_data['season'] not in ids_yearwise:
            ids_yearwise[id_data['season']] = {}

    matches_of_each_season = {}
    for year in sorted(ids_yearwise.keys()):
        matches_of_each_season[year] = {}

    return matches_of_each_season


def compute_scores_of_each_batsman(matches_per_season, deliveries_data):

    for ball in deliveries_data:
        for year in matches_per_season:
            if ball['match_id'] in matches_per_season[str(year)]:
                if ball['batsman'] not in \
                     matches_per_season[str(year)][ball['match_id']]:
                    matches_per_season[str(year)][ball['match_id']][
                        ball['batsman']] = int(ball['batsman_runs'])
                elif ball['batsman'] in \
                        matches_per_season[str(year)][ball['match_id']]:
                    matches_per_season[str(year)][ball['match_id']][
                        ball['batsman']] += int(ball['batsman_runs'])

    return matches_per_season


def calculate_centuries_of_all_seasons(matches, scores_year_wise,
                                       centuries_of_each_season):
    for match in matches:
        for runs in scores_year_wise[match['season']][match['id']]:
            if int(scores_year_wise[match['season']][match['id']][runs]) >=\
                 100:
                if runs not in centuries_of_each_season[match['season']]:
                    centuries_of_each_season[match['season']][runs] = 1
                else:
                    centuries_of_each_season[match['season']][runs] += 1

    return centuries_of_each_season


def ids_of_each_year(years_and_ids, matches):

    for match in matches:
        years_and_ids[match['season']][match['id']] = {}

    return years_and_ids


def compute_centuries_data_over_all_years(matches, deliveries):

    matches_played_per_season = compute_years_and_matches(matches)
    centuries_of_each_season = compute_years_and_matches(matches)

    season_and_ids = ids_of_each_year(matches_played_per_season, matches)

    scores_of_all_seasons = compute_scores_of_each_batsman(season_and_ids,
                                                           deliveries)
    centuries_per_year =\
        calculate_centuries_of_all_seasons(matches, scores_of_all_seasons,
                                           centuries_of_each_season)

    print(centuries_per_year)
