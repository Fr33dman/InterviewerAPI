# Generated by Django 2.2.10 on 2021-05-14 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of each interview', max_length=100)),
                ('start_time', models.DateTimeField(help_text='Time when interview starts')),
                ('end_time', models.DateTimeField(help_text='Time when interview ends')),
                ('Description', models.TextField(help_text='Interview description', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(help_text='Question text', max_length=500)),
                ('type', models.CharField(choices=[('TA', 'Text answer'), ('OA', 'One answer'), ('MA', 'Many answers')], default='TA', help_text='Type of question', max_length=2)),
                ('answers', models.TextField(default='', help_text='Answers to choose if type of question is one answer of many answers', max_length=500)),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.Interview')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('token', models.IntegerField(help_text='Token of user who answered')),
                ('answers', models.TextField(help_text='Users answer on interview, in json format [answer1, answer2, answer3, ...]', max_length=2000)),
                ('interview', models.ForeignKey(on_delete=models.SET('deleted'), to='interview.Interview')),
            ],
        ),
    ]
