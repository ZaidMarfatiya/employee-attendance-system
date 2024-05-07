from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from core_app.models import Employee, Attendance
from core_app.forms import EmployeeForm, AttendanceForm


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee created successfully.')
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})


def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated successfully.')
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})


def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee deleted successfully.')
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'employee': employee})


def attendance_today(request):
    today = timezone.now().date()
    attendances = Attendance.objects.filter(date=today)
    employees = Employee.objects.exclude(attendance__date=today)
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.date = today
            attendance.save()
            data = {
                'success': True,
                'message': 'Attendance updated successfully.'
            }
            return JsonResponse(data)
        else:
            data = {
                'success': False,
                'message': 'Error updating attendance.'
            }
            return JsonResponse(data, status=400)
    else:
        form = AttendanceForm()
    return render(request, 'attendance_today.html', {
        'attendances': attendances,
        'employees': employees,
        'form': form
    })


def attendance_list(request):
    attendances = Attendance.objects.all()
    return render(request, 'attendance_list.html', {'attendances': attendances})

