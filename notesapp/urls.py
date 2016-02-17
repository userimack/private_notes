from django.conf.urls import url

from notesapp import views

urlpatterns = [

	#url(r'^$',views.home,name='home'),

	#user authentication url
	url(r'^login/$',views.login,name='login'),
	url(r'^auth/$',views.auth_view,name='auth'),
	url(r'^register/$',views.register,name='register'),
	url(r'^register_success/$',views.register_success,name='register_success'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^loggedin/$',views.loggedin,name='loggedin'),
	url(r'^invalid/$',views.invalid_login,name='invalid'),
	url(r'^createnote/$',views.createnote,name='createnote'),
	url(r'^note/delete/(?P<pk>\d+)/$',views.delete_notes,name='delete_notes'),


]
