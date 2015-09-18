from django.shortcuts import render,render_to_response
from django.contrib import auth
from django.template import RequestContext
from djnaog.http import HttpResponseRedirect
from django.core.context_processors import csrf
from djnago.contrib.auth.forms import UserCreationForm
from djnago.contrib.auth.decorators import login_required


# Create your views here.

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html',c)

def register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		if request.method== 'POST' :
			form = UserCreationForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect("/accounts/register_succcess")
			else:
				return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))

		args = {}
		args.update(csrf(request))

		args['form'] = UserCreationForm()
		return render_to_response('register.html',args)

def register_success(request):
	return render_to_response('register_success.html')

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')

	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin/')
	else:
		return HttpresponseRedirect('/accounts/invalid/')

@login_required
def loggedin(request):
	tasks =	