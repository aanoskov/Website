# Generated by Django 3.1.6 on 2021-03-30 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_blog_opened'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=18)),
                ('cost', models.IntegerField()),
            ],
        ),
    ]