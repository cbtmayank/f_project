# Generated by Django 5.0.4 on 2024-05-06 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='svmStudent',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('mobile', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'svm_student',
            },
        ),
    ]