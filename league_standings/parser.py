import xml.etree.ElementTree as ET
from pprint import pprint

class Parser():
	def __init__(self):
		#The XML outputs the stat categories as the numbers shown below. The stats_mapping routes the corresponding number to the intended stat category name
		self.stats_mapping  = {
			'5':'FG%',
			'8':'FT%',
			'10':'3PTM',
			'12':'PTS',
			'15':'REB',
			'16':'AST',
			'17':'ST',
			'18':'BLK',
			'19':'TO',
		}
		self.xmlns = '{http://fantasysports.yahooapis.com/fantasy/v2/base.rng}'

	def parse_stats(self, response, team, week):
		#xmlns strings are prepended to each tag name in the xml file
		root = ET.fromstring(response.text)
		if self._same_team_id(root, team):
			self._update_name(root, team)
			if self._same_week(root, week):
				stat_category, stat_values = [], []
				self._parse_stats(root, stat_category, stat_values)
				stats_dict = self._create_stats_dictionary(stat_category,stat_values)		
				print("Before save team stats func")
				pprint(stats_dict)
				self._save_team_stats(team, week, stats_dict)
				print("After save team stats func")
				pprint(stats_dict)

			else: print('Weeks do not match. Cannot parse Team ID #{}'.format(team.id))

		else: print('Team IDs do not match. Cannot parse Team ID #{}'.format(team.id))

	def _parse_stats(self, root, stat_category, stats):
		# stats_container contains the stats category and stats value from the xml hence the name container
		stats_container = (root.find(self.xmlns+'team')
								.find(self.xmlns+'team_stats')
								.find(self.xmlns+'stats')
								.findall(self.xmlns+'stat'))
		# Run method to extract the stat category
		self._parse_stat_categories(stats_container, stat_category)
		# Run another method to extract the stat value
		self._parse_stat_values(stats_container,stats)

	def _parse_stat_categories(self, stats_container, stat_category):
		for container in stats_container:
			category = container.find(self.xmlns+'stat_id').text
			stat_category.append(category)

	def _parse_stat_values(self, stats_container, stats):
		for container in stats_container:
			value = container.find(self.xmlns+'value').text
			#Convert stat values from string to floats. Some of the resulting floats must be converted to int's
			try:
				stats.append(float(value))
			# Will get a Value Error for intermediary stats like "32/100". We won't need those types of stats anyways so we can fill in with a dummy value
			except ValueError:
				stats.append(0)

	def _same_team_id(self, root, team):
		xml_team_id = (root.find(self.xmlns+'team')
						.find(self.xmlns+'team_id')
						.text)
		xml_team_id = int(xml_team_id)
		return xml_team_id == team.id

	def _same_week(self, root, week):
		xml_week = (root.find(self.xmlns+'team')
						.find(self.xmlns+'team_stats')
						.find(self.xmlns+'week')
						.text)
		return xml_week == str(week)

	# Converts the resulting stat category and stat values list and makes them key value pairs respectively
	def _create_stats_dictionary(self,stat_category,stat_values):
		return dict(zip(stat_category, stat_values))

	# MAKE SURE THE STATS ARE CONVERTED TO FLOAT OR INTS
	def _save_team_stats(self, team, week, stats_dict):
		for category_num in stats_dict:
			if category_num in self.stats_mapping:
				category = self.stats_mapping[category_num]
				self._insert_stat(team, week, category, category_num, stats_dict)

	# Create a dictionary of stats for each week
	def _create_week_entry(self, team, week):
		team.stats[str(week)] = {}

	def _parse_name(self, root):
		return (root.find(self.xmlns + 'team')
				.find(self.xmlns + 'name')
				.text)

	def _update_name(self,root, team):
		if team.name: return
		name = self._parse_name(root)
		team.name = name

	def _insert_stat(self, team, week, category, category_num, stats_dict):
		if not str(week) in team.stats:
			self._create_week_entry(team, week)
		
		self._clean_stat(category_num, stats_dict)
		team.stats[str(week)][category] = stats_dict[category_num]

	# If the stat category is not a FG% or a FT% then the data should be an int not a float
	def _clean_stat(self, category_num, stats_dict):
		if category_num != '5' and category_num != '8':
			stats_dict[category_num] = int(stats_dict[category_num])

	def _parse_week_calendar(self, response):
		pass


def main():
	pass

if __name__ == "__main__":
	main()