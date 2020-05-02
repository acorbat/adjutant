from abilities import Waker
from pathlib import Path

def test_waker_can_be_created():
    w = Waker(Path('here/it/is'))
    assert w is not None