from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model



User = get_user_model()
 


# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries', null=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='entries', default=None)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name_plural = "Entries"
        
        
