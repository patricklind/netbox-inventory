from netbox.ui import panels, attrs

class AssetRolePanel(panels.NestedGroupObjectPanel):
    color = attrs.ColorAttr('color')