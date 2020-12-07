from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'computers', views.ComputerViewSet)
router.register(r'computer-cpu-relations', views.ComputerCpuRelationViewSet)
router.register(r'computer-disk-relations', views.ComputerDiskRelationViewSet)
router.register(r'computer-gpu-relations', views.ComputerGpuRelationViewSet)
router.register(r'computer-ram-relations', views.ComputerRamRelationViewSet)
router.register(r'computer-software-relations',
                views.ComputerSoftwareRelationViewSet)
router.register(r'cpu-architectures', views.CpuArchitectureViewSet)
router.register(r'cpu-manufacturers', views.CpuManufacturerViewSet)
router.register(r'cpus', views.CpuViewSet)
router.register(r'disk-types', views.DiskTypeViewSet)
router.register(r'disks', views.DiskViewSet)
router.register(r'gpu-manufacturers', views.GpuManufacturerViewSet)
router.register(r'gpus', views.GpuViewSet)
router.register(r'disks-in-raid', views.DisksInRaidViewSet)
router.register(r'raid-types', views.RaidTypeViewSet)
router.register(r'raids', views.RaidViewSet)
router.register(r'ram-types', views.RamTypeViewSet)
router.register(r'rams', views.RamViewSet)
