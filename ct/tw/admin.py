from django.contrib import admin
from tw.models import TwitterUser, Tweet, Credential
# Register your models here.

admin.site.register(TwitterUser)
admin.site.register(Tweet)
admin.site.register(Credential)
