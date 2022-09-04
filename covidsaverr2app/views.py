from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from pyexpat.errors import messages
from django.contrib import messages
from covidsaverr2app.forms import UserRegisterForm
from .models import covidappUser, Grad, Restoran, Person
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import kadesteform
from .forms import welcomeform
from .forms import kadesakateform
from .forms import statusform


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserRegisterForm()
    return render(request=request, template_name="register.html", context={"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def homepage(request):
    return render(request, 'homepage.html')


def welcome(request):
    if request.method == "POST":
        form_data = welcomeform(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            welcome = form_data.save(commit=False)

            welcome.cover_image = form_data.cleaned_data['cover_image']
            welcome.save()

    # context = {"books": queryset, "Date": datetime.now().date(), "form": BookForm}
    context = {'welcome': welcomeform}
    return render(request, 'welcome.html', context)


def kadesakate(request):
    context = {'kadesakate': kadesakateform}

    return render(request, 'kadesakate.html', context)


def status(request):
    if request.method == "POST":
        form_data = statusform(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            statusf = form_data.save(commit=False)
            statusf.first_name = form_data.cleaned_data['first_name']

            statusf.save()
    context = {'status': statusform}
    return render(request, 'status.html', context)


def kadeste(request):
    context = {'form': kadesteform}

    return render(request, 'kadeste.html', context)


def load_restorani(request):
    grad_id = request.GET.get('grad')
    restoran = Restoran.objects.filter(grad_id=grad_id)

    return render(request, 'restoran_dropdown_list_options.html', {'restoran': restoran})
