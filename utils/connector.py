import winrm
import functools
import json
from requests.exceptions import ConnectTimeout

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
    def wrapped(ip_address, wmi_class, *args, **kwargs):
        try:
            session = Connector(
                ip_address,
                auth=(settings.WINRM_USERNAME, settings.WINRM_PASSWORD)
            )

            result = session.run(
                compare_command(
                    get_wim_object_with_properties(wmi_class),
                    ConvertToJson
                )
            )

            assert result.status_code == 0

            data = json.loads(result.std_out)
            kwargs['data'] = data if isinstance(data, list) else [data]

        except ConnectTimeout as e:
            kwargs['error'] = f'{e}'
        except AssertionError as e:
            kwargs['error'] = f'{e}'
        except json.JSONDecodeError as e:
            kwargs['error'] = f'{e}'

        return func(*args, **kwargs)
    return wrapped
