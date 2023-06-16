from django.urls import path
from .  import views

urlpatterns = [
    path('',views.student_register,name='student_register'),
    path('student_request',views.student_request,name='student_request'),
    path('student_accept/<int:st_id>/',views.student_accept,name='student_accept'),
    path('student_waiting_profile/<int:swp_id>/',views.student_waiting_profile,name ='student_waiting_profile'),
    path('id_student/<int:id_st>/',views.id_student,name='id_student'),
]