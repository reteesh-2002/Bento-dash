from django.db import models

class Widget(models.Model):
    WIDGET_TYPES = [
        ('timer', 'Timer'),
        ('calendar', 'Calendar'),
        ('test','Test'),
    ]
    widget_type = models.CharField(max_length=50, choices=WIDGET_TYPES)
    position = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.widget_type} - {self.id}"