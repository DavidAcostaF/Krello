# Generated by Django 4.1.4 on 2022-12-17 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workspace', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersworkspaces',
            name='workspace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workspace.workspace'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usertype'),
        ),
    ]
