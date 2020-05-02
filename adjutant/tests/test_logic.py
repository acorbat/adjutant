from adjutant import Adjutant
from pathlib import Path
from unittest import mock


def test_adjutant_can_be_created():
    with mock.patch('adjutant.logic.load'):
        a = Adjutant(Path('here/i/am'))
        assert a is not None
