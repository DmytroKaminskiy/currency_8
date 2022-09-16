from rest_framework.throttling import AnonRateThrottle


class AnonRateModelThrottle(AnonRateThrottle):
    scope = 'rate'


class AnonSourceThrottle(AnonRateThrottle):
    scope = 'source'
