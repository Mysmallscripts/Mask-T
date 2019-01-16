# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
# Contributed to by
# Pontiac, Fourmadmen, varkenvarken, tuga3d, meta-androcto, metalliandy, dreampainter & cotejrp1#


bl_info = {
    "name": "Pose Hidden",
    "author": "John Doe",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Pose hidden parts of the object from the sculpt mode to edit mode",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}
import bpy


def main(context):
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            override = bpy.context.copy()
            override['area'] = area
            bpy.ops.paint.mask_flood_fill(mode='VALUE', value=0)
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_mode(type="FACE")
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.mesh.reveal()
            bpy.ops.object.hook_add_newob()
            bpy.ops.object.editmode_toggle()



    
            break

class PosetHidden(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "myops.pose_hidden"
    bl_label = "Pose Hidden"


    def execute(self, context):
        main(context)
        return {'FINISHED'}

class PoseHiddenPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Pose Hidden"
    bl_idname = "OBJECT_PT_pose"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Mask T"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("myops.pose_hidden")
        
        
def register():
    bpy.utils.register_class(PoseHiddenPanel)
    bpy.utils.register_class(PosetHidden)

def unregister():
    bpy.utils.unregister_class(PoseHiddenPanel)
    bpy.utils.unregister_class(PosetHidden)

if __name__ == "__main__":
    register()

