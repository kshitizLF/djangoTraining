from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader
from home.models import Employee,Desk
from .models import Tasks
# Create your views here.
def index(request):
    t = loader.get_template("employees/index.html")
    if request.method == 'POST':
        i = request.POST.get("name")
        d = Employee.objects.get(name = i)
        d.delete()
        # return HttpResponse("hello")
    employees = Employee.objects.all().values()
    # print(employees)
    context = {
        "employees":employees, 
    }

    return HttpResponse(t.render(context=context))
def deskNo(request,id):
    d = Desk.objects.get(id=id)

    return HttpResponse(f"Employee is on table number {d.number} , {d.floor}th floor ")

def getTasks(request,id):
    taskList = list(Tasks.objects.filter(employee_id = id).values())
    if len(taskList) == 0:
        return HttpResponse("No ongoing Tasks")
    # print(taskList)
    obj = {
        "taskList":taskList
    }
    t = loader.get_template("employees/tasks.html")
    return HttpResponse(t.render(context = obj))