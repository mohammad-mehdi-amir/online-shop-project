# Generated by Django 4.2.3 on 2023-07-30 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_comment_rate_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(blank=True, default=True),
            preserve_default=False,
        ),
    ]
