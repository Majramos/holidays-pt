#!/usr/bin/env python
# coding: utf-8


"""


"""


CODES = {
    'ptn0001': {
        'country': 'PT', 'extent': 'national', 'label': 'Ano Novo',
                'type': 'f', 'codes': [1, 1, 0], 'calculate': 'january 1st'
    },
    'ptn0002': {
        'country': 'PT', 'extent': 'national', 'label': 'Carnaval',
                'type': 'e', 'codes': [-47, 0, 0], 'calculate': '47 days before easter sunday on a tuesday'
    },
    'ptn0003': {
        'country': 'PT', 'extent': 'national', 'label': 'Sexta-Feira Santa',
                'type': 'e', 'codes': [-2, 0, 0], 'calculate': 'friday right before easter sunday'
    },
    'ptn0004': {
        'country': 'PT', 'extent': 'national', 'label': 'Pascoa',
                'type': 'e', 'codes': [0, 0, 0], 'calculate': 'easter sunday'
    },
    'ptn0005': {
        'country': 'PT', 'extent': 'national', 'label': '25 de Abril',
                'type': 'f', 'codes': [4, 25, 0], 'calculate': 'april 25th'
    },
    'ptn0006': {
        'country': 'PT', 'extent': 'national', 'label': 'Dia do Trabalhador',
        'type': 'f', 'codes': [5, 1, 0], 'calculate': 'may 1th'
    },
    'ptn0007': {
        'country': 'PT', 'extent': 'national', 'label': 'Dia de Portugal',
        'type': 'f', 'codes': [6, 10, 0], 'calculate': 'june 10th'
    },
    'ptn0008': {
        'country': 'PT', 'extent': 'national', 'label': 'Corpo de Deus',
        'type': 'e', 'codes': [60, 0, 0], 'calculate': '60 days after easter sunday, on a thursday'
    },
    'ptn0009': {
        'country': 'PT', 'extent': 'national', 'label': 'Assuncao Maria',
        'type': 'f', 'codes': [8, 15, 0], 'calculate': 'august 15th'
    },
    'ptn0010': {
        'country': 'PT', 'extent': 'national', 'label': 'Implatacao da Republica',
        'type': 'f', 'codes': [10, 5, 0], 'calculate': 'october 5th'
    },
    'ptn0011': {
        'country': 'PT', 'extent': 'national', 'label': 'Todos os Santos', 
        'type': 'f', 'codes': [11, 1, 0], 'calculate': 'november 1st'
    },
    'ptn0012': {
        'country': 'PT', 'extent': 'national', 'label': 'Restauracao da Independencia',
        'type': 'f', 'codes': [12, 1, 0], 'calculate': 'december 1st'
    },
    'ptn0013': {
        'country': 'PT', 'extent': 'national', 'label': 'Imaculada Conceicao',
        'type': 'f', 'codes': [12, 8, 0], 'calculate': 'december 8th'
    },
    'ptn0014': {
        'country': 'PT', 'extent': 'national', 'label': 'Natal',
        'type': 'f', 'codes': [12, 25, 0], 'calculate': 'december 25th'
    },
    'ptr0001': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Geraldo', 
        'type': 'e', 'codes': [50, 0, 0], 'calculate': 'monday after pentacost sunday'
    },
    'ptr0002': {
        'country': 'PT', 'extent': 'regional', 'label': 'Segunda-feira da Senhora do Socorro', 
        'type': 'm', 'codes': [8, 3, 0], 'calculate': 'monday after third sunday of august'
    },
    'ptr0003': {
        'country': 'PT', 'extent': 'regional', 'label': 'Quinta-feira da Ascensao/Dia da Espiga', 
        'type': 'e', 'codes': [39, 0, 0], 'calculate': 'sixth thursday after easter sunday'
    },
    'ptr0004': {
        'country': 'PT', 'extent': 'regional', 'label': 'Rainha Santa Mafalda',
        'type': 'f', 'codes': [5, 2, 0], 'calculate': 'may 2nd'
    },
    'ptr0005': {
        'country': 'PT', 'extent': 'regional', 'label': 'Santa Joana Princesa',
        'type': 'f', 'codes': [5, 12, 0], 'calculate': 'may 12th'
    },
    'ptr0006': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Joao',
        'type': 'f', 'codes': [6, 24, 0], 'calculate': 'june 24th'
    },
    'ptr0007': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao a cidade de Espinho',
        'type': 'f', 'codes': [6, 16, 0], 'calculate': 'june 16th'
    },
    'ptr0008': {
        'country': 'PT', 'extent': 'regional', 'label': 'Santo Antonio',
        'type': 'f', 'codes': [6, 13, 0], 'calculate': 'june 13th'
    },
    'ptr0009': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Sebastiao',
        'type': 'f', 'codes': [1, 20, 0], 'calculate': 'january 20th'
    },
    'ptr0010': {
        'country': 'PT', 'extent': 'regional', 'label': 'Segunda-feira de Pascoa',
        'type': 'e', 'codes': [1, 0, 0], 'calculate': 'monday after easter'
    },
    'ptr0011': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora da Natividade',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0012': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora de La Salette',
        'type': 'm', 'codes': [8, 2, 0], 'calculate': 'monday after first sunday of august'
    },
    'ptr0013': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Cristovao',
        'type': 'f', 'codes': [7, 25, 0], 'calculate': 'july 25th'
    },
    'ptr0014': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao a cidade e fundacao do municipio',
        'type': 'f', 'codes': [10, 11, 0], 'calculate': 'october 11th'
    },
    'ptr0015': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Mateus',
        'type': 'f', 'codes': [9, 21, 0], 'calculate': 'september 21th'
    },
    'ptr0016': {
        'country': 'PT', 'extent': 'regional', 'label': 'Divino Espirito Santo',
        'type': 'e', 'codes': [50, 0, 0], 'calculate': '50 days after easter sunday'
    },
    'ptr0017': {
        'country': 'PT', 'extent': 'regional', 'label': 'Festa de Nossa Senhora da Conceicao',
        'type': 'f', 'codes': [8, 28, 0], 'calculate': 'august 28th'
    },
    'ptr0018': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Pedro',
        'type': 'f', 'codes': [6, 29, 0], 'calculate': 'june 29th'
    },
    'ptr0019': {
        'country': 'PT', 'extent': 'regional', 'label': 'Outorgacao do foral manuelino',
        'type': 'f', 'codes': [3, 5, 0], 'calculate': 'march 5th'
    },
    'ptr0020': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora da Piedade',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0021': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora da Cola',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0022': {
        'country': 'PT', 'extent': 'regional', 'label': 'Santa Cruz',
        'type': 'f', 'codes': [5, 3, 0], 'calculate': 'may 5th'
    },
    'ptr0023': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Miguel Arcanjo',
        'type': 'f', 'codes': [9, 29, 0], 'calculate': 'september 29th'
    },
    'ptr0024': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Tiago',
        'type': 'f', 'codes': [7, 25, 0], 'calculate': 'july 25th'
    },
    'ptr0025': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao Esposende a categoria de vila',
        'type': 'f', 'codes': [8, 19, 0], 'calculate': 'august 19th'
    },
    'ptr0026': {
        'country': 'PT', 'extent': 'regional', 'label': 'Feiras Francas',
        'type': 'f', 'codes': [5, 16, 0], 'calculate': 'may 16th'
    },
    'ptr0027': {
        'country': 'PT', 'extent': 'regional', 'label': 'Batalha de Sao Mamede (1128)',
        'type': 'f', 'codes': [6, 24, 0], 'calculate': 'june 24th'
    },
    'ptr0028': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Jose',
        'type': 'f', 'codes': [3, 19, 0], 'calculate': 'march 19th'
    },
    'ptr0029': {
        'country': 'PT', 'extent': 'regional', 'label': 'Foral de D. Manuel I (1514)',
        'type': 'f', 'codes': [10, 20, 0], 'calculate': 'october 20th'
    },
    'ptr0030': {
        'country': 'PT', 'extent': 'regional', 'label': 'Encerramento da tradicional Feira da Ladra',
        'type': 'm', 'codes': [10, 1, 0], 'calculate': 'monday after first saturday of october'
    },
    'ptr0031': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora das Gracas',
        'type': 'f', 'codes': [8, 22, 0], 'calculate': 'august 22th'
    },
    'ptr0032': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao de Miranda do Douro a cidade',
        'type': 'f', 'codes': [7, 10, 0], 'calculate': 'july 10th'
    },
    'ptr0033': {
        'country': 'PT', 'extent': 'regional', 'label': 'Recebimento do Foral de D. Afonso III (1250)',
        'type': 'f', 'codes': [5, 25, 0], 'calculate': 'may 25th'
    },
    'ptr0034': {
        'country': 'PT', 'extent': 'regional', 'label': 'Feira dos Gorazes',
        'type': 'f', 'codes': [10, 15, 0], 'calculate': 'october 15th'
    },
    'ptr0035': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Bartolomeu',
        'type': 'f', 'codes': [8, 24, 0], 'calculate': 'august 24th'
    },
    'ptr0036': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Lourenco',
        'type': 'f', 'codes': [8, 10, 0], 'calculate': 'august 10th'
    },
    'ptr0037': {
        'country': 'PT', 'extent': 'regional', 'label': 'Outorgacao do foral manuelino',
        'type': 'f', 'codes': [5, 20, 0], 'calculate': 'may 20th'
    },
    'ptr0038': {
        'country': 'PT', 'extent': 'regional', 'label': 'Primeira missa no Brasil',
        'type': 'f', 'codes': [4, 26, 0], 'calculate': 'april 26th'
    },
    'ptr0039': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora de Mercoles',
        'type': 'e', 'codes': [9, 0, 0], 'calculate': 'tuesday from second week after sunday easter'
    },
    'ptr0040': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao Covilha a cidade',
        'type': 'f', 'codes': [10, 20, 0], 'calculate': 'october 20th'
    },
    'ptr0041': {
        'country': 'PT', 'extent': 'regional', 'label': 'Santa Luzia',
        'type': 'f', 'codes': [9, 15, 0], 'calculate': 'september 15th'
    },
    'ptr0042': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora do Almortao',
        'type': 'e', 'codes': [15, 0, 0], 'calculate': 'third monday after easter'
    },
    'ptr0043': {
        'country': 'PT', 'extent': 'regional', 'label': 'Santa Margarida',
        'type': 'e', 'codes': [8, 2, 0], 'calculate': 'monday after second sunday of august'
    },
    'ptr0044': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Nuno de Santa Maria (1360)',
        'type': 'f', 'codes': [6, 24, 0], 'calculate': 'june 24th'
    },
    'ptr0045': {
        'country': 'PT', 'extent': 'regional', 'label': 'Recebimento do foral de D. Dinis',
        'type': 'f', 'codes': [9, 19, 0], 'calculate': 'september 19th'
    },
    'ptr0046': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora da Alagada', 
        'type': 'm', 'codes': [8, 4, 0], 'calculate': 'monday after forth sunday of august'
    },
    'ptr0047': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora do Mont Alto',
        'type': 'f', 'codes': [9, 7, 0], 'calculate': 'september 7th'
    },
    'ptr0048': {
        'country': 'PT', 'extent': 'regional', 'label': 'Rainha Santa Isabel',
        'type': 'f', 'codes': [7, 4, 0], 'calculate': 'july 4th'
    },
    'ptr0049': {
        'country': 'PT', 'extent': 'regional', 'label': 'Santa Cristina',
        'type': 'f', 'codes': [7, 24, 0], 'calculate': 'july 24th'
    },
    'ptr0050': {
        'country': 'PT', 'extent': 'regional', 'label': 'Doacao de Gois a Anaia Vestrares',
        'type': 'f', 'codes': [8, 13, 0], 'calculate': 'august 13th'
    },
    'ptr0051': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Tome',
        'type': 'f', 'codes': [7, 25, 0], 'calculate': 'july 25th'
    },
    'ptr0052': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nascimento de Jose Falcao (1841)',
        'type': 'f', 'codes': [6, 1, 0], 'calculate': 'june 1st'
    },
    'ptr0053': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora da Vitoria',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0054': {
        'country': 'PT', 'extent': 'regional', 'label': 'Recebimento da noticia da Implantacao da Republica',
        'type': 'f', 'codes': [10, 7, 0], 'calculate': 'october 7th'
    },
    'ptr0055': {
        'country': 'PT', 'extent': 'regional', 'label': 'Restauracao dos titulos de vila isenta',
        'type': 'f', 'codes': [4, 10, 0], 'calculate': 'april 10th'
    },
    'ptr0056': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nascimento de António Jose de Almeida',
        'type': 'f', 'codes': [7, 17, 0], 'calculate': 'july 17th'
    },
    'ptr0057': {
        'country': 'PT', 'extent': 'regional', 'label': 'Restauracao da Comarca',
        'type': 'f', 'codes': [4, 10, 0], 'calculate': 'april 10th'
    },
    'ptr0058': {
        'country': 'PT', 'extent': 'regional', 'label': 'Restauracao do municipio',
        'type': 'f', 'codes': [1, 13, 0], 'calculate': 'january 13th'
    },
    'ptr0059': {
        'country': 'PT', 'extent': 'regional', 'label': 'Segunda-feira de Pascoela/Nossa Senhora da Boa Nova', 
        'type': 'e', 'codes': [8, 0, 0], 'calculate': 'monday after easter'
    },
    'ptr0060': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Joao de Deus',
        'type': 'f', 'codes': [3, 8, 0], 'calculate': 'march 8th'
    },
    'ptr0061': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora das Candeias',
        'type': 'f', 'codes': [2, 2, 0], 'calculate': 'february 2nd'
    },
    'ptr0062': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao de Vendas Novas a municipio',
        'type': 'f', 'codes': [9, 7, 0], 'calculate': 'september 7th'
    },
    'ptr0063': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nascimento de Couto Jardim',
        'type': 'f', 'codes': [8, 16, 0], 'calculate': 'august 16th'
    },
    'ptr0064': {
        'country': 'PT', 'extent': 'regional', 'label': 'Foral de D. Manuel I (1504)',
        'type': 'f', 'codes': [8, 20, 0], 'calculate': 'august 20th'
    },
    'ptr0065': {
        'country': 'PT', 'extent': 'regional', 'label': 'Dia do Municipio',
        'type': 'm', 'codes': [9, 1, 4], 'calculate': 'second monday of september'
    },
    'ptr0066': {
        'country': 'PT', 'extent': 'regional', 'label': 'Banho Santo',
        'type': 'f', 'codes': [8, 29, 0], 'calculate': 'august 29th'
    },
    'ptr0067': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao de Faro a cidade/Santa Maria de Faro',
        'type': 'f', 'codes': [9, 7, 0], 'calculate': 'september 7th'
    },
    'ptr0068': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora da Luz',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0069': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Goncalo de Lagos',
        'type': 'f', 'codes': [10, 27, 0], 'calculate': 'october 27th'
    },
    'ptr0070': {
        'country': 'PT', 'extent': 'regional', 'label': 'Revolta de Olhao contra os Franceses (1808)',
        'type': 'f', 'codes': [6, 16, 0], 'calculate': 'june 16th'
    },
    'ptr0071': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao de Portimao a cidade (1924)',
        'type': 'f', 'codes': [12, 11, 0], 'calculate': 'december 11th'
    },
    'ptr0072': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao de Sao Bras de Alportel a cidade (1914)',
        'type': 'f', 'codes': [6, 1, 0], 'calculate': 'june 1st'
    },
    'ptr0073': {
        'country': 'PT', 'extent': 'regional', 'label': 'Conquista da cidade aos mouros',
        'type': 'f', 'codes': [9, 3, 0], 'calculate': 'september 3rd'
    },
    'ptr0074': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Vicente',
        'type': 'f', 'codes': [1, 22, 0], 'calculate': 'january 22th'
    },
    'ptr0075': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevação de Vila Real de Santo Antonio a cidade',
        'type': 'f', 'codes': [5, 13, 0], 'calculate': 'may 13th'
    },
    'ptr0076': {
        'country': 'PT', 'extent': 'regional', 'label': 'Restauracao do concelho de Aguiar da Beira',
        'type': 'f', 'codes': [2, 10, 0], 'calculate': 'february 10th'
    },
    'ptr0077': {
        'country': 'PT', 'extent': 'regional', 'label': 'Batalha do Coa (1810)',
        'type': 'f', 'codes': [7, 2, 0], 'calculate': 'july 2nd'
    },
    'ptr0078': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nascimento de Sacadura Cabral',
        'type': 'f', 'codes': [5, 23, 0], 'calculate': 'may 23th'
    },
    'ptr0079': {
        'country': 'PT', 'extent': 'regional', 'label': 'Batalha de Salgadela (1664)',
        'type': 'f', 'codes': [7, 7, 0], 'calculate': 'july 7th'
    },
    'ptr0080': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nosso Senhor do Calvario', 
        'type': 'm', 'codes': [8, 2, 0], 'calculate': 'monday after second sunday of august'
    },
    'ptr0081': {
        'country': 'PT', 'extent': 'regional', 'label': 'Foral de D. Sancho I (1199)',
        'type': 'f', 'codes': [11, 27, 0], 'calculate': 'november 27th'
    },
    'ptr0082': {
        'country': 'PT', 'extent': 'regional', 'label': 'Atribuicao do foral',
        'type': 'f', 'codes': [3, 4, 0], 'calculate': 'march 4th'
    },
    'ptr0083': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Martinho',
        'type': 'f', 'codes': [11, 11, 0], 'calculate': 'november 11th'
    },
    'ptr0084': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao de Pinhel a cidade (2007)',
        'type': 'f', 'codes': [8, 25, 0], 'calculate': 'august 25th'
    },
    'ptr0085': {
        'country': 'PT', 'extent': 'regional', 'label': 'Segunda-feira de Pascoela/Nossa Senhora dos Prazeres/Nossa Senhora da Graça)', 
        'type': 'e', 'codes': [8, 0, 0], 'calculate': 'second monday after easter'},
    'ptr0086': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao de Seia a cidade',
        'type': 'f', 'codes': [7, 3, 0], 'calculate': 'may 3rd'
    },
    'ptr0087': {
        'country': 'PT', 'extent': 'regional', 'label': 'Batalha de Sao Marcos (1385)',
        'type': 'f', 'codes': [5, 29, 0], 'calculate': 'may 29th'
    },
    'ptr0088': {
        'country': 'PT', 'extent': 'regional', 'label': 'Outorgacao do foral de D. Dinis',
        'type': 'f', 'codes': [5, 21, 0], 'calculate': 'may 21th'
    },
    'ptr0089': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Bernardo',
        'type': 'f', 'codes': [8, 20, 0], 'calculate': 'august 20th'
    },
    'ptr0090': {
        'country': 'PT', 'extent': 'regional', 'label': 'Batalha de Aljubarrota (1385)',
        'type': 'f', 'codes': [8, 14, 0], 'calculate': 'august 14th'
    },
    'ptr0091': {
        'country': 'PT', 'extent': 'regional', 'label': 'Fundacao da localidade pela rainha D. Leonor',
        'type': 'f', 'codes': [5, 15, 0], 'calculate': 'may 15th'
    },
    'ptr0092': {
        'country': 'PT', 'extent': 'regional', 'label': 'Instalacao do municipio',
        'type': 'f', 'codes': [7, 4, 0], 'calculate': 'july 4th'
    },
    'ptr0093': {
        'country': 'PT', 'extent': 'regional', 'label': 'Passagem a cidade e criacao da diocese',
        'type': 'f', 'codes': [5, 22, 0], 'calculate': 'may 22th'
    },
    'ptr0094': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora das Areias (ou da Nazare)',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0095': {
        'country': 'PT', 'extent': 'regional', 'label': 'Tomada de Obidos aos mouros',
        'type': 'f', 'codes': [1, 11, 0], 'calculate': 'january 11th'
    },
    'ptr0096': {
        'country': 'PT', 'extent': 'regional', 'label': 'Criacao do municipio',
        'type': 'f', 'codes': [7, 24, 0], 'calculate': 'july 24th'
    },
    'ptr0097': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora da Boa Viagem', 
        'type': 'm', 'codes': [8, 1, 0], 'calculate': 'monday after first sunday of august'
    },
    'ptr0098': {
        'country': 'PT', 'extent': 'regional', 'label': 'Criacao do municipio',
        'type': 'f', 'codes': [8, 26, 0], 'calculate': 'august 26th'
    },
    'ptr0099': {
        'country': 'PT', 'extent': 'regional', 'label': 'Criacao do municipio (1759)',
        'type': 'f', 'codes': [6, 7, 0], 'calculate': 'july 7th'
    },
    'ptr0100': {
        'country': 'PT', 'extent': 'regional', 'label': 'Criacao do municipio',
        'type': 'f', 'codes': [9, 11, 0], 'calculate': 'september 11th'
    },
    'ptr0101': {
        'country': 'PT', 'extent': 'regional', 'label': 'Criacao do municipio',
        'type': 'f', 'codes': [11, 19, 0], 'calculate': 'november 19th'
    },
    'ptr0102': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora da Luz',
        'type': 'e', 'codes': [1, 0, 0], 'calculate': 'monday after easter'
    },
    'ptr0103': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Gregorio',
        'type': 'e', 'codes': [1, 0, 0], 'calculate': 'monday after easter'
    },
    'ptr0104': {
        'country': 'PT', 'extent': 'regional', 'label': 'Batalha das Linhas de Elvas (1659)',
        'type': 'f', 'codes': [1, 14, 0], 'calculate': 'january 14th'
    },
    'ptr0105': {
        'country': 'PT', 'extent': 'regional', 'label': 'Batalha dos Atoleiros',
        'type': 'f', 'codes': [4, 6, 0], 'calculate': 'april 6th'
    },
    'ptr0106': {
        'country': 'PT', 'extent': 'regional', 'label': 'Recebimento do foral manuelino',
        'type': 'f', 'codes': [11, 23, 0], 'calculate': 'november 23th'
    },
    'ptr0107': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora da Estrela',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0108': {
        'country': 'PT', 'extent': 'regional', 'label': 'Segunda-feira de Pascoela/Nossa Senhora dos Prazeres', 
        'type': 'e', 'codes': [8, 0, 0], 'calculate': 'second monday after easter'
    },
    'ptr0109': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora da Graca',
        'type': 'e', 'codes': [1, 0, 0], 'calculate': 'monday after easter'
    },
    'ptr0110': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao Portalegre a cidade e criacao da diocese',
        'type': 'f', 'codes': [5, 23, 0], 'calculate': 'may 23th'
    },
    'ptr0111': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora do Carmo da Serra (de Sao Miguel)', 
        'type': 'e', 'codes': [1, 0, 0], 'calculate': 'monday after easter'
    },
    'ptr0112': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao Amarante a cidade',
        'type': 'f', 'codes': [7, 8, 0], 'calculate': ''
    },
    'ptr0113': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora do Rosario',
        'type': 'm', 'codes': [10, 1, 0], 'calculate': 'monday after first sunday of october'
    },
    'ptr0114': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nosso Senhor dos Aflitos',
        'type': 's', 'codes': [7, 0, 0], 'calculate': 'monday after last sunday of july'
    },
    'ptr0115': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora do Bom Despacho',
        'type': 'm', 'codes': [7, 2, 0], 'calculate': 'monday after second sunday of july'
    },
    'ptr0116': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora do Castelinho',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0117': {
        'country': 'PT', 'extent': 'regional', 'label': 'Terca-feira de Pentecostes',
        'type': 'e', 'codes': [51, 0, 0], 'calculate': 'tuesday after sunday of pentacoste'
    },
    'ptr0118': {
        'country': 'PT', 'extent': 'regional', 'label': 'Criacao do municipio',
        'type': 'f', 'codes': [11, 6, 0], 'calculate': 'november 6th'
    },
    'ptr0119': {
        'country': 'PT', 'extent': 'regional', 'label': 'Divino Salvador',
        'type': 'm', 'codes': [7, 3, 0], 'calculate': 'monday after third sunday of july'
    },
    'ptr0120': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Bento',
        'type': 'f', 'codes': [7, 11, 0], 'calculate': 'july 11th'
    },
    'ptr0121': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao Abrantes a cidade (1916)',
        'type': 'f', 'codes': [6, 14, 0], 'calculate': 'june 14th'
    },
    'ptr0122': {
        'country': 'PT', 'extent': 'regional', 'label': 'Criacao do municipio',
        'type': 'f', 'codes': [4, 2, 0], 'calculate': 'april 2nd'
    },
    'ptr0123': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora da Boa Viagem',
        'type': 'e', 'codes': [1, 0, 0], 'calculate': 'monday after easter'
    },
    'ptr0124': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora do Castelo',
        'type': 'f', 'codes': [8, 17, 0], 'calculate': 'august 17th'
    },
    'ptr0125': {
        'country': 'PT', 'extent': 'regional', 'label': 'Criacao do municipio Entroncamento (1945)',
        'type': 'f', 'codes': [11, 24, 0], 'calculate': 'november 24th'
    },
    'ptr0126': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora de Fatima',
        'type': 'f', 'codes': [5, 13, 0], 'calculate': 'may 13th'
    },
    'ptr0127': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao Sardoal a categoria de vila',
        'type': 'f', 'codes': [9, 22, 0], 'calculate': 'september 22th'
    },
    'ptr0128': {
        'country': 'PT', 'extent': 'regional', 'label': 'Fundacao do Castelo Templario',
        'type': 'f', 'codes': [3, 1, 0], 'calculate': 'march 1st'
    },
    'ptr0129': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao a cidade Ourem/Praia da Vitoria',
        'type': 'f', 'codes': [6, 28, 0], 'calculate': 'june 28th'
    },
    'ptr0130': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao Barreiro a cidade',
        'type': 'f', 'codes': [6, 28, 0], 'calculate': 'june 28th'
    },
    'ptr0131': {
        'country': 'PT', 'extent': 'regional', 'label': 'Criacao do municipio de Grandola atraves do foral',
        'type': 'f', 'codes': [10, 22, 0], 'calculate': 'october 22th'
    },
    'ptr0132': {
        'country': 'PT', 'extent': 'regional', 'label': 'Festas em Honra de Nossa Senhora da Boa Viagem',
        'type': 'm', 'codes': [9, 2, 1], 'calculate': 'tuesday after second sunday of september'
    },
    'ptr0133': {
        'country': 'PT', 'extent': 'regional', 'label': 'Atribuicao do foral manuelino (1512) Palmela',
        'type': 'f', 'codes': [6, 1, 0], 'calculate': 'june 1st'
    },
    'ptr0134': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nosso Senhor Jesus das Chagas',
        'type': 'f', 'codes': [5, 4, 0], 'calculate': 'may 4th'
    },
    'ptr0135': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nascimento de Bocage',
        'type': 'f', 'codes': [9, 15, 0], 'calculate': 'september 15th'
    },
    'ptr0136': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao Sines a vila (1362)',
        'type': 'f', 'codes': [11, 24, 0], 'calculate': 'november 24th'
    },
    'ptr0137': {
        'country': 'PT', 'extent': 'regional', 'label': 'Atribuicao do foral a Moncao',
        'type': 'f', 'codes': [3, 12, 0], 'calculate': 'march 12th'
    },
    'ptr0138': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora das Dores',
        'type': 'f', 'codes': [9, 20, 0], 'calculate': 'september 20th'
    },
    'ptr0139': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Teotonio',
        'type': 'f', 'codes': [2, 18, 0], 'calculate': 'february 18th'
    },
    'ptr0140': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora da Agonia',
        'type': 'f', 'codes': [8, 20, 0], 'calculate': 'august 20th'
    },
    'ptr0141': {
        'country': 'PT', 'extent': 'regional', 'label': 'Recebimento do foral manuelino Vila Nova de Cerveira',
        'type': 'f', 'codes': [10, 1, 0], 'calculate': 'october 1st'
    },
    'ptr0142': {
        'country': 'PT', 'extent': 'regional', 'label': '1 Incursao Monarquica (1912) Chaves',
        'type': 'f', 'codes': [7, 8, 0], 'calculate': 'july 8th'
    },
    'ptr0143': {
        'country': 'PT', 'extent': 'regional', 'label': 'Santo Andre',
        'type': 'f', 'codes': [11, 30, 0], 'calculate': 'november 30th'
    },
    'ptr0144': {
        'country': 'PT', 'extent': 'regional', 'label': 'Atribuicao do foral Montalegre',
        'type': 'f', 'codes': [6, 9, 0], 'calculate': 'june 9th'
    },
    'ptr0145': {
        'country': 'PT', 'extent': 'regional', 'label': 'Criacao do municipio Murça',
        'type': 'f', 'codes': [5, 8, 0], 'calculate': 'may 8th'
    },
    'ptr0146': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora do Socorro',
        'type': 'f', 'codes': [8, 16, 0], 'calculate': 'august 16th'
    },
    'ptr0147': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora do Rosario',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0148': {
        'country': 'PT', 'extent': 'regional', 'label': 'Atribuicao do foral manuelino Vila Pouca de Aguiar',
        'type': 'f', 'codes': [6, 22, 0], 'calculate': 'june 22th'
    },
    'ptr0149': {
        'country': 'PT', 'extent': 'regional', 'label': '',
        'type': 'm', 'codes': [7, 3, 0], 'calculate': 'monday after third sunday of july'
    },
    'ptr0150': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora dos Remedios',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0151': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora do Castelo',
        'type': 'f', 'codes': [9, 8, 0], 'calculate': 'september 8th'
    },
    'ptr0152': {
        'country': 'PT', 'extent': 'regional', 'label': 'Restauracao do municipio Oliveira de Frades',
        'type': 'f', 'codes': [10, 7, 0], 'calculate': 'october 7th'
    },
    'ptr0153': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Genesio',
        'type': 'f', 'codes': [8, 25, 0], 'calculate': 'august 25th'
    },
    'ptr0154': {
        'country': 'PT', 'extent': 'regional', 'label': 'Festa de Nossa Senhora ao Pe da Cruz',
        'type': 'f', 'codes': [5, 3, 0], 'calculate': 'may 3rd'
    },
    'ptr0155': {
        'country': 'PT', 'extent': 'regional', 'label': 'Santa Eufemia',
        'type': 'f', 'codes': [9, 16, 0], 'calculate': 'september 16th'
    },
    'ptr0156': {
        'country': 'PT', 'extent': 'regional', 'label': 'Estabelecimento e denominacao da sede de concelho',
         'type': 'f', 'codes': [3, 2, 0], 'calculate': 'march 2nd'
    },
    'ptr0157': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Frei Gil',
        'type': 'f', 'codes': [5, 14, 0], 'calculate': 'may 14th'
    },
    'ptr0158': {
        'country': 'PT', 'extent': 'regional', 'label': 'Santo Amaro',
        'type': 'f', 'codes': [1, 15, 0], 'calculate': 'january 15th'
    },
    'ptr0159': {
        'country': 'PT', 'extent': 'regional', 'label': 'Santa Maria Madalena',
        'type': 'f', 'codes': [7, 22, 0], 'calculate': 'july 22th'
    },
    'ptr0160': {
        'country': 'PT', 'extent': 'regional', 'label': 'Criacao do municipio Porto Santo (1835)',
        'type': 'f', 'codes': [6, 24, 0], 'calculate': 'june 24th'
    },
    'ptr0161': {
        'country': 'PT', 'extent': 'regional', 'label': 'Criacao do municipio Santana (1835)',
        'type': 'f', 'codes': [5, 25, 0], 'calculate': 'may 25th'
    },
    'ptr0162': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao Funchal a cidade',
        'type': 'f', 'codes': [8, 21, 0], 'calculate': 'august 21th'
    },
    'ptr0163': {
        'country': 'PT', 'extent': 'regional', 'label': 'Criacao do municipio Camara de Lobos',
        'type': 'f', 'codes': [10, 4, 0], 'calculate': 'october 4th'
    },
    'ptr0164': {
        'country': 'PT', 'extent': 'regional', 'label': 'Criacao da Capitania de Machico',
        'type': 'f', 'codes': [10, 9, 0], 'calculate': 'october 9th'
    },
    'ptr0165': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Roque', 
        'type': 'f', 'codes': [8, 16, 0], 'calculate': 'august 16th'
    },
    'ptr0166': {
        'country': 'PT', 'extent': 'regional', 'label': 'Criacao do municipio Lajes do Pico',
        'type': 'f', 'codes': [6, 29, 0], 'calculate': 'june 29th'
    },
    'ptr0167': {
        'country': 'PT', 'extent': 'regional', 'label': 'Elevacao a vila e sede de concelho (1832)',
        'type': 'f', 'codes': [6, 20, 0], 'calculate': 'june 20th'
    },
    'ptr0168': {
        'country': 'PT', 'extent': 'regional', 'label': 'Criacao do municipio de Lagoa',
        'type': 'f', 'codes': [4, 11, 0], 'calculate': 'april 11th'
    },
    'ptr0169': {
        'country': 'PT', 'extent': 'regional', 'label': 'Sao Jorge',
        'type': 'f', 'codes': [4, 23, 0], 'calculate': 'april 23th'
    },
    'ptr0170': {
        'country': 'PT', 'extent': 'regional', 'label': 'Fundacao do municipio de Nordeste (1514)',
        'type': 'f', 'codes': [7, 18, 0], 'calculate': 'july 18th'
    },
    'ptr0171': {
        'country': 'PT', 'extent': 'regional', 'label': 'Santa Catarina',
        'type': 'f', 'codes': [11, 25, 0], 'calculate': 'november 25th'
    },
    'ptr0172': {
        'country': 'PT', 'extent': 'regional', 'label': 'Senhor Santo Cristo dos Milagres', 
        'type': 'e', 'codes': [36, 0, 0], 'calculate': 'fifth monday after easter'
    },
    'ptr0173': {
        'country': 'PT', 'extent': 'regional', 'label': 'Nossa Senhora Mae de Deus', 
        'type': 'e', 'codes': [61, 0, 0], 'calculate': 'friday after Corpus Crist'
    },
    'ptr0174': {
        'country': 'PT', 'extent': 'regional', 'label': 'Senhor Santo Cristo dos Milagres', 
        'type': 'm', 'codes': [8, 2, 0], 'calculate': 'monday after second sunday of august'
    }
}
    