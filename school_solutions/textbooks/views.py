from django.shortcuts import render, get_object_or_404
from .models import Textbook, Subject, GradeLevel, Solution


def home(request):
    subjects = Subject.objects.all()
    grades = GradeLevel.objects.all()
    most_viewed = Textbook.objects.order_by('-view_count')[:10]  # Топ 10 самых просматриваемых

    context = {
        'subjects': subjects,
        'grades': grades,
        'most_viewed': most_viewed,
    }
    return render(request, 'home.html', context)


def textbook_list(request, grade, subject):
    # Получаем список учебников по классу и предмету
    textbooks = Textbook.objects.filter(grade_level__level=grade, subject__english_name=subject)

    context = {
        'textbooks': textbooks,
    }
    return render(request, 'textbook_list.html', context)


def textbook_detail(request, grade, subject, short_name):
    # Находим конкретный учебник
    textbook = get_object_or_404(Textbook, grade_level__level=grade, subject__english_name=subject,
                                 short_name=short_name)

    # Получаем все решения, связанные с данным учебником по short_name
    solutions = Solution.objects.filter(short_name=textbook.short_name)

    context = {
        'textbook': textbook,
        'solutions': solutions,  # Передаем список решений в контекст
    }

    return render(request, 'textbook_detail.html', context)


def solution_detail(request, grade, subject, short_name, folder, image_name):
    solution = get_object_or_404(Solution, folder=folder, image_name=image_name, short_name=short_name)

    context = {
        'solution': solution,
    }
    return render(request, 'solution_detail.html', context)

