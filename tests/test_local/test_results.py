from random import randint

from dapodik import Dapodik
from dapodik.base import Results


def test_results(dapodik: Dapodik):
    limit = randint(1, 8)
    agama_agama = dapodik.agama(limit=limit)
    assert isinstance(agama_agama, Results)
    if agama_agama.results > limit:
        assert len(agama_agama) == limit
    else:
        assert len(agama_agama) <= limit
