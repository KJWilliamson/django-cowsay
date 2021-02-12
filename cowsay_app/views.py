# https://stackoverflow.com/questions/34147353/python-subprocess-chaining-commands-with-subprocess-run?rq=1
# https://docs.djangoproject.com/en/3.1/howto/outputting-csv/
# getting errors on pycharm but not vscode so pasted code from there. it's being buggy
# got help from Juddie

from django.shortcuts import render
from cowsay_app.models import Cowsay
from cowsay_app.forms import CowsayForm
import subprocess as sp
import platform


# Create your views here.
def index_view(request):
    if request.method == 'POST':
        form = CowsayForm(request.POST)
        if form.is_valid():
            name = request.POST['cowsay_string']
            form.save()
            if platform.system() == "OSX":
                expand_shell = True
            else:
                expand_shell = False
            s = sp.check_output(
                ['cowsay', name], universal_newlines=True, stderr=sp.STDOUT, shell=expand_shell) # noqa
            return render(request, 'index.html', {'name': s})
    return render(request, 'index.html')


def history(request):
    cowsay_list = Cowsay.objects.all().order_by('id').reverse()[:10]
    return render(request, "history.html", {"cowsay_list": cowsay_list})
