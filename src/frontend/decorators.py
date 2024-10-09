from django.contrib.auth.decorators import user_passes_test


def admin_required(function=None):
    return user_passes_test(
        lambda u: u.groups.filter(name='Admin').exists(),  
        login_url='/login'  
    )(function)

def staff_required(function=None):
    return user_passes_test(
        lambda u: u.groups.filter(name='Staff').exists(),  
        login_url='/login'
    )(function)


def accountant_required(function=None):
    return user_passes_test(
        lambda u: u.groups.filter(name='Accountant').exists(), 
        login_url='/login'
    )(function)
