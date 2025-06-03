import bpy

class PACKFORGE_PT_MainPanel(bpy.types.Panel):
    bl_label = "PackForge"
    bl_idname = "PACKFORGE_PT_main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'PackForge'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Exporta tus assets en un clic")
        layout.operator("packforge.export_assets", icon='EXPORT')

classes = [PACKFORGE_PT_MainPanel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
