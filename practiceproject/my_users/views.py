from django.shortcuts import render
from my_users.models import Users
from . import forms
# Create your views here.


def index(request):
    index_dic = {}
    return render(request, 'my_users/index.html', context=index_dic)


def help_page(request):
    help_dic = {}
    return render(request, 'my_users/help.html', context=help_dic)


def user_page(request):
    user_list = Users.objects.order_by('last')
    users_dic = {'user_list': user_list}
    return render(request, 'my_users/users.html', context=users_dic)


def add_users(request):
    form = forms.AddUser()

    if request.method == "POST":
        form = forms.AddUser(request.POST)

        if form.is_valid():
            print("Form Validated. Adding User.")
            """
            first = form.cleaned_data['first']
            last = form.cleaned_data['last']
            email = form.cleaned_data['email']
            """

            form.save(commit=True)
            return index(request)

            print("User added")
        else:
            print("ERROR FORM INVALID")

    return render(request, 'my_users/add_user.html', {'form': form})

