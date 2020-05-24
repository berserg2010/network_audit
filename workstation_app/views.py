# from django.shortcuts import render
#
# from utils.connector import connector
# from utils.utils import render_item
# from .models import (
#     BaseBoard,
#     Processor,
#     PhysicalMemory,
#     DiskDrive,
#     VideoController,
#     NetworkAdapter,
#     OperatingSystem,
# )
#
#
# def index(request):
#     return render(request, "workstation_app/index.html")
#
#
# @connector(BaseBoard)
# @render_item
# def baseboard(res):
#     return res
#
#
# @connector(Processor)
# @render_item
# def processor(res):
#     return res
#
#
# @connector(PhysicalMemory)
# @render_item
# def physical_memory(res):
#     return res
#
#
# @connector(DiskDrive)
# @render_item
# def disk_drive(res):
#     return res
#
#
# @connector(VideoController)
# @render_item
# def video_controller(res):
#     return res
#
#
# @connector(NetworkAdapter)
# @render_item
# def network_adapter(res):
#     return res
#
#
# @connector(OperatingSystem)
# @render_item
# def operating_system(res):
#     return res
