.. meta::

   :description: Kdenlive Video Effects - Defish
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, defish

.. metadata-placeholder

   :authors: - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Marko (https://userbase.kde.org/User:Marko)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Defish
======

.. figure:: /images/effects_and_compositions/effects-defish-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Defish

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      defish0r
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      8bit
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect can transform footage shot with a fisheye lens to look like it was shot with a rectilinear lens, and vice versa. It can also be used to straighten the video that was shot with one of these wide angle converters, which are only slightly curvy, or with a semi-fisheye camera, like the GoPro Hero.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - De-Fish
     - Switch
     - If checked, the transform direction is from fisheye to rectilinear, when not checked, it is rectilinear to fisheye.
   * - Type
     - Selection
     - Selects the fisheye angular mapping function used
   * - Scaling
     - Selection
     - Select the scaling method
   * - Straighten all Edges of Video Frame
     - Switch
     - 
   * - Interpolation
     - Selection
     - Select which interpolation method to use. Options: see below.
   * - Aspect Type
     - Selection
     - Select the pixel aspect type\ [1]_.
   * - Amount
     - Integer
     - Controls the amount of (de)distortion applied to the video. More details below.
   * - Fix Camera Scaling Between 4:3 and 16:9
     - Integer
     - 
   * - Scale Y to Affect Aspect Ratio
     - Integer
     - 
   * - Manual Scale
     - Integer
     - Scales the video. Range is 0 to 1000 (divided by 500 to get scaling factor).
   * - Manual Aspect
     - Integer
     - Controls directly the pixel aspect ratio. Range is 0 to 1000 mapped to from 0.5 to 2. Only used if :guilabel:`Aspect Type` is set to **manual**.


The following selection items are available:

:guilabel:`Type`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-wrap

   * - Equidistant
     - 
   * - Orthographic
     - Straighten all edges of video frame
   * - Equiarea
     - default
   * - Stereographic
     - 

:guilabel:`Scaling`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-wrap

   * - Fit
     - no cropping but there will be blank area at the borders
   * - Manual
     - see :guilabel:`Manual Scale`

:guilabel:`Interpolator`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-wrap

   * - Nearest neighbor
     - 
   * - Bilinear
     - default
   * - Bicubic smooth
     - 
   * - Bicubic sharp
     - 
   * - Spline 4x4
     - 
   * - Spline 6x6
     - 
   * - Lanczos 16x16
     - 

:guilabel:`Aspect Type`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-wrap

   * - Square
     - default
   * - PAL DV
     - 1.067 ratio
   * - NTSC DV
     - 0.889
   * - HDV
     - 1.333
   * - Manual
     - see :guilabel:`Manual Aspect`


.. rubric:: Parameters explained

:Interpolation:
 The seven different interpolation methods allow making a quality/speed trade-off. The interpolators are ordered from fast, low quality to (very) slow, high quality. The spline interpolating polynomials are from Helmut Dersch. For real-time use, **Nearest neighbor** is the fastest because, in fact, it is equal to no interpolation. In most cases **Bilinear** should be good enough, and on a decent machine should still run in real time. Beyond **Bicubic**, the quality gain is marginal for a single resampling. **Lanczos** takes an eternity!

:Amount:
 Controls the amount of (de)distortion applied to the video. It controls the ratio of fisheye focal length to image half diagonal, but in an nonlinear inverse way, to make the control more "comfortable". It can be adjusted beyond "reasonable" values (which differ between the mapping function types), to produce some looney effects. When exploring this range and the image disappears, check the scaling as it could be that the image became too big or too small to see. For some unreasonable values the image might indeed disappear, when there are math overflows or imaginary results (:guilabel:`Type` **Equidistant** and **Orthographic** are more prone to image vanishing). When working in the "special effect" range, it is always worth to try manual scaling. If the video contains zooming through a curvy wide angle adaptor, the needed amount will vary. In this case use keyframing.


.. rubric:: Notes

1. Tweaking the parameters for best defish

 Take a shot of something like a brick wall or bathroom tiles, that has a lot of horizontal and vertical straight lines. Be careful to keep the optical axis as perpendicular as possible to the wall (i.e. keep a maximally symmetrical image in the viewfinder). Use this image to tweak the parameters, primarily amount, type and aspect.

2. Some examples of effect abuse

 These were tried with PAL DV. These examples work best when there is some interesting action near the center of the image.

 For a kind of roundish kaleidoscope, try this:

 .. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Amount
     - 775
   * - Defish
     - OFF
   * - Type
     - equidistant
   * - Scaling
     - Manual
   * - Manual Scale
     - 300...400

 Another crazy distortion:

 .. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Amount
     - 921
   * - Defish
     - OFF
   * - Type
     - stereographic
   * - Scaling
     - Manual
   * - Manual Scale
     - 191

 For an effect reminiscent of some scenes from the "2001 Space Odyssey" movie try this:

 .. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Amount
     - 900
   * - Defish
     - ON
   * - Type
     - Stereographic
   * - Scaling
     - Fill


----

.. [1] To get the math right, the effect's algorithm needs to know the pixel aspect ratio.


.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Icons used here (remove comment indent to enable them for this document)
   
   .. |linux| image:: /images/icons/linux.png
   :width: 14px
      :class: no-scaled-link

   .. |appimage| image:: /images/icons/kdenlive-appimage_3.svg
   :width: 14px
      :class: no-scaled-link

   .. |windows| image:: /images/icons/windows.png
   :width: 14px
      :class: no-scaled-link

   .. |apple| image:: /images/icons/apple.png
   :width: 14px
      :class: no-scaled-link
