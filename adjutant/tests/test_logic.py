from adjutant import Adjutant
from pathlib import Path
from unittest import mock


def test_adjutant_can_be_created():
    a = Adjutant(Path('here/i/am'), mock.Mock())
    assert a is not None
