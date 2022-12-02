# Generated by Django 4.1.3 on 2022-12-02 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petitions', '0004_remove_petition_comment_delete_petitioncomment'),
        ('comments', '0003_remove_comment_petitions_alter_comment_payload'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='petition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='petitions.petition'),
        ),
    ]
