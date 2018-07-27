from django.http import HttpResponseRedirect


def login(func):
    def login_fun(request,*args,**kwargs):
        if request.session.has_key('user_id'):
            return func(request,*args,**kwargs)
        else:
            redirect=HttpResponseRedirect('/user/login')
            redirect.set_cookie('url',request.get_full_path())
            return redirect
    return login_fun