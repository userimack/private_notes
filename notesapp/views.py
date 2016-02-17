from django.shortcuts import render,render_to_response
from django.contrib import auth
#from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
	return render(request,'home.html',{}) 


def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/loggedin/')
	else:
		return render(request,'login.html',{})



def register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/loggedin/')
	else:

		if request.method== 'POST' :
			form = UserCreationForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect("/accounts/register_success/")
			else:
				return render(request,'register.html',{'form':form})

		args = {}
		args.update(csrf(request))
		print (args)

		args['form'] = UserCreationForm()
		print (args)
		return render_to_response('register.html',args)

def register_success(request):
	return render(request,'register_success.html',{})

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')

	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin/')
	else:
		return HttpResponseRedirect('/accounts/invalid/')

@login_required
def loggedin(request):
	notes =	request.user.notes_set.all()
	username = request.user.username
	return render(request,'loggedin.html',{'username':username,'notes':notes})

def invalid_login(request):
	return render(request,'invalid_login.html',{})

def logout(request):
	auth.logout(request)
	return render(request,'logout.html',{})


@login_required
def createnote(request):
	title = request.POST.get('title','')
	note = request.POST.get('note','')
	request.user.notes_set.create(title=title,note=note)
	return HttpResponseRedirect('/accounts/loggedin/')

@login_required
def delete_notes(request,pk):
	title = request.user.notes_set.get(id=pk)
	title.delete()
	return HttpResponseRedirect('/accounts/loggedin/')