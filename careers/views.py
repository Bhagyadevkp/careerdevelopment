from django.shortcuts import render, redirect
from careers.models import career,Job
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    obj = career.objects.all()
    job = Job.objects.all()
    return render(request, 'index.html', {'careers': obj, 'jobs': job})


def detail(request, career_id):
    obj = career.objects.get(id=career_id)
    return render(request, 'career-detail.html', {'career': obj})


def jobs(request):
    if request.method == 'POST':
        company_description = request.POST.get('company_description')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        vacancy = request.POST.get('vacancy')
        post = request.POST.get('post')
        contact = request.POST.get('contact')
        company = User.objects.get(pk=request.user.id)
        ob = Job(company_name_id=company.id, company_description=company_description, image1=image1, image2=image2, image3=image3, vacancy=vacancy, post=post, contact=contact)
        ob.save()
        print("Job added")
        return redirect('jobs')
    else:
        obj=Job.objects.all()
        return render(request, 'admin.html', {'jobs': obj})


# UPDATE JOBS

def update(request,id):
    if request.method == 'POST':
        # company_name = request.POST.get('company_name')
        company_description = request.POST.get('company_description')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        vacancy = request.POST.get('vacancy')
        post = request.POST.get('post')
        contact = request.POST.get('contact')
        job = Job.objects.get(id=id)
        # job.company_name = company_name
        job.company_description = company_description
        job.image1 = image1
        job.image2 = image2
        job.image3 = image3
        job.vacancy = vacancy
        job.post = post
        job.contact = contact
        job.save()
        print("Job updated")
        return redirect('/')
    else:
        obj = Job.objects.get(id=id)
        return render(request, 'update.html', {'job': obj})


# DELETE JOBS

def delete(request,id):
    if request.method =='POST':
        job = Job.objects.get(id=id)
        job.delete()
        print("Job deleted")
        return redirect('/')
    return render(request, 'delete.html')

def jobdetail(request, job_id):
    obj = Job.objects.get(id=job_id)
    return render(request, 'job-detail.html', {'job':obj})



