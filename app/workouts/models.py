from django.db import models

# Create your models here.

# variation | equipment | direction | movement
# incline   | dumbbell  | overhead  | press
# bent over | barbell   |           | row
# bench     | barbell   |           | press


class Exercise(models.Model):  # definition of a specific movement
    id = models.AutoField(primary_key=True)
    equipment = models.CharField(max_length=30)  # barbell, dumbbell...
    variation = models.CharField(max_length=30)  # incline, bench, standing...
    direction = models.CharField(max_length=30)  # overhead
    movement = models.CharField(max_length=30)  # press


class Set(models.Model):  # date, movement, reps
    id = models.AutoField(primary_key=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.IntegerField()
    weight = models.FloatField()
    date = models.DateField()


class Workout(models.Model):  # a workout is composed of multiple exercises
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)


class WorkoutExercises(models.Model):  # list of exercises in a workout
    id = models.AutoField(primary_key=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
