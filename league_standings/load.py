import psycopg2


# What is test and the '1' needs to be in a for loop

def load(teams):
	print("Loading onto db...")
	conn = psycopg2.connect(host="localhost",database="fantasystats",user="rodell",password="password")
	cur = conn.cursor()

	#teams[0]'s value is None
	for team in teams[1:]:
		for week in range(1, len(team.stats)+1):
			statement = (
				'INSERT INTO ' + 'graphs_stats' + ' (' 
				+ 'team_id, week_id,' 
				+ 'field_goal_percentage, free_throw_percentage, three_points_made, points, '
				+ 'rebounds, assists, steals, blocks, turnovers' + ') VALUES (' 
				+ "{},{},{},{},{},{},{},{},{},{},{}".format(
					str(team.id)
					,str(week),team.stats[str(week)]['FG%']
					,team.stats[str(week)]['FT%']
					,str(team.stats[str(week)]['3PTM'])
					,str(team.stats[str(week)]['PTS'])
					,str(team.stats[str(week)]['REB'])
					,str(team.stats[str(week)]['AST'])
					,str(team.stats[str(week)]['ST'])
					,str(team.stats[str(week)]['BLK'])
					,str(team.stats[str(week)]['TO'])) +')'
				)
			cur.execute(statement)
			print(statement)

	conn.commit()
	conn.close()

 
