# osvi-rtled

##Usage Instructions

1. Install Django latest version, ```pip3 install django```
2. Install RPi.GPIO latest version
3. ```source myvenv bin activate```
4. ```python3 manage.py makemigrations```
5. ```python3 manage.py migrate```
6. Install ```motion``` using ```sudo apt install motion```
7. Add your password in ```runcode/views.py : start_vid and stop_vid and accounts/signals.py```
8. Comment GPIO functions in ```accounts/signals.py``` when not on RPi


