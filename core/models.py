from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True, unique=True, default=None)

class Follows(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_id')
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leader_id')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['follower_id', 'leader_id'], name='UQ_Core_Follows_follower_id_leader_id')
        ]

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(default=datetime.now())

class Post_Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(default=datetime.now())

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['user_id', 'post_id'], name='UQ_Core_Post_Comment_user_id_post_id')
    #     ]

class Comment_Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Post_Comment, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(default=datetime.now())

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'comment_id'], name='UQ_Core_Comment_Comment_user_id_comment_id')
        ]



class Post_Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'post_id'], name='UQ_Core_Post_Likes_user_id_post_id')
        ]

class Comment_Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'comment_id'], name='UQ_Core_Comment_Likes_user_id_comment_id')
        ]


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
