from django.db import models

# Create your models here.

class UserInfo(models.Model):
    # id
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=60)
    # gender = models.CharField(max_length=60, null=True)

    user_group = models.ForeignKey('UserGroup', on_delete=models.CASCADE, to_field='uid', default=1)
    # user_group为一个对象
    user_type_choices = (
        (1, '超级用户'),
        (2, '普通用户'),
        (3, '普普通用户'),
    )
    user_type_id = models.IntegerField(choices=user_type_choices, default=1)

class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)   # 自增时primary_key必须加
    caption = models.CharField(max_length=32, unique=True)
    ctime = models.DateTimeField(auto_now_add=True, null=True)
    uptime = models.DateTimeField(auto_now=True, null=True)