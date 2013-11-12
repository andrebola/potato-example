from google.appengine.api import users
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Post
from forms import EditPost, CreatePost

def posts(request):
    posts = Post.all().order('-created_at')
    form=CreatePost()
    if users.get_current_user():
        url = users.create_logout_url(request.get_full_path())
        url_linktext = 'Logout'
    else:
        url = users.create_login_url(request.get_full_path())
        url_linktext = 'Login'
    return render_to_response('posts.html',
                              {'url':url,
                               'url_linktext':url_linktext,
                               'posts':posts,
                               'user':users.is_current_user_admin(),
                               'form':form
                               },context_instance=RequestContext(request))


def create_post(request):
    if users.is_current_user_admin():
        if request.method=='POST':
            form=CreatePost(request.POST)
            if form.is_valid():
                post=form.save()
                post.creator=users.get_current_user()
                post.put()
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')

def edit_post(request,key):
    if users.is_current_user_admin():
        post = Post.get(key)
        user=users.get_current_user()
        if request.method == 'POST':
            form = EditPost(user,post, request.POST)
            if form.is_valid():
                form.save(post)
                return HttpResponseRedirect('/')
        elif request.method == 'GET':
            form = EditPost(user,post)
        return render_to_response('edit_post.html', {'post':post, 'form':form},context_instance=RequestContext(request))
    return HttpResponseRedirect('/')

def delete_post(request,key):
    if users.is_current_user_admin():
        post = Post.get(key)
        post.delete()
    return HttpResponseRedirect('/')