from django.db import models
from profiles.models import UserProfile


class Post(models.Model):
    user_profile = models.ForeignKey(
                                     UserProfile, on_delete=models.CASCADE,
                                     null=False, blank=False,
                                     related_name='posts')
    heading = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE,
        null=False, blank=False, related_name='comments')
    for_post = models.ForeignKey('Post', null=False, on_delete=models.CASCADE)
    body = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.id


class Like(models.Model):
    post = models.ForeignKey('Post', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(
                             UserProfile, null=False, on_delete=models.CASCADE,
                             related_name='likes')

    def __str__(self):
        return str(self.id)
