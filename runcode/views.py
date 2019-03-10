from django.shortcuts import render
from django.shortcuts import redirect
import runcode.execcode as exec
from django.contrib.auth.decorators import login_required
import os
from time import sleep

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
    else:
        code = default_py_code
        resrun = 'No result!'
        rescompil = ''
    return render(request, 'runcode/post_list.html', {'code': code,'target': "runpy",'resrun': resrun,'rescomp': rescompil,
                                                      'rows': default_rows, 'cols': default_cols})


def start_vid(void):
    cmd = " echo samsanjana12 | sudo -S motion -b"
    os.system(cmd)
    sleep(1.5)          # don't have any other option as of now to wait for iframe loading
    return redirect('code_home')


def stop_vid(void):
    cmd = " var=$(pidof motion) && echo samsanjana12 | sudo -S kill $var"
    os.system(cmd)
    return redirect('code_home')
