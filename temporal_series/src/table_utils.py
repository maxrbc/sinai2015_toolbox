from datetime import date , timedelta

# Table loader only works for saving right now a txt
# still need to be added version for the biom table

def table_loader(FILE):
	with open("static/media/table_upload.txt" , "wb+") as destination:
		for chunk in FILE.chunks():
			destination.write(chunk)

def generate_cluster_index(dates):
	result = []
	for i in dates:
		if not i in result:
			result.append(i)
	return result


	#timedelta parses the descrite value to a date
	# and is added to the 1,1,1 date which default
	# date for conversion
def parse_timepoint_to_date(timepoints):
	d = date(1,1,1)
	result = []
	for i in timepoints:
		result.append(str(d + timedelta(i)))
	return result


	#makes a new column but with the
	#timepoint variable parsed to a new
	#variable with the date like value
def convert_timepoint_to_date(table , timepoint):
	parsed = parse_timepoint_to_date(table[timepoint])
	print parsed
	name = timepoint + "_to_date"
	table[name] = parsed
	return name,table

# this expects you passing a panda table
# as the internal is desing for it
def generate_discrete_timepoint(table , timestamp):
	indexer = generate_cluster_index(table[timestamp])
	result = []
	for i in table[timestamp]:
		result.append(indexer.index(i))
	name = timestamp+"_descrete"
	table[name] = result
	return name,table
