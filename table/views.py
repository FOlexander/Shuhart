import time

from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView

from table.datastruc import read_file
from table.forms import UserCreationForm, TableDownload


# Create your views here.


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class TableDownloadView(FormView):
    form_class = TableDownload
    template_name = "chart_download.html"

    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES.get('user_table')
        # print(uploaded_file)
        fs = FileSystemStorage()
        r = fs.save(uploaded_file.name, uploaded_file)
        # time.sleep(2.4)
        current_user = request.user
        read_file(r, current_user)
        return render(request, 'chart_download.html')


# def my_form(request):
#     print(request.FILES)
#     form = TableDownload(request.POST or None, request.FILES or None)
# #
#     return render(request, 'chart_download.html', context={'form': form})
