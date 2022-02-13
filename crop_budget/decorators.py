from django.shortcuts import redirect

def unauthenticated_user(redirect_url='home'):
    def wrapped_func(view_func):
        def wrapper_func(request,*args,**kwags):
            if request.user.is_authenticated:
                return redirect(redirect_url)
            else:
                return view_func(request,*args,**kwags)
        return wrapper_func
    return wrapped_func
