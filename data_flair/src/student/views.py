from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.

def student_show(request):  # Note that the function name does not have to be the same as the template's name.
    student = Student.objects.order_by('roll_no')
    return render(request, 'templates/student/student_show.html', {'student':student})
