import xlsxwriter

"""
	This script assumes that it's building the spreadsheet from scratch. It won't be capable of "appending" to an already existing spreadsheet yet

"""


class Excel():
	def __init__(self, file_name, teams, start_week, end_week):
		self.file_name = file_name
		self.teams = teams
		self.start_week = start_week
		self.end_week = end_week
		self.header = (
			'Team',
			'FG%',
			'FT%',
			'3PTM',
			'PTS',
			'REB',
			'AST',
			'ST',
			'BLK',
			'TO',
		)

	def write_to_spreadsheet(self):
		workbook = xlsxwriter.Workbook(self.file_name)
		for week in range(self.start_week, self.end_week + 1):
			self._fill_in_worksheet(workbook, self.teams, week)

	def _fill_in_worksheet(self, workbook, teams, week):
		worksheet_name = 'Week ' + str(week)
		worksheet = workbook.add_worksheet(worksheet_name)
		percent_format = workbook.add_format({'num_format': "0.0%"})
		worksheet.write_row('A1', self.header)
		worksheet.autofilter('A1:J1')
		self._fill_in_stats(worksheet, percent_format, teams, week)

	def _fill_in_stats(self, worksheet, cell_format, teams, week):
		for row,team in enumerate(teams[1:], 1):
			# Fill in Team Name first
			worksheet.write_string(row, 0, team.name)
			# Now fill in stats
			for column, stat_category in enumerate(self.header[1:], 1):
				if stat_category == 'FG%' or stat_category == 'FT%':
					worksheet.write_number(row, column, team.stats[str(week)][stat_category], cell_format)
				else:
					worksheet.write_number(row, column, team.stats[str(week)][stat_category])

def main():
	start_week = 1
	end_week = 2

	from team import Team
	teams = [None] * 3
	teams[1] = Team(1)
	teams[2] = Team(2)

	teams[1].name = 'The Clinic'
	teams[1].stats['1'] = {
		'FG%':.41,
		'FT%': .72,
		'3PTM': 30,
		'PTS': 742,
		'REB': 121,
		'AST': 90,
		'ST': 27,
		'BLK': 14,
		'TO': 81,
	}

	teams[1].stats['2'] = {
		'FG%':.536,
		'FT%': .81,
		'3PTM': 3,
		'PTS': 902,
		'REB': 111,
		'AST': 101,
		'ST': 31,
		'BLK': 41,
		'TO': 18,
	}


	teams[2].name = 'Bob The Builder'
	teams[2].stats['1'] = {
		'FG%':.2252,
		'FT%': .9019,
		'3PTM': 25,
		'PTS': 1000,
		'REB': 384,
		'AST': 78,
		'ST': 45,
		'BLK': 51,
		'TO': 97,
	}

	teams[2].stats['2'] = {
		'FG%':.6589,
		'FT%': .57,
		'3PTM': 99,
		'PTS': 323,
		'REB': 1123,
		'AST': 154,
		'ST': 13,
		'BLK': 66,
		'TO': 8,
	}


	test = Excel('test.xlsx', teams, start_week, end_week)
	test.write_to_spreadsheet()


if __name__ == "__main__":
	main()