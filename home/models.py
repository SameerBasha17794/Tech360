from django.db import models

# Create your models here.


BLOG_CATEGORIES = [('News','News'),("Business","Business"),("Technology","Technology"),("Python","Python"),("Java","Java"),("Startup","Startup")]

class SeparatedValuesField(models.TextField):
    #__metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super(SeparatedValuesField, self).__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return parse_hand(value)


    def to_python(self, value):
        if not value: return
        if isinstance(value, list):
            return value
        return value.split(self.token)

    def get_db_prep_value(self, value):
        if not value: return
        assert(isinstance(value, list) or isinstance(value, tuple))
        return self.token.join([unicode(s) for s in value])

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)



class MainBanner(models.Model):
	image = models.ImageField(upload_to="MainBanner/")

	def __str__(self):
		return str(self.image)

class Course(models.Model):
	coursename = models.CharField(max_length=1000)
	courseimage = models.ImageField(upload_to='CourseImages/')

	def __str__(self):
		return str(self.coursename)

class SubCourse(models.Model):
	coursename = models.ForeignKey(Course,on_delete=models.CASCADE)
	subcoursename = models.CharField(max_length=1000)

	def __str__(self):
		return str(self.subcoursename)

class CourseContent(models.Model):
	coursename = models.ForeignKey(SubCourse,on_delete=models.CASCADE)
	content = models.CharField(max_length=1000000000000)
	name = models.CharField(max_length=100,blank=True,null=True)
	heading = models.CharField(max_length=2000)

	def __str__(self):
		return str(self.coursename)		


class Blog(models.Model):
	image = models.ImageField(upload_to="Blogs/")
	author = models.CharField(max_length=1000)
	published_on = models.DateTimeField(auto_now=True,auto_now_add=False)
	category = models.CharField(max_length=1000,choices=BLOG_CATEGORIES,default="News")
	description = models.CharField(max_length=1000000000)
	title = models.CharField(max_length=100000)

	def __str__(self):
		return str(self.title)

