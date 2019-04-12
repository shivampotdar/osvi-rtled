from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

import os
from time import sleep
from django.utils import timezone

from .models import Pycode,UserVids
import runcode.execcode as exec
from django.core.files.base import ContentFile

from django_tables2 import RequestConfig
from .tables import PycodeTable, UserVidsTable

from django.contrib.auth.decorators import user_passes_test
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponseRedirect

from fabric import Connection
from mysite.settings import pi_ip

default_py_code = """print("Hello Python World!!")"""

default_rows = "7"
default_cols = "70"

@login_required
def py(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        #print(code)
        run = exec.RunPyCode(code)
        rescompil, resrun = run.run_py_code()
        if not resrun:
            resrun = 'No result!'
        var = Pycode(author = request.user, postdate= timezone.now(),result_error=rescompil,result_output=resrun, session=request.user.logged_in_user.session_key)
        fname = timezone.now().strftime('%d-%m-%y_%H:%M:%S')
        filename = 'user_{0}_{1}/{2}'.format(request.user.id, request.user.username, fname)
        filename = filename+'.py'
        var.pycode.save(filename,ContentFile(code))

    else:
        code = default_py_code
        resrun = 'No result!'
        rescompil = ''
    vid_url = pi_ip
    return render(request, 'runcode/post_list.html', {'code': code,'target': "runpy",'resrun': resrun,'rescomp': rescompil,'vid_url':'http://'+pi_ip+':8081',
                                                      'rows': default_rows, 'cols': default_cols})

#global a
a = 0

@csrf_exempt
@login_required
def start_vid(request):
    global filename_global
    filename_global = 'user_{0}_{1}'.format(request.user.id, request.user.username)
    with open('./runcode/motion.conf') as fin, open('./runcode/motion_new.conf','w') as fout:
        for i, item in enumerate(fin,1):
            if i == 450:    # 450 - dir for saving stuff
                item = 'target_dir "'+'/home/pi/runcode/data/videos/'+filename_global+'"\n'
                print(item)
            if i == 473:    # 473 - filename pattern
                global f
                f = request.user.username + '-' + timezone.now().strftime('%d-%m-%y_%H-%M-%S')
                # f_global = f
                item = 'movie_filename '+f+'\n'
                print(item)
            fout.write(item)
    c = Connection(host=pi_ip, user='pi', connect_kwargs={'password': 'samsanjana12'})
    c.put('./runcode/motion_new.conf','runcode/motion_new.conf')
    cmd = ' echo samsanjana12 | sudo -S motion -b -c '+'./runcode/motion_new.conf'
    c.run(cmd)
    #os.system(cmd)
    global a
    a = 1
    print('a1=',a)
    sleep(1.5)          # don't have any other option as of now to wait for iframe loading
    return HttpResponseRedirect('/')

@csrf_exempt
@login_required
def stop_vid(request):
    print('a=', a)
    cmd = " var=$(pidof motion) && echo samsanjana12 | sudo -S kill $var"
    c = Connection(host=pi_ip, user='pi', connect_kwargs={'password': 'samsanjana12'})
    c.run(cmd)
    if a == 1:
        var = UserVids(author=request.user, postdate=timezone.now(),session=request.user.logged_in_user.session_key)
        f2save = c.get('./runcode/data/videos/' + filename_global +'/' + f + '.mp4','./runcode/data/videos/'+filename_global+'/'+f + '.mp4')
        fopen = open('./runcode/data/videos/' + filename_global +'/' + f + '.mp4', 'rb')
        var.uservid.save('videos/'+filename_global+'/'+ f + '.mp4', File(fopen))
        cmd = './runcode/data/videos/' + filename_global
        cmd = " echo samsanjana12 | sudo -S rm -rf "+cmd
        c.run(cmd)
        c.close()
        #os.remove(os.getcwd() + ')
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def logtable(request):
    if request.user.is_staff or request.user.is_superuser:
        table = PycodeTable(Pycode.objects.all())
        table2 = UserVidsTable(UserVids.objects.all())
        #table3 =
    else:
        table = PycodeTable(Pycode.objects.filter(author = request.user.id))
        table2 = UserVidsTable(UserVids.objects.filter(author = request.user.id))
    RequestConfig(request).configure(table)
    return render(request, 'runcode/logs.html', {'table': table,'table2': table2})
