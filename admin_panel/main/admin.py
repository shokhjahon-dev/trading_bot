from django.contrib import admin
from .models import ForexSignal, HumanInfo, GetStart


admin.site.register([ForexSignal, HumanInfo, GetStart])
