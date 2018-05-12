from django.db import models


# Create your models here.
class GithubRepository(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    full_name = models.CharField(max_length=255)
    description = models.CharField(max_length=2048)
    fork = models.CharField(max_length=5)
    url = models.CharField(max_length=1024)
    created_at = models.DateTimeField()  # 2012-03-30T20:09:52Z
    homepage = models.CharField(max_length=1024)
    size = models.BigIntegerField()
    language = models.CharField(max_length=32)
    open_issues = models.IntegerField()
    watchers = models.IntegerField()
