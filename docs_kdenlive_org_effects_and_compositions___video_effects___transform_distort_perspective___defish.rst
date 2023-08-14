.. meta::

   :description: Do your first steps with Kdenlive video editor, using defish effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, defish

.. metadata-placeholder

   :authors: - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Marko (https://userbase.kde.org/User:Marko)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-defish:

Defish
======

This effect can transform footage shot with a fisheye lens to look like it was shot with a rectilinear lens, and vice versa. It can also be used to straighten the video that was shot with one of these wide angle converters, which are only slightly curvy, or with a semi-fisheye camera, like the GoPro Hero.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-defish.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-defish

   Defish effect

* **DeFish** - If checked, the transform direction is from fisheye to rectilinear, when not checked, it is rectilinear to fisheye.

* **Type** - Selects the fisheye angular mapping function used. Options are **equidistant**, **orthographic**, **equiarea** (default) and **stereographic**.

* **Scaling** - Select the scaling method. Options are **Fill** (default; no empty borders will be left but some cropping will occur), **Center**, **Fit** (no cropping but there will be blank area at the borders) and **Manual** (see :guilabel:`Manual Scale`).

* **Straighten all edges of video frame** -

* **Interpolator** - Select which interpolation method to use. Options: see below.

* **Aspect Type** - Select the pixel aspect type\ [1]_. Options are **Square** (default), **PAL DV** (1.067 ratio), **NTSC DV** (0.889), **HDV** (1.333) and **Manual** (see :guilabel:`Manual Aspect`).

* **Amount** - Controls the amount of (de)distortion applied to the video. More details below.

* **Fix camera scaling between 4:3 and 16:9**

* **Scale Y to affect aspect ratio**

* **Manual Scale** - Scales the video. Range is 0 to 1000 (divided by 500 to get scaling factor).

* **Manual Aspect** - Controls directly the pixel aspect ratio. Range is 0 to 1000 mapped to from 0.5 to 2. Only used if :guilabel:`Aspect Type` is set to **manual**.

.. rst-class:: clear-both


.. rubric:: Parameters explained

**Interpolator**

There are seven different interpolation methods allowing to make a quality/speed trade-off. The interpolators are ordered from fast, low quality to (very) slow, high quality. The spline interpolating polynomials are from Helmut Dersch. For real-time use, **Nearest neighbor** is the fastest because, in fact, it is equal to no interpolation. In most cases **Bilinear** should be good enough, and on a decent machine should still run in real time. Beyond **Bicubic**, the quality gain is marginal for a single resampling. **Lanczos** takes an eternity!

* Nearest neighbor
* Bilinear
* Bicubic smooth
* Bicubic sharp
* Spline 4x4
* Spline 6x6
* Lanczos 16x16

**Amount**

Controls the amount of (de)distortion applied to the video. It controls the ratio of fisheye focal length to image half diagonal, but
in an nonlinear inverse way, to make the control more "comfortable". It can be adjusted beyond "reasonable" values (which differ between the mapping function types), to produce some looney effects. When exploring this range and the image disappears, check the scaling as it could be that the image became too big or too small to see. For some unreasonable values the image might indeed disappear, when there are math overflows or imaginary results... (:guilabel:`Type` **Equidistant** and **Orthographic** are more prone to image vanishing). Anyway, when working in the "special effect" range, it is always worth to try manual scaling. If the video contains zooming through a curvy wide angle adaptor, the needed amount will vary. In this case use keyframing.


.. rubric:: Some application notes

1. Tweaking the parameters for best defish

Take a shot of something like a brick wall or bathroom tiles, that has a lot of horizontal and vertical straight lines. Be careful to keep the optical axis as perpendicular as possible to the wall (i.e. keep a maximally symmetrical image in the viewfinder). Use this image to tweak the parameters, primarily amount, type and aspect.

2. Some examples of effect abuse

These were tried with PAL DV. These examples work best when there is some interesting action near the center of the image.

For a kind of roundish kaleidoscope, try this:

.. list-table::

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

For an effect, reminiscent of some scenes from the "2001 Space Odyssey" movie try this:

.. list-table::

   * - Amount
     - 900
   * - Defish
     - ON
   * - Type
     - Stereographic
   * - Scaling
     - Fill


**Notes**

.. [1] To get the math right, the effect's algorithm needs to know the pixel aspect ratio.
