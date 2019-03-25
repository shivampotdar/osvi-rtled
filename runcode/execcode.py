import subprocess
import sys
import os
from fileinput import filename
import mmap
from .models import Pycode

'''
class RunPyCode(object):
    
    def __init__(self, code=None):
        self.code = code
        if not os.path.exists('running'):
            os.mkdir('running')

    def _run_py_prog(self, cmd="a.py"):
        cmd = [sys.executable, cmd]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = p.wait()
        a, b = p.communicate().
        self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")
        return result
     
    def run_py_code(self, code=None):
        filename = "./running/a.py"
        if not code:
            code = self.code
        with open(filename, "w") as f:
            f.write(code)
        self._run_py_prog(filename)
        return self.stderr, self.stdout
'''


class RunPyCode(object):
    
    def __init__(self, code=None):
        self.code = code
        if not os.path.exists('./runcode/running'):
            os.mkdir('./runcode/running')

    def _run_py_prog(self, cmd="a.py"):
        cmd = [sys.executable, cmd]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            result = p.wait(timeout=20)
            a, b = p.communicate()
            self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")
            return result
        except:
            self.stdout, self.stderr = " ", "Execution Timed Out! Please don't use infinite loops"
            #gp.cleanup()
    
    def run_py_code(self, code=None):
        filename = "./runcode/running/a.py"
        if not code:
            code = self.code
        with open(filename, "w") as f:
            f.write(code)
        self.test_py_code(filename)
        return self.stderr, self.stdout

    def test_py_code(self, code=None):
        '''filename = "./runcode/running/a.py"
        flag = 0
        f1 = open('./runcode/running/a.py', "r")
        f2 = open('./runcode/running/answer.py', "r")
        for line1 in f1:
            for line2 in f2:
                if line1 == line2:
                    flag = 1
                else:
                    flag = 0
                break
        f1.close()
        f2.close()
                if flag != 5 :
            self._run_py_prog(filename)
        else:
            self.stdout='Please check your code'
            self.stderr=
            '''

        filename = "./runcode/running/a.py"
        flag = 0
        with open(filename, 'rb', 0) as file, \
                mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
            while True:
                if s.find(b'shutdown') != -1:
                    flag = 1
                    break
                if s.find(b'ifconfig') != -1:
                    flag = 1
                    break
                if s.find(b'reboot') != -1:
                    flag = 1
                    break
                if s.find(b'reboot') != -1:
                    flag = 1
                    break
                if s.find(b'halt') != -1:
                    flag = 1
                    break
                if s.find(b'rm') != -1:
                    flag = 1
                    break
                if s.find(b'poweroff') != -1:
                    flag = 1
                    break
                else:
                    break
        if flag != 0:
            self.stdout = ''
            self.stderr = 'Malicious Code!'
        else:
            self._run_py_prog(filename)
            #return self.stderr, self.stdout
