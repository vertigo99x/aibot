from django.db import models
import uuid 
from django.utils import timezone
from django.core.exceptions import ValidationError
from accounts.models import User


def validate_json_is_list(value):
    if not isinstance(value, list):
        raise ValidationError('This field must be a list.')

class Conversation(models.Model):
    uuid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation_title = models.CharField(max_length=127, null=False, blank=False)
    conversation_list = models.JSONField(validators=[validate_json_is_list], default=list, null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.conversation_title
    
    def save(self, *args, **kwargs):
        if not self.conversation_list:
            self.conversation_list = []
        super(Conversation, self).save(*args, **kwargs)
        
    class Meta:
        ordering = ('-date_added',)

