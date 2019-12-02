matches = [
  {
    'id': 1,
    'season': 2008
  },
  {
    'id': 2,
    'season': 2008
  },
  {
    'id': 3,
    'season': 2009
  }
]
deliveries = [
  {
    'match_id': 1,
    'bowler': 'bowler-1',
    'player_dismissed': 'batsman-1'
  },
  {
    'match_id': 1,
    'bowler': 'bowler-3',
    'player_dismissed': 'sdfdf'
  },
  {
    'match_id': 1,
    'bowler': 'bowler-1',
    'player_dismissed': 'batsman-2'
  },
  {
    'match_id': 1,
    'bowler': 'bowler-1',
    'player_dismissed': 'batsman-3'
  },
  {
    'match_id': 1,
    'bowler': 'bowler-1',
    'player_dismissed': ''
  },
  {
    'match_id': 2,
    'bowler': 'bowler-1',
    'player_dismissed': 'batsman-1'
  },
  {
    'match_id': 2,
    'bowler': 'bowler-2',
    'player_dismissed': ''
  },
  {
    'match_id': 3,
    'bowler': 'bowler-3',
    'player_dismissed': 'batsman-2'
  },
  {
    'match_id': 3,
    'bowler': 'bowler-3',
    'player_dismissed': 'batsman-3'
  },
  {
    'match_id': 3,
    'bowler': 'bowler-2',
    'player_dismissed': ''
  }
]
ids_and_years={}
output={}

for match in matches:
    if match['season'] not in ids_and_years:
        ids_and_years[match['season']]=[]
        output[match['season']]={}
        ids_and_years[match['season']].append(match['id'])
    else:
        ids_and_years[match['season']].append(match['id'])
    
print(ids_and_years)
print(output)


for ball in deliveries:
    if ball['player_dismissed'] != '':
        for year in ids_and_years:
            if ball['match_id'] in ids_and_years[year]:
                if ball['bowler'] not in output[year]:
                    output[year][ball['bowler']] =1
                else:
                    output[year][ball['bowler']]+=1
print(output)



                
                
                


        






