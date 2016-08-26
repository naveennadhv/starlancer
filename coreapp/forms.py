from django.forms import ModelForm, CharField
from .models import Student

# Create the form class.
class StudentForm(ModelForm):
    silly_field = CharField(required=False)
    class Meta:
        model = Student
        fields = ['name', 'marks', 'school' ,'silly_field']
