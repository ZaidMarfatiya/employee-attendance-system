from django.urls import path
from core_app import views


urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path(
        'employees/create/',
        views.employee_create,
        name='employee_create'
    ),
    path(
        'employees/<int:pk>/update/',
        views.employee_update,
        name='employee_update'
    ),
    path(
        'employees/<int:pk>/delete/',
        views.employee_delete,
        name='employee_delete'
    ),
    path(
        'attendance/today/',
        views.attendance_today,
        name='attendance_today'
    ),
    path(
        'attendance/list/',
        views.attendance_list,
        name='attendance_list'
    ),
]
