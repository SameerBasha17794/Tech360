from django import forms
from .models import Course,CourseContent,SubCourse,Blog

class CourseContentForm(forms.ModelForm):
	class Meta:
		model = CourseContent
		fields = '__all__'

class SubCourseForm(forms.ModelForm):
	class Meta:
		model = SubCourse
		fields = '__all__'		

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = '__all__'		