import pytest
from mixer.backend.django import mixer

from ..models import *
from ..tasks import (
    task_entering_data_into_the_wmi_model,
    get_property_in_wmi_instance
)

pytestmark = pytest.mark.django_db


data = {
    'ip_address': '192.168.1.52',
    'wmi_class': 'Processor',
    'std_out': [
        {
            'AddressWidth': 64,
            'Description': 'AMD64 Family 21 Model 2 Stepping 0',
            'DeviceID': 'CPU0',
            'DoesNotExist': None,
            'Family': 63,
            'Manufacturer': 'AuthenticAMD',
            'MaxClockSpeed': 3800,
            'Meta': None,
            'MultipleObjectsReturned': None,
            'Name': 'AMD FX(tm)-4300 Quad-Core Processor            ',
            'NumberOfCores': 2,
            'NumberOfLogicalProcessors': 4,
            'ProcessorId': '178BFBFF00600F20',
            'Revision': 512,
            'SocketDesignation': 'CPUSocket',
            'Status': 'OK',
            'SystemName': 'DESKTOP-6CLKV57',
            'VirtualizationFirmwareEnabled': True
        },
        {
            'AddressWidth': 64,
            'Description': 'AMD64 Family 21 Model 2 Stepping 0',
            'DeviceID': 'CPU0',
            'DoesNotExist': None,
            'Family': 63,
            'Manufacturer': 'AuthenticAMD',
            'MaxClockSpeed': 3800,
            'Meta': None,
            'MultipleObjectsReturned': None,
            'Name': 'AMD FX(tm)-4300 Quad-Core Processor            ',
            'NumberOfCores': 2,
            'NumberOfLogicalProcessors': 4,
            'ProcessorId': '178BFBFF00600F20',
            'Revision': 512,
            'SocketDesignation': 'CPUSocket',
            'Status': 'OK',
            'SystemName': 'DESKTOP-6CLKV57',
            'VirtualizationFirmwareEnabled': True
        }
    ]
}

@pytest.mark.parametrize("data", [data])
def test_entering_data_into_the_wmi_model(data):

    Workstation(ip_address=data.get("ip_address")).save()

    task_entering_data_into_the_wmi_model(data)
    assert Processor.objects.count() == 2


@pytest.mark.parametrize("properties", [data.get("std_out")[0]])
def test_get_property_in_wmi_instance(properties):

    instance = Processor(workstation=mixer.blend(Workstation))

    instance_ = get_property_in_wmi_instance(instance, properties)

    instance_.save()

    assert Processor.objects.count() == 1
