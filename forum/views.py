from .models import Blog, Post, Order
from .forms import LoginForm, RegistrationForm, CreatingSection, BuyTickets, CreatingPost

from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseForbidden
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def log_out(request):
    logout(request)
    redirect_url = request.GET.get('next') or reverse('Index')
    return redirect(redirect_url)

def log_in(request):
    if request.method == 'POST':
        logout(request)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.GET['next'])
            else:
                form.add_error(field=None, error='Invalid credentials!')
    else: #GET
        form = LoginForm()
    return render(request, 'forum/login.html', {'form': form})



def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            logout(request)
            #blog_title = form.cleaned_data['blog_title']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_again = form.cleaned_data['password_again']
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'User already exists!')
            elif User.objects.filter(email=email).exists():
                form.add_error('email', 'User with entered e-mail already exists!')
            elif password != password_again:
                form.add_error('password_again', 'Password mismatch!')
            else:
                user = User.objects.create_user(username, email, password)
                login(request, user)

                #blog = Blog.objects.create(author=user, title=blog_title)
                #context = {'blog': blog, 'posts': []}
                #return render(request, 'forum/section.html', context)
                return get_blog_list(request)
    else:
        form = RegistrationForm()
    return render(request, 'forum/signup.html', {'form': form})

                
def get_blog_list(request):
    blogs = Blog.objects.order_by('-created_at')
    #context = {'title': blog.title, 'created_at': blog.created_at.date().isoformat()}
    context = {'blogs': blogs}
    #template = loader.get_template('forum/index.html')
    #return HttpResponse(template.render(context, request))
    return render(request, 'forum/index.html', context)

@login_required(login_url='/forum/login')
def blog(request, blog_id):
    if request.method == 'POST':
        return create_post(request, blog_id)
    else:
        return render_blog(request, blog_id)


def render_blog(request, blog_id, additional_context={}):
    blog = get_object_or_404(Blog, id=blog_id)
    
    context = {
        'blog': blog,
        'posts': blog.post_set.order_by('-created_at'),
        **additional_context
        }
    #template = loader.get_template('blogger/blog.html')
    #return HttpResponse(template.render(context, request))
    if blog.opened:
        return render(request, 'forum/opened_section.html', context)
    else:
        return render(request, 'forum/section.html', context)


def create_post(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if blog.author_id != request.user.id:
        return HttpResponseForbidden('You are not allowed to post in this blog!')
    if request.method == 'POST':
        form = CreatingPost(request.POST, request.FILES)
        if form.is_valid():
            #logout(request)
            subject = form.cleaned_data['subject']
            text = form.cleaned_data['text']
            saved_image = form.cleaned_data['review_image']
            Post.objects.create(blog=blog, subject=subject, text=text, review_image=saved_image).save()
            context = {'blog_id': blog.id}
            return HttpResponseRedirect(reverse('blog_by_id', kwargs=context) ) 
    else:
        form = CreatingPost()
    return render_blog(request, blog.id, {'form': form})
     

@login_required(login_url='/forum/login')
def create_section(request):
    if request.method == 'POST':
        form = CreatingSection(request.POST)
        if form.is_valid():
            #logout(request)
            blog_title = form.cleaned_data['blog_title']
            username = request.user.username
            password = form.cleaned_data['password']
            opened = form.cleaned_data['opened']
            user = authenticate(username=username, password=password)
            if Blog.objects.filter(title=blog_title).exists():
                form.add_error('blog_title', 'Section already exists!')
            elif user is None:
                form.add_error('password', 'Password mismatch! Enter account password')
            else:
                blog = Blog.objects.create(author=user, title=blog_title, opened=opened).save()
                context = {'blog': blog, 'posts': []}
                if not opened:
                    return render(request, 'forum/section.html', context)
                else:
                    return render(request, 'forum/opened_section.html', context)
                #return get_blog_list(request)
    else:
        form = CreatingSection()
    return render(request, 'forum/signup.html', {'form': form})


@login_required(login_url='/forum/login')
def buy_tickets(request):
        if request.method == 'POST':
            form = BuyTickets(request.POST)
            if form.is_valid():
                #logout(request)
                phone = form.cleaned_data['phone']
                adults = form.cleaned_data['adults']
                kids = form.cleaned_data['kids']
                days = int(form.cleaned_data['days'])
                if int(days) < 5:
                    cost = int(days) * (1500 * int(adults) + 750 * int(kids))
                else:
                    cost = int(days) * (1000 * int(adults) + 500 * int(kids)) 
                order = Order.objects.create(user = request.user, phone=phone, cost=cost).save()
                messages.info(request, 'Your order successfully added to DB! Your cost is %i. Check the phone. You have a new message from us!' % cost)
                return render(request, 'forum/index.html')
        else:
            form = BuyTickets()
            return render(request, 'forum/buy_tickets.html', {'form': form})
            

def index_page(request):
    return render(request, 'frontend/index.html')

def card_page(request):
    return render(request, 'frontend/card.html')

def economy_page(request):
    return render(request, 'frontend/economy.html')

def rules_page(request):
    return render(request, 'frontend/rules.html')

def contacts_page(request):
    return render(request, 'frontend/contacts.html')
