from django.db import models
from django.conf import settings

class Mail(models.Model):

    subject = models.CharField(max_length = 150)
    body = models.TextField()
    read = models.BooleanField(default=False)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    receipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mail_receipient")
    
    date_sent = models.DateTimeField(auto_now=True)
    date_read = models.DateTimeField(null=True)
    
    class Meta:
        verbose_name = "Mail"
        verbose_name_plural = "Mails"

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("mail_detail", kwargs={"pk": self.pk})
