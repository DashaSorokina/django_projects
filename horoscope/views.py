from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

type_of = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}


def create_types_page(request):
    types_lst = list(type_of)
    li_types = ''
    for type_el in types_lst:
        redirect_path = reverse('types-name', args=[type_el])
        li_types += f"<li><a href='{redirect_path}'><h2>{type_el.title()}</h2></a></li>"
    response = f"""
    <ul>
    {li_types}
    </ul>
    """
    return HttpResponse(response)


def get_info_in_types(request, sign_types):
    description = type_of.get(sign_types, None)
    if description:
        li_types = ''
        for type_el in description:
            redirect_path = reverse('horoscope-name', args=[type_el])
            li_types += f"<li><a href ='{redirect_path}'><h2>{type_el.title()}</h2></a></li>"
            response = f"""
            <ul>
            {li_types}
            </ul>
            """
        return HttpResponse(f'<h2>{response}</h2>')
    else:
        return HttpResponseNotFound(f'<h1>We dont found this type - {sign_types}</h1>')


def index(request):
    zodiacs = list(zodiac_dict)
    # f"<li><a href ='{redirect_path}'>{sign.title()}</a></li>"
    context = {
        'zodiac_dict': zodiac_dict,
        'zodiacs': zodiacs,
    }
    return render(request, 'horoscope/index.html', context)


# def get_info_about_sign_zodiac(request, sign_zodiac: str):
#     response = render_to_string('horoscope/info_zodiac.html')
#     return HttpResponse(response)

def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    zodiacs = list(zodiac_dict)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac,
        #'sign_name': description.split()[0],
        'zodiacs': zodiacs,

    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'This number is not in list  - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac-1]
    redirect_url = reverse('horoscope-name', args=[name_zodiac])  # get as list
    return HttpResponseRedirect(redirect_url)


