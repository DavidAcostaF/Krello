# Generated by Django 4.1.4 on 2022-12-22 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_alter_board_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='uid',
            field=models.CharField(blank=True, default='5689d023', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.column'),
        ),
    ]
