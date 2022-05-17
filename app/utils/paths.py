import os
from pathlib import Path

from dotenv import load_dotenv


def get_project_root():
    return Path(__file__).parent.parent.parent


def get_env_path():
    return os.path.join(get_project_root(), '.env')


def load_env():
    load_dotenv(get_env_path())


load_env()


def get_token():
    return os.environ.get("TOKEN")


def get_config_path():
    return f"{get_project_root()}/config.toml"
