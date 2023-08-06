from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from students.models import Student


# Create your views here.
def regStudents(request):
    return render(request, 'students/registerStudent.html')

def regConStudents(request):
    name = request.POST['name']
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']

    qs = Student(s_name=name, s_major=major, s_age=age, s_grade=grade, s_gender=gender)
    qs.save() # db 에 저장해준다.

    return HttpResponseRedirect(reverse('students:stuAll'))

def readStudentAll(request):
    qs = Student.objects.all()
    context = {'student_list': qs}
    return render(request, 'students/readStudents.html', context)

def detStudent(request, name):
    qs = Student.objects.get(s_name = name)
    context = {'student_info': qs}
    return render(request, 'students/detailStudent.html', context)

def readStudentOne(request, name):
    qs = Student.objects.get(s_name = name)
    context = {'student_info': qs}
    return render(request, 'students/modifyStudent.html', context)

def modConStudent(request):
    name = request.POST['name']
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']

    s_qs = Student.objects.get(s_name=name)

    s_qs.s_name = name
    s_qs.s_major = major
    s_qs.s_age = age
    s_qs.s_grade = grade
    s_qs.s_gender = gender

    s_qs.save()

    return HttpResponseRedirect(reverse('students:stuAll'))

def delConStudent(request, name):
    s_qs = Student.objects.get(s_name = name)
    s_qs.delete()

    return HttpResponseRedirect(reverse('students:stuAll'))