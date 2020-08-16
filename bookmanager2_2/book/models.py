from django.db import models

# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=20)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'
        verbose_name = '书籍信息'

    def __str__(self):
        return self.name

class PeopleInfo(models.Model):
    GENDER_CHOICE = (
        ('0','male'),
        ('1','female'),
    )

    name = models.CharField(max_length=20)
    gender = models.BooleanField(choices=GENDER_CHOICE,default=0)
    description = models.CharField(max_length=200,null=True)
    book = models.ForeignKey(BookInfo,models.CASCADE)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name