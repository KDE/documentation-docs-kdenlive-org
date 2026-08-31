.. meta::

   :description: Kdenlive Video Effects - Light Graffiti
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, lightgraffiti, light graffiti, light, graffiti

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. .. versionadded:: 26.08

  
Light Graffiti
==============

.. figure:: /images/effects_and_compositions/effects-lightgraffiti-2608.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Light Graffiti

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      lightgraffiti
   :**Available**:
      |appimage| |windows| |apple|
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

This effect/filter creates light graffitis from a video by keeping the brightest spots.


.. rubric:: Parameters

**Statistics** (above the keyframe ruler)

The stats switches allow easy and accurate adjustment of the threshold parameters.

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Show brightness statistics 
     - Switch
     - | If **on**, displays the brightness and threshold, for adjusting the brightness threshold parameter.
       | Example: To adjust the brightness threshold, check this box and adjust the threshold until the whole light source is highlighted. Repeat the same with the other parameters. Only parts that are highlighted in *all* thresholds will count as light source.
   * - Show background difference statistics
     - Switch
     - If **on**, displays the background difference and threshold
   * - Show background difference sum statistics
     - Switch
     - If **on**, displays the sum of the background difference and threshold

**Switches** (above the keyframe ruler)

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Transparent background
     - Switch
     - Makes the background transparent, allowing to apply a composite effect and paint the light mask over a completely different video.
   * - Nonlinear dimming
     - Switch
     - If **on**, uses nonlinear dimming (may look more natural)
   * - Reset
     - Switch
     - Use this to reset the clip if you need to adjust parameters. The effect will not reset if the clip is played again, so you need to do this manually.

.. note::
   If *Reset* is not switched off, the effect will not produce any visible results.

**Parameters**

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Brightness threshold
     - Integer
     - How bright (:code:`R+G+B`) does a pixel need to be in order to be recognized as a light source? Increasing this threshold requires brighter light sources (i.e. more white or less color, respectively) but prevents some «false alarms» where semi-bright parts, e.g. hands where colors can change quite a lot compared to the background, are incorrectly recognized as light source.
   * - Difference threshold
     - Integer
     - How much does the strongest color channel of a pixel have to change, compared to the background image (:code:`max(dR, dG, dB)`), in order to be recognized as light source? Increasing this threshold makes it harder for light sources to be accepted on bright backgrounds, but decreases the danger of noise or generally bright spots counting as light source.
   * - Difference sum threshold
     - Integer
     - How much does the sum of all color channels *relative to the background image* (:code:`dR + dG + dB`) have to change until a pixel is recognized as a light source? Raising this value might, in some cases, avoid that some light objects lit by the light source are added to the light mask.
   * - Sensitivity
     - Integer
     - For slowly moving light source try to use a lower sensitivity to obtain a better exposure.
   * - Lower overexposure
     - Integer
     - The light mask does not get white immediately when the light source is moving slowly or staying steady.
   * - Dimming
     - Integer
     - Dims the light mask. Lights will leave a fainting trail if it is set to a value > 0.
   * - Background weight
     - Integer
     - Strength of the (calculated) background image. Setting it to 100 paints the light mask directly over the background, without the painting person in the image if the video starts with a «clean» background image. (See the α parameter.)
   * - α
     - Integer
     - Determines how the effect tries to adapt to background changes. The Light Graffiti effect remembers the first frame of the clip it is applied to, so the clip should *always* start with the painter outside of the video. If the background constantly changes, e.g. on a street, try to set α > 0 to calculate an average background image.
   * - Saturation
     - Integer
     - Increases the saturation of lights.
