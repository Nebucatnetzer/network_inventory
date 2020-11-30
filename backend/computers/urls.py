from django.urls import path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'computers', views.ComputerViewSet)
router.register(r'computer-cpu-relations',
                views.ComputerCpuRelationViewSet,
                'computer-cpu-relation')
router.register(r'computer-disk-relations',
                views.ComputerDiskRelationViewSet,
                'computer-disk-relation')
router.register(r'computer-gpu-relations',
                views.ComputerGpuRelationViewSet,
                'computer-gpu-relation')
router.register(r'computer-ram-relations',
                views.ComputerRamRelationViewSet,
                'computer-ram-relation')
router.register(r'computer-software-relations',
                views.ComputerSoftwareRelationViewSet,
                'computer-software-relation')
router.register(r'cpu-architectures',
                views.CpuArchitectureViewSet,
                'cpu-architecture')
router.register(r'cpu-manufacturers',
                views.CpuManufacturerViewSet,
                'cpu-manufacturer')
router.register(r'cpus', views.CpuViewSet)
router.register(r'disk-types',
                views.DiskTypeViewSet,
                'disk-type')
router.register(r'disks', views.DiskViewSet)
router.register(r'gpu-manufacturers',
                views.GpuManufacturerViewSet,
                'gpu-manufacturer')
router.register(r'gpus', views.GpuViewSet)
router.register(r'disks-in-raid',
                views.DisksInRaidViewSet,
                'disks-in-raid')
router.register(r'raid-types',
                views.RaidTypeViewSet,
                'raid-type')
router.register(r'raids', views.RaidViewSet)
router.register(r'ram-types',
                views.RamTypeViewSet,
                'ram-type')
router.register(r'rams', views.RamViewSet)


urlpatterns = [
    # required for the login functionality
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]
