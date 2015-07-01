from django.db import models
import gviz_api

# Create your models here.
from .src.table_parser import Table_Parser as tp
from .src.table_utils import convert_timepoint_to_date as convert
from .src.filling_na import fill_na_in_table as fill_na

class Graph(models.Model):
	timevar = models.CharField(max_length = 100)
	subjectID = models.CharField(max_length = 100)


	def get_graph(self , timevar_type , na_complition):

		## Table uploading and selection
		table = tp("static/media/table_upload.txt")

		if timevar_type == '0':

			timevar , new_table = convert(table.get_table().copy(), self.timevar)
			table.set_table(new_table)
			table.set_timevar(timevar)
			table.set_IdVar(self.subjectID)

		else:
			table.set_timevar(self.timevar)
			table.set_IdVar(self.subjectID)

		## Filling NA based on the argument send from
		## the web page form
		table.set_table(fill_na(table.get_table() , na_complition))

		## Table Google Vis data
		description = table.generate_description()
		data = table.generate_data()

		### Generation of the table as google formats
		data_table = gviz_api.DataTable(description)
		data_table.LoadData(data)

		## to take the correct order of the table
		order_col = table.get_ordered_columns()

		## Producing JScode to add on the html
		code = data_table.ToJSCode("jscode_data" , columns_order=order_col)


		templ = '''
		<html>
  <script src="https://www.google.com/jsapi" type="text/javascript"></script>
  <script>
    google.load('visualization', '1', {packages:['table','motionchart']});

    google.setOnLoadCallback(drawTable);
    function drawTable() {
      %(code)s

      var jscode_table = new google.visualization.Table(document.getElementById('table_div_jscode'));
      var jscode_motion = new google.visualization.MotionChart(document.getElementById('motion_div_jscode'));

      jscode_table.draw(jscode_data, {showRowNumber: true} );
      jscode_motion.draw(jscode_data, {width: 600, height:600} );

    }
  </script>
  <body>

  	<H1 style=' text-align: center'>Motion created using ToJSCode</H1>
    <div id="motion_div_jscode" style=' text-align: center'></div><br><br>
    <H1>Table created using ToJSCode</H1>
    <div id="table_div_jscode"></div>


  </body>
</html>
		'''
		document = open("temporal_series/templates/ts/graph.html" , "w")
		document.write(templ % {'code' : code})
		document.close()
