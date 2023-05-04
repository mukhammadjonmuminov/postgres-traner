# Generated by Django 4.2 on 2023-05-03 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passenger',
            old_name='age',
            new_name='Age',
        ),
        migrations.RenameField(
            model_name='passenger',
            old_name='cabin',
            new_name='Cabin',
        ),
        migrations.RenameField(
            model_name='passenger',
            old_name='embarked',
            new_name='Embarked',
        ),
        migrations.RenameField(
            model_name='passenger',
            old_name='fare',
            new_name='Fare',
        ),
        migrations.RenameField(
            model_name='passenger',
            old_name='full_name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='passenger',
            old_name='passenger_id',
            new_name='PassengerId',
        ),
        migrations.RenameField(
            model_name='passenger',
            old_name='p_class',
            new_name='Pclass',
        ),
        migrations.RenameField(
            model_name='passenger',
            old_name='sex',
            new_name='Sex',
        ),
        migrations.RenameField(
            model_name='passenger',
            old_name='sib_sp',
            new_name='SibSp',
        ),
        migrations.RenameField(
            model_name='passenger',
            old_name='survived',
            new_name='Survived',
        ),
        migrations.RenameField(
            model_name='passenger',
            old_name='ticket',
            new_name='Ticket',
        ),
    ]