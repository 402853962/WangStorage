# Generated by Django 2.2.5 on 2020-08-15 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20200815_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='pub_date',
            field=models.DateField(null=True),
        ),
    ]