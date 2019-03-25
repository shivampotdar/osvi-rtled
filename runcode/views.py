from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

import os
from time import sleep
from django.utils import timezone

from .models import Pycode
import runcode.execcode as exec
from django.core.files.base import ContentFile

from django_tables2 import RequestConfig
from .tables import PycodeTable

from django.contrib.auth.decorators import user_passes_test


default_py_code = """
print("Hello Python World!!")
"""

default_rows = "7"
default_cols = "70"


@login_required
def py(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        print(code)
        run = exec.RunPyCode(code)
        rescompil, resrun = run.run_py_code()
        if not resrun:
            resrun = 'No result!'
        var = Pycode(author = request.user, postdate= timezone.now(),result_error=rescompil,result_output=resrun)
        fname = timezone.now().strftime('%d-%m-%y_%H:%M:%S')
        filename = 'user_{0}/{1}'.format(request.user.id, fname)
        filename = filename+'.py'
        var.pycode.save(filename,ContentFile(code))

    else:
        code = default_py_code
        resrun = 'No result!'
        rescompil = ''
    return render(request, 'runcode/post_list.html', {'code': code,'target': "runpy",'resrun': resrun,'rescomp': rescompil,
                                                      'rows': default_rows, 'cols': default_cols})


@login_required
def start_vid(void):
    cmd = " echo samsanjana12 | sudo -S motion -b"
    os.system(cmd)
    sleep(1.5)          # don't have any other option as of now to wait for iframe loading
    return redirect('code_home')


@login_required
def stop_vid(void):
    cmd = " var=$(pidof motion) && echo samsanjana12 | sudo -S kill $var"
    os.system(cmd)
    return redirect('code_home')

@user_passes_test(lambda u:u.is_staff, login_url='/')
def logtable(request):
    table = PycodeTable(Pycode.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'runcode/logs.html', {'table': table})
