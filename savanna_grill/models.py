from django.db import models
from django.contrib.auth.models import User

# Review model to store user reviews
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()  # The review content
    rating = models.PositiveIntegerField()  # A numeric rating eg 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the review was created

    def __str__(self):
        return f"Review by {self.user or 'Anonymous'} - {self.rating} Stars"

        