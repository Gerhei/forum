from pathlib import PurePath

from decouple import AutoConfig
from split_settings.tools import include


BASE_DIR = PurePath(__file__).parent.parent

config = AutoConfig(search_path=BASE_DIR.joinpath('config'))

base_settings = [
    'settings.py',
]

include(*base_settings)
