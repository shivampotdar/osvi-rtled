from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from .forms import PostForm
from .forms import CcodeForm
from .runcode import runcode
from .models import Post #The dot before models means current directory or current application
from .models import Ccode

default_c_code = """#include <stdio.h>

int main(int argc, char **argv)
{
    printf("Hello C World!!\\n");
    return 0;
}    
"""

default_cpp_code = """#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    cout << "Hello C++ World" << endl;
    return 0;
}
"""

default_py_code = """import sys
import os

if __name__ == "__main__":
    print("Hello Python World!!")
"""

default_rows = "15"
default_cols = "60"

# Create your views here.
# def post_list(request):
#     print('This is an info message')
#     return render(request, 'blog/post_list.html')

def post_list(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        print(code)
        run = runcode.RunCCode(code)
        rescompil, resrun = run.run_c_code()
        if not resrun:
            resrun = 'No result!'
    else:
        code = default_c_code
        resrun = 'No result!'
        rescompil = ''
    return render(request, 'blog/post_list.html',{'code':code,'target':"runc",'resrun':resrun,'rescomp':rescompil,'rows':default_rows, 'cols':default_cols})


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
    return render(request, 'blog/post_list.html',{'code':code,'target':"runpy",'resrun':resrun,'rescomp':rescompil,'rows':default_rows, 'cols':default_cols})


def post_detail(request, pk):
	#Note that we need to use exactly the same name as the one we specified in urls (pk). Omitting this variable is incorrect and will result in an error!
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False) #commit=False means that we don't want to save the Post model yet – we want to add the author first
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid:
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form':form})