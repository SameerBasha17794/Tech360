from django.shortcuts import render
from .models import Course,CourseContent,SubCourse,Blog
from .forms import CourseContentForm,SubCourseForm,BlogForm
from django.contrib import messages
# Create your views here.
def index(request):
	course = Course.objects.all()
	blogs = Blog.objects.all()
	return render(request,'index.html',{'courses':course,'blogs':blogs})

def base(request):
	course = Course.objects.all()
	return render(request,'base.html',{'courses':course})

def coursecontent(request,name):
	print(name)
	course = Course.objects.get(coursename=name)
	subcourse = SubCourse.objects.filter(coursename__coursename=name)[0]
	subcoursename = subcourse.subcoursename
	content = CourseContent.objects.filter(name = subcoursename)
	print(content)
	return render(request,'course_innerpage.html',{'coursecontent':content,'subcoursename':subcoursename})

def uploadsubcourse(request):
	if request.method == 'POST':
		form = SubCourseForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Successfully Uploaded')
		else:
			messages.error(request,'Error')
	form = SubCourseForm()
	courses = Course.objects.all()
	return render(request,'add_subcourse.html',{'form':form,'courses':courses})			

def uploadcoursecontent(request):
	if request.method=='POST':
		form = CourseContentForm(request.POST)
		if form.is_valid():
			a = form.save(commit=False)
			a.name = a.coursename
			a.save()
			messages.success(request,'Successfully Uploaded')
		else:
			messages.error(request,'Error')
	form = CourseContentForm()
	course = SubCourse.objects.all()
	return render(request,'upload_course_content.html',{'form':form,'courses':course})			


def blogs(request):
	blog = Blog.objects.all()
	return render(request,'blogs.html',{'blogs':blog})	


def uploadblogs(request):
	if request.method=='POST':
		form = BlogForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,'Successfully Uploaded')
		else:
			messages.error(request,'Error')
	form = BlogForm()
	return render(request,'upload_blogs.html',{'form':form})		


def blog_detail(request,name):
	blog = Blog.objects.get(title=name)
	return render(request,'blog_detail.html',{'blog':blog})	


def website(request):
	return render(request,'websites.html',{})	

def signup_login(request):
	return render(request,'signup_login.html',{})	