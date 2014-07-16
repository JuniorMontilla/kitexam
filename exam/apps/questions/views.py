from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect, HttpResponse, Http404

from django.contrib.auth.models import User
from exam.apps.questions.forms import loginform, registerform 
from exam.apps.questions.forms import profileform

from exam.apps.questions.models  import profile
from django.contrib.auth.decorators import login_required
from exam.settings import LOGIN_URL

def index_view(request):
    messagechallenge = 'LLego el momento de mostrar lo que sabes'
    freedom = 'libertad como en libertad'
    kitmessage= 'Gana una beca y estudia Python o GNU/Linux'
    kit = 'con el empuje de kitdevelop'
    ctx = {'messageone':messagechallenge , 'messagetwo':freedom, 'messagethree':kitmessage,'messagefour':kit}
    return render_to_response('questions/index.html', ctx, context_instance=RequestContext(request))

def login_view(request):
    messagelogin = ''
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            authenticateuser = authenticate(username=username,password=password)
            if authenticateuser is not None and authenticateuser.is_active:
                login(request,authenticateuser)
                profilex = profile.objects.all()
                if profilex.filter(nickname=request.user.id, selection='Python'):
                    return HttpResponseRedirect('/python/')
                elif  profilex.filter(nickname=request.user.id, selection='Linux'):
                    return HttpResponseRedirect('/gnu/')
                else:
                    return HttpResponseRedirect('/profile/')
        else:
            messagelogin = 'Nickname y/o Clave incorrecto'
            ctx = {'form':form, 'msglogin':messagelogin}
            return render_to_response('questions/login.html', ctx, context_instance=RequestContext(request))
    form = loginform()
    ctx = {'form':form, 'msglogin':messagelogin, 'next':next}
    return render_to_response('questions/login.html', ctx, context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_view(request):
    messageregister = ''
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            first_name = User.first_name = form.cleaned_data['first_name']
            last_name = User.lastname_name = form.cleaned_data['last_name']
            nickname  =  User.username = form.cleaned_data['nickname']
            email = User.email = form.cleaned_data['email']
            password = User.password = form.cleaned_data['password']
            u = User.objects.create_user(username=nickname,first_name=first_name,last_name=last_name,email=email,password=password)
            u.save()
            return HttpResponseRedirect('/login/')
        else:
            messageregister = 'Vuelva a intentarlo'
            ctx = {'form':form, 'msgregister':messageregister}
            return 	render_to_response('questions/register.html',ctx,context_instance=RequestContext(request))
    form = registerform()
    ctx = {'form':form}
    return render_to_response('questions/register.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=LOGIN_URL)
def profile_view(request):
    messageperfil= ''
    if request.method == 'POST':
        form = profileform(request.POST, request.FILES)
        if form.is_valid():
            avatar =  form.cleaned_data['avatar']
            selection  =  form.cleaned_data['selection']
            for usr in  User.objects.all():
		p = profile(nickname=usr)
            p.avatar = avatar
	    p.selection = selection
	    p.save()
	    return HttpResponseRedirect('/')
        messageperfil = 'Vuelva a intentarlo'
	ctx={'form':form, 'messageperfil': messageperfil}
	return render_to_response('questions/profile.html',ctx,context_instance=RequestContext(request))

    form = profileform()
    ctx = {'form':form}
    return render_to_response('questions/profile.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=LOGIN_URL)
def python_view(request):
    if  request.user.profile.selection == 'Linux':
        raise Http404
    ctx = {'msgpython': 'Prueba de Python'}
    return render_to_response('questions/python.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=LOGIN_URL) 
def gnu_view(request):
    if request.user.profile.selection  == 'Python':
        raise Http404
    ctx = {'msggnu':'Purueba de GNU/Linux'}
    return render_to_response('questions/gnu.html',ctx,context_instance=RequestContext(request))

def error403(request):
	return  render(request, '403.html')
def error404(request):
	return  render(request, '404.html')
def error500(request):
	return  render(request, '500.html')
