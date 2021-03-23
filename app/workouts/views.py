from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from workouts.models import Exercise, Set, Workout, WorkoutExercises
from rest_framework import viewsets
from rest_framework import permissions
from workouts.serializers import UserSerializer, GroupSerializer, ExerciseSerializer, SetSerializer, WorkoutSerializer, WorkoutExercisesSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExerciseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Exercises to be viewed or edited
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permissions_classes = [permissions.IsAuthenticated]


class SetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Sets to be viewed or edited
    """
    queryset = Set.objects.all()
    serializer_class = SetSerializer
    permissions_classes = [permissions.IsAuthenticated]


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Workouts to be viewed or edited
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permissions_classes = [permissions.IsAuthenticated]


class WorkoutExercisesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows WorkoutExercises to be viewed or edited
    """
    queryset = WorkoutExercises.objects.all()
    serializer_class = WorkoutExercisesSerializer
    permissions_classes = [permissions.IsAuthenticated]
