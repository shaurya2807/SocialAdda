
from django.shortcuts import redirect, render
from first_app.forms import formName, AddComment
from django import forms
from first_app.models import Conf, Comment
from django.views import generic

# Create your views here.

def start(request):
    return render(request, 'first_app/start.html')

def confFill(request):
    form = formName()
    if request.method == 'POST':
        form = formName(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return start(request)
        else:
            print('ERROR IN FORM')
    cd = {'form':form}
    return render(request, 'first_app/confFill.html', cd)

def okok(request, cpk):
    pls = Conf.objects.get(pk=cpk)
    pls.visible = True
    pls.save()
    return redirect('/first_app/adminList/')



def adminList(request):
    lis = Conf.objects.all()
    if request.method == 'POST':   
        pls = Conf.objects.get(pk=request.POST.get('id'))
        pls.visible = True
        pls.save()
        
    return render(request, 'first_app/adminList.html', {'object_list':lis})


def deleteView(request, cpk):
    target = Conf.objects.get(pk = cpk)
    target.delete()
    return redirect('/first_app/adminList/')

class confList(generic.ListView):
    model = Conf
    template_name = 'first_app/confList.html'

def postDetail(request, cpk):
    all_comments = Comment.objects.all()
    target = Conf.objects.get(pk = cpk)
    commentForm = AddComment()
    if request.method == 'POST':
        newObject = Comment(text = request.POST['text'], id_conf = cpk)
        newObject.save()
        return redirect(request.META['HTTP_REFERER'])
        
    return render(request, 'first_app/postPage.html', {'conf':target, 'commentForm':commentForm, 'all_comments':all_comments})
