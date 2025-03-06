from django.shortcuts import render

def home(request):
    student = {
        "full_name": "Пшенникова Диана Николаевна",
        "photo": "/static/images/me.png",  
        "email": "di.pshennikova@yandex.ru",
        "phone": "+7 (991) 999-52-21"
    }

    program = {
        "name": "Дизайн",
        "description": "Изучение дизайна и программирования.",
        "director": {
            "full_name": "Харитонов Захар",
            "photo": "/static/images/Zahar.jpg",  
            "email": "zakharday@yandex.ru"
        },
        "manager": {
            "full_name": "Матвиенко Бамба Владимировна",
            "photo": "/static/images/bamba.jpeg",  
            "email": "bnatvienko@hse.ru"
        }
    }

    # Данные о сокурсниках
    classmates = [
        {
            "full_name": "Зеленкова Александра",
            "photo": "/static/images/sasha.jpeg",
            "email": "zelen@gmail.com",
            "phone": "+7 (990) 111-33-11"
        },
        {
            "full_name": "Ляч Анастасия",
            "photo": "/static/images/nast.jpeg",  
            "email": "lyach@gmail.com",
            "phone": "+7 (991) 555-22-77"
        }
    ]

    context = {
        "student": student,
        "program": program,
        "classmates": classmates
    }

    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def animals(request):
    return render(request, 'animals.html')

def check_words(request):
    correct_words = []  

    if request.method == 'POST':
        words = request.POST.get('words', '').split(', ')
        lengths = request.POST.get('lengths', '').split()
        lengths = [int(length) for length in lengths]  
        correct_words = [words[i] for i in range(len(words)) if len(words[i]) == lengths[i]]

    context = {
        'correct_words': correct_words,
        'words': request.POST.get('words', ''),  
        'lengths': request.POST.get('lengths', '')  
    }
    return render(request, 'check_words.html', context)

def requirements(request):
    return render(request, 'requirements.html')


def rectangle_fit(request):
    result = None  

    if request.method == 'POST':
        a = float(request.POST.get('a', 0))
        b = float(request.POST.get('b', 0))
        c = float(request.POST.get('c', 0))
        d = float(request.POST.get('d', 0))

        
        if (a <= c and b <= d) or (a <= d and b <= c):
            result = "Прямоугольник со сторонами a и b МОЖЕТ уместиться внутри прямоугольника со сторонами c и d."
        else:
            result = "Прямоугольник со сторонами a и b НЕ МОЖЕТ уместиться внутри прямоугольника со сторонами c и d."

    context = {
        'result': result,
        'a': request.POST.get('a', ''), 
        'b': request.POST.get('b', ''),
        'c': request.POST.get('c', ''),
        'd': request.POST.get('d', '')
    }
    return render(request, 'rectangle_fit.html', context)