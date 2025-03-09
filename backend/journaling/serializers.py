from rest_framework import serializers
from .models import JournalEntry

class JournalEntrySerializer(serializers.ModelSerializer):
    """Serializer for journal entries."""
    
    class Meta:
        model = JournalEntry
        fields = ['id', 'title', 'content', 'mood', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
        
    def create(self, validated_data):
        """Create a new journal entry."""
        # Get the current user from the context
        user = self.context['request'].user
        
        # Create the journal entry with the user
        journal_entry = JournalEntry.objects.create(
            user=user,
            **validated_data
        )
        return journal_entry