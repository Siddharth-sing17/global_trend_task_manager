from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# 1. READ (Home Page par tasks dikhana)
def index(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/index.html', {'tasks': tasks})

# 2. CREATE 
def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        Task.objects.create(title=title, description=description, status=status)
    return redirect('index')

# 3. DELETE 
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')
# 4. UPDATE 
def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)  # Yahan hum task dhoond rahe hain

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.save()
        return redirect('index')  # Wapis home page par bhej do

    context = {'task': task}
    return render(request, 'tasks/update_task.html', context)
