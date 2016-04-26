from django.db import models

from authentication.models import Account

class Post(models.Model):
    author = models.ForeignKey(Account, related_name='post_author', verbose_name='author')
    #recipient = models.OneToOneField(Account)
    #recipient = models.ManyToManyField(Account)
    #recipient = models.ForeignObject(Account, username)
    recipient = models.ForeignKey(Account, related_name='post_recipient', null=True, blank=True, verbose_name='recipient')
    content = models.TextField()
    relationship = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.content)


