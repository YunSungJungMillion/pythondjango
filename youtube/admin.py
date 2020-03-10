from django.contrib import admin
from .models import Video,Comment


# Register your models here.
# 어드민 페이지에서 모델들을 제어 가능하도록 능록할수 있음.
admin.site.register([Video,Comment])