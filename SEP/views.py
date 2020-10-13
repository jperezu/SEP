from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Client, Event, RequestEvent, Task, RequestRecruitment, RequestBudget
from .forms import event_form, task_form
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):
	# Number of visits to this view, as counted in the session variable.
	num_visits = request.session.get('num_visits', 0)
	#request.session['num_visits'] = num_visits+1

	# Render the HTML template index.html with the data in the context variable.
	if (request.user.groups.filter(name='CS Manager').exists()):
		return get_pending_events(request)
	elif (request.user.groups.filter(name='Financial Manager').exists()):	
		return get_cs_accepted_events(request)
	elif (request.user.groups.filter(name='HR Manager').exists()):	
		return recruitment_list(request)
	elif (request.user.groups.filter(name='Administration Manager').exists()):
		return get_fin_accepted_events(request)
	elif (request.user.groups.filter(name='Production Manager').exists() or
		request.user.groups.filter(name='Services Manager').exists()):
		return show_events(request)
	elif (request.user.groups.filter(name='Chef').exists() or
		request.user.groups.filter(name='Computer').exists() or
		request.user.groups.filter(name='Decoration').exists() or
		request.user.groups.filter(name='Graphic Design').exists() or
		request.user.groups.filter(name='Music').exists() or
		request.user.groups.filter(name='Photography').exists() or
		request.user.groups.filter(name='Waiter').exists()):
		return get_tasks(request)
	else:
		return render(
			request,
			'index.html'
		)
	#return HttpResponse("You're at the SEP index.")
# Create your views here.

def login_view(request):
	user = request.POST.get("user_name")
	password = request.POST.get("user_password")

	log_user = authenticate(username=user,
	 	password=password,)
	if log_user :
		login(request, log_user)
	else :
		storage = messages.get_messages(request)
		storage.used = True
		messages.info(request, "Your username and password didn't match. Please try again.")
	return HttpResponseRedirect('/')

def event_request(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		new_req = RequestEvent(
			client = request.POST.get('client'),
			event_type = request.POST.get('event_type'),
			description = request.POST.get('description'),
			attendees = request.POST.get('attendees'),
			expected_budget = request.POST.get('expected_budget'),
			from_date = request.POST.get('from_date'),
			to_date = request.POST.get('to_date'),
			decorations = request.POST.get('decorations'),
			film_and_photos = request.POST.get('film_and_photos'),
			posters_art = request.POST.get('posters_art'),
			food_drinks = request.POST.get('food_drinks'),
			music = request.POST.get('music'),
			computers = request.POST.get('computers'),
			other = request.POST.get('other'),
			status = "created",
		)

		new_req.save()
		# redirect to a new URL:
		return HttpResponseRedirect('/')

def get_pending_events(request):
	event_requests = RequestEvent.objects.filter(status = "created")
	
	accepted_events = RequestEvent.objects.filter(status = "accepted")

	rejected_events = RequestEvent.objects.filter(status = "rejected")

	return render(
		request,
		'index.html',
		context={'event_requests': event_requests, 'accepted_events' : accepted_events, 'rejected_events' : rejected_events},
	)
		
def pending_event_cs_accept(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		request_id = request.POST.get('request_pk')
		accepted_request = RequestEvent.objects.get(pk=request_id)
		accepted_request.status = "cs_accepted"
		accepted_request.save()
	return get_pending_events(request)

def pending_event_reject(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		request_id = request.POST.get('request_pk')
		rejected_request = RequestEvent.objects.get(pk=request_id)
		rejected_request.status = "rejected"
		rejected_request.save()

		#rejected_request.delete()

	return get_pending_events(request)

def remove_req_event(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		request_id = request.POST.get('request_pk')
		rejected_request = RequestEvent.objects.get(pk=request_id)
		rejected_request.delete()

	return get_pending_events(request)

def get_cs_accepted_events(request):
	event_cs_requests = RequestEvent.objects.filter(status = "cs_accepted")
	b_request = RequestBudget.objects.all();
	return render(
		request,
		'index.html',
		context={'event_cs_requests': event_cs_requests, 'b_request' : b_request},
	)
def recruitment_list(request):
	r_request = RequestRecruitment.objects.all();
	return render(
		request,
		'index.html',
		context={'r_request' : r_request},
	)

def pending_event_financial_accept(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		request_id = request.POST.get('request_pk')
		accepted_request = RequestEvent.objects.get(pk=request_id)
		accepted_request.status = "financial_accepted"
		accepted_request.save()
	return get_cs_accepted_events(request)
def get_fin_accepted_events(request):
	event_fin_requests = RequestEvent.objects.filter(status = "financial_accepted")
	
	return render(
		request,
		'index.html',
		context={'event_fin_requests': event_fin_requests},
	)
def pending_event_admin_accept(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		request_id = request.POST.get('request_pk')
		accepted_request = RequestEvent.objects.get(pk=request_id)
		accepted_request.status = "accepted"
		accepted_request.save()
	return get_fin_accepted_events(request)

def create_event(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		request_id = request.POST.get('request_pk')
		accepted_request = RequestEvent.objects.get(pk=request_id)
		# process the data in form.cleaned_data as required
		old_client = Client.objects.get(client_name = accepted_request.client)

		if (old_client) :
			client_id = old_client
		else :
			client_id = Client(client_name = accepted_request.client, organized_events = 0)
			client_id.save()

		new_event = Event(
			client = client_id,
			event_type = accepted_request.event_type,
			description = accepted_request.description,
			attendees = accepted_request.attendees,
			expected_budget = accepted_request.expected_budget,
			from_date = accepted_request.from_date,
			to_date = accepted_request.to_date,
			decorations = accepted_request.decorations,
			film_and_photos = accepted_request.film_and_photos,
			posters_art = accepted_request.posters_art,
			food_drinks = accepted_request.food_drinks,
			music = accepted_request.music,
			computers = accepted_request.computers,
			other = accepted_request.other,
			status = "pending"
		)

		new_event.save()
		remove_req_event(request)

	return get_pending_events(request)


def show_events(request):

	all_events = Event.objects.exclude(status="finished").exclude(status="archived")
	for event in all_events:
		update_event_status(event.pk)

	event_pending = Event.objects.exclude(status="finished").exclude(status="archived")
	event_finished = Event.objects.filter(status="finished")
	b_request = RequestBudget.objects.all();
	r_request = RequestRecruitment.objects.all();

	return render(
		request,
		'index.html',
		context={'event_pending': event_pending, 'event_finished': event_finished,
		 'b_request' : b_request, 'r_request' : r_request},
		)

def update_event_status(event_id):

	event = Event.objects.get(pk=event_id)	
	tasks = Task.objects.filter(project=event)
	finish = False
	all_finish = True
	event_status = "pending"
	for sample in tasks:
		if sample.status == "blocked" :
			event_status = sample.status
			finish = False
			all_finish = False
			break
		elif sample.status == "in progress" :
			event_status = sample.status
			all_finish = False
			finish = False
		elif sample.status == "assigned"  and event_status != 'in progress' :
			event_status = "open"
			all_finish = False
			finish = False
		elif sample.status == "finished" and all_finish :
			finish = True

	if finish:
		event.status = "finished"
		client_id = event.client
		client_id.organized_events = client_id.organized_events + 1
		client_id.save()
		for sample in tasks:
			sample.delete()
	else:
		event.status = event_status
	event.save()
def archive_event(request):
	event_id = request.GET.get('event_pk')
	event = Event.objects.get(pk=event_id)
	event.status = "archived"
	event.save()
	return show_events(request)

def assign_tasks(request):

	users = User.objects.all()

	if request.method == 'POST':
		assigned_user = User.objects.all().filter(pk = request.POST.get('assigned'))[0];
		event_id = request.POST.get('event_pk')
		event = Event.objects.get(pk=event_id)
		duplicated = Task.objects.all().filter(project = event).filter(assigner = request.user).filter(description = request.POST.get('description')).filter(assigned = assigned_user)
		
		if (not duplicated) :
			new_task = Task(
				project = event,
				assigner = request.user,
				description = request.POST.get('description'),
				assigned = assigned_user,
				priority = request.POST.get('priority'),
				status = "assigned"
			)
			new_task.save()
			# redirect to a new URL:
		tasks = Task.objects.all().filter(project=event)
		update_event_status(event_id)
		return render(request, 'taskassign.html',context={'event': event, 'users' : users, 'tasks':tasks})

		# if a GET (or any other method) we'll create a blank form
	else:	
		event_id = request.GET.get('event_pk')
		task_id = request.GET.get('task_pk', None)

		event = Event.objects.get(pk=event_id)	
		if task_id:
			try:
				task = Task.objects.get(pk=task_id)
				task.delete()
			except Task.DoesNotExist:
				task = None

		tasks = Task.objects.all().filter(project=event)
		update_event_status(event_id)
		return render(
		request,
		'taskassign.html',
		context={'event': event, 'users' : users, 'tasks':tasks},
		)

def remove_task(request):
	if request.method == 'GET':
		task_id = request.GET.get('task_pk')
		task = Task.objects.get(pk=task_id)
		task.delete()

	return assign_tasks(request)

def get_tasks(request):

	tasks = Task.objects.all().filter(assigned = request.user)

	return render(
		request,
		'index.html',
		context={'tasks': tasks},
		)
def set_task_status(request):
	tasks = Task.objects.all().filter(assigned = request.user)

	task_id = request.POST.get('task_pk')
	task_status = request.POST.get('task_status')

	task = Task.objects.get(pk=task_id)

	task.status = task_status
	task.save()

	return render(
		request,
		'index.html',
		context={'tasks': tasks},
		)

def get_history(request):
	archived_events = Event.objects.filter(status = "archived")
	archived_clients = Client.objects.filter(organized_events__gte=1)

	return render(
		request,
		'recordhistory.html',
		context={'archived_events': archived_events, 'archived_clients' : archived_clients},
	)
def add_request(request):
	request_type = request.POST.get('request_type')
	event_id = request.POST.get('event_pk')
	event = Event.objects.get(pk=event_id)

	if (request_type == "budg"):
		duplicated = RequestBudget.objects.all().filter(project = event).filter(department = request.POST.get('department'))
		if (not duplicated) :
			req = RequestBudget(
				project = event,
				department = request.POST.get('department'),
				budget = request.POST.get('budget'),
				description = request.POST.get('description'),
				status = "requested"
			)
			req.save()
	elif(request_type == "recruit"):
		duplicated = RequestRecruitment.objects.all().filter(type = request.POST.get('contract')).filter(department = request.POST.get('department')).filter(job = request.POST.get('job'))
		if (not duplicated) :
			req = RequestRecruitment(
				type = request.POST.get('contract'),
				department = request.POST.get('department'),
				experience = request.POST.get('experience'),
				job = request.POST.get('job'),
				description = request.POST.get('description'),
				status = "requested"
			)
			req.save()
	else :
		storage = messages.get_messages(request)
		storage.used = True
		messages.info(request, "Error creating request")
		#HttpResponseRedirect("/")
	return show_events(request)

def update_budrequest(request):
	req_id = request.POST.get('request_pk')
	request_status = request.POST.get('request_status')
	requested_budget = request.POST.get('requested_budget')

	bud_req = RequestBudget.objects.get(pk=req_id)

	bud_req.status = request_status
	bud_req.save()

	if (bud_req.status == "agreed") :
		event = Event.objects.get(pk = bud_req.project.pk)
		event.expected_budget = requested_budget
		event.save()

	return HttpResponseRedirect("/")

def remove_budrequest(request):
	req_id = request.POST.get('request_pk')
	bud_req = RequestBudget.objects.get(pk=req_id)

	bud_req.delete()

	return HttpResponseRedirect("/")

def update_recrequest(request):
	req_id = request.POST.get('request_pk')
	request_status = request.POST.get('request_status')

	rec_req = RequestRecruitment.objects.get(pk=req_id)

	rec_req.status = request_status

	rec_req.save()

	return HttpResponseRedirect("/")

def remove_recrequest(request):
	req_id = request.POST.get('request_pk')
	rec_req = RequestRecruitment.objects.get(pk=req_id)

	rec_req.delete()

	return HttpResponseRedirect("/")