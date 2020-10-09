from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect

from .models import Client, Event, RequestEvent

def index(request):
	# Number of visits to this view, as counted in the session variable.
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits+1

	# Render the HTML template index.html with the data in the context variable.
	if (request.user.groups.filter(name='CS Manager').exists()):
		return get_pending_events(request)
	elif (request.user.groups.filter(name='Financial Manager').exists()):	
		return get_cs_accepted_events(request)
	elif (request.user.groups.filter(name='Administration Manager').exists()):
		return get_fin_accepted_events(request)
	else:
		return render(
			request,
			'index.html'
		)
	#return HttpResponse("You're at the SEP index.")
# Create your views here.

from .forms import event_form

def event_request(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = event_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_req = RequestEvent(
	            client = form.cleaned_data['client'],
			    event_type = form.cleaned_data['event_type'],
			    description = form.cleaned_data['description'],
			    attendees = form.cleaned_data['attendees'],
			    expected_budget = form.cleaned_data['expected_budget'],
			    from_date = form.cleaned_data['from_date'],
			    to_date = form.cleaned_data['to_date'],
			    decorations = form.cleaned_data['decorations'],
			    film_and_photos = form.cleaned_data['film_and_photos'],
			    posters_art = form.cleaned_data['posters_art'],
			    food_drinks = form.cleaned_data['food_drinks'],
			    music = form.cleaned_data['music'],
			    computers = form.cleaned_data['computers'],
			    other = form.cleaned_data['other'],
			    status = "created"
			)

            new_req.save()
            # redirect to a new URL:
            return render(request, 'index.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = event_form()

    return render(request, 'forms/event_form.html', {'form': form})

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
	
	return render(
		request,
		'index.html',
		context={'event_cs_requests': event_cs_requests},
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
        old_client = Client.objects.filter(client_name = accepted_request.client)
        

        if (old_client) :
        	client_id = Client.objects.get(client_name = accepted_request.client)[0]
        	client_id.organized_events = old_client.organized_events + 1
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
