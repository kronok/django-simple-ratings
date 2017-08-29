__version__ = '0.3.4'

from django.conf import settings

# backward compat
VERSION = tuple([int(version) for version in __version__.split('.')])

RATINGS_BAYESIAN_PRETEND_VOTES = getattr(settings, 'RATINGS_BAYESIAN_PRETEND_VOTES', [2, 2, 2, 2, 2])

RATINGS_BAYESIAN_UTILITIES = getattr(settings, 'RATINGS_BAYESIAN_UTILITIES', [1, 2, 3, 4, 5])
