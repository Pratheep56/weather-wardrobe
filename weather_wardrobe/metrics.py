import statsd

c = statsd.StatsClient(host='graphite', port=8125, prefix='weather_wardrobe')

def record_request(success=True):
    try:
        c.incr('requests.total')
        if success:
            c.incr('requests.success')
        else:
            c.incr('requests.failure')
    except Exception:
        pass

