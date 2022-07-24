from django.db import models


class Post(models.Model):
    writer = models.CharField(max_length=10, default='')
    #category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    #tags = models.ManyToManyField('Tag', blank=True)
    title = models.CharField('TITLE', max_length=50, default='')
    #hook_text = models.CharField('HOOK_TEXT', max_length=100, blank=True, help_text='simple one-line text.')
    #image = models.ImageField('IMAGE', upload_to='blog/%Y/%m/', blank=True, null=True)
    content = models.TextField('CONTENT')
    created_time = models.DateTimeField('CREATED TIME', auto_now_add=True)
    #update_dt = models.DateTimeField('UPDATE DT', auto_now=True)
    #like = models.PositiveSmallIntegerField('LIKE', default=0)

    class Meta:
        ordering = ('created_time',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    com_content = models.TextField('COM_CONTENT')
    created_time = models.DateTimeField('CREATED_TIME', auto_now_add=True)
    #update_dt = models.DateTimeField('UPDATE DT', auto_now=True)

    @property
    def short_content(self):
        return self.com_content[:10]

    def __str__(self):
        return self.short_content