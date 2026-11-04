"""Enable the installed addon in a newly launched Blender session."""
import bpy
import addon_utils
addon_utils.enable("blender_mcp", default_set=True, persistent=True)
bpy.context.scene.blendermcp_auto_start_server = True
bpy.context.scene.blendermcp_port = 9876
bpy.ops.wm.save_userpref()
if not getattr(bpy.types, "blendermcp_server", None):
    bpy.ops.blendermcp.start_server()
print("PERHOP_BLENDER_ADDON_READY")
