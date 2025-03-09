from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Extended user model with personal development features."""
    bio = models.TextField(blank=True)
    
    # AI preferences
    ai_tone = models.CharField(
        max_length=50, 
        default="supportive",
        choices=[
            ("supportive", "Supportive"),
            ("challenging", "Challenging"),
            ("neutral", "Neutral"),
        ]
    )
    
    # Notification settings
    email_notifications = models.BooleanField(default=True)
    
    def __str__(self):
        return self.username