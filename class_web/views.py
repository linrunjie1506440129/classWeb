from django.shortcuts import render
from .models import ClassActive,ClassNews,ClassNote,MessageBox,UserProfile
from .forms import MessForm,NewsForm,NoteForm,ActiveForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

def index(request):
    clane=ClassNews.objects.order_by('date_added')
    clasc=ClassActive.objects.order_by('date_added')
    clano=ClassNote.objects.order_by('date_added')
    context={'clane':clane,'clasc':clasc,'clano':clano}
    return render(request,'class_web/index.html',context)

def news(request):
    clane=ClassNews.objects.order_by('date_added')
    context={'clane':clane}
    return render(request,'class_web/news.html',context)

def notes(request):
    clano=ClassNote.objects.order_by('date_added')
    context={'clano':clano}
    return render(request,'class_web/notes.html',context)

def actives(request):
    clasc=ClassActive.objects.order_by('date_added')
    context={'clasc':clasc}
    return render(request,'class_web/actives.html',context)

def new(request,news_id):
    new=ClassNews.objects.get(id=news_id)
    context={'new':new}
    return render(request,'class_web/new.html',context)

def note(request,note_id):
    note=ClassNote.objects.get(id=note_id)
    context={'note':note}
    return render(request,'class_web/note.html',context)

def active(request,active_id):
    active=ClassActive.objects.get(id=active_id)
    context={'active':active}
    return render(request,'class_web/active.html',context)

def download(request):
    return render(request,'class_web/download.html')

def messge(request):
    if request.method != 'POST':
        form = MessForm()
    else:
        form = MessForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('class_web:messge'))
    messger = MessageBox.objects.order_by('-time')
    context = {'form':form,'messger':messger}
    return render(request,'class_web/messge.html',context)


def acc_login(request):
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(username = request.POST.get('username'),
                            password = request.POST.get('password')
                            )
        if user is not None:
            login(request,user) 
            return HttpResponseRedirect('edito') 
        else:
            login_err = '嗷，你密码错了小老弟'
            return render(request,'class_web/login.html',{'login_err':login_err})
    return render(request,'class_web/login.html')

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def adminindex(request):
    if request.method == 'POST':
        nf=NoteForm(request.POST)
        ef=NewsForm(request.POST)
        af=ActiveForm(request.POST)
        if nf.is_valid():
            nf.save()
            return HttpResponseRedirect(reverse('class_web:adminindex'))
        elif ef.is_valid():
            ef.save()
            return HttpResponseRedirect(reverse('class_web:adminindex'))
        else:
            af.save()
            return HttpResponseRedirect(reverse('class_web:adminindex'))
    return render(request,'class_web/adminedito.html')