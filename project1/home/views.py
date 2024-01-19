from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader
from .models import Member,Question,Choice
import urllib,json
from .forms import addEmpForm,findUserForm
from django.views.decorators.csrf import csrf_protect

def funct(request):
    members = Member.objects.all().values()
    t = loader.get_template('home/index.html')
    context = {
        "age":21,
        "members":members
    }
    return HttpResponse(t.render(context=context))
def f1(request,id):
    m1 = Member.objects.get(id=id)
    obj = {
        "first_name" : m1.first_name,
        "last_name" : m1.last_name,
        "email":  m1.email,
        "age":m1.age
    }
    print(m1)
    template = loader.get_template('home/detail.html')
    return HttpResponse(template.render(context=obj))

def polls(request):
    return HttpResponse("hello, ready for questions")

def quest(request,id):
    q1 = Question.objects.get(id = id)
    choiceList = Choice.objects.filter(question_id=id)
    template = loader.get_template("home/question.html")
    m = {
        "question_text" : q1.question_text,
        "choice_list" : choiceList
    }
    return HttpResponse(template.render(context=m))
    # print(q1)

    # raise Http404("so")
    # return 
def form(request):
    template = loader.get_template('home/form.html')
    context = {
        'form':addEmpForm(),
        'form1':findUserForm()
    }
    return HttpResponse(template.render(context=context, request=request))

def formSubmit(request):
    if request.method == "POST":
        obj = request.POST
        try:
            m1 = Member.objects.get(email = obj.get("email"))
            return HttpResponse("Entry Already in Database")
        except:
            m1 = Member(first_name = obj.get("first_name"),last_name = obj.get("last_name"),age = obj.get("age"), email = obj.get("email"))
            m1.save()
            print(obj)
            template = loader.get_template("home/formSubmitted.html")
            return HttpResponse(template.render(context=obj))
    else:
        email = request.GET.get("email")
        template = loader.get_template("home/detail.html")
        try:
            m1 = Member.objects.get(email = email)
        except:
            return HttpResponse("Email not in DataBase")
        obj = {
            "first_name" : m1.first_name,
            "last_name" : m1.last_name,
            "email":  m1.email,
            "age":m1.age
        }
        template = loader.get_template('home/detail.html')
        return HttpResponse(template.render(context=obj))
        