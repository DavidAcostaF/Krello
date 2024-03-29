# Generated by Django 4.1.4 on 2023-01-11 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_alter_board_uid_alter_card_deadline_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='card',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='board.card'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='board',
            name='uid',
            field=models.CharField(blank=True, default='2f1023ce', max_length=8, null=True),
        ),
    ]
