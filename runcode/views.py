from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import redirect
from .runcode import runcode
from .models import Ccode
from django.contrib.auth.decorators import login_required

default_py_code = """import sys
import os

if __name__ == "__main__":
    print("Hello Python World!!")
"""

default_rows = "7"
default_cols = "70"
@login_required
def py(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        print(code)
        run = runcode.RunPyCode(code)
        rescompil, resrun = run.run_py_code()
        if not resrun:
            resrun = 'No result!'
    else:
        code = default_py_code
        resrun = 'No result!'
        rescompil = ''
    return render(request, 'runcode/post_list.html',{'code':code,'target':"runpy",'resrun':resrun,'rescomp':rescompil,'rows':default_rows, 'cols':default_cols})
