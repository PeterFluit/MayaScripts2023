import maya.cmds as cmd
cmd.select("ctrl", r=True)
cmd.listRelatives("curveShape1", shapes=True)
cmd.setAttr("curveShape1.overrideEnabled", 1)
cmd.setAttr("curveShape1.overrideColor", 14)
cmd.select(cl=True)