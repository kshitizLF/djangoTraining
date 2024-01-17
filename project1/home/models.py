from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    age = models.SmallIntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email},{self.age}"

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"{self.question_text} published on {self.pub_date.date()}"
    
    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=3)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return f"Option {self.choice_text} has {self.votes} votes"

class Owner(models.Model):
    name = models.CharField(verbose_name="Full Name", max_length=50)
    age = models.SmallIntegerField()
    choices = [
        ("M","Male"),
        ("F","Female"),
        ("O","Others")
    ]
    sex = models.CharField(verbose_name="Gender",max_length=10,choices=choices)
    def __str__(self):
        return f"{self.name}"
    
class Car(models.Model):
    company = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    owner = models.ForeignKey(Owner,on_delete = models.CASCADE)

'''
    in case of One-to-Many relationship:
        eg above : one owner can be associated with many cars

        model.object.__dict__ will return a dictionary with all the field of the row fields

        o1.car_set will return objects associated to o1 owner in form of QuerySet
        
        o1.car_set.values()[0].get("model")

        o1.car_set.get(model="i20") will return a Car Object

        o1.car_set.get(model="i20").__dict__ will return a dictionary will object's fields as keys
        
        can access field of onwer corressponding to a car by : c1.owner.sex
'''

class Desk(models.Model):
    number = models.SmallIntegerField(verbose_name="Desk Number")
    floor = models.SmallIntegerField(verbose_name="Floor No.")

    class Meta:
        ordering = ['floor','number']
    
    def employeeAssigned(self):
        try:
            e1 = self.employee
            return True
        except:
            return False
    
    
class Employee(models.Model):
    name = models.CharField(max_length=50)
    choices = [
        ("IN","Intern"),
        ("EP","Employee")
    ]
    position = models.CharField(max_length = 20,choices = choices)
    desk = models.OneToOneField(Desk,on_delete=models.CASCADE)

    '''
        OneToOne relationship : 
        Only one entry in Employee for a corresspon
        Some Basic commands
            Employee.objects.filter(desk__number__gt = 1)
            Employee.objects.get(name="Abhi").desk
            Employee.objects.order_by("-name").values()
    '''

class Customer(models.Model):
    name = models.CharField(max_length = 40)
    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length = 40)
    customer = models.ManyToManyField(Customer)
    
    def __str__(self):
        return f"{self.name}"    

'''
>>> from home.models import Customer,Product
>>> c1 = Customer(name="Kshitiz")
>>> c1.save()
>>> c2 = Customer(name="Pree")    
>>> c2.save()
>>> p1 = Product(name = "watch")
>>> p1.save()
>>> p1.customer.add(c1,c2)
>>> Product.objects.get(id=1).customer.values()[0]["name"]
'''

class Citizen(models.Model):
    name = models.CharField(max_length=40)
    age = models.SmallIntegerField()
    adhaar = models.BigIntegerField()
    class Meta:
        abstract = True

class ArmyMan(Citizen):
    posting = models.CharField(max_length=30)

class Civilian(Citizen):
    company = models.CharField(max_length=30)

'''
    Abstract Model doesnot create a table in the database
    instead is just used to provide common attributes for inherited model classes
'''
