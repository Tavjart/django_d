from .models import GradeLevel, Subject


def grade_subjects(request):
    grades = GradeLevel.objects.all()
    subjects = Subject.objects.all()
    return {
        'grades': grades,
        'subjects': subjects
    }
