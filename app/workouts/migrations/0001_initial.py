# Generated by Django 3.1.7 on 2021-03-23 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('equipment', models.CharField(max_length=30)),
                ('variation', models.CharField(max_length=30)),
                ('direction', models.CharField(max_length=30)),
                ('movement', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutExercises',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.exercise')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.workout')),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reps', models.IntegerField()),
                ('weight', models.FloatField()),
                ('date', models.DateField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.exercise')),
            ],
        ),
    ]
