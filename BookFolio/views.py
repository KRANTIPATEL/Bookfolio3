from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm
from service.models import Service
from Prices.models import Prices
from news.models import News
from booksDetail.models import BooksDetail
from django.core.paginator import Paginator
from logindata.models import LoginDetails

def aboutUs(request):

   
    if request.method == "GET":
        output = request.GET.get('output')
        
    return render(request,"about.html",{ 'output1': output})
        
def signin(request):
    error = False
    datasignup={}
    booksData = BooksDetail.objects.all()

    try:
        datasignin = LoginDetails.objects.all()
        if request.method == "POST":
            email1 = request.POST['email1']
            pwd1 = request.POST['pwd1']
            
            for n in datasignin:
                if email1 == n.login_email and pwd1 == n.login_pwd:
                    error = True


            if error :
                return render(request,"gallery.html",{'booksData':booksData})
            else:
                return render(request,"signinpage.html",{'booksData':booksData,'error':error})

                # if email1 != n.login_email or pwd1 != n.login_pwd:
                #     return render(request,"signinpage.html",{'error':error})




        return render(request,"signinpage.html",{'error': error})

    except:
        pass
    
def gallery(request):

    booksData = BooksDetail.objects.all()
    # data={'booksData':booksData}


    return render(request,"gallery.html",{'booksData':booksData})

    # return render(request,"gallery.html")
def gallery1(request,slug):
    # newsDetail = News.objects.get(news_slug=slug)
    booksData = BooksDetail.objects.get(book_slug = slug)

    data={'booksData':booksData}


    return render(request,"gallery1.html",data)
def signup(request):

        booksData = BooksDetail.objects.all()
        datasignin = LoginDetails.objects.all()

        if request.method == "POST":
            email = request.POST['email']
            pwd = request.POST['pwd']

            for n in datasignin:
                if email != n.login_email and pwd != n.login_pwd:
                    en = LoginDetails(login_email=email,login_pwd=pwd)
                    en.save()
                    return render(request,"gallery.html",{'booksData':booksData})
                
           

        
   
        return render(request,"signup.html",{'booksData':booksData})

def course(request):
    return HttpResponse("Heres Your CourseList")

def services(request):

    servicesdata = Service.objects.all()
    paginator =Paginator(servicesdata,2)
    pagenumber = request.GET.get('page')
    ServiceDataFinal = paginator.get_page(pagenumber)
    lastpage = ServiceDataFinal.paginator.num_pages
    pricedata = Prices.objects.all()

    if request.method == "GET":
        pt = request.GET.get('servicename')

        if pt!= None:
            pricedata = Prices.objects.filter(things__icontains = pt)


    data = {'servicesdata':ServiceDataFinal,'pricedata':pricedata,
            'lastpage':lastpage
                }


    return render(request,"services.html",data)

def contact(request):

    return render(request,"contact.html")


def homePage(request):
    # data = {
    #     'title':'HomePage',
    #     'greet':'Welcome to FirstSite',
    #     'clist' : ["php","java","Django"],
    #     'numbers' : [10,20,30,40,50],
    #     'student_details' : [
    #         {'name':'kranti','phone':'8799474999'},
    #         {'name':'romio','phone':'4207864207'}
    #     ]
    # }

    newsdata = News.objects.all()
    data = { 'newsdata':newsdata
    }

    return render(request,"index.html",data)

def newsDetail(request,slug):

    newsDetail = News.objects.get(news_slug=slug)

    data={'newsDetail':newsDetail}


    return render(request,"newsdetail.html",data)

def userForm(request):
    total=0
    fn = UserForm()
    data={'form':fn}
    try:

        if request.method == "POST":
            n1 = int(request.POST['num1'])
            n2 = int(request.POST['num2'])
            total = n1+n2

            data={
                'n1':n1,
                'n2':n2,
                'output':total,
                'form':fn
                  }
            
            url = "/aboutus/?output={}".format(total)
            
            return HttpResponseRedirect(url)

    except:
        pass
    return render(request,"userform.html",data)

def submitform(request):
    total=0
    data={}
    try:

        if request.method == "POST":
            n1 = int(request.POST['num1'])
            n2 = int(request.POST['num2'])
            total = n1+n2

            data={
                'n1':n1,
                'n2':n2,
                'output':total
                  }
            
            
            return HttpResponse(total)

    except:
        pass

def calculator(request):

    c=''
    dimension ={}
    try:
        if request.method == "POST":

            if request.POST.get('num1')=="" or request.POST.get('num2')=="" :
                return render(request,"calculator.html",{'error':True})
            
            # if type(request.POST.get('num1'))!= int or type(request.POST.get('num2'))!= int :
            #     return render(request,"calculator.html",{'error2':True})
            
            n1 = eval(request.POST.get('num1'))
            opr = request.POST.get('opr')
            n2 = eval(request.POST.get('num2'))
            en =Prices(things=n1,things_price=n2)
            en.save()
            if opr == "+":
                c=n1+n2
            elif opr == "-":
                c=n1-n2
            elif opr == "*":
                c=n1*n2
            elif opr == "/":
                c=n1/n2

            dimension = {'c':c,
                'n1':n1,
                'n2':n2
                }


           

    except:
        c="Invalid Entry"
        

    
    return render(request,"calculator.html",dimension)

def validationForm(request):

    if request.method == "POST":
            
            if request.POST.get('num1')=="" or request.POST.get('num2')=="" :
                return render(request,"ValidationForm.html",{'error':True})
            
            # if type(request.POST.get('num1'))!= "<class 'int'>" or type(request.POST.get('num2'))!= "<class 'int'>" :
            #     return render(request,"ValidationForm.html",{'error2':True})

            n1 = eval(request.POST.get('num1'))
            opr = request.POST.get('opr')
            n2 = eval(request.POST.get('num2'))
        
    return render(request,"ValidationForm.html")
