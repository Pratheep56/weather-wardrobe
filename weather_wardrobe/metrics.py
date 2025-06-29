try:
    import statsd
    c = statsd.StatsClient(host='graphite', port=8125, prefix='weather_wardrobe')
except Exception as e:
    print(f"⚠️ StatsD client not active: {e}")
    c = None

def record_request(endpoint):
    if c:
        c.incr(f"{endpoint}_hits")


