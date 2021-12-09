# Generated by Django 3.1.5 on 2021-12-08 06:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('posted_at', models.DateTimeField(verbose_name=django.utils.timezone.now)),
            ],
        ),
    ]
