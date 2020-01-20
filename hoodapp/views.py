from django.shortcuts import render
from .models import Hood,Biz,Member,Posts
from .forms import HoodCreateForm,BizCreateForm,HoodPostsForm,ProfileUpdateForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    hoods = Hood.objects.all()
    new_hood=HoodCreateForm(request.POST)
    if new_hood.is_valid():
        new=new_hood.save(commit=False)
        new.user=request.user
        new.save
        return HttpResponseRedirect(request.path_info)
    else:
        new_hood=HoodCreateForm()

    return render(request, 'index.html',locals())

@login_required(login_url='/accounts/login/')
def hood_details(request, id):
    details=Hood.objects.get(id=id)
    posts=Posts.objects.filter(hood=details)
    business=Biz.objects.filter(hood=details)
    biz_post=BizCreateForm(request.POST)
    create_post=HoodPostsForm(request.POST)
    if create_post.is_valid():
        post=create_post.save(commit=False)
        post.user=request.user
        post.hood=details
        post.save()

        return HttpResponseRedirect(request.path_info)
    else:
        create_post=HoodPostsForm()

    if biz_post.is_valid():
        biz=biz_post.save(commit=False)
        biz.hood=details
        biz.save()

        return HttpResponseRedirect(request.path_info)
    else:
        biz_post=BizCreateForm()

    return render(request, 'hood_detail.html', locals())

@login_required(login_url='/accounts/login/')
def search_biz(request):
    if request.method == "GET":
        search_term=request.GET.get('search')
        got_biz=Biz.objects.filter(name__icontains=search_term)[::-1]

        return render(request, 'results.html', locals())
    else:
        message="Looking for something, type it and hit search"
    return render(request, 'results.html', locals())

@login_required(login_url='/accounts/login/')
def myProfile(request,**kwargs):
    current_user=request.user
    prof_update=ProfileUpdateForm(request.POST)
    user_posts=Posts.objects.filter(user=current_user)
    if prof_update.is_valid():
        profile=prof_update.save(commit=False)
        profile.user=current_user
        profile.save()
        return HttpResponseRedirect(request.path_info)
    else:
        prof_update=ProfileUpdateForm()
    return render(request, 'profile.html', locals())
