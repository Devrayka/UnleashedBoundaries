from datetime import date
from django.db.models import Sum
from django.shortcuts import render, redirect
from myapp.models import *
from django.contrib import messages
import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":

        uid = request.session["loginid"]
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        try:
            insertdata = complaintable(userid=usertable(id=uid),subject=subject,message=message)
            insertdata.save()
            return redirect(contact)
        except:
            pass
    return render(request, 'contact.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def fetchsignupdata(request):

    username=request.POST.get("uname")
    useremail=request.POST.get("uemail")
    userphone=request.POST.get("uphone")
    userpassword=request.POST.get("upassword")
    usergender=request.POST.get("ugender")

    insertdata= usertable(name=username,email=useremail,phonenumber=userphone,password=userpassword,gender=usergender)
    insertdata.save()

    return render(request, 'login.html')

def checklogindata(request):

    useremail= request.POST.get("uemail")
    userpassword = request.POST.get("upassword")

    try:
        checkuser=usertable.objects.get(email=useremail,password=userpassword)
        request.session["loginid"]=checkuser.id
        request.session["loginname"]=checkuser.name
        request.session.save()

    except:
        checkuser= None

    if checkuser is not None:
        return redirect("/")


    else:
        print("Incorrect Password")
        messages.error(request,"Incorrect email or password")
        print(useremail)
        print(userpassword)

    return render(request, 'login.html')

from django.core.paginator import Paginator

def turf(request):
    # Get all data from pitchtable
    all_data = pitchtable.objects.all()

    # Pagination
    paginator = Paginator(all_data, 6)  # 6 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "pitchtable": page_obj,
    }
    return render(request, 'turf.html', context)


def logout(request):
    try:
        del request.session["loginid"]
        del request.session["loginname"]

    except:
        pass

    return render(request,template_name="login.html")

def booking(request , id):
    context = {
        "pitchid":id
    }
    return render(request,"booking.html",context)


def product(request):
    # Get all data from itemtable
    all_data = itemtable.objects.all()

    # Pagination
    paginator = Paginator(all_data, 6)  # 6 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "itemtable": page_obj,
    }
    return render(request, "product.html", context)

def singleturf(request, tid):
    getsingledata = pitchtable.objects.get(id=tid)
    getseconddata= turfimages.objects.filter(turfid=tid)
    context = {
        "singledata": getsingledata,
        "seconddata": getseconddata,

    }
    return render(request, 'singleturf.html', context)

def singleproduct(request, pid):
    getsingledata = itemtable.objects.get(id=pid)
    getseconddata= productimages.objects.filter(itemid=pid)
    context = {
        "singledata": getsingledata,
        "seconddata": getseconddata,
    }

    return render(request, 'singleproduct.html', context)

def addtocart(request):
    uid= request.session["loginid"]
    proid=request.POST.get("pid")
    quantity=request.POST.get("quantity")
    price= request.POST.get("price")
    total = float(price) * int(quantity)
    print(total)


    try:
        checkitemincart = carttable.objects.get(userid=uid,itemid=proid,cartstatus=0)
    except:
        checkitemincart = None

    if checkitemincart is None:
         storedata= carttable(userid=usertable(id=uid),itemid=itemtable(id=proid),quantity=quantity,cartstatus=0,total=total
                              ,orderid=0)
         storedata.save()
    else:
        checkitemincart.quantity += int(quantity)
        checkitemincart.total += float(total)
        checkitemincart.save()

    return redirect("/cart")

def cart(request):
    uid = request.session["loginid"]
    getalldata = carttable.objects.filter(userid=uid,cartstatus=0,orderid=0)
    total_amount = getalldata.aggregate(total=Sum('total'))['total']
    print(total_amount)
    context = {
        "carttable": getalldata,
        "totalamount": total_amount
    }
    print(getalldata)
    return render(request, 'cart.html', context)

def increaseitem(request , id):
    getdata = carttable.objects.get(id=id)
    getdata.quantity += 1
    getdata.total += getdata.itemid.price
    getdata.save()
    return redirect("/cart")

def decreaseitem(request , id):
    getdata = carttable.objects.get(id=id)
    getdata.quantity -= 1
    getdata.total -= getdata.itemid.price
    getdata.save()
    return redirect("/cart")

def deleteitem(request, id):

    getturf= carttable.objects.get(id=id)
    getturf.delete()

    return redirect("/cart")

def fetchturfdata(request):
    pid = request.POST.get("pitchid")
    uid = request.session["loginid"]
    name=request.POST.get("uname")
    phone=request.POST.get("uphone")
    bdate=request.POST.get("udate")
    btime=request.POST.get("utime")
    payment = request.POST.get("payment")

    if bookingtable.objects.filter(pitchid=pitchtable(id=pid), bookingdate=bdate, bookingtime=btime).exists():
        messages.error(request, "Selected Slot Is Allready Booked")
        return redirect(index)

    insertdata = bookingtable(userid=usertable(id=uid),pitchid=pitchtable(id=pid),name=name,phonenumber=phone,bookingdate=bdate,bookingtime=btime,paymentmode=payment)
    insertdata.save()

    return redirect("/booked")

def booked(request):
    getalldata = bookingtable.objects.all()
    context ={
        "bookedtable": getalldata
    }
    return render(request,'booked.html',context)


def deleteturf(request, id):

    getturf= bookingtable.objects.get(id=id)
    getturf.delete()

    return redirect("/booked")


def placeorderpage(request):
    uid = request.session["loginid"]
    cartdata = carttable.objects.filter(userid=usertable(id=uid),orderid=0,cartstatus=0).aggregate(Sum('total'))
    data = cartdata.get('total__sum')
    context = {
        'data':data
    }
    return render(request,"placeorderproduct.html",context)

def placeorderproduct(request):
    uid = request.session["loginid"]
    phone = request.POST.get("phone")
    address = request.POST.get("address")
    finaltotal = request.POST.get("totalbill")
    payment = request.POST.get("payment")

    # print(uid)
    # print(phone)
    # print(address)
    # print(finaltotal)
    # print(payment)


    storedata = ordertable(userid=usertable(id=uid), phonenumber=phone, address=address, totalbill=finaltotal,
                           paymentmode=payment, orderstatus="confirmed")
    storedata.save()

    lastid = storedata.id  # fetch last inserted id in order
    getdata = carttable.objects.filter(userid=uid, cartstatus=0)
    print(getdata)

    for i in getdata:
        i.cartstatus = 1
        i.orderid = lastid
        i.save()

    # messages.success(request, "order placed successfully")
    return redirect(showorders)

def showorders(request):
    uid = request.session["loginid"]
    getdata = ordertable.objects.filter(userid=uid)
    context = {
        "orderdata":getdata
    }

    return render(request,'showorders.html', context)



def cancelorder(request,id):
    getorderdata = ordertable.objects.get(id=id)
    getorderdata.orderstatus = "cancelled"
    getorderdata.save()
    messages.success(request,"order cancelled succesfully")
    return redirect("/showorders")

def singleorder(request , id):
    getitemdata = carttable.objects.filter(orderid=id)
    context = {
        "cartdata":getitemdata
    }
    return render(request,"singleorder.html",context)


from django.db.models import Q
def findproduct(request):
    query = request.POST.get("query")
    finddata = itemtable.objects.filter(Q(name__icontains=query) | Q(catid__name__icontains=query) | Q(price__icontains=query) | Q(brand__icontains=query))
    context = {
        "itemtable": finddata
    }
    print(context)
    return render(request,"product.html", context)


def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        rating = request.POST.get("rating")
        comment = request.POST.get("review")

        try:
            insertdata = feedbacktable(name=name,rating=rating,comment=comment)
            insertdata.save()
            return redirect(feedback)
        except:
            pass
    return render(request, "feedback.html")



def forgotpasswordpage(request):
    return render(request, "forgotpassword.html")


def forgotpassword(request):
    if request.method == 'POST':
        username = request.POST.get('email')

        try:
            user = usertable.objects.get(email=username)

        except usertable.DoesNotExist:
            user = None

        if user is not None:
            #################### Password Generation ##########################
            import random
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

            nr_letters = 6
            nr_symbols = 1
            nr_numbers = 3
            password_list = []

            for char in range(1, nr_letters + 1):
                password_list.append(random.choice(letters))

            for char in range(1, nr_symbols + 1):
                password_list += random.choice(symbols)

            for char in range(1, nr_numbers + 1):
                password_list += random.choice(numbers)

            print(password_list)
            random.shuffle(password_list)
            print(password_list)

            password = ""  #we will get final password in this var.
            for char in password_list:
                password += char

            ##############################################################


            msg = "hello here it is your new password  "+password   #this variable will be passed as message in mail

            ############ code for sending mail ########################

            from django.core.mail import send_mail

            send_mail(
                'Your New Password',
                msg,
                'devinfolabz@gmail.com',
                [username],
                fail_silently=False,
            )

            #now update the password in model
            cuser = usertable.objects.get(email=username)
            cuser.password = password
            cuser.save(update_fields=['password'])

            print('Mail sent')
            messages.info(request, 'mail is sent successfully to your registered email')
            return redirect(index)
        else:
            messages.info(request, 'This account does not exist')
    return redirect(index)

