from django.shortcuts import render,redirect
from .models import Poll
from .form import poll_form
# Create your views here.
from django.http import HttpResponse
def home(request):
    polls = Poll.objects.all()
    context = {'polls': polls}
    return render(request,'poll/home.html',context)
def create(request):
    form=poll_form()
    poll=Poll.objects.all()
    if request.method == 'POST':
        form = poll_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'poll':poll,'form':form}
    return render(request,'poll/create.html',context)
def result(request,poll_id):
    polls= Poll.objects.get(id=poll_id)
    context = {'polls': polls}

    return render(request,'poll/result.html',context)
def vote(request,poll_id):
    polls= Poll.objects.get(id=poll_id)
    if request.method == 'POST':
        select_value=request.POST['poll']
        if select_value == 'option1':
            polls.poll_one_count+=1
        elif select_value == 'option2':
            polls.poll_two_count += 1
        elif select_value == 'option3':
            polls.poll_third_count += 1
        else:
            return HttpResponse(400,'invalid form')
        polls.save()
        return redirect('result',polls.id)
    context = {'polls': polls}

    return render(request,'poll/vote.html',context)