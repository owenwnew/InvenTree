# Generated by Django 3.0.7 on 2020-12-18 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0039_auto_20201112_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='target_date',
            field=models.DateField(blank=True, help_text='Target date for order completion. Order will be overdue after this date.', null=True, verbose_name='Target completion date'),
        ),
    ]