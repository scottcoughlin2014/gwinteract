# Generated by Django 2.1.4 on 2019-02-12 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popsynth_generation', '0002_auto_20190212_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newpopsynthmodel',
            old_name='LISA_convergence',
            new_name='lisa_convergence',
        ),
    ]
