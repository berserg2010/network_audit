

GetHelp = 'Get-Help'
GetWinUserLanguageList = 'Get-WinUserLanguageList'
GetComputerInfo = 'Get-ComputerInfo'

# Motherboard
BaseBoard = (
    "Win32_BaseBoard",
    "Description",
    "Manufacturer",
    "Product",
    "SerialNumber",
    "Status",
    "Tag",
    "Version",
)

# Disk
DiskDrive = (
    "Win32_DiskDrive",
    "BytesPerSector",
    "ConfigManagerErrorCode",
    "Description",
    "DeviceID",
    "FirmwareRevision",
    "Index",
    "InterfaceType",
    "Manufacturer",
    "Model",
    "Partitions",
    "SerialNumber",
    "Signature",
    "Size",
    "Status",
    "SystemName",
    "TotalCylinders",
    "TotalHeads",
    "TotalSectors",
    "TotalTracks",
    "TracksPerCylinders",
)

Processor = (
    "Win32_Processor",
    "AddressWidth",
    "Description",
    "DeviceID",
    "Family",
    "Manufacturer",
    "MaxClockSpeed",
    "Name",
    "NumberOfCores",
    "NumberOfLogicalProcessors",
    "ProcessorId",
    "Revision",
    "SocketDesignation",
    "Status",
    "SystemName",
    "VirtualizationFirmwareEnabled",
)

PhysicalMemory = (
    "Win32_PhysicalMemory",
    "BankLabel",
    "Capacity",
    "DataWidth",
    "Description",
    "FormFactor",
    "Manufacturer",
    "MemoryType",
    "PartNumber",
    "PositionInRow",
    "SerialNumber",
    "Speed",
    "Status",
    "TotalWidth",
    "TypeDetail",
)

VideoController = (
    "Win32_VideoController",
    "AdapterRAM",
    "Availability",
    "ConfigManagerErrorCode",
    "CurrentBitsPerPixel",
    "CurrentHorizontalResolution",
    "CurrentNumberOfColors",
    "CurrentRefreshRate",
    "CurrentVerticalResolution",
    "Description",
    "DeviceID",
    "DriverVersion",
    "InfFilename",
    "InstalledDisplayDrivers",
    "MaxRefreshRate",
    "MinRefreshRate",
    "PNPDeviceID",
    "Status",
    "SystemName",
    "VideoArchitecture",
    "VideoMemoryType",
    "VideoProcessor",
)


NetworkAdapter = (
    "Win32_NetworkAdapter",
    "AdapterType",
    "Availability",
    "Description",
    "DeviceID",
    "InterfaceIndex",
    "MACAddress",
    "Manufacturer",
    "Name",
    "PhysicalAdapter",
    "PNPDeviceID",
    "ServiceName",
    "Speed",
    "SystemName",
)

OperatingSystem = (
    "Win32_OperatingSystem",
    "BootDevice",
    "BuildNumber",
    "Caption",
    "CodeSet",
    "CountryCode",
    "CSName",
    "CurrentTimeZone",
    "EncryptionLevel",
    "InstallDate",
    "LastBootUpTime",
    "LocalDateTime",
    "Locale",
    "Manufacturer",
    "NumberOfUsers",
    "OSArchitecture",
    "OSLanguage",
    "OSProductSuite",
    "RegisteredUser",
    "SerialNumber",
    "ServicePackMajorVersion",
    "ServicePackMinorVersion",
    "Status",
    "Version",
)


test = (
    "Win32_NetworkAdapterConfiguration",
)