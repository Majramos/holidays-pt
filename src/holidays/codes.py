#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  codes.py
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
module to store the codes used to calculate the date of the holidays
"""


from typing import Union


CODES: dict[str, dict[str, Union[str, list[int]]]] = {
    'ptn0001': {
        'extent': 'national', 'label': 'Ano Novo', 'type': 'f',
        'codes': [1, 1, 0], 'calculate': 'january 1st'
    },
    'ptn0002': {
        'extent': 'national', 'label': 'Carnaval', 'type': 'e', 'codes': [-47, 0, 0],
        'calculate': '47 days before easter sunday on a tuesday'
    },
    'ptn0003': {
        'extent': 'national', 'label': 'Sexta-Feira Santa', 'type': 'e',
        'codes': [-2, 0, 0], 'calculate': 'friday right before easter sunday'
    },
    'ptn0004': {
        'extent': 'national', 'label': 'Pascoa', 'type': 'e',
        'codes': [0, 0, 0], 'calculate': 'easter sunday'
    },
    'ptn0005': {
        'extent': 'national', 'label': '25 de Abril','type': 'f',
        'codes': [4, 25, 0], 'calculate': 'april 25th'
    },
    'ptn0006': {
        'extent': 'national', 'label': 'Dia do Trabalhador', 'type': 'f',
        'codes': [5, 1, 0], 'calculate': 'may 1th'
    },
    'ptn0007': {
        'extent': 'national', 'label': 'Dia de Portugal', 'type': 'f',
        'codes': [6, 10, 0], 'calculate': 'june 10th'
    },
    'ptn0008': {
        'extent': 'national', 'label': 'Corpo de Deus', 'type': 'e',
        'codes': [60, 0, 0], 'calculate': '60 days after easter sunday, on a thursday'
    },
    'ptn0009': {
        'extent': 'national', 'label': 'Assuncao Maria', 'type': 'f',
        'codes': [8, 15, 0], 'calculate': 'august 15th'
    },
    'ptn0010': {
        'extent': 'national', 'label': 'Implatacao da Republica',
        'type': 'f', 'codes': [10, 5, 0], 'calculate': 'october 5th'
    },
    'ptn0011': {
        'extent': 'national', 'label': 'Todos os Santos',
        'type': 'f', 'codes': [11, 1, 0], 'calculate': 'november 1st'
    },
    'ptn0012': {
        'extent': 'national', 'label': 'Restauracao da Independencia',
        'type': 'f', 'codes': [12, 1, 0], 'calculate': 'december 1st'
    },
    'ptn0013': {
        'extent': 'national', 'label': 'Imaculada Conceicao',
        'type': 'f', 'codes': [12, 8, 0], 'calculate': 'december 8th'
    },
    'ptn0014': {
        'extent': 'national', 'label': 'Natal', 'type': 'f',
        'codes': [12, 25, 0], 'calculate': 'december 25th'
    },
    'ptr0001': {
        'extent': 'regional', 'label': 'Sao Geraldo', 'type': 'e',
        'codes': [50, 0, 0], 'calculate': 'monday after pentacost sunday'
    },
    'ptr0002': {
        'extent': 'regional', 'label': 'Segunda-feira da Senhora do Socorro',
        'type': 'm', 'codes': [8, 3, 0], 'calculate': 'monday after third sunday of august'
    },
    'ptr0003': {
        'extent': 'regional', 'label': 'Quinta-feira da Ascensao/Dia da Espiga',
        'type': 'e', 'codes': [39, 0, 0], 'calculate': 'sixth thursday after easter sunday'
    },
    'ptr0004': {
        'extent': 'regional', 'label': 'Rainha Santa Mafalda',
        'type': 'f', 'codes': [5, 2, 0], 'calculate': 'may 2nd'
    },
    'ptr0005': {
        'extent': 'regional', 'label': 'Santa Joana Princesa',
        'type': 'f', 'codes': [5, 12, 0], 'calculate': 'may 12th'
    },
    'ptr0006': {
        'extent': 'regional', 'label': 'Sao Joao', 'type': 'f',
        'codes': [6, 24, 0], 'calculate': 'june 24th'
    },
    'ptr0007': {
        'extent': 'regional', 'label': 'Elevacao a cidade de Espinho',
        'type': 'f', 'codes': [6, 16, 0], 'calculate': 'june 16th'
    },
    'ptr0008': {
        'extent': 'regional', 'label': 'Santo Antonio', 'type': 'f',
        'codes': [6, 13, 0], 'calculate': 'june 13th'
    },
    'ptr0009': {
        'extent': 'regional', 'label': 'Sao Sebastiao', 'type': 'f',
        'codes': [1, 20, 0], 'calculate': 'january 20th'
    },
    'ptr0010': {
        'extent': 'regional', 'label': 'Segunda-feira de Pascoa',
        'type': 'e', 'codes': [1, 0, 0], 'calculate': 'monday after easter'
    },
    'ptr0011': {
        'extent': 'regional', 'label': 'Nossa Senhora da Natividade',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0012': {
        'extent': 'regional', 'label': 'Nossa Senhora de La Salette',
        'type': 'm', 'codes': [8, 2, 0], 'calculate': 'monday after first sunday of august'
    },
    'ptr0013': {
        'extent': 'regional', 'label': 'Sao Cristovao', 'type': 'f',
        'codes': [7, 25, 0], 'calculate': 'july 25th'
    },
    'ptr0014': {
        'extent': 'regional', 'label': 'Elevacao a cidade e fundacao do municipio',
        'type': 'f', 'codes': [10, 11, 0], 'calculate': 'october 11th'
    },
    'ptr0015': {
        'extent': 'regional', 'label': 'Sao Mateus', 'type': 'f',
        'codes': [9, 21, 0], 'calculate': 'september 21th'
    },
    'ptr0016': {
        'extent': 'regional', 'label': 'Divino Espirito Santo', 'type': 'e',
        'codes': [50, 0, 0], 'calculate': '50 days after easter sunday'
    },
    'ptr0017': {
        'extent': 'regional', 'label': 'Festa de Nossa Senhora da Conceicao',
        'type': 'f', 'codes': [8, 28, 0], 'calculate': 'august 28th'
    },
    'ptr0018': {
        'extent': 'regional', 'label': 'Sao Pedro', 'type': 'f',
        'codes': [6, 29, 0], 'calculate': 'june 29th'
    },
    'ptr0019': {
        'extent': 'regional', 'label': 'Outorgacao do foral manuelino',
        'type': 'f', 'codes': [3, 5, 0], 'calculate': 'march 5th'
    },
    'ptr0020': {
        'extent': 'regional', 'label': 'Nossa Senhora da Piedade',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0021': {
        'extent': 'regional', 'label': 'Nossa Senhora da Cola',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0022': {
        'extent': 'regional', 'label': 'Santa Cruz', 'type': 'f',
        'codes': [5, 3, 0], 'calculate': 'may 5th'
    },
    'ptr0023': {
        'extent': 'regional', 'label': 'Sao Miguel Arcanjo', 'type': 'f',
        'codes': [9, 29, 0], 'calculate': 'september 29th'
    },
    'ptr0024': {
        'extent': 'regional', 'label': 'Sao Tiago', 'type': 'f',
        'codes': [7, 25, 0], 'calculate': 'july 25th'
    },
    'ptr0025': {
        'extent': 'regional', 'label': 'Elevacao Esposende a categoria de vila',
        'type': 'f', 'codes': [8, 19, 0], 'calculate': 'august 19th'
    },
    'ptr0026': {
        'extent': 'regional', 'label': 'Feiras Francas', 'type': 'f',
        'codes': [5, 16, 0], 'calculate': 'may 16th'
    },
    'ptr0027': {
        'extent': 'regional', 'label': 'Batalha de Sao Mamede (1128)',
        'type': 'f', 'codes': [6, 24, 0], 'calculate': 'june 24th'
    },
    'ptr0028': {
        'extent': 'regional', 'label': 'Sao Jose', 'type': 'f',
        'codes': [3, 19, 0], 'calculate': 'march 19th'
    },
    'ptr0029': {
        'extent': 'regional', 'label': 'Foral de D. Manuel I (1514)',
        'type': 'f', 'codes': [10, 20, 0], 'calculate': 'october 20th'
    },
    'ptr0030': {
        'extent': 'regional', 'label': 'Encerramento da tradicional Feira da Ladra',
        'type': 'm', 'codes': [10, 1, 0], 'calculate': 'monday after first saturday of october'
    },
    'ptr0031': {
        'extent': 'regional', 'label': 'Nossa Senhora das Gracas',
        'type': 'f', 'codes': [8, 22, 0], 'calculate': 'august 22th'
    },
    'ptr0032': {
        'extent': 'regional', 'label': 'Elevacao de Miranda do Douro a cidade',
        'type': 'f', 'codes': [7, 10, 0], 'calculate': 'july 10th'
    },
    'ptr0033': {
        'extent': 'regional', 'label': 'Recebimento do Foral de D. Afonso III (1250)',
        'type': 'f', 'codes': [5, 25, 0], 'calculate': 'may 25th'
    },
    'ptr0034': {
        'extent': 'regional', 'label': 'Feira dos Gorazes', 'type': 'f',
        'codes': [10, 15, 0], 'calculate': 'october 15th'
    },
    'ptr0035': {
        'extent': 'regional', 'label': 'Sao Bartolomeu', 'type': 'f',
        'codes': [8, 24, 0], 'calculate': 'august 24th'
    },
    'ptr0036': {
        'extent': 'regional', 'label': 'Sao Lourenco', 'type': 'f',
        'codes': [8, 10, 0], 'calculate': 'august 10th'
    },
    'ptr0037': {
        'extent': 'regional', 'label': 'Outorgacao do foral manuelino',
        'type': 'f', 'codes': [5, 20, 0], 'calculate': 'may 20th'
    },
    'ptr0038': {
        'extent': 'regional', 'label': 'Primeira missa no Brasil',
        'type': 'f', 'codes': [4, 26, 0], 'calculate': 'april 26th'
    },
    'ptr0039': {
        'extent': 'regional', 'label': 'Nossa Senhora de Mercoles', 'type': 'e',
        'codes': [9, 0, 0], 'calculate': 'tuesday from second week after sunday easter'
    },
    'ptr0040': {
        'extent': 'regional', 'label': 'Elevacao Covilha a cidade',
        'type': 'f', 'codes': [10, 20, 0], 'calculate': 'october 20th'
    },
    'ptr0041': {
        'extent': 'regional', 'label': 'Santa Luzia', 'type': 'f',
        'codes': [9, 15, 0], 'calculate': 'september 15th'
    },
    'ptr0042': {
        'extent': 'regional', 'label': 'Nossa Senhora do Almortao', 'type': 'e',
        'codes': [15, 0, 0], 'calculate': 'third monday after easter'
    },
    'ptr0043': {
        'extent': 'regional', 'label': 'Santa Margarida', 'type': 'e',
        'codes': [8, 2, 0], 'calculate': 'monday after second sunday of august'
    },
    'ptr0044': {
        'extent': 'regional', 'label': 'Sao Nuno de Santa Maria (1360)',
        'type': 'f', 'codes': [6, 24, 0], 'calculate': 'june 24th'
    },
    'ptr0045': {
        'extent': 'regional', 'label': 'Recebimento do foral de D. Dinis',
        'type': 'f', 'codes': [9, 19, 0], 'calculate': 'september 19th'
    },
    'ptr0046': {
        'extent': 'regional', 'label': 'Nossa Senhora da Alagada', 'type': 'm',
        'codes': [8, 4, 0], 'calculate': 'monday after forth sunday of august'
    },
    'ptr0047': {
        'extent': 'regional', 'label': 'Nossa Senhora do Mont Alto',
        'type': 'f', 'codes': [9, 7, 0], 'calculate': 'september 7th'
    },
    'ptr0048': {
        'extent': 'regional', 'label': 'Rainha Santa Isabel',
        'type': 'f', 'codes': [7, 4, 0], 'calculate': 'july 4th'
    },
    'ptr0049': {
        'extent': 'regional', 'label': 'Santa Cristina',
        'type': 'f', 'codes': [7, 24, 0], 'calculate': 'july 24th'
    },
    'ptr0050': {
        'extent': 'regional', 'label': 'Doacao de Gois a Anaia Vestrares',
        'type': 'f', 'codes': [8, 13, 0], 'calculate': 'august 13th'
    },
    'ptr0051': {
        'extent': 'regional', 'label': 'Sao Tome',
        'type': 'f', 'codes': [7, 25, 0], 'calculate': 'july 25th'
    },
    'ptr0052': {
        'extent': 'regional', 'label': 'Nascimento de Jose Falcao (1841)',
        'type': 'f', 'codes': [6, 1, 0], 'calculate': 'june 1st'
    },
    'ptr0053': {
        'extent': 'regional', 'label': 'Nossa Senhora da Vitoria',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0054': {
        'extent': 'regional', 'label': 'Recebimento da noticia da Implantacao da Republica',
        'type': 'f', 'codes': [10, 7, 0], 'calculate': 'october 7th'
    },
    'ptr0055': {
        'extent': 'regional', 'label': 'Restauracao dos titulos de vila isenta',
        'type': 'f', 'codes': [4, 10, 0], 'calculate': 'april 10th'
    },
    'ptr0056': {
        'extent': 'regional', 'label': 'Nascimento de António Jose de Almeida',
        'type': 'f', 'codes': [7, 17, 0], 'calculate': 'july 17th'
    },
    'ptr0057': {
        'extent': 'regional', 'label': 'Restauracao da Comarca',
        'type': 'f', 'codes': [4, 10, 0], 'calculate': 'april 10th'
    },
    'ptr0058': {
        'extent': 'regional', 'label': 'Restauracao do municipio',
        'type': 'f', 'codes': [1, 13, 0], 'calculate': 'january 13th'
    },
    'ptr0059': {
        'extent': 'regional', 'label': 'Segunda-feira de Pascoela/Nossa Senhora da Boa Nova',
        'type': 'e', 'codes': [8, 0, 0], 'calculate': 'monday after easter'
    },
    'ptr0060': {
        'extent': 'regional', 'label': 'Sao Joao de Deus', 'type': 'f',
        'codes': [3, 8, 0], 'calculate': 'march 8th'
    },
    'ptr0061': {
        'extent': 'regional', 'label': 'Nossa Senhora das Candeias', 'type': 'f',
        'codes': [2, 2, 0], 'calculate': 'february 2nd'
    },
    'ptr0062': {
        'extent': 'regional', 'label': 'Elevacao de Vendas Novas a municipio',
        'type': 'f', 'codes': [9, 7, 0], 'calculate': 'september 7th'
    },
    'ptr0063': {
        'extent': 'regional', 'label': 'Nascimento de Couto Jardim', 'type': 'f',
        'codes': [8, 16, 0], 'calculate': 'august 16th'
    },
    'ptr0064': {
        'extent': 'regional', 'label': 'Foral de D. Manuel I (1504)', 'type': 'f',
        'codes': [8, 20, 0], 'calculate': 'august 20th'
    },
    'ptr0065': {
        'extent': 'regional', 'label': 'Dia do Municipio', 'type': 'm',
        'codes': [9, 1, 4], 'calculate': 'second monday of september'
    },
    'ptr0066': {
        'extent': 'regional', 'label': 'Banho Santo', 'type': 'f',
        'codes': [8, 29, 0], 'calculate': 'august 29th'
    },
    'ptr0067': {
        'extent': 'regional', 'label': 'Elevacao de Faro a cidade/Santa Maria de Faro',
        'type': 'f', 'codes': [9, 7, 0], 'calculate': 'september 7th'
    },
    'ptr0068': {
        'extent': 'regional', 'label': 'Nossa Senhora da Luz',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0069': {
        'extent': 'regional', 'label': 'Sao Goncalo de Lagos',
        'type': 'f', 'codes': [10, 27, 0], 'calculate': 'october 27th'
    },
    'ptr0070': {
        'extent': 'regional', 'label': 'Revolta de Olhao contra os Franceses (1808)',
        'type': 'f', 'codes': [6, 16, 0], 'calculate': 'june 16th'
    },
    'ptr0071': {
        'extent': 'regional', 'label': 'Elevacao de Portimao a cidade (1924)',
        'type': 'f', 'codes': [12, 11, 0], 'calculate': 'december 11th'
    },
    'ptr0072': {
        'extent': 'regional', 'label': 'Elevacao de Sao Bras de Alportel a cidade (1914)',
        'type': 'f', 'codes': [6, 1, 0], 'calculate': 'june 1st'
    },
    'ptr0073': {
        'extent': 'regional', 'label': 'Conquista da cidade aos mouros',
        'type': 'f', 'codes': [9, 3, 0], 'calculate': 'september 3rd'
    },
    'ptr0074': {
        'extent': 'regional', 'label': 'Sao Vicente',
        'type': 'f', 'codes': [1, 22, 0], 'calculate': 'january 22th'
    },
    'ptr0075': {
        'extent': 'regional', 'label': 'Elevação de Vila Real de Santo Antonio a cidade',
        'type': 'f', 'codes': [5, 13, 0], 'calculate': 'may 13th'
    },
    'ptr0076': {
        'extent': 'regional', 'label': 'Restauracao do concelho de Aguiar da Beira',
        'type': 'f', 'codes': [2, 10, 0], 'calculate': 'february 10th'
    },
    'ptr0077': {
        'extent': 'regional', 'label': 'Batalha do Coa (1810)',
        'type': 'f', 'codes': [7, 2, 0], 'calculate': 'july 2nd'
    },
    'ptr0078': {
        'extent': 'regional', 'label': 'Nascimento de Sacadura Cabral',
        'type': 'f', 'codes': [5, 23, 0], 'calculate': 'may 23th'
    },
    'ptr0079': {
        'extent': 'regional', 'label': 'Batalha de Salgadela (1664)',
        'type': 'f', 'codes': [7, 7, 0], 'calculate': 'july 7th'
    },
    'ptr0080': {
        'extent': 'regional', 'label': 'Nosso Senhor do Calvario',
        'type': 'm', 'codes': [8, 2, 0], 'calculate': 'monday after second sunday of august'
    },
    'ptr0081': {
        'extent': 'regional', 'label': 'Foral de D. Sancho I (1199)',
        'type': 'f', 'codes': [11, 27, 0], 'calculate': 'november 27th'
    },
    'ptr0082': {
        'extent': 'regional', 'label': 'Atribuicao do foral',
        'type': 'f', 'codes': [3, 4, 0], 'calculate': 'march 4th'
    },
    'ptr0083': {
        'extent': 'regional', 'label': 'Sao Martinho',
        'type': 'f', 'codes': [11, 11, 0], 'calculate': 'november 11th'
    },
    'ptr0084': {
        'extent': 'regional', 'label': 'Elevacao de Pinhel a cidade (2007)',
        'type': 'f', 'codes': [8, 25, 0], 'calculate': 'august 25th'
    },
    'ptr0085': {
        'extent': 'regional', 'label': 'Segunda-feira de Pascoela/Nossa Senhora dos Prazeres/Nossa Senhora da Graça)',
        'type': 'e', 'codes': [8, 0, 0], 'calculate': 'second monday after easter'
    },
    'ptr0086': {
        'extent': 'regional', 'label': 'Elevacao de Seia a cidade',
        'type': 'f', 'codes': [7, 3, 0], 'calculate': 'may 3rd'
    },
    'ptr0087': {
        'extent': 'regional', 'label': 'Batalha de Sao Marcos (1385)',
        'type': 'f', 'codes': [5, 29, 0], 'calculate': 'may 29th'
    },
    'ptr0088': {
        'extent': 'regional', 'label': 'Outorgacao do foral de D. Dinis',
        'type': 'f', 'codes': [5, 21, 0], 'calculate': 'may 21th'
    },
    'ptr0089': {
        'extent': 'regional', 'label': 'Sao Bernardo',
        'type': 'f', 'codes': [8, 20, 0], 'calculate': 'august 20th'
    },
    'ptr0090': {
        'extent': 'regional', 'label': 'Batalha de Aljubarrota (1385)',
        'type': 'f', 'codes': [8, 14, 0], 'calculate': 'august 14th'
    },
    'ptr0091': {
        'extent': 'regional', 'label': 'Fundacao da localidade pela rainha D. Leonor',
        'type': 'f', 'codes': [5, 15, 0], 'calculate': 'may 15th'
    },
    'ptr0092': {
        'extent': 'regional', 'label': 'Instalacao do municipio',
        'type': 'f', 'codes': [7, 4, 0], 'calculate': 'july 4th'
    },
    'ptr0093': {
        'extent': 'regional', 'label': 'Passagem a cidade e criacao da diocese',
        'type': 'f', 'codes': [5, 22, 0], 'calculate': 'may 22th'
    },
    'ptr0094': {
        'extent': 'regional', 'label': 'Nossa Senhora das Areias (ou da Nazare)',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0095': {
        'extent': 'regional', 'label': 'Tomada de Obidos aos mouros',
        'type': 'f', 'codes': [1, 11, 0], 'calculate': 'january 11th'
    },
    'ptr0096': {
        'extent': 'regional', 'label': 'Criacao do municipio',
        'type': 'f', 'codes': [7, 24, 0], 'calculate': 'july 24th'
    },
    'ptr0097': {
        'extent': 'regional', 'label': 'Nossa Senhora da Boa Viagem', 
        'type': 'm', 'codes': [8, 1, 0], 'calculate': 'monday after first sunday of august'
    },
    'ptr0098': {
        'extent': 'regional', 'label': 'Criacao do municipio',
        'type': 'f', 'codes': [8, 26, 0], 'calculate': 'august 26th'
    },
    'ptr0099': {
        'extent': 'regional', 'label': 'Criacao do municipio (1759)',
        'type': 'f', 'codes': [6, 7, 0], 'calculate': 'july 7th'
    },
    'ptr0100': {
        'extent': 'regional', 'label': 'Criacao do municipio',
        'type': 'f', 'codes': [9, 11, 0], 'calculate': 'september 11th'
    },
    'ptr0101': {
        'extent': 'regional', 'label': 'Criacao do municipio',
        'type': 'f', 'codes': [11, 19, 0], 'calculate': 'november 19th'
    },
    'ptr0102': {
        'extent': 'regional', 'label': 'Nossa Senhora da Luz',
        'type': 'e', 'codes': [1, 0, 0], 'calculate': 'monday after easter'
    },
    'ptr0103': {
        'extent': 'regional', 'label': 'Sao Gregorio',
        'type': 'e', 'codes': [1, 0, 0], 'calculate': 'monday after easter'
    },
    'ptr0104': {
        'extent': 'regional', 'label': 'Batalha das Linhas de Elvas (1659)',
        'type': 'f', 'codes': [1, 14, 0], 'calculate': 'january 14th'
    },
    'ptr0105': {
        'extent': 'regional', 'label': 'Batalha dos Atoleiros',
        'type': 'f', 'codes': [4, 6, 0], 'calculate': 'april 6th'
    },
    'ptr0106': {
        'extent': 'regional', 'label': 'Recebimento do foral manuelino',
        'type': 'f', 'codes': [11, 23, 0], 'calculate': 'november 23th'
    },
    'ptr0107': {
        'extent': 'regional', 'label': 'Nossa Senhora da Estrela',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0108': {
        'extent': 'regional', 'label': 'Segunda-feira de Pascoela/Nossa Senhora dos Prazeres',
        'type': 'e', 'codes': [8, 0, 0], 'calculate': 'second monday after easter'
    },
    'ptr0109': {
        'extent': 'regional', 'label': 'Nossa Senhora da Graca', 'type': 'e',
        'codes': [1, 0, 0], 'calculate': 'monday after easter'
    },
    'ptr0110': {
        'extent': 'regional', 'label': 'Elevacao Portalegre a cidade e criacao da diocese',
        'type': 'f', 'codes': [5, 23, 0], 'calculate': 'may 23th'
    },
    'ptr0111': {
        'extent': 'regional', 'label': 'Nossa Senhora do Carmo da Serra (de Sao Miguel)',
        'type': 'e', 'codes': [1, 0, 0], 'calculate': 'monday after easter'
    },
    'ptr0112': {
        'extent': 'regional', 'label': 'Elevacao Amarante a cidade',
        # TODO: check why this doesnt have calculate
        'type': 'f', 'codes': [7, 8, 0], 'calculate': ''
    },
    'ptr0113': {
        'extent': 'regional', 'label': 'Nossa Senhora do Rosario', 'type': 'm',
        'codes': [10, 1, 0], 'calculate': 'monday after first sunday of october'
    },
    'ptr0114': {
        'extent': 'regional', 'label': 'Nosso Senhor dos Aflitos', 'type': 's',
        'codes': [7, 0, 0], 'calculate': 'monday after last sunday of july'
    },
    'ptr0115': {
        'extent': 'regional', 'label': 'Nossa Senhora do Bom Despacho', 'type': 'm',
        'codes': [7, 2, 0], 'calculate': 'monday after second sunday of july'
    },
    'ptr0116': {
        'extent': 'regional', 'label': 'Nossa Senhora do Castelinho',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0117': {
        'extent': 'regional', 'label': 'Terca-feira de Pentecostes', 'type': 'e',
        'codes': [51, 0, 0], 'calculate': 'tuesday after sunday of pentacoste'
    },
    'ptr0118': {
        'extent': 'regional', 'label': 'Criacao do municipio', 'type': 'f',
        'codes': [11, 6, 0], 'calculate': 'november 6th'
    },
    'ptr0119': {
        'extent': 'regional', 'label': 'Divino Salvador', 'type': 'm',
        'codes': [7, 3, 0], 'calculate': 'monday after third sunday of july'
    },
    'ptr0120': {
        'extent': 'regional', 'label': 'Sao Bento', 'type': 'f',
        'codes': [7, 11, 0], 'calculate': 'july 11th'
    },
    'ptr0121': {
        'extent': 'regional', 'label': 'Elevacao Abrantes a cidade (1916)',
        'type': 'f', 'codes': [6, 14, 0], 'calculate': 'june 14th'
    },
    'ptr0122': {
        'extent': 'regional', 'label': 'Criacao do municipio',
        'type': 'f', 'codes': [4, 2, 0], 'calculate': 'april 2nd'
    },
    'ptr0123': {
        'extent': 'regional', 'label': 'Nossa Senhora da Boa Viagem',
        'type': 'e', 'codes': [1, 0, 0], 'calculate': 'monday after easter'
    },
    'ptr0124': {
        'extent': 'regional', 'label': 'Nossa Senhora do Castelo',
        'type': 'f', 'codes': [8, 17, 0], 'calculate': 'august 17th'
    },
    'ptr0125': {
        'extent': 'regional', 'label': 'Criacao do municipio Entroncamento (1945)',
        'type': 'f', 'codes': [11, 24, 0], 'calculate': 'november 24th'
    },
    'ptr0126': {
        'extent': 'regional', 'label': 'Nossa Senhora de Fatima',
        'type': 'f', 'codes': [5, 13, 0], 'calculate': 'may 13th'
    },
    'ptr0127': {
        'extent': 'regional', 'label': 'Elevacao Sardoal a categoria de vila',
        'type': 'f', 'codes': [9, 22, 0], 'calculate': 'september 22th'
    },
    'ptr0128': {
        'extent': 'regional', 'label': 'Fundacao do Castelo Templario',
        'type': 'f', 'codes': [3, 1, 0], 'calculate': 'march 1st'
    },
    'ptr0129': {
        'extent': 'regional', 'label': 'Elevacao a cidade Ourem/Praia da Vitoria',
        'type': 'f', 'codes': [6, 28, 0], 'calculate': 'june 28th'
    },
    'ptr0130': {
        'extent': 'regional', 'label': 'Elevacao Barreiro a cidade',
        'type': 'f', 'codes': [6, 28, 0], 'calculate': 'june 28th'
    },
    'ptr0131': {
        'extent': 'regional', 'label': 'Criacao do municipio de Grandola atraves do foral',
        'type': 'f', 'codes': [10, 22, 0], 'calculate': 'october 22th'
    },
    'ptr0132': {
        'extent': 'regional', 'label': 'Festas em Honra de Nossa Senhora da Boa Viagem',
        'type': 'm', 'codes': [9, 2, 1], 'calculate': 'tuesday after second sunday of september'
    },
    'ptr0133': {
        'extent': 'regional', 'label': 'Atribuicao do foral manuelino (1512) Palmela',
        'type': 'f', 'codes': [6, 1, 0], 'calculate': 'june 1st'
    },
    'ptr0134': {
        'extent': 'regional', 'label': 'Nosso Senhor Jesus das Chagas',
        'type': 'f', 'codes': [5, 4, 0], 'calculate': 'may 4th'
    },
    'ptr0135': {
        'extent': 'regional', 'label': 'Nascimento de Bocage', 'type': 'f',
        'codes': [9, 15, 0], 'calculate': 'september 15th'
    },
    'ptr0136': {
        'extent': 'regional', 'label': 'Elevacao Sines a vila (1362)',
        'type': 'f', 'codes': [11, 24, 0], 'calculate': 'november 24th'
    },
    'ptr0137': {
        'extent': 'regional', 'label': 'Atribuicao do foral a Moncao',
        'type': 'f', 'codes': [3, 12, 0], 'calculate': 'march 12th'
    },
    'ptr0138': {
        'extent': 'regional', 'label': 'Nossa Senhora das Dores',
        'type': 'f', 'codes': [9, 20, 0], 'calculate': 'september 20th'
    },
    'ptr0139': {
        'extent': 'regional', 'label': 'Sao Teotonio',
        'type': 'f', 'codes': [2, 18, 0], 'calculate': 'february 18th'
    },
    'ptr0140': {
        'extent': 'regional', 'label': 'Nossa Senhora da Agonia',
        'type': 'f', 'codes': [8, 20, 0], 'calculate': 'august 20th'
    },
    'ptr0141': {
        'extent': 'regional', 'label': 'Recebimento do foral manuelino Vila Nova de Cerveira',
        'type': 'f', 'codes': [10, 1, 0], 'calculate': 'october 1st'
    },
    'ptr0142': {
        'extent': 'regional', 'label': '1 Incursao Monarquica (1912) Chaves',
        'type': 'f', 'codes': [7, 8, 0], 'calculate': 'july 8th'
    },
    'ptr0143': {
        'extent': 'regional', 'label': 'Santo Andre',
        'type': 'f', 'codes': [11, 30, 0], 'calculate': 'november 30th'
    },
    'ptr0144': {
        'extent': 'regional', 'label': 'Atribuicao do foral Montalegre',
        'type': 'f', 'codes': [6, 9, 0], 'calculate': 'june 9th'
    },
    'ptr0145': {
        'extent': 'regional', 'label': 'Criacao do municipio Murça',
        'type': 'f', 'codes': [5, 8, 0], 'calculate': 'may 8th'
    },
    'ptr0146': {
        'extent': 'regional', 'label': 'Nossa Senhora do Socorro',
        'type': 'f', 'codes': [8, 16, 0], 'calculate': 'august 16th'
    },
    'ptr0147': {
        'extent': 'regional', 'label': 'Nossa Senhora do Rosario',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0148': {
        'extent': 'regional', 'label': 'Atribuicao do foral manuelino Vila Pouca de Aguiar',
        'type': 'f', 'codes': [6, 22, 0], 'calculate': 'june 22th'
    },
    'ptr0149': {
        'extent': 'regional', 'label': '', 'type': 'm', 'codes': [7, 3, 0],
        'calculate': 'monday after third sunday of july'
    },
    'ptr0150': {
        'extent': 'regional', 'label': 'Nossa Senhora dos Remedios',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0151': {
        'extent': 'regional', 'label': 'Nossa Senhora do Castelo',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0152': {
        'extent': 'regional', 'label': 'Restauracao do municipio Oliveira de Frades',
        'type': 'f', 'codes': [10, 7, 0], 'calculate': 'october 7th'
    },
    'ptr0153': {
        'extent': 'regional', 'label': 'Sao Genesio', 'type': 'f',
        'codes': [8, 25, 0], 'calculate': 'august 25th'
    },
    'ptr0154': {
        'extent': 'regional', 'label': 'Festa de Nossa Senhora ao Pe da Cruz',
        'type': 'f', 'codes': [5, 3, 0], 'calculate': 'may 3rd'
    },
    'ptr0155': {
        'extent': 'regional', 'label': 'Santa Eufemia', 'type': 'f',
        'codes': [9, 16, 0], 'calculate': 'september 16th'
    },
    'ptr0156': {
        'extent': 'regional', 'label': 'Estabelecimento e denominacao da sede de concelho',
        'type': 'f', 'codes': [3, 2, 0], 'calculate': 'march 2nd'
    },
    'ptr0157': {
        'extent': 'regional', 'label': 'Sao Frei Gil', 'type': 'f',
        'codes': [5, 14, 0], 'calculate': 'may 14th'
    },
    'ptr0158': {
        'extent': 'regional', 'label': 'Santo Amaro', 'type': 'f',
        'codes': [1, 15, 0], 'calculate': 'january 15th'
    },
    'ptr0159': {
        'extent': 'regional', 'label': 'Santa Maria Madalena', 'type': 'f',
        'codes': [7, 22, 0], 'calculate': 'july 22th'
    },
    'ptr0160': {
        'extent': 'regional', 'label': 'Criacao do municipio Porto Santo (1835)',
        'type': 'f', 'codes': [6, 24, 0], 'calculate': 'june 24th'
    },
    'ptr0161': {
        'extent': 'regional', 'label': 'Criacao do municipio Santana (1835)',
        'type': 'f', 'codes': [5, 25, 0], 'calculate': 'may 25th'
    },
    'ptr0162': {
        'extent': 'regional', 'label': 'Elevacao Funchal a cidade', 'type': 'f',
        'codes': [8, 21, 0], 'calculate': 'august 21th'
    },
    'ptr0163': {
        'extent': 'regional', 'label': 'Criacao do municipio Camara de Lobos',
        'type': 'f', 'codes': [10, 4, 0], 'calculate': 'october 4th'
    },
    'ptr0164': {
        'extent': 'regional', 'label': 'Criacao da Capitania de Machico',
        'type': 'f', 'codes': [10, 9, 0], 'calculate': 'october 9th'
    },
    'ptr0165': {
        'extent': 'regional', 'label': 'Sao Roque', 'type': 'f', 'codes': [8, 16, 0],
        'calculate': 'august 16th'
    },
    'ptr0166': {
        'extent': 'regional', 'label': 'Criacao do municipio Lajes do Pico',
        'type': 'f', 'codes': [6, 29, 0], 'calculate': 'june 29th'
    },
    'ptr0167': {
        'extent': 'regional', 'label': 'Elevacao a vila e sede de concelho (1832)',
        'type': 'f', 'codes': [6, 20, 0], 'calculate': 'june 20th'
    },
    'ptr0168': {
        'extent': 'regional', 'label': 'Criacao do municipio de Lagoa',
        'type': 'f', 'codes': [4, 11, 0], 'calculate': 'april 11th'
    },
    'ptr0169': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Jorge',
        'type': 'f', 'codes': [4, 23, 0], 'calculate': 'april 23th'
    },
    'ptr0170': {
        'extent': 'regional', 'label': 'Fundacao do municipio de Nordeste (1514)',
        'type': 'f', 'codes': [7, 18, 0], 'calculate': 'july 18th'
    },
    'ptr0171': {
        'extent': 'regional', 'label': 'Santa Catarina', 'type': 'f',
        'codes': [11, 25, 0], 'calculate': 'november 25th'
    },
    'ptr0172': {
        'extent': 'regional', 'label': 'Senhor Santo Cristo dos Milagres',
        'type': 'e', 'codes': [36, 0, 0], 'calculate': 'fifth monday after easter'
    },
    'ptr0173': {
        'extent': 'regional', 'label': 'Nossa Senhora Mae de Deus', 'type': 'e',
        'codes': [61, 0, 0], 'calculate': 'friday after Corpus Crist'
    },
    'ptr0174': {
        'extent': 'regional', 'label': 'Senhor Santo Cristo dos Milagres',
        'type': 'm', 'codes': [8, 2, 0], 'calculate': 'monday after second sunday of august'
    }
}


LS_CODES: list[str] = list(CODES.keys())

NATIONAL_CODES: list[str] = list(filter(lambda x: x[2]=='n', LS_CODES))

REGIONAL_CODES: list[str] = list(filter(lambda x: x[2]=='r', LS_CODES))


def select(*, codes: Union[str, list[str]]) -> list[dict[str, Union[str, list[int]]]]:
    """ Select the holiday information for the input codes

    Parameters
    ----------
    codes : list with with the selected codes

    Returns
    -------
    list of dictonaries with info on selected holidays
    """

    if codes == 'national':
        codes = NATIONAL_CODES
    elif codes == 'regional':
        codes = REGIONAL_CODES
    elif codes == 'all':
        codes = LS_CODES

    return [CODES[c] for c in codes]