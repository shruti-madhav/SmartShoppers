from django.http import HttpResponse
from django.shortcuts import render, redirect
from websites import *
from pcapp.models import register
from django.db import connection, transaction

# Create your views here.

cursor = connection.cursor()

def home(request):
    return render(request, "home.html")

def profile(request):
    sql = register.objects.all()
    return render(request, "profile.html", {"user": sql})

def update(request):
    sql = register.objects.all()
    return render(request, "update.html", {"user": sql})

def updatepass(request):
    if request.method == "POST":
        oldpass = request.POST.get("old")
        newpass = request.POST.get("new")
        name = request.POST.get("username")
        email = request.POST.get("email")
        if newpass == "":
            newpass = oldpass
        sqll = "update register set password='%s',name='%s',email='%s' where password='%s'" % (newpass, name, email, oldpass)
        cursor.execute(sqll)
        transaction.commit()
        session_keys = list(request.session.keys())
        for key in session_keys:
            del request.session[key]
        return redirect("/login")
    sql = register.objects.all()
    return render(request, "update.html", {"user": sql})

def login(request):
    return render(request, "login.html")

def dologin(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        for e in register.objects.raw('select * from register where email="%s" and password="%s"'%(email, password)):
            if e.name == name:
                request.session['name'] = name
                print('Welcome '+e.name)
                return render(request, "home.html", {'success': 'Welcome '+e.name})
            else:
                print('Sorry ' + e.name + ' something went wrong!')
                return render(request, "login.html", {'fail': 'Sorry ' + e.name + ' something went wrong!'})
    return render(request, "login.html")

def Register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        sql = 'insert into register(name, email, password)values("%s", "%s", "%s")' %(name, email, password)
        cursor.execute(sql)
        transaction.commit()
        return render(request, "login.html")
    return render(request, "register.html")

def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return render(request, "login.html", {"successlogout": 'you are successfully logged out'})

def filetry(request):
    if request.method == "POST":
        name = request.POST.get("searchtext")
        product = name.replace(" ", "+")
        snap = snapdeal(product, name)
        print("snap ", snap)

        eb = ebay(product, name)
        print("ebay ", eb)

        ama = amazon(product, name)
        print("amazon ", ama)

        flip = flipkart(product, name)
        print("flip ", flip)

        paytm = paytmmall(product, name)
        print("paytm ", paytm)

        if snap is None:
            snap = ['0', 'not found']
        if eb is None:
            eb = ['0', 'not found']
        if ama is None:
            ama = ['0', 'not found']
        if flip is None:
            flip = ['0', 'not found']
        if paytm is None:
            paytm = ['0', 'not found']

        return render(request, "search.html",
                      {"sprice": snap[0], "slink": snap[1], "eprice": eb[0], "elink": eb[1],
                       "amaprice": ama[0], "amalink": ama[1], "fprice": flip[0], "flink": flip[1],
                       "pprice": paytm[0], "plink": paytm[1]})
    else:
        return render(request, "search.html")