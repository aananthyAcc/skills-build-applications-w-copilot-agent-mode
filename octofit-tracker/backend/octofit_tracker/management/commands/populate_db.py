from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team='marvel')
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team='marvel')
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team='dc')
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team='dc')

        # Activities
        Activity.objects.create(user=tony.name, type='run', duration=30, date='2025-09-01')
        Activity.objects.create(user=steve.name, type='cycle', duration=45, date='2025-09-02')
        Activity.objects.create(user=bruce.name, type='swim', duration=60, date='2025-09-03')
        Activity.objects.create(user=clark.name, type='run', duration=50, date='2025-09-04')

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=110)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Pullups', description='Do 10 pullups', difficulty='medium')
        Workout.objects.create(name='Squats', description='Do 30 squats', difficulty='easy')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
