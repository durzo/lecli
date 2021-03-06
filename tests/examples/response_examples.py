links = {
    'links': [
        {
            'rel': 'Self',
            'href': 'http://mydummylink.com/query/sample-continuity-suffix'
        }
    ],
    'id': 'sample-continuity-id',
}

group_response = {
    'statistics': {
        'from': 123123,
        'to': 1231323,
        'granularity': 0,
        'count': 1234,
        'timeseries': {},
        'groups': [{
            '200': {
                'count': 802.0,
                'min': 802.0,
                'max': 802.0,
                'sum': 802.0,
                'bytes': 802.0,
                'percentile': 802.0,
                'unique': 802.0,
                'average': 802.0
            }
        }, {
            '400': {
                'count': 839.0,
                'min': 839.0,
                'max': 839.0,
                'sum': 839.0,
                'bytes': 839.0,
                'percentile': 839.0,
                'unique': 839.0,
                'average': 839.0
            }
        }, {
            '404': {
                'count': 839.0,
                'min': 839.0,
                'max': 839.0,
                'sum': 839.0,
                'bytes': 839.0,
                'percentile': 839.0,
                'unique': 839.0,
                'average': 839.0
            }
        }, {
            'status': {
                'count': 205.0,
                'min': 205.0,
                'max': 205.0,
                'sum': 205.0,
                'bytes': 205.0,
                'percentile': 205.0,
                'unique': 205.0,
                'average': 205.0
            }
        }],
        'stats': {}
    }
}

ts_response = {
    'statistics': {
        'from': 123123,
        'to': 123123,
        'count': 1234,
        'stats': {
            'global_timeseries':
                {'count': 27733.0}
        },
        'granularity': 120000,
        'timeseries': {
            'global_timeseries': [
                {'count': 2931.0},
                {'count': 2869.0},
                {'count': 2852.0},
                {'count': 2946.0},
                {'count': 2733.0},
                {'count': 2564.0},
                {'count': 2801.0},
                {'count': 2773.0},
                {'count': 2698.0},
                {'count': 2566.0}
            ]
        }
    }
}

events_response = {
    'events': [
        {'timestamp': 1432080000011, 'message': 'Message contents1'},
        {'timestamp': 1432080000021, 'message': 'Message contents2'},
        {'timestamp': 1432080000033, 'message': 'Message contents3'}
    ]
}

team_response = {
    'id': '123456789012345678901234567890123456',
    'name': 'my_team',
    'users': [
        {
            'id': '123456789012345678901234567890123456',
            'links': {
                'href': 'https://dummy.link',
                'ref': 'Self'
            }
        }
    ]
}
