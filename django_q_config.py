import os
import django

# Configuration du script standalone
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'savtech_project.settings')
django.setup()

from django_q.models import Schedule
from django.utils import timezone

def setup_periodic_tasks():
    """
    Configure le ré-entraînement hebdomadaire du modèle RandomForest via Django-Q.
    Ce script peut être exécuté une fois pour initialiser les tâches.
    """
    # Create or update the schedule
    schedule, created = Schedule.objects.get_or_create(
        func='ai_engine.ml.repair_predictor.train_model',
        defaults={
            'schedule_type': Schedule.WEEKLY,
            'repeats': -1,  # Infinite
            'next_run': timezone.now() + timezone.timedelta(minutes=5)
        }
    )
    
    if created:
        print("Tâche planifiée créée : Ré-entraînement hebdomadaire ML.")
    else:
        print("La tâche planifiée existe déjà.")

if __name__ == '__main__':
    setup_periodic_tasks()
