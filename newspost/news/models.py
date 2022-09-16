from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Author(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE, primary_key=True)
    author_rate = models.IntegerField(default=0.0)

    def update_rate(self):
        auth_post_rate = self.post.all().aggregate(Sum('post_rate'))['post_rate__sum']*3
        auth_com_rate = self.comment.all().aggregate(Sum('com_rate'))['com_rate__sum']
        auth_post_com_rate = self.post.comment.all().aggregate(Sum('Comment__com_rate'))['Comment__com_rate__sum']
        self.author_rate = auth_post_rate + auth_com_rate + auth_post_com_rate
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255,
                            unique=True,
                            default='unknown')


class Post(models.Model):
    news = 'n'
    article = 'a'
    TYPES = [
        (news, 'новости'),
        (article, 'статья')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=1,
                            choices=TYPES,
                            default='n')
    post_date = models.DateTimeField(auto_now_add=True,
                                null=True)
    category = models.ManyToManyField(Category,
                                      through='PostCategory')
    post_name = models.CharField(max_length=255,
                            blank=True)
    post_text = models.TextField(blank=True)
    post_rate = models.IntegerField(default=0.0)

    def like(self):
        self.post_rate += 1
        self.save()

    def dislike(self):
        self.post_raterate -= 1
        self.save()

    def preview(self):
        return self.post_text[:123] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    com_text = models.TextField(max_length=1500,
                            blank=True)
    com_date = models.DateTimeField(auto_now_add=True)
    com_rate = models.IntegerField(default=0)

    def like(self):
        self.com_rate += 1
        self.save()

    def dislike(self):
        self.com_rate -= 1
        self.save()


# Create your models here.
