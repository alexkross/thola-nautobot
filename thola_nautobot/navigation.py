"""Plugin additions to the Nautobot navigation menu."""
from nautobot.apps.ui import NavMenuGroup, NavMenuItem, NavMenuTab
from nautobot.core.apps import NavMenuAddButton
#from nautobot.core.choices import ButtonActionColorChoices #, ButtonActionIconChoices

items = (
    NavMenuItem(
        link="plugins:thola_nautobot:tholaconfig_list",
        name="Configurations",
        buttons=(
            NavMenuAddButton(
                link="plugins:thola_nautobot:tholaconfig_add",
                title="Add",
                icon_class="mdi mdi-plus-thick",
                #button_class=ButtonActionColorChoices.GREEN,
            ),
        ),
    ),
    NavMenuItem(
        link="plugins:thola_nautobot:tholaonboarding_list",
        name="Onboardings",
        buttons=(
            NavMenuAddButton(
                link="plugins:thola_nautobot:tholaonboarding_add",
                title="Add",
                icon_class="mdi mdi-plus-thick",
                #button_class=ButtonActionColorChoices.GREEN
            ),
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Plugins",
        groups=(NavMenuGroup(name="Thola SNMP", weight=1000, items=tuple(items)),),
    ),
)
