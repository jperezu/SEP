from django import forms

class event_form(forms.Form):
	client = forms.CharField(max_length=20)
	event_type = forms.CharField(max_length=200)
	description = forms.CharField(max_length= 1000)
	attendees = forms.IntegerField()
	expected_budget = forms.IntegerField()
	from_date = forms.DateField()
	to_date = forms.DateField()
	decorations = forms.CharField(max_length=500)
	film_and_photos = forms.CharField(max_length=500)
	posters_art = forms.CharField(max_length=500)
	food_drinks = forms.CharField(max_length=500)
	music = forms.CharField(max_length=500)
	computers = forms.CharField(max_length=500)
	other = forms.CharField(max_length=500)

class task_form(forms.Form):

#	#overwrite __init__
#	def __init__(self,val,*args,**kwargs):
#		# call standard __init__
#		super().__init__(*args,**kwargs)
#		#extend __init__
#		self.fields['assigner'] =forms.CharField(disabled = True, initial=val)

	description = forms.CharField(max_length=500)
	assigned = forms.IntegerField()
	priority = forms.CharField(max_length=10)