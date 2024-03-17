from django.contrib import admin

from lms.models import Payment
from users.models import User

admin.site.register(User)
admin.site.register(Payment)
