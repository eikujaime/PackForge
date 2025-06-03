import bpy

class PACKFORGE_OT_ExportAssets(bpy.types.Operator):
    bl_idname = "packforge.export_assets"
    bl_label = "Exportar Assets"

    def execute(self, context):
        self.report({'INFO'}, "Exportación completada (demo)")
        return {'FINISHED'}

classes = [PACKFORGE_OT_ExportAssets]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
