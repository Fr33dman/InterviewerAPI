# Generated by Django 2.2.10 on 2021-05-14 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0002_auto_20210514_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answers',
            field=models.TextField(help_text='Users answer on interview, in json format [answer1, answer2, answer3, ...]', max_length=2000),
        ),
        migrations.AlterField(
            model_name='interview',
            name='Description',
            field=models.TextField(help_text='Interview description', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='answers',
            field=models.TextField(help_text='Answers to choose if type of question is one answer of many answers', max_length=500, null=True),
        ),
    ]
