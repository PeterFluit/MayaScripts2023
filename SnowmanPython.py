CreatePolygonSphere;
polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1;
// Result: pSphere1 polySphere1
scale -r 1.643372 1.643372 1.643372 ;
CreatePolygonSphere;
polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1;
// Result: pSphere2 polySphere2
move -r 0 1.936576 0 ;
CreatePolygonSphere;
polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1;
// Result: pSphere3 polySphere3
move -r 0 3.031574 0 ;
scale -r 0.634119 0.634119 0.634119 ;
CreatePolygonCylinder;
polyCylinder -r 1 -h 2 -sx 20 -sy 1 -sz 1 -ax 0 1 0 -rcp 0 -cuv 3 -ch 1;
// Result: pCylinder1 polyCylinder1
move -r 0 4.279348 0 ;
scale -r 0.482155 0.482155 0.482155 ;
move -r 0 -0.342927 0 ;
select -cl  ;
CreatePolygonCone;
polyCone -r 1 -h 2 -sx 20 -sy 1 -sz 0 -ax 0 1 0 -rcp 0 -cuv 3 -ch 1;
// Result: pCone1 polyCone1
rotate -r -os -fo 81.348127 0 0 ;
move -r 0 2.993922 0 ;
scale -r 0.402655 0.402655 0.402655 ;
move -r 0 0 0.728381 ;
move -r 0 0.155978 0 ;