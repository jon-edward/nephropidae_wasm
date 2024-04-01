# Demos

## [Cube](https://jon-edward.github.io/nephropidae_wasm/demos/cube)
Taken from [Lobster sample](https://github.com/aardappel/lobster/blob/master/samples/cube.lobster). 

[Demo](https://jon-edward.github.io/nephropidae_wasm/demos/cube)

<details open>
<summary>Docstring</summary>
<pre>
This example renders a cube with a different colorèd number on each face.
Moving the mouse or WASD rotates the viewport around the cube like turning a
globe in front of the camera.

The example illustrates creating a simple mesh and rendering a texture on
the mesh in various orientations.
The example showcases the render_to_texture utility, which allows us to
render a 2D drawing on the surfaces of a 3D object, using a frame buffer.
The example also demostrates using gl.new_mesh, which allows us to orient
the texture on each face of the cube, since the simpler gl.new_poly is not
quite sufficient for this purpose.

To generate the mesh for each face, cube_face_meshes uses the three least
significant bits of ASCII characters to represent whether the edge is on the
near or far side of the cube along each axis.

 -----ZYX CHR corner
 00110000 '0' origin
 00110001 '1' x
 00110010 '2' y
 00110011 '3' xy
 00110100 '4' z
 00110101 '5' xz
 00110110 '6' yz
 00110111 '7' zyz

Each face of the cube contains four of the cube's vertices.
The normal vector for the face of the cube must face outward to be opaque to
an outside observer, so the vertices are listed counter-clockwise.
In the following illustration, the interior faces are inverted, so the
vertices appear in clockwise order from our perspective.

The first index must be the top-right corner of the texture.
The textures are arranged such that the textures are upright around the
equator and the poles are connected top to bottom with their nearest
neighbor.
Rotating the vertex strings rotates the corresponding texture orientation.

The faces are numbered according to the conventions of right-handed dice.
All faces in opposition have the same sum.
Numbers read counter-clockwise about the origin and its opposite vertex.

                                 inverted clockwise
 Z       4---5             .---.   .---.
  \      |\  |\    1540->2 |\ 2 \  |   |\  6<-5464
   0--X  | 0---1           | .---. | 6 | .
   |     | | | |   0462->3 |3|   | |   |4| 4<-5137
   Y     6-|-7 |           ' | 1 | '---' |
          \|  \|   3102->1  \|   |  \ 5 \| 5<-7326
           2---3             '---'   '---'
                   counter-clockwise

Kris Kowal &lt;kris@cixar.com&gt;</pre>
</details>

## [LobsterCraft](https://jon-edward.github.io/nephropidae_wasm/demos/lobstercraft/)
Taken from [Lobster sample](https://github.com/aardappel/lobster/blob/master/samples/lobstercraft.lobster).

[Demo](https://jon-edward.github.io/nephropidae_wasm/demos/lobstercraft/)

<details open>
<summary>Docstring</summary>
<pre>
A minecraft clone in very few lines of code implements random world generation, 
chunks, rendering, and mining/building of blocks created in response to https://github.com/fogleman/Minecraft 
(which is 10x bigger in code).
</pre>
</details>

## [Pendulum](https://jon-edward.github.io/nephropidae_wasm/demos/pendulum/)
Taken from [Lobster sample](https://github.com/aardappel/lobster/blob/master/samples/pendulum.lobster). 

[Demo](https://jon-edward.github.io/nephropidae_wasm/demos/pendulum/)

<details open>
<summary>Docstring</summary>
<pre>
based on: http://www.physicsandbox.com/projects/double-pendulum.html</pre>
</details>


## [Physics Boxes](https://jon-edward.github.io/nephropidae_wasm/demos/physics_boxes/)
Taken from [Lobster sample](https://github.com/aardappel/lobster/blob/master/samples/physics_boxes.lobster). 

[Demo](https://jon-edward.github.io/nephropidae_wasm/demos/physics_boxes/)

<details open>
<summary>Docstring</summary>
<pre>
Showing off physics features in Lobster</pre>
</details>


## [Physics Water](https://jon-edward.github.io/nephropidae_wasm/demos/physics_water/)
Taken from [Lobster sample](https://github.com/aardappel/lobster/blob/master/samples/physics_water.lobster). 

[Demo](https://jon-edward.github.io/nephropidae_wasm/demos/physics_water/)

<details open>
<summary>Docstring</summary>
<pre>
Showing off physics features in Lobster</pre>
</details>


## [PythTree](https://jon-edward.github.io/nephropidae_wasm/demos/pythtree/)
Taken from [Lobster sample](https://github.com/aardappel/lobster/blob/master/samples/pythtree.lobster). 

[Demo](https://jon-edward.github.io/nephropidae_wasm/demos/pythtree/)

<details open>
<summary>Docstring</summary>
<pre>
graphics demo showing an animated "tree of pythagoras"</pre>
</details>
