"""REST API serializers for thola nautobot."""
from nautobot.core.api.serializers import BaseModelSerializer
from nautobot.extras.api.serializers import RoleSerializer
from nautobot.dcim.api.serializers import DeviceSerializer, LocationSerializer
from thola_nautobot.models import TholaConfig, TholaOnboarding


class TholaConfigSerializer(BaseModelSerializer):
    """Serializer for config API."""

    device = DeviceSerializer

    class Meta:
        """Meta class for TholaConfigSerializer."""

        model = TholaConfig
        fields = ["id", "device", "snmp_community", "snmp_version", "snmp_port", "snmp_discover_par_requests",
                  "snmp_discover_retries", "snmp_discover_timeout", "http_password", "http_port", "http_username",
                  "https_port"]


class TholaOnboardingSerializer(BaseModelSerializer):
    """Serializer for onboarding API."""

    role = RoleSerializer
    device = DeviceSerializer
    site = LocationSerializer

    class Meta:
        """Meta class for TholaOnboardingSerializer."""

        model = TholaOnboarding
        fields = ["id", "device", "ip", "site", "role", "snmp_community", "snmp_version", "snmp_port",
                  "snmp_discover_par_requests", "snmp_discover_retries", "snmp_discover_timeout", "status"]
