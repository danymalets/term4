from django.contrib import admin
from ugc.models.user import User
from ugc.models.group import Group
from ugc.models.queue import Queue

admin.site.register(User)
admin.site.register(Group)
admin.site.register(Queue)
