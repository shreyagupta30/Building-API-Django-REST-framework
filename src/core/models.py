from django.db import models

User = get_user_mode()

# Create your models here.
class Post(models.Model):
    title = models.Charfield(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title