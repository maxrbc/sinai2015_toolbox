from django.shortcuts import render

# Create your views here.

from .models import Graph
from .forms import SubmitTable
from .src.table_utils import table_loader as tl

def index(request):
	return render(request , 'ts/index.html' , {})


def submit(request):
	# printing a form based on the data present
	# if not data in request make a blank form to fill
	form  = SubmitTable(request.POST , request.FILES)

	if form.is_valid():
		# the file needs to be handle seprt.
		# for this the is a function module
		tl(request.FILES['table_fd'])

		#This request loops the form so that it stays
		#The same while loading the info. BY the reload
		#time it doesnt sends you to a new form but prints
		#the last one present.

		return do_graph(request , form)

	return render(request , 'ts/ts.html', {'form':form})




def do_graph(request , form):

	graph = Graph.objects.get_or_create(
		timevar = form.cleaned_data['table_timevar'] ,
		subjectID = form.cleaned_data['table_idVar'] )

	print form.cleaned_data['na_complition'] , "\n"

	graph[0].get_graph(form.cleaned_data['timepoint_type'] ,
						form.cleaned_data['na_complition'])
	return render(request , 'ts/graph.html' , {})
