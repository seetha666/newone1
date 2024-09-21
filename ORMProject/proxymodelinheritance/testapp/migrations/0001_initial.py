# Generated by Django 3.2 on 2024-09-21 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=100)),
                ('esal', models.FloatField()),
                ('eadd', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='proxyEmployee',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('testapp.employee',),
        ),
    ]
