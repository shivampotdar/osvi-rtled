import subprocess
import sys
import os
from fileinput import filename

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
        a, b = p.communicate()
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
        if not os.path.exists('running'):
            os.mkdir('running')

    def _run_py_prog(self, cmd="a.py"):
        cmd = [sys.executable, cmd]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = p.wait()
        a, b = p.communicate()
        self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")
        return result
    
    def run_py_code(self, code=None):
        filename = "./running/a.py"
        if not code:
            code = self.code
        with open(filename, "w") as f:
            f.write(code)
        self.test_py_code(filename)
        return self.stderr, self.stdout

    def test_py_code(self, code=None):
        filename = "./running/a.py"
        flag = 0
        f1 = open('./running/a.py', "r")
        f2 = open('./running/answer.py', "r")
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
            self.stderr=''
            #return self.stderr, self.stdout
