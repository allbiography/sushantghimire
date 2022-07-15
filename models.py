from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings

User = settings.AUTH_USER_MODEL


class history(models.Model):
    student = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    # object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey
    viewed_on = models.DateTimeField(auto_now_add=True)
    book = models.CharField(max_length=222, blank=True, null=True)
    issued_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    returned_date = models.DateField(null=True, blank=True)

    # def __str__(self):
    #     return self.student
