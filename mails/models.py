from django.db import models
from django.shortcuts import reverse
from django.conf import settings

from persons.models import Person

class Mail(models.Model):

    subject = models.CharField(max_length = 150)
    body = models.TextField()

    read = models.BooleanField(default=False)
    sender_trash = models.BooleanField(default=False)
    receipient_trash = models.BooleanField(default=False)
    
    sender_person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='sent_mails')
    sender_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="sent_mails")
    receipient = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="received_mails")
    
    attachment = models.FileField(upload_to='uploads/mails/attachment/%Y-$m-%d', blank=True, null=True)
    
    date_sent = models.DateTimeField(auto_now_add=True)
    date_read = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Mail"
        verbose_name_plural = "Mails"
        ordering = ['-date_sent']

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("mail_detail", kwargs={"pk": self.pk})
