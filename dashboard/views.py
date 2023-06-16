from django.shortcuts import render,get_list_or_404,redirect,get_object_or_404
from staff.models import *
from student.models import * 
from student.form import StudentApplicationForm
from staff.models import*
from staff.form import TeacherForm
from django.shortcuts import render,HttpResponsePermanentRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . models import*
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
# ====================ADMIN====================
@login_required(login_url='das_login')
def loginadmin(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                error_message = 'Username is already taken!!!!!!!'
                return render(request,'dashboard.html',{'error_message':error_message})
            if User.objects.filter(email = email).exists():
                error_message = 'Email is already registered'
                return render(request,'dashboard.html',{'error_message':error_message})
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('dashboard')
        else:
            error_message = 'Passwords do not match.'
            return render(request, 'dashboard.html', {'error_message': error_message})
    return render(request, 'dashbase.html')

def das_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/dashboard_login/das_login.html',{'error_message': 'Invalid credentials!'})
    else:
        return render(request,'accounts/dashboard_login/das_login.html')

def logout_view(request):
    auth.logout(request)
    return redirect('das_login')

def admin_profile(request):
    admin_user = User.objects.all()
    return render(request, 'admin/admin_profile.html',{'admin_user':admin_user})
# ======================ENDADMIN=====================
# ======================DASH=========================
@login_required(login_url='das_login')
def dashboard(request):
    student_count = StudentApplication.objects.count()
    staff_count = Teacher.objects.count()
    department_count = Course.objects.count()

    context ={
        'student_count':student_count,
        'staff_count':staff_count,
        'department_count':department_count,
    }
    return render(request,'dashboard.html',context)
# ======================ENDDASH======================
# ======================Student======================
@login_required(login_url='das_login')
def student_details(request):
    student = StudentApplication.objects.filter(accepted=True)
    query = request.GET.get('q')
    if query:
        student = StudentApplication.objects.filter(student_name__icontains = query) | \
                  StudentApplication.objects.filter(email__icontains=query)
    else:
        student = StudentApplication.objects.filter(accepted=True)
    return render(request, 'das_student_details.html',{'student':student,'query':query})

@login_required(login_url='das_login')
def student_profile(request,sp):
    profile = StudentApplication.objects.filter(id=sp)
    return render(request,'student/das_student_profile.html',{'profile':profile})

@login_required(login_url='das_login')
def student_update(request,su):
    studup = StudentApplication.objects.get(id=su)
    form = StudentApplicationForm(instance=studup)
    if request.method == 'POST':
        form = StudentApplicationForm(request.POST,request.FILES,instance=studup)
        if form.is_valid():
            form.save()
            return redirect('student_details')
    return render(request,'application.html',{'form':form})

@login_required(login_url='das_login')
def student_delete(request,sd):
    studdelete = StudentApplication.objects.filter(id=sd)
    studdelete.delete()
    return redirect('student_details')

@login_required(login_url='das_login')
def search_student():
    return render(request, '/')

@login_required(login_url='das_login')
def new_student(request):
    return render(request,'das_new_student.html')
# ======================ENDSTUDENT====================
# ======================STAFF=========================
@login_required(login_url='das_login')
def staff(request):
    staff = Teacher.objects.all()
    query = request.GET.get('q')
    if query:
        staff = Teacher.objects.filter(name__icontains = query) | \
        Teacher.objects.filter(email__icontains = query) 
    else:
        staff = Teacher.objects.all()
    return render(request,'das_staff.html',{'staff':staff,'query':query})

@login_required(login_url='das_login')
def staff_register(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect('staff_register')
        else:
            return render(request,'staff_register.html',{'form':form})
    else:
        form =  TeacherForm()
        return render(request,'staff_register.html',{'form':form})

@login_required(login_url='das_login')
def staff_details(request,td):
    staff_d = Teacher.objects.filter(id=td)
    return render(request,'staff/staff_details.html',{'staff_d':staff_d})

@login_required(login_url='das_login')
def staff_delete(request,tde):
    staff_delete = Teacher.objects.filter(id=tde)
    staff_delete.delete()
    return redirect('staff')
# ======================END STAFF======================

# ======================COURSE=========================
@login_required(login_url='das_login')
def course_add(request):
    if request.method == "POST":
        course_name = request.POST['course_name']
        course_name = Course.objects.create(course_name=course_name)
        course_name.save()
        return redirect('course_add')
    else:
        return render(request,'course/course_add.html')
    
@login_required(login_url='das_login')
def course_details(request):
    course_details = Course.objects.all()
    return render(request, 'course/course_details.html',{'course_details':course_details})

@login_required(login_url='das_login')
def course_update(request,id):    
    course_details = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        course_name = request.POST['course_name']
        course_details.course_name = course_name
        course_details.save()
        return redirect('course_details')
    return render(request, 'course/update_course.html', {'course_details': course_details})

@login_required(login_url='das_login')
def course_delete(request,id):
    course_delete = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        course_delete.delete()
        return redirect('course_details')
    return redirect('course_details')
# ======================ENDCOURSE======================