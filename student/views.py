from django.shortcuts import render,redirect,HttpResponsePermanentRedirect
from . models import *
from .form import StudentApplicationForm
from django.views import View
from .forms import RegisterForm

# =======================STUDENTREGISTER=======================
def student_register(request):
    if request.method == 'POST':
        form = StudentApplicationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect('/')
        else:
            return render(request,'application.html',{'form':form})
    else:
        form = StudentApplicationForm()
        return render(request,'application.html',{'form':form})
# =======================ENDSTUDENT=======================


def id_student(request,id_st):
    student_id = StudentApplication.objects.get(id=id_st)
    return render(request, 'idcard/ID_card.html',{'student_id':student_id})

def student_request(request):
    st_request = StudentApplication.objects.filter(accepted=False)
    return render(request, 'request/student_request.html',{'st_request':st_request})

def student_accept(request, st_id):
    if request.method == 'POST':
        student = StudentApplication.objects.get(id=st_id)
        student.accepted = True
        student.save()
        return redirect('student_request')
    
def student_waiting_profile(request,swp_id):
    sw_profile = StudentApplication.objects.filter(id=swp_id)
    return render(request, 'request/student_waiting_profile.html',{'sw_profile':sw_profile})
