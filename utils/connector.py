import winrm
import functools
import json
from requests.exceptions import ConnectTimeout
from django.core.cache import cache

from network_audit import settings
from utils.utils import (
    get_wim_object_with_properties,
    compare_command,
    ConvertToJson,
)


class Connector:
    def __init__(self, client, auth):
        self.client = client
        self.auth = auth

    def run(self, command: str):
        session = winrm.Session(
            self.client,
            auth=self.auth
        )

        return session.run_ps(command)


def connector(func):
    @functools.wraps(func)
    def wrapped(ip_address: str, wmi_class: str, *args, **kwargs):

        kwargs["ip_address"] = ip_address
        kwargs["wmi_class"] = wmi_class

        try:
            session = Connector(
                ip_address,
                auth=(cache.get("WINRM_USERNAME"), cache.get("WINRM_PASSWORD"))
            )

            result = session.run(
                compare_command(
                    get_wim_object_with_properties(wmi_class),
                    ConvertToJson
                )
            )

            assert result.status_code == 0

            kwargs["std_out"] = json.loads(result.std_out)

        except ConnectTimeout as e:
            kwargs["error"] = f'{e}'
        except AssertionError as e:
            kwargs["error"] = f'{e}'
        except json.JSONDecodeError as e:
            kwargs["error"] = f'{e}'

        return func(**kwargs)
    return wrapped
