# Generated by Django 4.1.4 on 2022-12-17 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_name_user_first_name_user_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
