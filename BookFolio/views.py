from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UserForm
from service.models import Service
from Prices.models import Prices
from news.models import News
from booksDetail.models import BooksDetail
from django.core.paginator import Paginator
from logindata.models import LoginDetails
from django.contrib.sessions.models import Session
from django.contrib import messages
from bookDB.models import bookColumn
from cartDB.models import cartColumn


def aboutUs(request):
    # if request.session.get('is_signin'):
    #     return redirect('aboutus')
   
    if request.method == "GET":
        output = request.GET.get('output')
        
    return render(request,"about.html",{ 'output1': output})
        

    
def gallery(request):
    if request.session.get('is_signin'):
        booksData = bookColumn.objects.all()
        data={'booksData':booksData}
        return render(request,'gallery.html',data)
    else:
        return render(request,'signinpage.html')
    
    # return render(request,"gallery.html")
def gallery1(request,slug):
    # newsDetail = News.objects.get(news_slug=slug)
    booksData = bookColumn.objects.get(bookDB_slug = slug)

    data={'booksData':booksData}


    return render(request,"gallery1.html",data)

def signin(request):
    # error = False
    # datasignup={}
    # booksData = BooksDetail.objects.all()

    # try:
    #     datasignin = LoginDetails.objects.all()
    #     if request.method == "POST":
    #         email1 = request.POST['email1']
    #         pwd1 = request.POST['pwd1']
    #         count = LoginDetails.objects.filter(login_email=email1, login_password=pwd1).count()
    #         for n in datasignin:
    #             if email1 == n.login_email and pwd1 == n.login_pwd:
    #                 error = True
        #     if error :
        #         return render(request,"gallery.html",{'booksData':booksData})
        #     else:
        #         return render(request,"signinpage.html",{'booksData':booksData,'error':error})

        #          if email1 != n.login_email or pwd1 != n.login_pwd:
        #             return render(request,"signinpage.html",{'error':error})
        # return render(request,"signinpage.html",{'error': error})

    # except:
        # pass

    if 'is_signin' in request.session and request.session['is_signin']:
        return redirect('home')
    
    else:
    
        if request.method == "POST":
            email = request.POST.get('email1')
            password = request.POST.get('pwd1')
            count = LoginDetails.objects.filter(login_email=email, login_pwd = password).count()
            if count > 0:
                request.session['is_signin'] = True
                return redirect('home')
            else:
                messages.error(request, "Wrong email or password" , extra_tags='signin')
                return render(request,"signinpage.html")
            
        return render(request, 'signinpage.html')


def signup(request):

    if request.session.get('is_signin'):
        return render(request,"index.html")
    else:
        # booksData = BooksDetail.objects.all()

        if request.method == "POST":
            email = request.POST['email']
            pwd = request.POST['pwd']

            if LoginDetails.objects.filter(login_email=email).exists():
                messages.error(request, "Email already exists", extra_tags='signup')
                return render(request, 'signup.html')
            
            en = LoginDetails(login_email=email,login_pwd=pwd)
            en.save()
                    # request.session['is_signin'] = True
            return redirect("signin")
   
        return render(request,"signup.html")


def services(request):

    # if request.session.get('is_signin'):
    #     return redirect('services')
    
    # else :
    #     redirect("signin")
    
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

def cart(request, slug=None):
    if slug:
        booksData2 = bookColumn.objects.get(bookDB_slug=slug)
        if not cartColumn.objects.filter(item_title=booksData2.bookDB_title).exists():
            change = cartColumn(
                item_title=booksData2.bookDB_title,
                item_imglink=booksData2.bookDB_imglink,
                item_price=booksData2.bookDB_price,
                item_des=booksData2.bookDB_des,
                item_author=booksData2.bookDB_author,
                item_releaseDate=booksData2.bookDB_releaseDate,
                item_quantity=1  # Set initial quantity to 1
            )
            change.save()

    CartData = cartColumn.objects.all()

    return render(request, "cart.html", {'cartData': CartData})

def update_cart_quantity(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        action = request.POST.get('action')

        item = cartColumn.objects.get(id=item_id)
        if action == 'increase':
            item.item_quantity += 1
        elif action == 'decrease' and item.item_quantity > 1:
            item.item_quantity -= 1

        item.save()
        return redirect('cart')

def homePage(request):
    status = False

    if 'is_signin' in request.session and request.session['is_signin']:
            status = request.session['is_signin'] 
            booksData = bookColumn.objects.all()
            newsdata = News.objects.all()
            data = { 'newsdata':newsdata,'booksData':booksData,
                'status':status
            }
            return render(request,"index.html",data)

    else:
            # status = request.session['is_signin'] 
            booksData = bookColumn.objects.all()
            newsdata = News.objects.all()
            data = { 
                'status':status,'booksData':booksData
                ,'newsdata':newsdata
            }

            return render(request,"index.html",data)
    
def newsDetail(request,slug):

    newsDetail = News.objects.get(news_slug=slug)
    data={'newsDetail':newsDetail}
    return render(request,"newsdetail.html",data)

def logout(request):

    #logic for transfer data from one model to other
    # olddata = BooksDetail.objects.all()

    # for n in olddata:
    #     change = bookColumn(bookDB_title = n.book_title,bookDB_imglink = n.book_imglink,bookDB_price = '25.00$',bookDB_des = n.book_des,bookDB_author= n.book_author,bookDB_releaseDate = n.book_releaseDate)
    #     change.save()
    return redirect('home')

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


