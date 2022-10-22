# Generated by Django 4.1.2 on 2022-10-20 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_author_jobpost_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='jobpost',
            name='skills',
            field=models.ManyToManyField(to='app1.skills'),
        ),
    ]