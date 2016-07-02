# Perspective

## Import

* base-geometry

## Lists

* **shape types** *square,rect,circle,diamond,void*

* **shape style** *1,2,3,4,5,6,7,8,9,10,11,12* 

## Models

### Variation 3D

* **var3d** `linear005`; `linear005`; `linear005`

### Setting 3D

* **conf3d** `linear005`; `linear005`; `linear005`

### Point

* **point2d** `linear005`; `linear005`

### Horizontal

* **horizontal2d** `linear005`

### Vertical

* **vertical2d** `linear005`

### Zone

* **zone2d** `linear1035`

### Shape

* **shape3d** `shape types`; `shape style` ; `Variation 3D` ; `Setting 3D`

### Scene

* **shapes** 3 to 10 of `Shape` ; `fg obj left` ; `fg horiz` ; `fg vert left` ; `vp`
* **shapes** 3 to 10 of `Shape` ; `fg obj right` ; `fg horiz` ; `fg vert right` ; `vp`
* **aka** *main-scene*

## References

* **vp** `Point`
* **fg horiz** `Horizontal`
* **fg vert left** `Vertical` ; *0/0.5*
* **fg vert right** `Horizontal` ; *0.5/1*
* **fg obj left** `Zone`
* **fg obj right** `Zone`





	
