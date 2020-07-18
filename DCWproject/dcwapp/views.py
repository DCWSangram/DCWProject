from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import *
from .forms import *
from django.core.mail import send_mail
from random import randint
from django.contrib import messages
# Create your views here.
def otp_generate():
    return randint(1010,9999)

def home_view(request):
    return render(request,'dcwapp/home.html')

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            request.session['username'] = form.cleaned_data['email']
            request.session['fullname'] = form.cleaned_data['full_name']
            request.session['pwd'] = form.cleaned_data['password']
            request.session['mobile'] = form.cleaned_data['mobile_number']
            request.session['gender'] = form.cleaned_data['gender']
            try:
                data = User.objects.get(username=request.session['username'])
                return render(request,'dcwapp/signup.html',{"error1":"Email alreday registered..choose anothe one...","form":form})
            except User.DoesNotExist:
                try:
                    data = CustomerInformation.objects.get(mobile_number=request.session['mobile'])
                    return render(request,'dcwapp/signup.html',{"error2":"Mobile Number already registered...","form":form})
                except (CustomerInformation.DoesNotExist,IntegrityError):
                    request.session['OTP']= str(otp_generate()) # OTP Generated and session management starts
                    # write code for sendin sms to the mobile number. To get user mobile number ---> request.session['mobile']
                    return redirect("/dcw/mobileverification/")
        else:
            return render(request,'dcwapp/signup.html',{"form":form})
    else:
        form = SignupForm()
        return render(request,'dcwapp/signup.html',{"form":form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if "@" in username:
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                request.session['username'] = username
                messages.success(request,'Login Successfully')
                request.session.set_expiry(24*60*3600)
                return redirect('/dcw/dashboard')
            else:
                return render(request,'dcwapp/login.html',{"error":"Invalid Credential"})
        else:
            mobile_number = request.POST.get('username','')
            try:
                c = CustomerInformation.objects.get(mobile_number=mobile_number)
                user = authenticate(username=c.user.username,password=password)
                if user is not None:
                    request.session['username'] = c.user.username
                    login(request,user)
                    messages.success(request,'Login Successfully')
                    request.session.set_expiry(24*60*3600)
                    return redirect("/dcw/dashboard/")
                else:
                    return render(request,'dcwapp/login.html',{"error":"Invalid Credential"})
            except CustomerInformation.DoesNotExist:
                return render(request,'dcwapp/login.html',{"error":"Invalid Credentials"})
    else:
        return render(request,'dcwapp/login.html')
 
def mobile_verification(request):
    if request.method == "POST":
        user_otp = request.POST.get('otp','')
        if user_otp == request.session['OTP']:
            user = User.objects.create_user(username=request.session['username'],password=request.session['pwd'])
            c = CustomerInformation(user=user,full_name=request.session['fullname'],mobile_number=request.session['mobile'],gender=request.session['gender']).save()
            login(request,user)
            request.session.set_expiry(24*60*3600)
            del request.session['OTP']
            return redirect("/dcw/dashboard/")
        else:
            request.session.set_expiry(300)
            return render(request,'dcwapp/mobile_verification.html',{'otp_error':'Invalid OTP'})
    else:
        print(request.session["OTP"])
        return render(request,'dcwapp/mobile_verification.html',{'mobile_number':request.session['mobile']})
@login_required(login_url='/dcw/login/')
def dashboard_view(request):
    try:
        data = User.objects.get(username=request.session['username'])
        c = CustomerInformation.objects.get(id=data.custuser.id)
        data2 = VehicleDetails.objects.filter(customer_name=c).order_by('-created_at')
        return render(request,'dcwapp/dashboard.html',{"vehicle":data2,'data':data})
    except VehicleDetails.DoesNotExist:
        return render(request,'dcwapp/dashboard.html',{"data":data})

@login_required(login_url='/dcw/login/')
def add_address(request,id):
    u = User.objects.get(id=id)
    c = CustomerInformation.objects.get(user=u)
    # ca = CustomerAddress.objects.get(customer_info=c)
    if request.method == "POST":
        if request.POST['address'] == "individual":
            area = request.POST.get('area','')
            lane_number = request.POST.get('lane','')
            house_number = request.POST.get('house','')
            address1 = request.POST.get('address1','')
            address2 = request.POST.get('address2','')
            city = request.POST.get('city','')
            state = request.POST.get('state','')
            pin = request.POST.get('pin','')
            CustomerAddress.objects.create(customer_info=c,area=area,lane_number=lane_number,House_no=house_number,address_line1=address1,address_line2=address2,city=city,state=state,zipcode=pin).save()
            return redirect("/dcw/dashboard")
        elif request.POST['address'] == "appartment":
            appartment_name = request.POST.get('apptname',"")
            tower_no = request.POST.get('towno',"")
            flat_number = request.POST.get('fltno',"")
            address_lin1 = request.POST.get('address1',"")
            address_lin2 = request.POST.get('address2',"")
            city = request.POST.get('city',"")
            state = request.POST.get('state',"")
            pin = request.POST.get('pin',"")
            CustomerAddress.objects.create(customer_info=c,appt_name=appartment_name,block_name=tower_no,House_no=flat_number,address_line1=address1,address_line2=address2,city=city,state=state,zipcode=pin).save()
            return redirect("/dcw/dashboard")
        return redirect("dcwapp/dashboard.html")
    else:
        return render(request,'dcwapp/addressform.html')
@login_required(login_url='/dcw/login/')
def update_address(request,id):
    u = User.objects.get(id=id)
    c = CustomerInformation.objects.get(user=u)
    ca = CustomerAddress.objects.get(customer_info=c)
    if request.method == "POST":
        apppt_name = request.POST.get("apptname"," ")
        area = request.POST.get("area"," ")
        block_name = request.POST.get("blockname"," ")
        house_no = request.POST.get("houseno"," ")
        lane_no = request.POST.get("laneno"," ")
        address1 = request.POST.get("address1"," ")
        address2 = request.POST.get("address2"," ")
        city = request.POST.get("city"," ")
        zipcode = request.POST.get("zipcode"," ")
        state = request.POST.get("state"," ")
        ca.appt_name = apppt_name
        ca.area = area
        ca.lane_number = lane_no
        ca.block_name = block_name
        ca.House_no = house_no
        ca.address_line1 = address1
        ca.address_line2 = address1
        ca.city = city
        ca.state = state
        ca.zipcode = zipcode
        ca.save()
        return redirect("/dcw/dashboard/")
    else:
        return render(request,'dcwapp/updateaddressform.html',{'userdata':u})
@login_required(login_url='/dcw/login/')
def add_vehicle(request,id):
    if request.method == "POST":
        c = CustomerInformation.objects.get(id=id)
        v = VehicleDetails.objects.create(customer_name=c,vehicle_brand=request.POST.get('brand',''),vehicle_model=request.POST.get('model',''),vehicle_category=request.POST.get('category',''),vehicle_number=request.POST.get('number',''),Fuel_type=request.POST.get('fuel',''),vehicle_color=request.POST.get('colour',''),parking_lot_no=request.POST.get('lot',''),parking_area=request.POST.get('area',''),preferred_time=request.POST.get('time')).save()
        return redirect("/dcw/dashboard")
    else:
        return render(request,'dcwapp/addvehicle.html')

def logout_view(request):
    logout(request)
    request.session.clear()
    return redirect("/dcw/")

def forgot_password(request):
    if request.method == "POST":
        request.session['otp_for_password_reset'] = x = str(otp_generate())
        email = request.POST['email']
        try:
            user = User.objects.get(username=email)
            request.session['username_for_password_reset'] = user.username
            send_mail("Password Reset From Daily Car Wash",f"Your OTP: {request.session['otp_for_password_reset']}","sangram@blog.com",[email,],fail_silently=True)
            return render(request,'dcwapp/confirm.html',{"email":email})
        except User.DoesNotExist:
            return render(request,'dcwapp/forgotpassword.html',{"error":"This Email ID is not registered"})
    else:
        return render(request,'dcwapp/forgotpassword.html')

def password_validate_otp(request):
    if request.method == "POST":
        password_otp = request.POST.get('passwordotp','')
        if request.session['otp_for_password_reset'] == password_otp:
            return redirect('/dcw/reset-password')
        else:
            return render(request,'dcwapp/confirm.html',{"error":"Invalid OTP"})
def reset_password(request):
    if request.method == 'POST':
        u = User.objects.get(username=request.session['username_for_password_reset'])
        u.set_password(request.POST['pwd1'])
        u.save()
        messages.success(request,'Password Reset Successfully')
        return redirect("/dcw/login")
    else:
        if 'otp_for_password_reset' in request.session:
            del request.session['otp_for_password_reset']
            return render(request,'dcwapp/resetpassword.html')
        else:
            return redirect('/dcw/forgot-password')

def reset_password2(request):
    return render(request,'dcwapp/reset.html')

def reset_password_via_mobile(request):
    if request.method == "POST":
        try:
            request.session['otp_for_mobile'] = str(otp_generate())
            print(request.session['otp_for_mobile'])
            c = CustomerInformation.objects.get(mobile_number=request.POST['mobile'])
            request.session['mobile_number'] = request.POST['mobile']
            return render(request,'dcwapp/mobileotp.html',{"mobile":request.session['mobile_number']})
        except CustomerInformation.DoesNotExist:
            return render(request,'dcwapp/passwordresetmobile.html',{"invlid_mobile":"Please Enter Registed Mobile Number"})
    else:
        return render(request,'dcwapp/passwordresetmobile.html')

def validate_otp_mobile(request):
    if request.method == "POST":
        if request.session['otp_for_mobile'] == request.POST['otpmobile']:
            return redirect("/dcw/reset-password3")
        else:
            return render(request,'dcwapp/mobileotp.html',{"invlid_otp":"Invalid OTP","mobile":request.session['mobile_number']})

def reset_password3(request):
    if request.method == 'POST':
        c = CustomerInformation.objects.get(mobile_number = request.session['mobile_number'])
        u1 = User.objects.get(username=c.user.username)
        u1.set_password(request.POST['pwd1'])
        u1.save()
        messages.success(request,'Password Reset Successfully')
        return redirect("/dcw/login")
    else:
        if 'otp_for_mobile' in request.session:
            del request.session['otp_for_mobile']
            return render(request,'dcwapp/resetpassword.html')
        else:
            return redirect('/dcw/forgot-password')