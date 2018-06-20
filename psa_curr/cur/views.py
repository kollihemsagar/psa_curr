from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from cur import convert

# Create your views here.
@csrf_exempt
def index(request):
	if request.method == "POST":
		form = request.POST
		amount = int(form['amount'])
		curr_fr = form['curr_fr']
		curr_to = form['curr_to']
		exchange = convert.conv(curr_fr, curr_to)
		result = amount * exchange
		return render(request, 'index.html', {'the_result': result})
	else:
		return render(request, 'index.html')
