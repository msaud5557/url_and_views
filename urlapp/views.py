from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.urls import reverse
# Create your views here.

def home_view(request):
    return HttpResponse("<h1>This is Our Home Page </h1>")

def about_view(request):
    return HttpResponse("This is a about page")

def user_profile_view(request,username):
    return HttpResponse(f"My Name is {username}")

def profile_redirect(request,username):
    return redirect(reverse('user_profile_view' ,args=[username] )) 


def html(request,username,bootcamp):
    text=f"<h1>My name is {username} and I'll Enrolled bootcamp in {bootcamp} </h1>"
    return HttpResponse(text,content_type="text/html")

# def home_file(request):
#     # name="saud"
#     # arr=[1,2,3,4]
#     dict1={"name":"Daniyal"}
#     dict2={"age":23}
#     dict3={"fruit_list":['bnanna','mango','apple']}
    
    
#     context={"username":"saud","d1":dict1,"d2":dict2,"d3":dict3}
#     return render(request,"home.html",context)


# def home_file(request):
#     class __init__(self,name,age,school,Class_name):
#         self.name = name
#         self.age = age
#         self.school=school
#         self.Class_name=Class_name
         
         
         
#         student1={"name":"Saud","age":23,"school":"abc","Class_name":"Django_python"}
#         student2={"name":"Saud","age":24,"school":"abc","Class_name":"Django_python"}
#         student3={"name":"Saud","age":26,"school":"abc","Class_name":"Django_python"}
#         student4={"name":"Saud","age":25,"school":"abc","Class_name":"Django_python"}
#         student5={"name":"Saud","age":23,"school":"abc","Class_name":"Django_python"}
        

#     context={"student1":student1,"student2":student2,"student3":student3,"student4":student4,"student5":student5}
#     return render(request,"home.html",context)



class Student:
    def __init__(self, name, age, course,degree):
        self.name = name
        self.age = age
        self.course = course
        self.degree = degree

def student_list(request):
    students = [
        Student("Muhammad Saud", 22, "CS","IT"),
        Student("Daniyal", 24, "DS","CS"),
        Student("Umair Arshad", 20, "Mern","SE"),
        Student("Umar", 23, "Django","AI"),
        Student("Asim", 27, "Python","ICT")
    ]
    
    context = {
        'students': students
    }
    
    return render(request,'home.html', context)


             

         
         


 




