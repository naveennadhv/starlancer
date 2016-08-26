from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student, School
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def home(request):
    form = StudentForm()
    if request.method  == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New student added.')
            form = StudentForm()
    return render(request, "welcome.html",{
        "undapori":"HELLO",
        "form": form
        })




class StudentList(ListView):
    model = Student
    context_object_name = 'students'
    paginate_by = 3
    template_name = 'coreapp/student_list.html'
    def post(self, request):
        messages.success(request, "Testing post")
        return redirect('/core/students')
