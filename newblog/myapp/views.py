from django.shortcuts import render ,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.core.paginator import Paginator
from .models import user,article
from .ver import hashs,get_verification
from django.core.mail import send_mail,message
from django.conf import settings
from .translate import words,sentences
# Create your views here 

#首页
def index(request):
    username = request.session.get('username','游客')
    allarticle = article.articles.all()
    return render(request,'myapp/index.html',{'articles':allarticle,'username':username})





#文章的发布,管理，增删改查！
def articles_by_id(request,article_id):
    username = request.session.get('username','游客')
    article_context = article.articles.get(pk = article_id)
    return render(request,'myapp/article.html',{'article':article_context,'username':request.session.get('username','游客')})


def myarticle_by_id(request,article_id):
    username = request.session.get('username','游客')
    article_context = article.articles.get(pk = article_id)
    if (username == '游客'):
        mean  = "游客状态下暂无权限！"
        return render(request,'myapp/redirect_login.html',{'mean':mean})
    elif(username == article_context.aemail.username):
        request.session['id'] = article_id
        return render(request,'myapp/change_article.html',{'username':username,'article':article_context})
    else:
        mean = "您无权限修改此用户的文章！"
        return render(request,'myapp/redirect_index.html',{'mean':mean})

def change_article(request):
    try:
        idc = request.session.get('id')
        article_class = article.articles.get(pk =idc)
        article_class.title = request.POST['msg-title']
        article_class.context = request.POST['msg-context']
        article_class.save()
        mean = '修改成功!'
        return render(request,'myapp/redirect_index.html',{'mean':mean})
    except:
        mean = '修改失败'
        return render(request,'myapp/redirect_index.html',{'mean':mean})


def create_article(request):
    
    return render(request,'myapp/create_article.html',{'username':request.session.get('username','游客')})

def release(request):
    username = request.session.get('username','游客')
    if(username == "游客"):
        mean = "必须登录才能发布文章"
        return render(request,'myapp/redirect_login.html',{'mean':mean})
    else:
        try:
            userclass = user.users.get(username = username)
            title = request.POST['msg_title']
            context = request.POST['msg_context']
            article.articles.create_article(title,context,userclass)
            status = '发布成功！'
            return render(request,'myapp/redirect_index.html',{'mean':status})
        except:
            status = '发布失败！'
            return render(request,'myapp/redirect_index.html',{'mean':status})

def article_manage(request):

    username = request.session.get('username','游客')
    if (username =='游客'):
        mean = "请先登录"
        return render(request,'myapp/redirect_login.html',{'mean':mean})
    else:    
        one = user.users.get(username=username)
        all = article.articles.all()
        article_lists = user.users.users_aticle(all,one)
        return render(request,'myapp/article_manage.html',{'username':username,'articles':article_lists})


#登录登出cookie清除
def quits(request):
    request.session.clear()
    return redirect('/index/')


def logins(request):
    status = request.session.get('username','游客')
    if (status=='游客'):
         return render(request,'myapp/logins.html',{'username':status})
    else:
        mean = "已登录"
        return render(request,'myapp/redirect_index.html',{'mean':mean})


def logining(request):
    email = request.POST['email']
    try:
        a = user.users.get(pk = email)
        password = request.POST['password']
        print(hashs(password),a.password)
        if (hashs(password)==a.password):
            request.session['username'] = a.username
            request.session.set_expiry(0)
            mean = "登录成功"
            return render(request,'myapp/redirect_index.html',{'mean':mean})
        else:
            mean = "登录失败（密码错误）"
            return render(request,'myapp/redirect_index.html',{'mean':mean})
    except:
        mean = "该用户不存在"
        return render(request,'myapp/redirect_index.html',{'mean':mean})


def logouts(request):
    request.session.clear()
    return redirect('/index/')




#用户的注册，邮件验证！


def register(request):
    return render(request,'myapp/register.html',{'username':request.session.get('username','游客')})



def registering(request):
    email = request.POST['email']
    username = request.POST['username']
    try:
        user.users.get(pk=email)
        mean = "该用户已存在！"
        return render(request,'myapp/redirect_register.html',{'mean':mean})
    except:
        right_capital = request.session.get('ver')
        username = request.POST['username']
        password = hashs(request.POST['password'])
        ver = request.POST['ver']
        if(right_capital.upper()==ver.upper()):
            user.users.create_user(username,email,password)
            mean = "注册成功！"
            return render(request,'myapp/redirect_login.html',{'mean':mean})
        else:
            mean = "注册失败！"
            return render(request,'myapp/redirect_register.html',{'mean':mean})

def emails(request):
    request.session.clear()
    email = request.GET['info']
    try :
        user.users.get(pk = email)
        fail = ['该用户已存在！']
        return JsonResponse({'data':fail})
    except:
        status = ['验证码已发送！']
        lists = [email]
        capital = get_verification()
        request.session['ver'] = capital
        request.session.set_expiry(300)
        send_mail('验证码！',capital,settings.EMAIL_FROM,lists,fail_silently=True) 
        return JsonResponse({'data':status})

def search_username(request):
    username = request.GET['username']
    try:
        user.users.get(username=username)
        status = ['该用户名已存在']
        return JsonResponse({'data':status})
    except:
        status = ['该用户名可以注册']
        return JsonResponse({'data':status})





#密码的修改！

def userinfo(request):
    username = request.session.get('username','游客')
    if (username =="游客"):
        return redirect('/logins/')
    else:
        usernames = request.GET['usernames']
        try:
            one = user.users.get(username = usernames)
            return render(request,'myapp/userinfo.html',{'username':one.username,'email':one.email})
        except:
            return HttpResponse(usernames)
    return render(request,'myapp/userinfo.html')


def change(request):
    username = request.session.get('username','游客')
    if (username =='游客'):
        return redirect('/logins/')
    else:
        try:
            newpassword = request.POST['password']
            one = user.users.get(username = username)
            one.password = hashs(newpassword)
            one.save()
            request.session.clear()
            mean = "密码修改成功"
            return render(request,'myapp/redirect_login.html')
        except:
            mean = "密码修改失败"
            return render(request,'myapp/redirect_index.html')







#翻译功能！
def translate(request):
    username = request.session.get('username','游客')
    return render(request,'myapp/translate.html',{'username':username})


def word_translates(request):
    context = request.GET['word']
    print(context)
    result = words(context)
    return JsonResponse({'data':result})

def sentence_translates(request):
    context = request.GET['sentence']
    print(context)
    result =sentences(context)
    return JsonResponse({'data':result})












def test(request):
    username = request.session.get('username','游客')
    return render(request,'myapp/tests.html',{'username':username})




def resume(request):
    return render(request,'myapp/resume.html')




# def successful(request):
#     return render(request,'myapp/successful.html')


# def fail(request):
#     return render(request,'myapp/fail.html')