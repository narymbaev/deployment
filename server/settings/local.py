settings = {
    'psql': {    # DEMO
            'host': '127.0.0.1',
            'port': 5432,
            'user': 'root',
            'password': 'root',
            'database': 'deployment'
        },

    'mq': 'amqp://guest:guest@127.0.0.1/',
    'redis': 'redis://127.0.0.1',

    'mongo': {
	'msg': 'mongodb://chatbot:x42abn6@localhost:27017/chatbot',
        'kpi': 'mongodb://localhost:27017/kpi',
        'qmgr': 'mongodb://localhost:27017/qmgr',
        'extras': 'mongodb://localhost:27017/extras',
        'regions': 'mongodb://localhost:27017/regions',
        'bmg': 'mongodb://localhost:27017/bmg'
    },

    'timber': {
        'enabled': True,
        'level': 'DEBUG'
    },

    'document_path': '/home/nurm/q19/files',
    'project_settings': {
        'task_rating': {
            'PERFECT': {'rate': 5, 'title': {'ru': '⭐⭐⭐⭐⭐', 'en': '⭐⭐⭐⭐⭐', 'kk': '⭐⭐⭐⭐⭐'}},
            'SOGOOD': {'rate': 4, 'title': {'ru': '⭐⭐⭐⭐', 'en': '⭐⭐⭐⭐', 'kk': '⭐⭐⭐⭐'}},
            'GOOD': {'rate': 3, 'title': {'ru': '⭐⭐⭐', 'en': '⭐⭐⭐', 'kk': '⭐⭐⭐', }},
            'NORMAL': {'rate': 2, 'title': {'ru': '⭐⭐', 'en': '⭐⭐', 'kk': '⭐⭐'}},
            'BAD': {'rate': 1, 'title': {'ru': '⭐', 'en': '⭐', 'kk': '⭐'}}
        },
	'task_rating_ordering': ['PERFECT', 'SOGOOD', 'GOOD', 'NORMAL', 'BAD'],
        'weight': 1
    },
    'storage': 'nurm'
}