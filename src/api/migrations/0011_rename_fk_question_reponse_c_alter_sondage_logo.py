# Generated by Django 4.0.7 on 2022-09-11 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_option_reponse_type_question_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reponse',
            old_name='fk_question',
            new_name='c',
        ),
        migrations.AlterField(
            model_name='sondage',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
