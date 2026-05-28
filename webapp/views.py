from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, STATUS_CHOICES
from django.utils.dateparse import parse_date


def task_list_view(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'webapp/task_list.html', {'tasks': tasks})


def task_detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'webapp/task_detail.html', {'task': task})


def task_create_view(request):
    if request.method == 'POST':
        description = request.POST.get('description', '').strip()
        detailed_description = request.POST.get('detailed_description', '').strip()
        status = request.POST.get('status', 'new')
        due_date = request.POST.get('due_date', '').strip()
        
        if description:
            Task.objects.create(
                description=description,
                detailed_description=detailed_description,
                status=status,
                due_date=parse_date(due_date) if due_date else None
            )
            return redirect('task_list')
    
    return render(request, 'webapp/task_create.html', {
        'status_choices': STATUS_CHOICES
    })


def task_delete_view(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.delete()
    return redirect('task_list')