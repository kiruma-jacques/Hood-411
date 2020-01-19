from django.shortcuts import render
from .models import Hood,Biz,Member,Posts
from .forms import HoodCreateForm,BizCreateForm,HoodPostsForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    hoods = Hood.objects.all()
    return render(request, 'index.html',{'hoods':hoods})

def hood_details(request, id):
    details=Hood.objects.get(id=id)

    posts=Posts.objects.filter(hood=details.id)
    business=Biz.objects.filter(hood=details.id)

    create_post=HoodPostsForm(request.FILES,request.POST)
    biz_post=BizCreateForm(request.FILES, request.POST)
    if create_post.is_valid() and biz_post.is_valid():
        post=create_post.save(commit=False)
        post.user=request.user
        post.hood=current_hood
        post.save()

        biz=biz_post.save(commit=False)
        biz.hood=current_hood
        biz.save()
        return HttpResponseRedirect(request.path_info)
    else:
        create_post=HoodPostsForm()
        biz_post=BizCreateForm()

    return render(request, 'hood_detail.html', locals())

def search_title(request):
    if request.method == "GET":
        search_term=request.GET.get('search')
        got_biz=Biz.objects.filter(name__icontains=search_term)[::-1]
        
        return render(request, 'results.html', locals())
    else:
        message="Looking for something, type it and hit search"
    return render(request, 'results.html', locals())
