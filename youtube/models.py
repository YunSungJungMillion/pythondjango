from django.db import models

# Create your models here.
# 이건 중요한 작업이니 항상 조심해서 해야한다.

class Video(models.Model):
    title = models.CharField(max_length = 30)                    #varible => field
    description = models.TextField(max_length = 300)                    #varible => field
    path = models.CharField(max_length = 60)                    #varible => field
    datetime = models.DateTimeField(blank = False,null=False)                    #varible => field  
    user = models.ForeignKey('auth.User',on_delete = models.CASCADE)                    #varible => field

class Comment(models.Model):
    text = models.CharField(max_length = 30)                    #varible => field
    datetime = models.DateTimeField(blank = False,null=False)                    #varible => field  
    user = models.ForeignKey('auth.User',on_delete = models.CASCADE)                    #varible => field
    video = models.ForeignKey(Video,on_delete = models.CASCADE)    #내가 만든 클래스가 포린키                


#클래스를 넘기면 이전 라인에 클래스가 선언되어야 하고
#문자열로 넘기면 이전 이후 라인 상간없이 찾는다.


