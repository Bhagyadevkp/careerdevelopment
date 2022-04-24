from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

from accounts.models import Student
from careers.models import Job




# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1'] 
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect ('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                print("User Created")
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'registration.html')


def register_company(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        company_email = request.POST['company_email']
        company_password1 = request.POST['company_password1'] 
        company_password2 = request.POST['company_password2']
        if company_password1 == company_password2:
            if User.objects.filter(username=company_name).exists():
                messages.info(request, "Username Taken")
                return redirect('register_company')
            elif User.objects.filter(email=company_email).exists():
                messages.info(request, "Email Taken")
                return redirect ('register_company')
            else:
                user = User.objects.create_user(username=company_name, email=company_email, password=company_password1,is_staff=True)
                user.save()
                # print("User Created")
        else:
            messages.info(request, "Password not matching")
            return redirect('register_company')
    else:
        return render(request, 'company-signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')





# PROFILE VIEW
def profile(request):
    user=User.objects.get(pk=request.user.id)
    if user.is_staff:
        if request.method == 'POST':
            company_description = request.POST.get('company_description')
            image1 = request.FILES.get('image1')
            image2 = request.FILES.get('image2')
            image3 = request.FILES.get('image3')
            vacancy = request.POST.get('vacancy')
            post = request.POST.get('post')
            contact = request.POST.get('contact')
            company = user.id
            ob = Job(company_name_id=company, company_description=company_description, image1=image1, image2=image2, image3=image3, vacancy=vacancy, post=post, contact=contact)
            ob.save()
            print("Job added")
            return redirect('profile')
        else:
            obj=Job.objects.filter(company_name_id=user.id)
            return render(request, 'admin.html', {'jobs': obj})
    else:
        if request.method == 'POST':
            email = user.id
            qualification = request.POST.get('qualification')
            resume = request.FILES.get('resume')
            us= Student(qualification=qualification, email_id=email, resume=resume) 
            us.save()
            return redirect('profile')
        else:
            usr = Student.objects.filter(email_id= user.id)
            # for i in usr:
                # print(i.qualification)
            return render(request, 'userprofile.html', {'usr':usr,})

