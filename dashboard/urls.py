from django.urls import path
from .  import views

urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    
    path('student_details',views.student_details,name='student_details'),
    path('student_profile/<int:sp>/',views.student_profile,name='student_profile'),
    path('student_update/<int:su>/',views.student_update,name='student_update'),
    path('student_delete/<int:sd>/',views.student_delete,name='student_delete'),
    path('new_student',views.new_student,name='new_student'),

    path('staff',views.staff,name='staff'),
    path('staff_register',views.staff_register,name='staff_register'),
    path('staff_details/<int:td>/',views.staff_details,name='staff_details'),
    path('staff_delete/<int:tde>/',views.staff_delete,name='staff_delete'),

    path('search_student',views.search_student,name = 'search_student'),
    path('course_add',views.course_add,name='course_add'),
    path('course_details',views.course_details,name = 'course_details'),
    path('course_update/<int:id>/',views.course_update,name = 'course_update'),
    path('course_delete/<int:id>/',views.course_delete,name='course_delete'),

    path('das_login',views.das_login,name='das_login'),
    path('loginadmin',views.loginadmin,name='loginadmin'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('admin_profile',views.admin_profile,name='admin_profile'),
]