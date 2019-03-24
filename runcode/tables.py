import django_tables2 as tables
from .models import Pycode

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

class PycodeTable(tables.Table):
    class Meta:
        model = Pycode
        template_name = 'django_tables2/bootstrap.html'
