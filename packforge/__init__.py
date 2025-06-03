bl_info = {
    "name": "PackForge",
    "author": "EiKu",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Tool Shelf > PackForge",
    "description": "Empaquetador automático de assets con thumbnails y documentación",
    "category": "Import-Export",
}

import bpy
from . import packforge_ui, packforge_operator

def register():
    packforge_ui.register()
    packforge_operator.register()

def unregister():
    packforge_ui.unregister()
    packforge_operator.unregister()

if __name__ == "__main__":
    register()
