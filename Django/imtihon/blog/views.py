from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post,Contact,Kor
from django.core.mail import EmailMessage
def index(request):
    post1=Post.objects.all()
    data=get_object_or_404(Kor,id=1)
    data.son=data.son+1
    data.save()
    context={
        'post1':post1,
        'data':data.son
    }
    return render(request,'index.html',context)
def about(request):
    data = get_object_or_404(Kor, id=1)
    data.son = data.son + 1
    data.save()
    context = {
        'data': data
    }
    return render(request,'about.html')
def contact(request):
    data1 = get_object_or_404(Kor, id=1)
    data1.son = data1.son + 1
    data1.save()
    context={
        'data': data1.son
             }
    if request.method == 'POST':
        name = request.POST['ism']
        email = request.POST['email']
        text = request.POST['text']
        data=Contact(name=name,email=email,text=text)
        data.save()
        context['status']=f'Xurmatli {name} sizni xabaringiz yuborildi!'
    return render(request, 'contact.html',context)
def post(request):
    post1 = Post.objects.all()
    data = get_object_or_404(Kor, id=1)
    data.son = data.son + 1
    data.save()
    context = {
        'post1': post1,
        'data': data.son
    }
    return render(request, 'post.html', context)
def postDetails(request,pk):
    post10=get_object_or_404(Post,pk=pk)
    post10.views=post10.views+1
    post10.save()
    data = get_object_or_404(Kor, id=1)
    data.son = data.son + 1
    data.save()
    context={'post':post10,
             'data': data.son
             }
    return render(request, 'postdetails.html',context)

