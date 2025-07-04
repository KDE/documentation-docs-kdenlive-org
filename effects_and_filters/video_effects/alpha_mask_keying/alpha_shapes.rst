.. meta::

   :description: Kdenlive Video Effects - Alpha Shapes
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha shapes

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |alphaspot| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-alphaspot/" target="_blank">frei0r.alphasp0t</a>

.. |alphaops| raw:: html

   <a href="https://github.com/dyne/frei0r/blob/master/src/filter/alpha0ps/readme" target="_blank">frei0r.alpha0ps</a>


Alpha Shapes
============

.. figure:: /images/effects_and_compositions/effects-alpha_shapes-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-show-video| Alpha Shapes

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      alphaspot
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This is the |alphaspot| MLT filter, see also the |alphaops| readme file.

This effect creates an area of transparency in the clip such that the underlying clip shows through in places defined by geometric shapes. By default, the area of transparency is outside the shape that is drawn. Inside the shape is an area of opacity where the overlaying clip is visible. The effect can be stacked to create odd shaped or many areas fo transparency.

.. rst-class:: clear-both


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Shape
     - Selection
     - Controls the shape of the area of opacity that the effect will create.
   * - Operation
     - Selection
     - Defines what is to happen when you have more than one alpha effect on the clip
   * - Position X / Y
     - Integer
     - Defines the position of the shape on the screen. The range of values is from 0 to 1000 where 500 defines the middle of the screen.
   * - Size X / Y
     - Integer
     - Defines the size of the shape. The range of values is from 0 to 1000 where 500 defines 100%,
   * - Tilt
     - Integer
     - Controls the angle the shape appears on the screen. The units are in 1000ths of a full rotation. For example, a value of 250 is one quarter of a circle turn and 500 is a 180-degree turn. That means, 1000 tilt units = 360 degrees.
   * - Transition width
     - Integer
     - Defines the width of a border on the shape where the transparency grades from the inside to the outside of the shape. Can be used for feathering_ or creating a frame.
   * - Min
     - Integer
     - 
   * - Max
     - Integer
     - 

The following selection items are available:

:guilabel:`Shape`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Rectangle
     - Draws a rectangle
   * - Ellipse
     - Draws an ellipse/circle
   * - Triangle
     - Draws a triangle
   * - Diamond
     - Draws a diamond

:guilabel:`Operation`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Write On Clear
     - Existing alpha mask is overwritten
   * - Max
     - Take the maximum between the existing alpha mask and the mask generated by this filter
   * - Min
     - Take the minimum between existing alpha mask and mask generated by this filter
   * - Add
     - Add the existing alpha mask and the mask generated by this filter
   * - Subtract
     - Subtract from the existing alpha mask the mask generated by this filter

.. rst-class:: clear-both


.. _effects-alpha_shapes_examples:

.. rubric:: Working Examples

**Min and Max values and operations**

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-alpha_shapes_example.webp
   :width: 800px
   :alt: kdenlive2304_effects-alpha_shapes_example

   Alpha Shapes example timeline

For the examples we are using a video clip on video track V1 and a title clip (blue background and "Video 1" as text) on video track V2. The Alpha Shape effect is applied to the overlaying clip on V2. This is important to understand the explanations of the various parameters and operations in the examples below.

The Alpha Shapes effect draws areas of opacity onto the clip. The addition of this filter (with the default settings of Min = 0 and Max = 1000) makes the whole clip transparent except for an area of opaqueness defined by the shape and its position and size where the clip can be seen. If you reversed the Min and Max values the result would be that the whole clip is opaque (can be seen) except for an area of transparency defined by the shape and its position and size.

The Max and Min values adjust the opacity of the clip inside and outside of the shape, respectively. A setting of 1000 is 100% opaque. A setting of zero is 0% opaque (i.e. 100% transparent).

**Max control**

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-alpha_shapes_example_1.webp
   :align: left
   :width: 400px
   :figwidth: 400px
   :alt: kdenlive2304_effects-alpha_shapes_example_1

   Max parameter at 1000

The :guilabel:`Max` parameter controls how opaque it is *inside* the shape. At Max = 1000 it is completely opaque inside the shape and nothing of the clip on V1 (background) shows through.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/kdenlive2304_effects-alpha_shapes_example_2.webp
      :align: left
      :width: 400px
      :figwidth: 400px
      :alt: Alpha_shapes_max_control

      Max parameter at 500

   At Max = 500 it is semi-transparent inside the shape and you can see the clip on V1 bleeding through.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/kdenlive2304_effects-alpha_shapes_example_3.webp
      :align: left
      :width: 400px
      :figwidth: 400px
      :alt: Alpha_shapes_max_control3

      Max parameter at 0; Min parameter at 0

   At Max = 0 the inside of the shape is completely transparent - the same as the rest of the clip on V2 (foreground) - and you can see all of the background.

.. rst-class:: clear-both


**Min Control**

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-alpha_shapes_example_4.webp
   :align: left
   :width: 400px
   :figwidth: 400px
   :alt: kdenlive2304_effects-alpha_shapes_example_4

   Min parameter at 100

The :guilabel:`Min` parameter adjusts how opaque it is *outside* the shape. When Min = 1000 the outside of the shape is completely opaque (opacity of 100%), and at Min = 500 we see something of the foreground appear outside the shape.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/kdenlive2304_effects-alpha_shapes_example_6.webp
      :align: left
      :width: 400px
      :figwidth: 400px
      :alt: kdenlive2304_effects-alpha_shapes_example_5

      Min parameter at 1000

   At Min = 1000 the opacity outside the shape is 100% and nothing of the background appears.

.. rst-class:: clear-both


**Combining Alpha Shapes - Operations**

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-alpha_shapes_example_7.webp
   :align: left
   :width: 400px
   :figwidth: 400px
   :alt: kdenlive2304_effects-alpha_shapes_example_14

   Alpha Shape effects stacked: (1) & (2)

In this example, we added a second alpha shape effect (2) using a triangle as the shape. As effects are processed from the top down the two effects interact with each other. At the onset we are using the operation :guilabel:`Write on clear` so the second alpha shape effect appears on its own.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/kdenlive2304_effects-alpha_shapes_example_8.webp
      :align: left
      :width: 400px
      :figwidth: 400px
      :alt: kdenlive2304_effects-alpha_shapes_example_8

      Max at 1000; Min at 500

   With Max = 1000 the opacity inside the triangle is 100% while Min = 500 determines an opacity of 50% outside the triangle which makes the background and foreground blend together. Still, the operation :guilabel:`Write on clear` makes Kdenlive ignore the previous alpha shape effect (1) - it is simply overwritten.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/kdenlive2304_effects-alpha_shapes_example_9.webp
      :align: left
      :width: 400px
      :figwidth: 400px
      :alt: kdenlive2304_effects-alpha_shapes_example_9

      Operation set to Max

   Now that we changed the operation to :guilabel:`Max` the previous alpha shape effect is taken into consideration and both areas defined by the respective shapes - the rectangle from effect (1) and the triangle from effect (2) - show up because both have the :guilabel:`Max` parameter value set to 1000 (= 100% opaque).

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/kdenlive2304_effects-alpha_shapes_example_10.webp
      :align: left
      :width: 400px
      :figwidth: 400px
      :alt: kdenlive2304_effects-alpha_shapes_example_10

      Operation set to Min

   With the operation set to :guilabel:`Min` the blending is different. Kdenlive takes the minimum values of the Min and Max parameter values: Min value for effect (2) is 500 in areas where the Max value of effect (1) is 1000. There is no distinction between Min or Max, only the value of that pixel is taken into account.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/kdenlive2304_effects-alpha_shapes_example_11.webp
      :align: left
      :width: 400px
      :figwidth: 400px
      :alt: kdenlive2304_effects-alpha_shapes_example_11

      Operation set to Add

   The operation :guilabel:`Add` performs a simple mathematical addition of the respective Min and Max values (and caps it at 1000 or 100%). Now the areas defined by both effect shapes are visible.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/kdenlive2304_effects-alpha_shapes_example_12.webp
      :align: left
      :width: 400px
      :figwidth: 400px
      :alt: Okdenlive2304_effects-alpha_shapes_example_12

      Operation set to Substract

   The operation :guilabel:`Subtract` performs a simple mathematical subtraction of the respective Min and Max values (and floors it at 0 or 0%). In this example because the Max value of effect (2) is 1000, it practically brings the opacity down to 0 hence the background is visible (the area of the shape is 100% transparent).

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/kdenlive2304_effects-alpha_shapes_example_13.webp
      :align: left
      :width: 400px
      :figwidth: 400px
      :alt: kdenlive2304_effects-alpha_shapes_example_13

      Operation set to Substract; Min = 0

   In this example we have reduced the Min value of effect (2) to 0 making the area outside the triangle 0% opaque (= 100% transparent). This results in the rectangular shape from effect (1) being cut by the triangle shape from effect (2) because the Max values in both effects are at 1000 (100% opaque), and with the :guilabel:`Subtract` operation the Max value of the pixels in the overlapping area is 0.


.. _feathering:

**Feathering**

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-alpha_shapes_example_14.webp
   :align: left
   :width: 400px
   :figwidth: 400px
   :alt: Operation_max

   Transition width set to 100 (default = 200) for feathering

Use the :guilabel:`Transition width` parameter to create a bleeding edge (aka feathering) for the alpha shape.
