# Generated by Django 4.1.4 on 2022-12-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_alter_board_uid_alter_card_column'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='uid',
            field=models.CharField(blank=True, default='aa84e745', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='deadline_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]