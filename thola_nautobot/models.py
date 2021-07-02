"""Models for thola nautobot."""
from django.db import models
from django.urls import reverse
from nautobot.core.models.generics import PrimaryModel


class TholaConfig(PrimaryModel):
    """
    A Thola Config represents a configuration for a device that can be monitored by Thola. Each Thola Config is assigned
    a Device (nautobot.dcim.models), snmp and http properties and its available components.
    """

    device = models.ForeignKey(to="dcim.Device", on_delete=models.CASCADE)

    # snmp properties of the device
    snmp_community = models.CharField(max_length=255, help_text="snmp community of the device", null=True)
    snmp_version = models.CharField(max_length=255, help_text="snmp version of the device", null=True)
    snmp_port = models.PositiveSmallIntegerField(null=True)
    snmp_discover_par_requests = models.PositiveSmallIntegerField(null=True)
    snmp_discover_retries = models.PositiveSmallIntegerField(null=True)
    snmp_discover_timeout = models.PositiveSmallIntegerField(null=True)

    # http properties of the device
    http_password = models.CharField(max_length=255, help_text="http password of the device", null=True)
    http_port = models.PositiveSmallIntegerField(null=True)
    http_username = models.CharField(max_length=255, help_text="http username of the device", null=True)
    https_port = models.PositiveSmallIntegerField(null=True)

    # all available components of the device
    interfaces = models.BooleanField(editable=False)
    cpu = models.BooleanField(editable=False)
    memory = models.BooleanField(editable=False)
    disk = models.BooleanField(editable=False)
    hardware_health = models.BooleanField(editable=False)
    ups = models.BooleanField(editable=False)
    server = models.BooleanField(editable=False)

    def __str__(self):
        """String representation of a Thola Config."""
        return super().__str__()

    def get_absolute_url(self):
        """Provide absolute URL to a Thola Config."""
        return reverse("plugins:thola_nautobot:tholaconfig", args=[self.pk])


class TholaOnboarding(PrimaryModel):
    """
    Thola Onboarding represents an onboarding task.
    """

    device = models.ForeignKey(to="dcim.Device", on_delete=models.CASCADE, null=True, blank=True, editable=False)
    ip = models.CharField(max_length=255, help_text="ip address of the device", null=False)
    site = models.ForeignKey(to="dcim.Site", on_delete=models.CASCADE, null=False)

    # snmp properties of the device
    snmp_community = models.CharField(max_length=255, help_text="snmp community of the device", null=True)
    snmp_version = models.CharField(max_length=255, help_text="snmp version of the device", null=True)
    snmp_port = models.PositiveSmallIntegerField(null=True)
    snmp_discover_par_requests = models.PositiveSmallIntegerField(null=True)
    snmp_discover_retries = models.PositiveSmallIntegerField(null=True)
    snmp_discover_timeout = models.PositiveSmallIntegerField(null=True)

    status = models.CharField(editable=False, max_length=255, help_text="status of the onboarding task")

    def __str__(self):
        """String representation of a Thola Onboarding task."""
        return super().__str__()

    def get_absolute_url(self):
        """Provide absolute URL to a Thola Onboarding task."""
        return reverse("plugins:thola_nautobot:tholaonboarding", args=[self.pk])
