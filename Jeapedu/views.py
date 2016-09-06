from django.shortcuts import render_to_response
from Jeapedu.models import *
from django.template import RequestContext

def index(request):
	news     = News.objects.all()
	teachers = Teachers.objects.filter(order__lt=7).filter(kw="open").order_by("order")
	students = Students.objects.filter(order__lt=4).filter(kw="open").order_by("order")
	course   = Course.objects.filter(kw="open").order_by("order")
	d        = {'news':news,'teachers':teachers,'students':students,'course':course}
	return render_to_response('index_tag.html', d, context_instance=RequestContext(request))
	
def course(request):
	courses     = Course.objects.all()
	courses_num = Course.objects.all().count()
	d           = {'courses':courses,'courses_num':courses_num}
	return render_to_response('course.html', d, context_instance=RequestContext(request))
	
def teachers(request):
	teachers     = Teachers.objects.all()
	teachers_num = Teachers.objects.all().count()
	d            = {'teachers':teachers,'teachers_num':teachers_num}
	return render_to_response('teachers.html', d, context_instance=RequestContext(request))
	
def courseshow(request,id):
	course = Course.objects.get(id=int(id))
	d      = {'course':course}
	return render_to_response('courseshow.html', d, context_instance=RequestContext(request))
	
	
	
	
	
	
	