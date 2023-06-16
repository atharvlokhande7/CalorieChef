from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.forms import modelformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import connection
from datetime import date
import random
# Create your views here.
from .models import *
from .forms import *

 


def rec(request):
    userid = request.user.id
    lu=     recipe.objects.filter(rtype="L")
    dn=     recipe.objects.filter(rtype="D")
    user=   account.objects.filter(pk=userid)
    height= account.objects.filter(pk=userid).values_list('height',flat=True)
    weight= account.objects.filter(pk=userid).values_list('weight',flat=True)
    extype= account.objects.filter(pk=userid).values_list('extype',flat=True)
    gender= account.objects.filter(pk=userid).values_list('gender',flat=True)
    veg=    account.objects.filter(pk=userid).values_list('veg',flat=True)
    cveg=   0
    age=    user[0].get_age()
    m1=     10*weight[0]+6.25*height[0]-5*age+gender[0]
    m2=     extype[0]
    e46=    m1+m2
    f82=    e46
    m3=     0.325*e46
    m4=     0.35*f82
    print(veg[0])
    if(veg[0]==False):
       v="User is non vegetarian"
       
       breakfastnv=     "SELECT * FROM 'main_recipe' WHERE energy<="+str(m3)+" and energy>="+str(m3-400)+" and rtype='B' ORDER BY RANDOM() LIMIT 3"
       bft=             recipe.objects.raw(breakfastnv)
       lunchnv=         "SELECT * FROM 'main_recipe' WHERE energy<="+str(m4)+" and energy>="+str(m4-300)+" and rtype='L' ORDER BY RANDOM() LIMIT 3"
       lun=             recipe.objects.raw(lunchnv)
       dinnernv=        "SELECT * FROM 'main_recipe' WHERE energy<="+str(m3)+" and energy>="+str(m3-250)+" and rtype='D' ORDER BY RANDOM() LIMIT 3"
       din=             recipe.objects.raw(dinnernv)
       cveg=0
    
    else:
        breakfastnv=     "SELECT * FROM 'main_recipe' WHERE energy<="+str(m3)+" and energy>="+str(m3-400)+" and veg=1 and rtype='B' ORDER BY RANDOM() LIMIT 3"
        bft=             recipe.objects.raw(breakfastnv)
        lunchnv=         "SELECT * FROM 'main_recipe' WHERE energy<="+str(m4)+" and energy>="+str(m4-300)+" and veg=1 and rtype='L' ORDER BY RANDOM() LIMIT 3"
        lun=             recipe.objects.raw(lunchnv)
        dinnernv=        "SELECT * FROM 'main_recipe' WHERE energy<="+str(m3)+" and energy>="+str(m3-250)+" and veg=1 and rtype='D' ORDER BY RANDOM() LIMIT 3"
        din=             recipe.objects.raw(dinnernv)
        v="User is vegetarian"
        cveg=1
    
    
    context = {'rb':bft,'rl':lun,'rd':din,'idle':m1,'ex':m2,'tot':e46,'Break':m3,'Lunch':m4,'vs':v,'age':age,'cveg':cveg}
    return render(request, 'main/rec.html',context)


def loginp(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)    
    
        if user is not None:
          login(request, user)
          return redirect('main:dash')
        else:
            messages.info(request, 'Check Username or password')
        
    
    context = {}
    return render(request, 'main/login.html',context)

def rpass(request):
    if request.method == 'POST':
        user=request.post.username
        pass1=request.post.password1
        pass2=request.post.password2
        '''
        if (pass1==pass2):
         u= account.objects.get(username=user)
         u.set_password(pass1)
        '''
    
    context = {''}
    return render(request, 'main/rpass.html')
    
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            print(user)
            sql1="SELECT id FROM main_account WHERE username='"+user+"'"
            print(sql1)
            cursor = connection.cursor()
            cursor.execute(sql1)
            r= cursor.fetchone()
            bar=str(r[0])
            cursor1 = connection.cursor()
            cursor1.execute("INSERT INTO main_suser(name_id) VALUES ("+bar+")")
            messages.success(request,'User Account was created ' + user )
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'main/register.html',context)

def dash(request):
    return render(request, 'main/dash.html')

def udetail(request):
    
    userid = request.user.id
    user = account.objects.get(pk=userid)
    userm= suser.objects.get(pk=userid)
    form= updateuser(instance=user)
    fmc=updatehcon(instance=userm)
    if request.method == 'POST':
        form = updateuser(request.POST, instance=user)
        fmc=updatehcon(request.POST,instance=userm)
        if form.is_valid():
            if fmc.is_valid:
              form.save()
              fmc.save()
              messages.success(request,'User data updated')
              return redirect('main:dash')
            
            
    context = {'form':form,'fmc':fmc,'userm':userm}    
    return render(request, 'main/udetail.html', context)


def logoutUser(request):
    
    logout(request)
    return redirect('main:login')

def about(request):
    return render(request, 'main/about.html')
    
def aboutl(request):
    userid = request.user.id
    user=   account.objects.filter(pk=userid)
    height= account.objects.filter(pk=userid).values_list('height',flat=True)
    weight= account.objects.filter(pk=userid).values_list('weight',flat=True)
    extype= account.objects.filter(pk=userid).values_list('extype',flat=True)
    gender= account.objects.filter(pk=userid).values_list('gender',flat=True)
    veg=    account.objects.filter(pk=userid).values_list('veg',flat=True)
    h1=height[0]
    h2=weight[0]
    h3=user[0].get_age()
    h4=gender[0]
    m1=10*h2+6.25*h1-5*h3+h4
    m2=extype[0]
    e46=m1+m2
    f82=e46
    m3=0.3*e46
    m4=0.4*f82
    context = {'idle':m1,'ex':m2,'tot':e46,'Break':m3,'Lunch':m4}
    return render(request, 'main/aboutl.html',context)    

