from django.shortcuts import render
from random import randint

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def add(request):
    num1=randint(0,10)
    num2=randint(0,10)
    if request.method=='POST':
        answer=request.POST['answer']
        old_num1=request.POST['old_num1']
        old_num2=request.POST['old_num2']
        corrent_answer=int(old_num1)+int(old_num2)
        if int(answer)==corrent_answer:
            my_answer='Correct!'
            color='warning'
        else:
            my_answer='Incorrect!'
            color='danger'
        return render(request, 'add.html', {'answer':answer, 'my_answer':my_answer, 
                                            'num1':num1, 'num2':num2, 'color':color})
    return render(request, 'add.html', {'num1':num1, 'num2':num2})

def subtract(request):
    num1=randint(0,10)
    num2=randint(0,10)
    if request.method=='POST':
        answer=request.POST['answer']
        old_num1=request.POST['old_num1']
        old_num2=request.POST['old_num2']
        corrent_answer=int(old_num1)-int(old_num2)
        if int(answer)==corrent_answer:
            my_answer='Correct!'
            color='warning'
        else:
            my_answer='Incorrect!'
            color='danger'
        return render(request, 'subtract.html', {'answer':answer, 'my_answer':my_answer, 
                                            'num1':num1, 'num2':num2, 'color':color})
    return render(request, 'subtract.html', {'num1':num1, 'num2':num2})

def multiply(request):
    num1=randint(0,10)
    num2=randint(0,10)
    if request.method=='POST':
        answer=request.POST['answer']
        old_num1=request.POST['old_num1']
        old_num2=request.POST['old_num2']
        corrent_answer=int(old_num1)*int(old_num2)
        if int(answer)==corrent_answer:
            my_answer='Correct!'
            color='warning'
        else:
            my_answer='Incorrect!'
            color='danger'
        return render(request, 'multiply.html', {'answer':answer, 'my_answer':my_answer, 
                                            'num1':num1, 'num2':num2, 'color':color})
    return render(request, 'multiply.html', {'num1':num1, 'num2':num2})

def divide(request):
    num1=randint(0,10)
    num2=randint(1,10)
    if request.method=='POST':
        answer=request.POST['answer']
        old_num1=request.POST['old_num1']
        old_num2=request.POST['old_num2']
        corrent_answer=int(old_num1)/int(old_num2)
        if int(answer)==corrent_answer:
            my_answer='Correct!'
            color='warning'
        else:
            my_answer='Incorrect!'
            color='danger'
        return render(request, 'divide.html', {'answer':answer, 'my_answer':my_answer, 
                                            'num1':num1, 'num2':num2, 'color':color})
    return render(request, 'divide.html', {'num1':num1, 'num2':num2})