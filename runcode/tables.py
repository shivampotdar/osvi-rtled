import django_tables2 as tables
from .models import Pycode


class PycodeTable(tables.Table):
    class Meta:
        model = Pycode
        template_name = 'django_tables2/bootstrap.html'

