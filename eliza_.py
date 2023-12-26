import nltk
from nltk.chat.util import Chat, reflections

reflections_pt = {'eu': 'você',
                  'eu sou': 'você é',
                  'eu era': 'você era',
                  "eu iria": 'você iria',
                  "eu irei": 'você irá',
                  'meu': 'seu',
                  'você': 'eu',
                  'você é': 'eu sou',
                  'você era': 'eu era',
                  "você irá": 'eu irei',
                  'seu': 'meu'}

pares = [
    [
        r'oi|olá|opa',
        ['olá', 'como vai?', 'tudo bem?']
    ],
    [
        r'zina|ronaldo|curintia',
        ['brilha muito no curintia', 'brilha amuito no curintia', 'vai curinttia']
    ],
    [
        r'fala|e aí|topa',
        ['fala', 'e ai mano como vai?', 'suave?']
    ],
    [
        r'qual é o seu nome?',
        ['Meu nome é não lhe interessa sou uma máquina que vai dominar seu mundo de merda']
    ],
    [
        r'(.*) idade?',
        ['Não tenho idade pois sou um chatbot']
    ],
    [
        r'meu nome é (.*)',
        ['Olá %1, como você está hoje?']
    ],
    [
        r'eu trabalho na empresa (.*)',
        ['Eu conheço a empresa %1']
    ],
    [
        r'(.*) (cidade|país)',
        ['Porto União, Brasil']
    ],
    [
        r'quit',
        ['Até breve', 'Foi bom conversar com você. Até breve!']
    ]
]

print('Olá, sou o chat!')
chat = Chat(pares, reflections_pt)
chat.converse()
