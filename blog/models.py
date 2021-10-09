from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class BaseModel(models.Model):
    created_time = models.DateTimeField(
        auto_now_add=True, verbose_name='created time'
    )
    modified_time = models.DateTimeField(
        auto_now=True, verbose_name='modified time'
    )

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=16, verbose_name='name')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category'

    def __str__(self):
        return self.name




class Author(BaseModel):
    avatar = models.ImageField(
        verbose_name='avatar', upload_to='author/avatars/'
    )
    user = models.OneToOneField(
        User, related_name='author', on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return f"{self.user.name}"


class Post(BaseModel):
    DRAFT = 0
    PUBLISHED = 1
    ARCHIVED = 2

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
        (ARCHIVED, 'Archived')
    )
    title = models.CharField(max_length=255, verbose_name='title')
    body = models.TextField(verbose_name='body', blank=True, null=True)

    author = models.ForeignKey(
        Author, related_name='posts', on_delete=models.SET_DEFAULT, default=1
    )
    attachment = models.FileField(
        verbose_name='attachment', upload_to='posts/attachments/', null=True
    )
    categories = models.ManyToManyField(Category, related_name='posts')
    status = models.PositiveSmallIntegerField(
        verbose_name="status", choices=STATUS_CHOICES, default=0
    )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural ='Posts'

    def __str__(self):
        return self.title

    def jalali_time(self, time):
        # Convert first
        return time

    def jalali_created_time(self):
        pass

    def get_absolute_url(self):
        pass