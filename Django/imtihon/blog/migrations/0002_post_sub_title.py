# Generated by Django 4.0.1 on 2022-01-13 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sub_title',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
