from pandas import read_table 
from datetime import date
import os


class Table_Parser():

	def __init__(self , table_fp ):

		self.timevar = None
		self.idVar = None
		self.table_fp = table_fp

		if os.path.exists(table_fp):
			self.table = read_table(table_fp)
		else: 
			raise IOError("Table does not exist! \n"+os.getcwd())


	def set_timevar(self , timevar):
		self.timevar = timevar

	def set_IdVar(self , idVar):
		self.idVar = idVar

	def set_table(self,table):
		self.table = table

	def get_table(self):
		return self.table

	def get_ordered_columns(self):
		result = []
		t = list(self.table.keys())
		t.remove(self.timevar)
		t.remove(self.idVar)
		result = [self.idVar , self.timevar]
		result.extend(t)

		return result
		

	def generate_description(self):
		results = {}
		k_v = {}
		
		data_types = {
		str : 'string',
		int : 'number',
		float : 'number',
		bool : 'boolean'
		}

		for key in self.table.keys():
			tp = type(self.table[key][0]).mro()[-2]
			k_v[key] = tp


		for k,v in k_v.iteritems():
			if k == self.timevar : 
				results[k] = ('date' , k)
			elif v == basestring or k == self.idVar:
				results[k] = ( 'string' , k)
			else:
				results[k] = (data_types[v], k)

		return results	

	def generate_data(self):
		a = self.table.to_dict()
		result = []
		for i in range(len(a.values()[0])):
			line = {}

			for k,v in a.iteritems():

				if k == self.timevar:
					t = v[i].split("-")
					##print "> %(t1)s , %(t2)s , %(t3)s \n" % {'t1': t[0], 't2' : t[1] , 't3': t[2]}
					
					### this so far assumes the timevar is formated for date and not as 
					### timepoint ... should be done in next revision of application. 
					line[k] = date(int(t[0]),int(t[1]) ,int(t[2]))
					
				else: 
					line[k] = v[i]
			result.append(line)
		return result


def DebugOutput():

	table_fp = "R.adiv_taxa_pc.txt" 
	table = Table_Parser(table_fp)
	table.set_timevar('timepoint_date')
	table.set_IdVar('subjectID')
	schema = table.generate_description()

	templ = "ITEM : %(k)s | ( %(t1)s , %(t2)s ) "
	print "Generating Schema \n=================================================================="
	for k,v in schema.iteritems():
		print templ % {'k': k   , 't1' : v[0] , 't2': v[1] }

	print "==================================================================\nGenerating Data "
	print "\n=================================================================="
	data = table.generate_data()
	for i in data:
		print i

	print "\n=================================================================="


if __name__ == "__main__":
	DebugOutput()


	