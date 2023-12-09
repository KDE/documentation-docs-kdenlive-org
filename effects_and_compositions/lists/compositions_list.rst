.. meta::
  
   :description: Alphabetical list of all compositions in Kdenlive
   :keywords: KDE, Kdenlive, video effects, plugins, composition, transition

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Roger (https://userbase.kde.org/User:Roger)
             - ChristianW (https://userbase.kde.org/User:ChristianW)
             - Tenzen (https://userbase.kde.org/User:Tenzen)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


============
Compositions
============

.. note::
   The effects and compositions included will differ depending on the available plug-ins on the specific packaging on each operating system. Kdenlive will auto-detect and make available any supported LADSPA plug-in packages from your distribution. For the greatest compatibility, please use the AppImage version of Kdenlive.


.. list-table::
   :class: table-wrap
   :header-rows: 1
   :width: 100%
   :widths: 20 8 62

   * - Composition
     - OS\ [1]_
     - Description
   * - :doc:`/effects_and_compositions/transitions/addition`
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform an RGB[A] addition operation of the pixel sources (|frei0r.addition|)
   * - :doc:`/effects_and_compositions/transitions/addition_alpha`
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform an RGB[A] addition_alpha operation of the pixel sources (|frei0r.addition_alpha|)
   * - :doc:`/effects_and_compositions/transitions/alphaatop`
     - |linux|\ |appimage|\ |windows|\ |apple|
     - The alpha ATOP operation (|frei0r.alphaatop|)
   * - :doc:`/effects_and_compositions/transitions/alphain`
     - |linux|\ |appimage|\ |windows|\ |apple|
     - The alpha IN operation (|frei0r.alphain|)
   * - :doc:`/effects_and_compositions/transitions/alphaout`
     - |linux|\ |appimage|\ |windows|\ |apple|
     - The alpha OUT operation (|frei0r.alphaout|)
   * - :doc:`/effects_and_compositions/transitions/alphaover`
     - |linux|\ |appimage|\ |windows|\ |apple|
     - The alpha OVER operation (|frei0r.alphaover|)
   * - :doc:`/effects_and_compositions/transitions/alphaxor`
     - |linux|\ |appimage|\ |windows|\ |apple|
     - The alpha XOR operation (|frei0r.alphaxor|)
   * - audio_mix
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Applies a stationary transition between the current and next frames. (|mix|)
   * - burn
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform an RGB[A] dodge operation between the pixel sources, using the generalized algorithm: D = saturation of 255 or depletion of 0, of ((255-A)*256) / (b+1) (|frei0r.burn|)
   * - cairo_affine_blend
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Composites second input on first input applying user-defined transformations, opacity, and blend mode (|frei0r.cairoaffineblend|)
   * - cairo_blend
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Composites second input on the first input with user-defined blend mode and opacity (|frei0r.cairoblend|)
   * - circle_wipe
     - |appimage|\ |windows|\ |apple|
     - Wipe from center to edge in a circle. (|frei0r.sleid0r_wipe-circle|)
   * - color_only
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform a conversion to color only of the source input using the hue and saturation values of input2 (|frei0r.color_only|)
   * - :doc:`/effects_and_compositions/transitions/composite`
     - |linux|\ |appimage|\ |windows|\ |apple|
     - A key-framable alpha-channel compositor for two frames (|composite|)
   * - composite_and_transform
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Composites second input on the first input with user-defined blend mode, opacity and scale (|qtblend|)
   * - darken
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform a darken operation between two sources (minimum value for both sources) (|frei0r.darken|)
   * - difference
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform an RGB[A] difference operation between the pixel sources. (|frei0r.difference|)
   * - dissolve
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Fade out one video while fading in the other video (|luma|)
   * - divide
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform an RGB[A] divide operation between the pixel sources: input1 is the numerator, input2 the denominator (|frei0r.divide|)
   * - dodge
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform an RGB[A] dodge operation between the pixel sources, using the generalized algorithm: D = saturation of 255 or (A*256)/(256-B) (|frei0r.dodge|)
   * - grain_extract
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform an RGB[A] grain-extract operation between the pixel sources (|frei0r.grain_extract|)
   * - grain_merge
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform an RGB[A] grain-merge operation between the pixel sources (|frei0r.grain_merge|)
   * - hardlight
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform an RGB[A] hardlight operation between the pixel sources (|frei0r.hardlight|)
   * - horizontal_barn_door_wipe
     - |appimage|\ |windows|\ |apple|
     - Horizontal barn door wipe. (|frei0r.sleid0r_wipe-barn-door-h|)
   * - :doc:`/effects_and_compositions/transitions/hue`
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform a conversion to hue only of the source input1 using the hue of input2 (|frei0r.hue|)
   * - lighten
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform a lighten operation between two sources (maximum value of both sources) (|frei0r.lighten|)
   * - luma
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Applies a stationary transition between the current and the next frames (|luma|)
   * - matte
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Replace the alpha channel of track A with the luma channel from track B. (|matte|)
   * - multiply
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform an RGB[A] multiply operation between the pixel sources (|frei0r.multiply|)
   * - overlay
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform an RGB[A] overlay operation between the pixel sources, using the generalized algorithm: D = A * (B + (2 * B) * (255 - A)) (|frei0r.overlay|)
   * - push_down
     - |appimage|\ |windows|\ |apple|
     - Push from top to bottom. (|frei0r.sleid0r_push-down|)
   * - push_left
     - |appimage|\ |windows|\ |apple|
     - Push from right to left. (|frei0r.sleid0r_push-left|)
   * - push_right
     - |appimage|\ |windows|\ |apple|
     - Push from left to right. (|frei0r.sleid0r_push-right|)
   * - push_up
     - |appimage|\ |windows|\ |apple|
     - Push from bottom to top. (|frei0r.sleid0r_push-up|)
   * - rectangular_wipe
     - |appimage|\ |windows|\ |apple|
     - Wipe from center to edge in a rectangle. (|frei0r.sleid0r_wipe-rect|)
   * - saturation
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform a conversion to saturation only of the source input1 using the saturation level of input2 (|frei0r.saturation|)
   * - :doc:`/effects_and_compositions/transitions/screen`
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform an RGB[A] screen operation between the pixel sources, using the generalized algorithm: D = 255 - (255 - A) * (255 - B) (|frei0r.screen|)
   * - slide_down
     - |appimage|\ |windows|\ |apple|
     - Slide from top to bottom. (|frei0r.sleid0r_slide-down|)
   * - slide_left
     - |appimage|\ |windows|\ |apple|
     - Slide from right to left. (|frei0r.sleid0r_slide-left|)
   * - slide_right
     - |appimage|\ |windows|\ |apple|
     - Slide from left to right. (|frei0r.sleid0r_slide-right|)
   * - slide_up
     - |appimage|\ |windows|\ |apple|
     - Slide from bottom to top. (|frei0r.sleid0r_slide-up|)
   * - slide
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Slide image from one side to another (|composite|)
   * - softlight
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform an RGB[A] softlight operation between the pixel sources (|frei0r.softlight|)
   * - subtract
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform an RGB[A] subtract operation of the pixel source input2 from input1 (|frei0r.subtract|)
   * - transform
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform an |affine| transform on for compositing (|affine|)
   * - uv_map
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Uses Input 1 as a UV Map to distort Input 2 (|frei0r.uvmap|)
   * - value
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Perform a conversion to value only of the source input1 using the value of input2. (|frei0r.value|)
   * - vertical_barn_door_wipe
     - |appimage|\ |windows|\ |apple|
     - Vertical barn door wipe. (|frei0r.sleid0r_wipe-barn-door-v|)
   * - video_quality_measurement
     - |linux|\ |appimage|\ |windows|\ |apple|
     - This performs the PSNR and SSIm video quality measurements by comparing the B frames to the reference frame A. It outputs the numbers to stdout in space-delimited format for easy use by another tool. The bottom half of the B frame is placed below the top half of the A frame for visual comparison (|vqm|)
   * - wipe_down
     - |appimage|\ |windows|\ |apple|
     - Wipe from top to bottom. (|frei0r.sleid0r_wipe-down|)
   * - wipe_left
     - |appimage|\ |windows|\ |apple|
     - Wipe from right to left. (|frei0r.sleid0r_wipe-left|)
   * - wipe_right
     - |appimage|\ |windows|\ |apple|
     - Wipe from left to right. (|frei0r.sleid0r_wipe-right|)
   * - wipe_up
     - |appimage|\ |windows|\ |apple|
     - Wipe from bottom to top. (|frei0r.sleid0r_wipe-up|)
   * - :doc:`/effects_and_compositions/transitions/wipe`
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Applies a stationary transition between the current and next frames (|composite|)


----

.. [1] |linux|: available in the installed version; |appimage|: available in the appimage; |windows|: available in the Windows version; |apple|: available in the MacOS (Intel only) version


.. Link list

.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   External
   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. |xbr_tutorial| raw:: html
   
   <a href="https://forums.libreto.com/t/xbr-algorithm-tutorial/123" target="_blank">xbr-algorithm-tutorial</a>

.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Compositions
   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. |frei0r.addition| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-addition/" target="_blank">frei0r.addition</a>

.. |frei0r.addition_alpha| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-addition_alpha/" target="_blank">frei0r.addition_alpha</a>

.. |frei0r.alphaatop| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-alphaatop/" target="_blank">frei0r.alphaatop</a>

.. |frei0r.alphain| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-alphain/" target="_blank">frei0r.alphain</a>

.. |frei0r.alphaout| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-alphaout/" target="_blank">frei0r.alphaout</a>

.. |frei0r.alphaover| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-alphaover/" target="_blank">frei0r.alphaover</a>

.. |frei0r.alphaxor| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-alphaxor/" target="_blank">frei0r.alphaxor</a>

.. |mix| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionMix/" target="_blank">mix</a>

.. |frei0r.burn| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-burn/" target="_blank">frei0r.burn</a>

.. |frei0r.cairoaffineblend| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-cairoaffineblend/" target="_blank">frei0r.cairoaffineblend</a>

.. |frei0r.cairoblend| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-cairoblend/" target="_blank">frei0r.cairoblend</a>

.. |frei0r.sleid0r_wipe-circle| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_wipe-circle/" target="_blank">frei0r.sleid0r_wipe-circle</a>

.. |frei0r.color_only| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-color_only/" target="_blank">frei0r.color_only</a>

.. |composite| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionComposite/" target="_blank">composite</a>

.. |qtblend| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionQtblend/" target="_blank">qtblend</a>

.. |frei0r.darken| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-darken/" target="_blank">frei0r.darken</a>

.. |frei0r.difference| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-difference/" target="_blank">frei0r.difference</a>

.. |luma| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionLuma/" target="_blank">luma</a>

.. |frei0r.divide| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-divide/" target="_blank">frei0r.divide</a>

.. |frei0r.dodge| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-dodge/" target="_blank">frei0r.dodge</a>

.. |frei0r.grain_extract| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-grain_extract/" target="_blank">frei0r.grain_extract</a>

.. |frei0r.grain_merge| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-grain_merge/" target="_blank">frei0r.grain_merge</a>

.. |frei0r.hardlight| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-hardlight/" target="_blank">frei0r.hardlight</a>

.. |frei0r.sleid0r_wipe-barn-door-h| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_wipe-barn-door-h/" target="_blank">frei0r.sleid0r_wipe-barn-door-h</a>

.. |frei0r.hue| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-hue/" target="_blank">frei0r.hue</a>

.. |frei0r.lighten| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-lighten/" target="_blank">frei0r.lighten</a>

.. |matte| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionMatte/" target="_blank">matte</a>

.. |frei0r.multiply| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-multiply/" target="_blank">frei0r.multiply</a>

.. |frei0r.overlay| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-overlay/" target="_blank">frei0r.overlay</a>

.. |frei0r.sleid0r_push-down| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_push-down/" target="_blank">frei0r.sleid0r_push-down</a>

.. |frei0r.sleid0r_push-left| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_push-left/" target="_blank">frei0r.sleid0r_push-left</a>

.. |frei0r.sleid0r_push-right| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_push-right/" target="_blank">frei0r.sleid0r_push-right</a>

.. |frei0r.sleid0r_push-up| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_push-up/" target="_blank">frei0r.sleid0r_push-up</a>

.. |frei0r.sleid0r_wipe-rect| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_wipe-rect/" target="_blank">frei0r.sleid0r_wipe-rect</a>

.. |frei0r.saturation| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-saturation/" target="_blank">frei0r.saturation</a>

.. |frei0r.screen| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-screen/" target="_blank">frei0r.screen</a>

.. |frei0r.sleid0r_slide-down| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_slide-down/" target="_blank">frei0r.sleid0r_slide-down</a>

.. |frei0r.sleid0r_slide-left| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_slide-left/" target="_blank">frei0r.sleid0r_slide-left</a>

.. |frei0r.sleid0r_slide-right| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_slide-right/" target="_blank">frei0r.sleid0r_slide-right</a>

.. |frei0r.sleid0r_slide-up| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_slide-up/" target="_blank">frei0r.sleid0r_slide-up</a>

.. |frei0r.softlight| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-softlight/" target="_blank">frei0r.softlight</a>

.. |frei0r.subtract| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-subtract/" target="_blank">frei0r.subtract</a>

.. |affine| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionAffine/" target="_blank">affine</a>

.. |frei0r.uvmap| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-uvmap/" target="_blank">frei0r.uvmap</a>

.. |frei0r.value| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-value/" target="_blank">frei0r.value</a>

.. |frei0r.sleid0r_wipe-barn-door-v| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_wipe-barn-door-v/" target="_blank">frei0r.sleid0r_wipe-barn-door-v</a>

.. |vqm| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionVqm/" target="_blank">vqm</a>

.. |frei0r.sleid0r_wipe-down| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_wipe-down/" target="_blank">frei0r.sleid0r_wipe-down</a>

.. |frei0r.sleid0r_wipe-left| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_wipe-left/" target="_blank">frei0r.sleid0r_wipe-left</a>

.. |frei0r.sleid0r_wipe-right| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_wipe-right/" target="_blank">frei0r.sleid0r_wipe-right</a>

.. |frei0r.sleid0r_wipe-up| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_wipe-up/" target="_blank">frei0r.sleid0r_wipe-up</a>


.. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   To be done

   :doc:`/effects_and_compositions/transitions/audio_mix`
   :doc:`/effects_and_compositions/transitions/burn`
   :doc:`/effects_and_compositions/transitions/cairo_affine_blend`
   :doc:`/effects_and_compositions/transitions/cairo_blend`
   :doc:`/effects_and_compositions/transitions/circle_wipe`
   :doc:`/effects_and_compositions/transitions/color_only`
   :doc:`/effects_and_compositions/transitions/composite_and_transform`
   :doc:`/effects_and_compositions/transitions/darken`
   :doc:`/effects_and_compositions/transitions/difference`
   :doc:`/effects_and_compositions/transitions/dissolve`
   :doc:`/effects_and_compositions/transitions/divide`
   :doc:`/effects_and_compositions/transitions/dodge`
   :doc:`/effects_and_compositions/transitions/grain_extract`
   :doc:`/effects_and_compositions/transitions/grain_merge`
   :doc:`/effects_and_compositions/transitions/hardlight`
   :doc:`/effects_and_compositions/transitions/horizontal__barn_door_wipe`
   :doc:`/effects_and_compositions/transitions/lighten`
   :doc:`/effects_and_compositions/transitions/luma`
   :doc:`/effects_and_compositions/transitions/matte`
   :doc:`/effects_and_compositions/transitions/multiply`
   :doc:`/effects_and_compositions/transitions/overlay`
   :doc:`/effects_and_compositions/transitions/push_down`
   :doc:`/effects_and_compositions/transitions/push_left`
   :doc:`/effects_and_compositions/transitions/push_right`
   :doc:`/effects_and_compositions/transitions/push_up`
   :doc:`/effects_and_compositions/transitions/rectangular_wipe`
   :doc:`/effects_and_compositions/transitions/saturation`
   :doc:`/effects_and_compositions/transitions/slide_down`
   :doc:`/effects_and_compositions/transitions/slide_left`
   :doc:`/effects_and_compositions/transitions/slide_right`
   :doc:`/effects_and_compositions/transitions/slide_up`
   :doc:`/effects_and_compositions/transitions/slide`
   :doc:`/effects_and_compositions/transitions/softlight`
   :doc:`/effects_and_compositions/transitions/subtract`
   :doc:`/effects_and_compositions/transitions/transform`
   :doc:`/effects_and_compositions/transitions/uv_map`
   :doc:`/effects_and_compositions/transitions/value`
   :doc:`/effects_and_compositions/transitions/vertical_barn_door_wipe`
   :doc:`/effects_and_compositions/transitions/video_quality_measurement`
   :doc:`/effects_and_compositions/transitions/wipe_down`
   :doc:`/effects_and_compositions/transitions/wipe_left`
   :doc:`/effects_and_compositions/transitions/wipe_right`
   :doc:`/effects_and_compositions/transitions/wipe_up`