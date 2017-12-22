import os
import collections
import smart_open
import random

import Config

"""
Load basic ingredients and compounds data from Nature Scientific Report(Ahn, 2011)

"""
class DataLoader:
	def load_drugResponse(self, path):
		print path
		with open(path, 'r') as f:
			for line_id, line in enumerate(f):
				print line_id, line

if __name__ == '__main__':
	dl = DataLoader()
	#ingredients = dl.load_ingredients(Config.path_ingr_info)
	#compounds = dl.load_compounds(Config.path_comp_info)
	#relations = dl.load_relations(Config.path_ingr_comp)

	file = "meropenem.csv"
	cuisines = dl.load_drugResponse(Config.path_perturbation + file)