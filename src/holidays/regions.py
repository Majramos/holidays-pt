#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  regions.py
#
#  Copyright 2022 Marco Ramos <majramos@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


"""
Module to store information on the distritos/concelhos and respective holidays
distrito -> concelho/municipio -> codigo
"""



from .utils import flatten


REGIONS_CODES: dict[str, dict[str, list[str]]] = {
    'aveiro': {
        'agueda': ['ptr0001'],
        'albergaria-a-velha': ['ptr0002'],
        'anadia': ['ptr0003'],
        'arouca': ['ptr0004'],
        'aveiro': ['ptr0005'],
        'castelo-de-paiva': ['ptr0006'],
        'espinho': ['ptr0007'],
        'estarreja': ['ptr0008'],
        'santa-maria-da-feira': ['ptr0009'],
        'ilhavo': ['ptr0010'],
        'mealhada': ['ptr0003'],
        'murtosa': ['ptr0011'],
        'oliveira-de-azemeis': ['ptr0012'],
        'oliveira-do-bairro': ['ptr0003'],
        'ovar': ['ptr0013'],
        'sao-joao-da-madeira': ['ptr0014'],
        'sever-do-vouga': ['ptr0015'],
        'vagos': ['ptr0016'],
        'vale-de-cambra': ['ptr0008']
    },
    'beja': {
        'aljustrel': ['ptr0008'],
        'almodovar': ['ptr0006'],
        'alvito': ['ptr0003'],
        'barrancos': ['ptr0017'],
        'beja': ['ptr0003'],
        'castro-verde': ['ptr0018'],
        'cuba': ['ptr0010'],
        'ferreira-do-alentejo': ['ptr0019'],
        'mertola': ['ptr0006'],
        'moura': ['ptr0006'],
        'odemira': ['ptr0020'],
        'ourique': ['ptr0021'],
        'serpa': [],
        'vidigueira': ['ptr0003']
    },
    'braga': {
        'amares': ['ptr0008'],
        'barcelos': ['ptr0022'],
        'braga': ['ptr0006'],
        'cabeceiras-de-basto': ['ptr0023'],
        'celorico-de-basto': ['ptr0024'],
        'esposende': ['ptr0025'],
        'fafe': ['ptr0026'],
        'guimaraes': ['ptr0027'],
        'povoa-de-lanhoso': ['ptr0028'],
        'terras-de-bouro': ['ptr0029'],
        'vieira-do-minho': ['ptr0030'],
        'vila-nova-de-famalicao': ['ptr0008'],
        'vila-verde': ['ptr0008'],
        'vizela': ['ptr0028']
    },
    'braganca': {
        'alfandega-da-fe': ['ptr0018'],
        'braganca': ['ptr0031'],
        'carrazeda-de-ansiaes': [],
        'freixo-de-espada-a-cinta': ['ptr0010'],
        'macedo-de-cavaleiros': ['ptr0018'],
        'miranda-do-douro': ['ptr0032'],
        'mirandela': ['ptr0033'],
        'mogadouro': ['ptr0034'],
        'torre-de-moncorvo': ['ptr0028'],
        'vila-flor': ['ptr0035'],
        'vimioso': ['ptr0036'],
        'vinhais': ['ptr0037']
    },
    'castelo-branco': {
        'belmonte': ['ptr0038'],
        'castelo-branco': ['ptr0039'],
        'covilha': ['ptr0040'],
        'fundao': ['ptr0041'],
        'idanha-a-nova': ['ptr0042'],
        'oleiros': ['ptr0043'],
        'penamacor': ['ptr0010'],
        'proenca-a-nova': ['ptr0008'],
        'serta': ['ptr0044'],
        'vila-de-rei': ['ptr0045'],
        'vila-velha-de-rodao': ['ptr0046']
    },
    'coimbra': {
        'arganil': ['ptr0047'],
        'cantanhede': ['ptr0024'],
        'coimbra': ['ptr0048'],
        'condeixa-a-nova': ['ptr0049'],
        'figueira-da-foz': ['ptr0006'],
        'gois': ['ptr0050'],
        'lousa': ['ptr0006'],
        'mira': ['ptr0051'],
        'miranda-do-corvo': ['ptr0052'],
        'montemor-o-velho': ['ptr0053'],
        'oliveira-do-hospital': ['ptr0054'],
        'pampilhosa-da-serra': ['ptr0055'],
        'penacova': ['ptr0056'],
        'penela': ['ptr0023'], 
        'soure': ['ptr0015'],
        'tabua': ['ptr0057'],
        'vila-nova-de-poiares': ['ptr0058']
    },
    'evora': {
        'alandroal': ['ptr0059'],
        'arraiolos': ['ptr0003'],
        'borba': ['ptr0010'],
        'estremoz': ['ptr0003'],
        'evora': ['ptr0018'],
        'montemor-o-novo': ['ptr0060'],
        'mora': ['ptr0010'],
        'mourao': ['ptr0061'],
        'portel': ['ptr0010'],
        'redondo': ['ptr0010'],
        'reguengos-de-monsaraz': ['ptr0008'],
        'vendas-novas': ['ptr0062'],
        'viana-do-alentejo': ['ptr0058'],
        'vila-vicosa': ['ptr0063']
    },
    'faro': {
        'albufeira': ['ptr0064'],
        'alcoutim': ['ptr0065'],
        'aljezur': ['ptr0066'],
        'castro-marim': ['ptr0006'],
        'faro': ['ptr0067'],
        'lagoa': ['ptr0068'],
        'lagos': ['ptr0069'],
        'loule': ['ptr0003'],
        'monchique': ['ptr0003'],
        'olhao': ['ptr0070'],
        'portimao': ['ptr0071'],
        'quarteira': ['ptr0003'],
        'sao-bras-de-alportel': ['ptr0072'],
        'silves': ['ptr0073'],
        'tavira': ['ptr0006'],
        'vila-do-bispo': ['ptr0074'],
        'vila-real-de-santo-antonio': ['ptr0075']
    },
    'guarda': {
        'aguiar-da-beira': ['ptr0076'],
        'almeida': ['ptr0076'],
        'celorico-da-beira': ['ptr0078'],
        'figueira-de-castelo-rodrigo': ['ptr0079'],
        'fornos-de-algodres': ['ptr0023'],
        'gouveia': ['ptr0080'],
        'guarda': ['ptr0081'],
        'manteigas': ['ptr0082'],
        'meda': ['ptr0083'],
        'pinhel': ['ptr0084'],
        'sabugal': ['ptr0085'],
        'seia': ['ptr0086'],
        'trancoso': ['ptr0087'],
        'vila-nova-de-foz-coa': ['ptr0088']
    },
    'leiria': {
        'alcobaca': ['ptr0089'],
        'alvaiazere': ['ptr0008'],
        'ansiao': ['ptr0003'],
        'batalha': ['ptr0090'],
        'bombarral': ['ptr0018'],
        'caldas-da-rainha': ['ptr0091'],
        'castanheira-de-pera': ['ptr0092'],
        'figueiro-dos-vinhos': ['ptr0006'],
        'leiria': ['ptr0093'],
        'marinha-grande': ['ptr0003'],
        'nazare': ['ptr0094'],
        'obidos': ['ptr0095'],
        'pedrogao-grande': ['ptr0096'],
        'peniche': ['ptr0097'],
        'pombal': ['ptr0083'],
        'porto-de-mos': ['ptr0018']
    },
    'lisboa': {
        'alenquer': ['ptr0003'],
        'arruda-dos-vinhos': ['ptr0003'],
        'azambuja': ['ptr0003'],
        'cadaval': ['ptr0058'],
        'cascais': ['ptr0008'],
        'lisboa': ['ptr0008'],
        'loures': ['ptr0098'],
        'lourinha': ['ptr0006'],
        'mafra': ['ptr0003'],
        'oeiras': ['ptr0099'],
        'sintra': ['ptr0018'],
        'sobral-de-monte-agraco': ['ptr0003'],
        'torres-vedras': ['ptr0083'],
        'vila-franca-de-xira': ['ptr0003'],
        'amadora': ['ptr0100'],
        'odivelas': ['ptr0101']
    },
    'portalegre': {
        'alter-do-chao': ['ptr0003'],
        'arronches': ['ptr0006'],
        'avis': ['ptr0010'],
        'campo-maior': ['ptr0010'],
        'castelo-de-vide': ['ptr0102'],
        'crato': ['ptr0103'],
        'elvas': ['ptr0104'],
        'fronteira': ['ptr0105'],
        'gaviao': ['ptr0106'],
        'marvao': ['ptr0107'],
        'monforte': ['ptr0108'],
        'nisa': ['ptr0109'],
        'ponte-de-sor': ['ptr0010'],
        'portalegre': ['ptr0110'],
        'sousel': ['ptr0111']
    },
    'porto': {
        'amarante': ['ptr0112'],
        'baiao': ['ptr0035'],
        'felgueiras': ['ptr0018'],
        'gondomar': ['ptr0113'],
        'lousada': ['ptr0114'],
        'maia': ['ptr0115'],
        'marco-de-canaveses': ['ptr0116'],
        'matosinhos': ['ptr0117'],
        'pacos-de-ferreira': ['ptr0118'],
        'paredes': ['ptr0119'],
        'penafiel': ['ptr0083'],
        'porto': ['ptr0006'],
        'povoa-de-varzim': ['ptr0018'],
        'santo-tirso': ['ptr0120'],
        'valongo': ['ptr0006'],
        'vila-do-conde': ['ptr0006'],
        'vila-nova-de-gaia': ['ptr0006'],
        'trofa': ['ptr0101']
    },
    'santarem': {
        'abrantes': ['ptr0121'],
        'alcanena': ['ptr0003'],
        'almeirim': ['ptr0003'],
        'alpiarca': ['ptr0122'],
        'benavente': ['ptr0003'],
        'cartaxo': ['ptr0003'],
        'chamusca': ['ptr0003'],
        'constancia': ['ptr0123'],
        'coruche': ['ptr0124'],
        'entroncamento': ['ptr0125'],
        'fatima': ['ptr0126'],
        'ferreira-do-zezere': ['ptr0008'],
        'golega': ['ptr0003'],
        'macao': ['ptr0010'],
        'rio-maior': ['ptr0118'],
        'salvaterra-de-magos': ['ptr0003'],
        'santarem': ['ptr0028'],
        'sardoal': ['ptr0127'],
        'tomar': ['ptr0128'],
        'torres-novas': ['ptr0003'],
        'vila-nova-da-barquinha': ['ptr0008'],
        'ourem': ['ptr0129']
    },
    'setubal': {
        'alcacer-do-sal': ['ptr0006'],
        'alcochete': ['ptr0006'],
        'almada': ['ptr0006'],
        'barreiro': ['ptr0130'],
        'grandola': ['ptr0131'],
        'moita': ['ptr0132'],
        'montijo': ['ptr0018'],
        'palmela': ['ptr0133'],
        'santiago-do-cacem': ['ptr0024'],
        'seixal': ['ptr0018'],
        'sesimbra': ['ptr0134'],
        'setubal': ['ptr0135'],
        'sines': ['ptr0136']
    },
    'viana-do-castelo': {
        'arcos-de-valdevez': ['ptr0120'],
        'caminha': ['ptr0010'],
        'melgaco': ['ptr0003'],
        'moncao': ['ptr0137'],
        'paredes-de-coura': ['ptr0036'],
        'ponte-da-barca': ['ptr0035'],
        'ponte-de-lima': ['ptr0138'],
        'valenca': ['ptr0139'],
        'viana-do-castelo': ['ptr0140'],
        'vila-nova-de-cerveira': ['ptr0141']
    },
    'vila-real': {
        'alijo': ['ptr0083'],
        'boticas': ['ptr0118'],
        'chaves': ['ptr0142'],
        'mesao-frio': ['ptr0143'],
        'mondim-de-basto': ['ptr0024'],
        'montalegre': ['ptr0144'],
        'murca': ['ptr0145'],
        'peso-da-regua': ['ptr0146'],
        'ribeira-de-pena': ['ptr0146'],
        'sabrosa': ['ptr0147'],
        'santa-marta-de-penaguiao': ['ptr0058'],
        'valpacos': ['ptr0118'],
        'vila-pouca-de-aguiar': ['ptr0148'],
        'vila-real': ['ptr0008']
    },
    'viseu': {
        'armamar': ['ptr0006'],
        'carregal-do-sal': ['ptr0149'],
        'castro-daire': ['ptr0018'],
        'cinfaes': ['ptr0006'],
        'lamego': ['ptr0150'],
        'mangualde': ['ptr0151'],
        'moimenta-da-beira': ['ptr0006'],
        'mortagua': ['ptr0003'],
        'nelas': ['ptr0006'],
        'oliveira-de-frades': ['ptr0152'],
        'penalva-do-castelo': ['ptr0153'],
        'penedono': ['ptr0018'],
        'resende': ['ptr0023'],
        'santa-comba-dao': ['ptr0003'],
        'sao-joao-da-pesqueira': ['ptr0006'],
        'sao-pedro-do-sul': ['ptr0018'],
        'satao': ['ptr0089'],
        'sernancelhe': ['ptr0154'],
        'tabuaco': ['ptr0006'],
        'tarouca': ['ptr0023'],
        'tondela': ['ptr0155'],
        'vila-nova-de-paiva': ['ptr0156'],
        'viseu': ['ptr0015'],
        'vouzela': ['ptr0157']
    },
    'madeira': {
        'santa-cruz': ['ptr0158'],
        'ponta-do-sol': ['ptr0068'],
        'porto-moniz': ['ptr0159'],
        'ribeira-brava': ['ptr0018'],
        'calheta': ['ptr0006'],
        'porto-santo': ['ptr0160'],
        'santana': ['ptr0161'],
        'sao-vicente': ['ptr0074'],
        'funchal': ['ptr0162'],
        'camara-de-lobos': ['ptr0163'],
        'machico': ['ptr0164']
    },
    'acores': {
        'sao-roque-do-pico': ['ptr0165'],
        'madalena': ['ptr0159'],
        'ribeira-grande': ['ptr0018'],
        'lajes-do-pico': ['ptr0166'],
        'angra-do-heroismo': ['ptr0006'],
        'horta': ['ptr0006'],
        'santa-cruz-das-flores': ['ptr0006'],
        'vila-franca-do-campo': ['ptr0006'],
        'vila-do-porto': ['ptr0006'],
        'praia-da-vitoria': ['ptr0129'],
        'vila-nova-do-corvo': ['ptr0167'],
        'lagoa': ['ptr0168'],
        'velas': ['ptr0169'],
        'nordeste': ['ptr0170'],
        'calheta': ['ptr0171'],
        'ponta-delgada': ['ptr0172'],
        'povoacao': ['ptr0173'],
        'santa-cruz-da-graciosa': ['ptr0174']
    }
}


ls_districts: list[str] =  list(REGIONS_CODES.keys())
ls_counties = flatten([k.keys() for k in REGIONS_CODES.values()])


# get a dict with only the counties and respective holidays
counties = {}
for i in REGIONS_CODES.values():
    for k, v in i.items():
        counties[k] = v


def _check_exists(source: list[str], to_check: list[str]) -> None:
    """ Check if the given district/county is valid

    TODO: add ability to check which value is wrong

    Parameters
    ----------
    source : str, default=None
        values which to_check is compared against, list of valid inputs
    to_check : list of str
        Values to check if exist in source
    """

    if set(to_check).issubset(source):
        pass
    else:
        raise Exception('Input does not exist in Regions')


def select(*, district: list[str] = [], county: list[str] = []) -> list[str]:
    """ Select all the required regional holidays by location.

    Parameters
    ----------
    district : str, default=None
        Corresponds to district in Portugal in all lower case.
    county : str, default=None
        Corresponds to a county in Portugal in all lower case.

    Returns
    -------
    list of strings with holidays codes
    """

    if not district and not county:
        raise Exception('Requires either district or county')

    if district:
        _check_exists(ls_districts, district)
        county += flatten([REGIONS_CODES[dis].keys() for dis in district])

    location = []
    _check_exists(ls_counties, county)
    for con in county:
        location += counties[con]

    return set(location)
