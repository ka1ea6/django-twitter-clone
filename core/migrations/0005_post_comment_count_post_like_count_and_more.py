# Generated by Django 4.2 on 2023-05-01 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "core",
            "0004_remove_comment_comment_uq_core_comment_comment_user_id_comment_id_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="comment_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="post",
            name="like_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="comment_comment",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 5, 1, 17, 22, 46, 701110)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 5, 1, 17, 22, 46, 699112)
            ),
        ),
        migrations.AlterField(
            model_name="post_comment",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 5, 1, 17, 22, 46, 700111)
            ),
        ),
    ]
