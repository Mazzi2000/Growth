from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class JournalEntry(models.Model):
    """Model for storing user journal entries."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journal_entries')
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    mood = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']  # Newest entries first
        verbose_name_plural = "Journal Entries"
        
    def __str__(self):
        """String representation of the model."""
        return f"{self.title or 'Untitled'} - {self.created_at.strftime('%Y-%m-%d')}"