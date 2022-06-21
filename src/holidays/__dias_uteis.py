#!/usr/bin/env python
# coding: utf-8

""" Conjunto de funcoes para calcular dias uteis e feriados feriados
Dias da semana segundo a norma ISO 8601
weekdays = {1: 'Segunda-feira', 2: 'Terça-feira', 3: 'Quarta-feira',
            4: 'Quinta-feira', 5: 'Sexta-Feira', 6: 'Sabado', 7: 'Domingo'}
"""

from datetime import datetime, timedelta
from dateutil.easter import easter
import calendar

from typing import Dict, List, Union, Tuple, Any, Optional

import pandas as pd


# o primeiro dia da semana aqui definido é so para poder calcular alguns feriados moveis
cld = calendar.Calendar(firstweekday=calendar.MONDAY)

# feriados de distritos e municipios de portugal
DISTRITOS: Dict[str, Dict[str, Tuple[Any, ...]]] = {
    'aveiro': {
        'agueda': ('p', 50), 'albergaria-a-velha': ('c', 8, 3, 0), 'anadia': ('p', 39),
        'arouca': ('d', 5, 2), 'aveiro': ('d', 5, 12), 'castelo-de-paiva': ('d', 6, 24),
        'espinho': ('d', 6, 16), 'estarreja': ('d', 6, 13), 'santa-maria-da-feira': ('d', 1, 20),
        'ilhavo': ('p', 1), 'mealhada': ('p', 39), 'murtosa': ('d', 9, 8),
        'oliveira-de-azemeis': ('c', 8, 2, 0), 'oliveira-do-bairro': ('p', 39),
        'ovar': ('d', 7, 25), 'sao-joao-da-madeira': ('d', 10, 11), 'sever-do-vouga': ('d', 9, 21),
        'vagos': ('p', 50), 'vale-de-cambra': ('d', 6, 13)
    },
    'beja': {
        'aljustrel': ('d', 6, 13), 'almodovar': ('d', 6, 24), 'alvito': ('p', 39),
        'barrancos': ('d', 8, 28), 'beja': ('p', 39), 'castro-verde': ('d', 6, 29),
        'cuba': ('p', 1), 'ferreira-do-alentejo': ('d', 3, 5), 'mertola': ('d', 6, 24),
        'moura': ('d', 6, 24), 'odemira': ('d', 9, 8), 'ourique': ('d', 9, 8), 'serpa': (None,),
        'vidigueira': ('p', 39)
    },
    'braga': {
        'amares': ('d', 6, 13), 'barcelos': ('d', 5, 3), 'braga': ('d', 6, 24),
        'cabeceiras-de-basto': ('d', 9, 29), 'celorico-de-basto': ('d', 7, 25),
        'esposende': ('d', 8, 19), 'fafe': ('d', 5, 16), 'guimaraes': ('d', 6, 24),
        'povoa-de-lanhoso': ('d', 3, 19), 'terras-de-bouro': ('d', 10, 20),
        'vieira-do-minho': ('c', 10, 1, 0), 'vila-nova-de-famalicao': ('d', 6, 13),
        'vila-verde': ('d', 6, 13), 'vizela': ('d', 3, 19)
    },
    'braganca': {
        'alfandega-da-fe': ('d', 6, 29), 'braganca': ('d', 8, 22), 'carrazeda-de-ansiaes': (None,),
        'freixo-de-espada-a-cinta': ('p', 1), 'macedo-de-cavaleiros': ('d', 6, 29),
        'miranda-do-douro': ('d', 7, 10), 'mirandela': ('d', 5, 25), 'mogadouro': ('d', 10, 15),
        'torre-de-moncorvo': ('d', 3, 19), 'vila-flor': ('d', 8, 24), 'vimioso': ('d', 8, 10),
        'vinhais': ('d', 5, 20)
    },
    'castelo-branco': {
        'belmonte': ('d', 4, 26), 'castelo-branco': ('p', 9), 'covilha': ('d', 10, 20),
        'fundao': ('d', 9, 15), 'idanha-a-nova': ('p', 15), 'oleiros': ('c', 8, 2, 0),
        'penamacor': ('p', 1), 'proenca-a-nova': ('d', 6, 13), 'serta': ('d', 6, 24),
        'vila-de-rei': ('d', 9, 19), 'vila-velha-de-rodao': ('c', 8, 4, 0)
    },
    'coimbra': {
        'arganil': ('d', 9, 7), 'cantanhede': ('d', 7, 25), 'coimbra': ('d', 7, 4),
        'condeixa-a-nova': ('d', 7, 24), 'figueira-da-foz': ('d', 6, 24), 'gois': ('d', 8, 13),
        'lousa': ('d', 6, 24), 'mira': ('d', 7, 25), 'miranda-do-corvo': ('d', 6, 1),
        'montemor-o-velho': ('d', 9, 8), 'oliveira-do-hospital': ('d', 10, 7),
        'pampilhosa-da-serra': ('d', 4, 10), 'penacova': ('d', 7, 17), 'penela': ('d', 9, 29),
        'soure': ('d', 9, 21), 'tabua': ('d', 4, 10), 'vila-nova-de-poiares': ('d', 1, 13)
    },
    'evora': {
        'alandroal': ('p', 8), 'arraiolos': ('p', 39), 'borba': ('p', 1), 'estremoz': ('p', 39),
        'evora': ('d', 6, 29), 'montemor-o-novo': ('d', 3, 8), 'mora': ('p', 1),
        'mourao': ('d', 2, 2), 'portel': ('p', 1), 'redondo': ('p', 1),
        'reguengos-de-monsaraz': ('d', 6, 13), 'vendas-novas': ('d', 9, 7),
        'viana-do-alentejo': ('d', 1, 13), 'vila-vicosa': ('d', 8, 16)
    },
    'faro': {
        'albufeira': ('d', 8, 20), 'alcoutim': ('c', 9, 1, 4), 'aljezur': ('d', 8, 29),
        'castro-marim': ('d', 6, 24), 'faro': ('d', 9, 7), 'lagoa': ('d', 9, 8),
        'lagos': ('d', 10, 27), 'loule': ('p', 39), 'monchique': ('p', 39), 'olhao': ('d', 6, 16),
        'portimao': ('d', 12, 11), 'quarteira': ('p', 39), 'sao-bras-de-alportel': ('d', 6, 1),
        'silves': ('d', 9, 3), 'tavira': ('d', 6, 24), 'vila-do-bispo': ('d', 1, 22),
        'vila-real-de-santo-antonio': ('d', 5, 13)
    },
    'guarda': {
        'aguiar-da-beira': ('d', 2, 10), 'almeida': ('d', 7, 2), 'celorico-da-beira': ('d', 5, 23),
        'figueira-de-castelo-rodrigo': ('d', 7, 7), 'fornos-de-algodres': ('d', 9, 29),
        'gouveia': ('c', 8, 2, 0), 'guarda': ('d', 11, 27), 'manteigas': ('d', 3, 4),
        'meda': ('d', 11, 11), 'pinhel': ('d', 8, 25), 'sabugal': ('p', 8), 'seia': ('d', 7, 3),
        'trancoso': ('d', 5, 29), 'vila-nova-de-foz-coa': ('d', 5, 21)
    },
    'leiria': {
        'alcobaca': ('d', 8, 20), 'alvaiazere': ('d', 6, 13), 'ansiao': ('p', 39),
        'batalha': ('d', 8, 14), 'bombarral': ('d', 6, 29), 'caldas-da-rainha': ('d', 5, 15),
        'castanheira-de-pera': ('d', 7, 4), 'figueiro-dos-vinhos': ('d', 6, 24),
        'leiria': ('d', 5, 22), 'marinha-grande': ('p', 39), 'nazare': ('d', 9, 8),
        'obidos': ('d', 1, 11), 'pedrogao-grande': ('d', 7, 24), 'peniche': ('c', 8, 1, 0),
        'pombal': ('d', 11, 11), 'porto-de-mos': ('d', 6, 29)
    },
    'lisboa': {
        'alenquer': ('p', 39), 'arruda-dos-vinhos': ('p', 39), 'azambuja': ('p', 39),
        'cadaval': ('d', 1, 13), 'cascais': ('d', 6, 13), 'lisboa': ('d', 6, 13),
        'loures': ('d', 8, 26), 'lourinha': ('d', 6, 24), 'mafra': ('p', 39),
        'oeiras': ('d', 6, 7), 'sintra': ('d', 6, 29), 'sobral-de-monte-agraco': ('p', 39),
        'torres-vedras': ('d', 11, 11), 'vila-franca-de-xira': ('p', 39), 'amadora': ('d', 9, 11),
        'odivelas': ('d', 11, 19)
    },
    'portalegre': {
        'alter-do-chao': ('p', 39), 'arronches': ('d', 6, 24), 'avis': ('p', 1),
        'campo-maior': ('p', 1), 'castelo-de-vide': ('p', 1), 'crato': ('p', 1),
        'elvas': ('d', 1, 14), 'fronteira': ('d', 4, 6), 'gaviao': ('d', 11, 23),
        'marvao': ('d', 9, 8), 'monforte': ('p', 8), 'nisa': ('p', 1), 'ponte-de-sor': ('p', 1),
        'portalegre': ('d', 5, 23), 'sousel': ('p', 1)
    },
    'porto': {
        'amarante': ('d', 7, 8), 'baiao': ('d', 8, 24), 'felgueiras': ('d', 6, 29),
        'gondomar': ('c', 10, 1, 0), 'lousada': ('e', 7), 'maia': ('c', 7, 2, 0),
        'marco-de-canaveses': ('d', 9, 8), 'matosinhos': ('p', 51),
        'pacos-de-ferreira': ('d', 11, 6), 'paredes': ('c', 7, 3, 0), 'penafiel': ('d', 11, 11),
        'porto': ('d', 6, 24), 'povoa-de-varzim': ('d', 6, 29), 'santo-tirso': ('d', 7, 11),
        'valongo': ('d', 6, 24), 'vila-do-conde': ('d', 6, 24),
        'vila-nova-de-gaia': ('d', 6, 24), 'trofa': ('d', 11, 19)
    },
    'santarem': {
        'abrantes': ('d', 6, 14), 'alcanena': ('p', 39), 'almeirim': ('p', 39),
        'alpiarca': ('d', 4, 2), 'benavente': ('p', 39), 'cartaxo': ('p', 39),
        'chamusca': ('p', 39), 'constancia': ('p', 1), 'coruche': ('d', 8, 17),
        'entroncamento': ('d', 11, 24), 'fatima': ('d', 5, 13), 'ferreira-do-zezere': ('d', 6, 13),
        'golega': ('p', 39), 'macao': ('p', 1), 'rio-maior': ('d', 11, 6),
        'salvaterra-de-magos': ('p', 39), 'santarem': ('d', 3, 19), 'sardoal': ('d', 9, 22),
        'tomar': ('d', 3, 1), 'torres-novas': ('p', 39), 'vila-nova-da-barquinha': ('d', 6, 13),
        'ourem': ('d', 6, 20)
    },
    'setubal': {
        'alcacer-do-sal': ('d', 6, 24), 'alcochete': ('d', 6, 24), 'almada': ('d', 6, 24),
        'barreiro': ('d', 6, 28), 'grandola': ('d', 10, 22), 'moita': ('c', 9, 2, 1),
        'montijo': ('d', 6, 29), 'palmela': ('d', 6, 1), 'santiago-do-cacem': ('d', 7, 25),
        'seixal': ('d', 6, 29), 'sesimbra': ('d', 5, 4), 'setubal': ('d', 9, 15),
        'sines': ('d', 11, 24)
    },
    'viana-do-castelo': {
        'arcos-de-valdevez': ('d', 7, 11), 'caminha': ('p', 1), 'melgaco': ('p', 39),
        'moncao': ('d', 3, 12), 'paredes-de-coura': ('d', 8, 10), 'ponte-da-barca': ('d', 8, 24),
        'ponte-de-lima': ('d', 9, 20), 'valenca': ('d', 2, 18), 'viana-do-castelo': ('d', 8, 20),
        'vila-nova-de-cerveira': ('d', 10, 1)
    },
    'vila-real': {
        'alijo': ('d', 11, 11), 'boticas': ('d', 11, 6), 'chaves': ('d', 7, 8),
        'mesao-frio': ('d', 11, 30), 'mondim-de-basto': ('d', 7, 25), 'montalegre': ('d', 6, 9),
        'murca': ('d', 5, 8), 'peso-da-regua': ('d', 8, 16), 'ribeira-de-pena': ('d', 8, 16),
        'sabrosa': ('d', 9, 8), 'santa-marta-de-penaguiao': ('d', 1, 13), 'valpacos': ('d', 11, 6),
        'vila-pouca-de-aguiar': ('d', 6, 22), 'vila-real': ('d', 6, 13)
    },
    'viseu': {
        'armamar': ('d', 6, 24), 'carregal-do-sal': ('c', 7, 3, 0), 'castro-daire': ('d', 6, 29),
        'cinfaes': ('d', 6, 24), 'lamego': ('d', 9, 8), 'mangualde': ('d', 9, 8),
        'moimenta-da-beira': ('d', 6, 24), 'mortagua': ('p', 39), 'nelas': ('d', 6, 24),
        'oliveira-de-frades': ('d', 10, 7), 'penalva-do-castelo': ('d', 8, 25),
        'penedono': ('d', 6, 29), 'resende': ('d', 9, 29), 'santa-comba-dao': ('p', 39),
        'sao-joao-da-pesqueira': ('d', 6, 24), 'sao-pedro-do-sul': ('d', 6, 29),
        'satao': ('d', 8, 20), 'sernancelhe': ('d', 5, 3), 'tabuaco': ('d', 6, 24),
        'tarouca': ('d', 9, 29), 'tondela': ('d', 9, 16), 'vila-nova-de-paiva': ('d', 3, 2),
        'viseu': ('d', 9, 21), 'vouzela': ('d', 5, 14)
    },
    'madeira': {
        'santa-cruz': ('d', 1, 15), 'ponta-do-sol': ('d', 9, 8), 'porto-moniz': ('d', 7, 22),
        'ribeira-brava': ('d', 6, 29), 'calheta': ('d', 6, 24), 'porto-santo': ('d', 6, 24),
        'santana': ('d', 5, 25), 'sao-vicente': ('d', 1, 22), 'funchal': ('d', 8, 21),
        'camara-de-lobos': ('d', 10, 4), 'machico': ('d', 10, 9)
    },
    'acores': {
        'sao-roque-do-pico': ('d', 8, 16), 'madalena': ('d', 7, 22), 'ribeira-grande': ('d', 6, 29),
        'lajes-do-pico': ('d', 6, 29), 'angra-do-heroismo': ('d', 6, 24), 'horta': ('d', 6, 24),
        'santa-cruz-das-flores': ('d', 6, 24), 'vila-franca-do-campo': ('d', 6, 24),
        'vila-do-porto': ('d', 6, 24), 'praia-da-vitoria': ('d', 6, 20),
        'vila-nova-do-corvo': ('d', 6, 20), 'lagoa': ('d', 4, 11), 'velas': ('d', 4, 23),
        'nordeste': ('d', 7, 18), 'calheta': ('d', 11, 25), 'ponta-delgada': ('p', 36),
        'povoacao': ('p', 61), 'santa-cruz-da-graciosa': ('c', 8, 2, 0),
    }
}


def get_leap_years(start: int, end: int, full=True) -> Union[List[int], Dict[int, bool]]:
    """ Checks for a range of year if they are leap years or not

    : params :
    start: starting year, format %Y
    end: end year, format %Y
    """
    check = {i: (True if calendar.isleap(i) else False) for i in range(start, end+1, 1)}

    if full:
        return check
    else:
        return [y for y, v in check.items() if v]


def get_leap_days(start: int, end: int) -> List[datetime]:
    """ Returns a list of datetime objects with the 29 of february for leap
    in the input range of years
    """
    leap_years = get_leap_years(start, end, full=False)

    return [datetime(y, 2, 29) for y in leap_years]


def get_feriados_nacionais(year: int) -> List[datetime]:
    """ Calculate the dates of all the Portuguese national holidays for a year

    : params :
    year: format %Y
    """

    _p = easter(year)  # isto da a data como objecto de date e nao datetime
    pascoa = datetime(_p.year, _p.month, _p.day)

    feriados_nacionais = [
        datetime(year, 1, 1),    # ano novo
        pascoa+timedelta(days=-47),  # carnaval
        pascoa+timedelta(days=-2),   # sexta-feira santa
        pascoa,  # pascoa
        datetime(year, 4, 25),   # 25 de abril
        datetime(year, 5, 1),    # dia do trabalhador
        datetime(year, 6, 10),   # dia de portugal
        pascoa+timedelta(days=60),  # corpo de deus
        datetime(year, 8, 15),   # assuncao maria
        datetime(year, 10, 5),   # implatacao da republica
        datetime(year, 11, 1),   # todos os santos
        datetime(year, 12, 1),   # restauracao da independencia
        datetime(year, 12, 8),   # imaculada conceicao
        datetime(year, 12, 25),  # natal
    ]

    return feriados_nacionais


def get_multi_feriados_nacionais(start: int, end: int) -> List[datetime]:
    """ Calculates the Portuguese national holidays for several years

    : params :
    start: starting year, format %Y
    end: end year, format %Y
    """

    feriados_nacionais = []
    for i in range(start, end+1, 1):
        feriados_nacionais += get_feriados_nacionais(i)

    return feriados_nacionais


def get_feriados_municipais(year: int, cidade: str) -> datetime:
    """ Calculate the municipal holiday for a Portuguse city for a given year

    : params :
    cidade: name of a Portuguese city available in the list DISTRITOS
    """

    _p = easter(year)  # convert easter date object to datetime
    pascoa = datetime(_p.year, _p.month, _p.day)

    def _get_cld(year, mes, semana, dia):
        """ To find moving holidays """
        d = cld.monthdatescalendar(year, mes)[semana][dia]
        return datetime(d.year, d.month, d.day)  # convert date to datetime

    # get the code from DISTRITOS, for the target city, to calculate the date
    for k, v in DISTRITOS.items():
        if cidade in v:
            codigo = v[cidade]
        else:
            pass

    # calculate the date of the holiday from the code
    check = codigo[0]
    if check == 'd':  # fix days
        feriado = datetime(year, codigo[1], codigo[2])
    elif check == 'p':  # holidays calculated based on easter day
        feriado = pascoa+timedelta(days=codigo[1])
    elif check == 'c':  # moving holidays 'segunda depois de terceiro domingo...'
        feriado = _get_cld(year, codigo[1], codigo[2], codigo[3])
    elif check == 'e':  # special case from 'lousada'
        feriado = datetime(year, 7, max(w[-1] for w in calendar.monthcalendar(year, 7)))\
                  + timedelta(days=1)
    else:
        feriado = None

    return feriado


def get_feriados_zona(ano: int, distrito: Optional[Union[str, List[str]]] = None,
                      municipio: Optional[Union[str, List[str]]] = None) -> List[datetime]:
    """ Get a list of the holidays for a distrito or municipio or a list o locations
    If given a distrito, it returns all the municipal holidays in that distrito
    """

    feriados = []

    if distrito is not None:
        dist = distrito if isinstance(distrito, list) else [distrito]
        for d in dist:
            for m in DISTRITOS[d].keys():
                feriado = get_feriados_municipais(ano, m)
                if feriado not in feriados:
                    feriados.append(feriado)

    if municipio is not None:
        muni = municipio if isinstance(municipio, list) else [municipio]
        for m in muni:
            feriado = get_feriados_municipais(ano, m)
            if feriado not in feriados:
                feriados.append(feriado)

    return feriados


def get_days_range(date_range: Union[Tuple[str, str], str],
                   date_format: str = '%Y-%m-%d') -> pd.Series:
    """ Build series with dates for the given date interval

    : params :
    The data_range can be:
    - (start, end) tuple with start and end date, ex. ('2020-4-6', '2020-4-12')
    - 'year-week' target year and week, ex. '2020-15'
    """

    if isinstance(date_range, tuple):
        start = datetime.strptime(date_range[0], date_format)
        end = datetime.strptime(date_range[1], date_format)
    else:
        # atention to ISO format; returns the start and end day of the given week
        start = datetime.strptime(date_range+'-1', "%G-%V-%u")
        end = datetime.strptime(date_range+'-7', "%G-%V-%u")

    return pd.Series(data=0., index=pd.date_range(start, end))


def calc_days_type(date_range: Union[Tuple[str, str], str], feriados: bool = False,
                   date_format: str = '%Y-%m-%d', **kwargs: Union[str, List[str]]) -> pd.Series:
    """ Classify the days acordling to the code below for the given date range
        - business day: 0
        - weekend: 1
        - national holiday: 2
        - municipal holiday: 3
    """

    target_days = get_days_range(date_range)

    # Ccalculate all the target holidays either national or municipal
    f_nacionais, f_municipais = [], []
    if feriados:
        # get the year in the given date range to calculate the holdidays
        years = [y.year for y in target_days.groupby(pd.Grouper(freq='Y')).sum().index.unique()]
        distrito = kwargs['distrito'] if 'distrito' in kwargs else None
        municipio = kwargs['municipio'] if 'municipio' in kwargs else None
        for y in years:
            f_nacionais += get_feriados_nacionais(y)
            f_municipais += get_feriados_zona(y, distrito=distrito,  municipio=municipio)

    # classify the date range
    for day in target_days.index:
        target_days[day] = 0 if day.isoweekday() < 6 else 1
        if feriados:
            if day in f_municipais:
                target_days[day] = 3
            if day in f_nacionais:
                target_days[day] = 2

    return target_days


def get_dias_uteis(date_range: Union[Tuple[str, str], str], group: Union[bool, str] = False,
                   feriados: bool = False, date_format: str = '%Y-%m-%d',
                   **kwargs: Union[str, List[str]]) -> pd.Series:
    """ Classify the days of the week in the input date range in business days (1)
    and non business days (0);
    If choosing to group the dates then returns the sum of business days

    : params :
    date_range: date range to classify the days
    group: if False returns a string with the sum of all day types, else it can
           group by week ('W'), month ('M'), year ('y')
    feriados: take into account holidays as non business days, may require input
              of kwargs (see below), if true national holidays are always included
    date_format: string format of input dates
    kwargs: option to include national and municipal holidays
        - distrito : include the municipal holidays of all the municipios in a
                     distrito
        - municipio : include holidays of a certain municipio
    """

    by_day = calc_days_type(date_range, feriados, date_format, **kwargs)

    if not group:  # senao agrupar calcula e devolve a soma
        dias_total = by_day.count()
        dias_uteis = by_day[by_day == 0].count()
        dias_f_nacionais = by_day[by_day == 2].count()
        dias_f_municipais = by_day[by_day == 3].count()

        results = (f'Total dias: {dias_total} - Dias uteis: {dias_uteis}'
                   f' - Feriados Nacionais: {dias_f_nacionais}'
                   f' - Feriados Municipais: {dias_f_municipais}')
    else:
        dias_uteis = by_day[by_day == 0]  # selecionar so dias uteis
        results = dias_uteis.groupby(pd.Grouper(freq=group)).count()

    return results


def class_distancia_fds(df: pd.DataFrame) -> pd.DataFrame:
    """ Classify the days of the week accrodling to the distance to the weekend
    weekend: 0; monday/friday: 3; tuesday/thursday: 2; wednesday: 1 ;

    Days of the week accordingly to ISO 8601 -> datetime.isoweekday()
    1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday',
    6: 'Saturday', 7: 'Sunday'
    """

    df = df.assign(distancia=0)

    distancias = {1: 3, 2: 2, 3: 1, 4: 2, 5: 3, 6: 0, 7: 0}

    for i in df.index:
        df.at[i, 'distancia'] = distancias[datetime.isoweekday(i)]

    return df


def get_feriados(date_range: Tuple[str, str], distance: bool = False,
                 multiply: bool = False, group: str = 'B', date_format: str = '%Y-%m-%d',
                 **kwargs: Union[str, List[str]]) -> pd.DataFrame:
    """ WRAPPER FUNCTION
    Classify the days of the week in the input date range in business days (0)
    and non business days (1), classify the weekdays accordingly to their
    distance to the weekend

    : params :
    date_range: date range to classify the days
    distance: calculate the distance to the weekend
    multiply: multiply the the distance by the classification of the holiday
    group: group by business days 'B' ou days 'D'
    kwargs : see function get_dias_uteis
    """

    df = (get_dias_uteis(date_range, group=group, feriados=True, date_format=date_format)
          .to_frame()
          .rename(columns={0: 'feriados'})
          .replace({0: 1, 1: 0}))  # invert the classes

    if distance:
        df = class_distancia_fds(df)
        if multiply:
            df = (df['feriados']*df['distancia']).to_frame().rename(columns={0: 'feriados'})

    return df
