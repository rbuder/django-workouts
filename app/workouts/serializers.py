from django.contrib.auth.models import User, Group
from rest_framework import serializers
from workouts.models import Exercise, Set, Workout, WorkoutExercises


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exercise
        fields = ['equipment', 'variation', 'direction', 'movement']


class SetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Set
        fields = ['exercise', 'reps', 'weight', 'date']


class WorkoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Workout
        fields = ['name']


class WorkoutExercisesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkoutExercises
        fields = ['workout', 'exercise']
