#Copyright(c) 2014, Konrad Sobon
# @arch_laboratory, http://archi-lab.net

import clr
import sys
clr.AddReference('ProtoGeometry')

RhinoCommonPath = r'C:\Program Files\Rhinoceros 5 (64-bit)\System'
if RhinoCommonPath not in sys.path:
	sys.path.Add(RhinoCommonPath)
clr.AddReferenceToFileAndPath(RhinoCommonPath + r"\RhinoCommon.dll")

pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)

from Autodesk.DesignScript.Geometry import *
import Rhino as rc

#The inputs to this node will be stored as a list in the IN variable.
dataEnteringNode = IN
rhObjects = IN[0]

#point/control point conversion function
def rhPointToPoint(rhPoint):
	rhPointX = rhPoint.Location.X
	rhPointY = rhPoint.Location.Y
	rhPointZ = rhPoint.Location.Z
	dsPoint = Point.ByCoordinates(rhPointX, rhPointY, rhPointZ)
	return dsPoint

#convert rhino/gh geometry to ds geometry
dsPoints = []
for i in rhObjects:
	try:
		i = i.Geometry
	except:
		pass
	if i.ToString() == "Rhino.Geometry.Point":
		dsPoints.append(rhPointToPoint(i))

#Assign your output to the OUT variable
OUT = dsPoints