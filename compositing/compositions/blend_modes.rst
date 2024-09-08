.. meta::
   :description: Kdenlive Documentation - Compositing: Composition Blend Modes
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, compositing, composition, compositions, blend, modes

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _compositions-blend_modes:

Composition Blend Modes
=======================

For Kdenlive, some composition types are basically :doc:`blending modes </compositing/blending_modes>` (see there for a detailed description).

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/compositions-blend_modes-timeline.gif
      :width: 360px
      :figwidth: 360px
      :align: left

      Changing the composition **Blend Mode**

   You can change the **Blend Mode** by selecting from the :guilabel:`Composition Type` drop-down list.

.. rst-class:: clear-both

The following table below lists the composition types and their blending mode counterpart in :guilabel:`Composition Type` **Cairo Blend**:

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 30 30 40
   :class: table-wrap

   * - Composition Type
     - Example
     - Blending Mode
   * - .. _addition_addition-alpha:
   
       | Addition /
       | addition_alpha
     - .. image:: /images/effects_and_compositions/composition_method-addition.webp
     - | Add
       | Perform an RGB[A] addition or addition_alpha operation of the pixel sources (|frei0r.addition| and |frei0r.addition_alpha|, respectively)
   * - .. _burn:
   
       Burn
     - .. image:: /images/effects_and_compositions/composition_method-burn.webp
     - | Color Burn
       | Perform an RGB[A] dodge operation between the pixel sources\ [1]_ (|frei0r.burn|)
   * - .. _color-only:
   
       Color Only
     - .. image:: /images/effects_and_compositions/composition_method-color_only.webp
     - | No equivalent
       | Perform a conversion to color only of the source input 1 using the hue and saturation values of input 2 (|frei0r.color_only|)
   * - .. _darken:
   
       Darken
     - .. image:: /images/effects_and_compositions/composition_method-darken.webp
     - | Darken
       | Perform a darken operation between two sources (minimum value for both sources) (|frei0r.darken|)
   * - .. _difference:
   
       Difference
     - .. image:: /images/effects_and_compositions/composition_method-difference.webp
     - | Difference
       | Perform an RGB[A] difference operation between the pixel sources. (|frei0r.difference|)
   * - .. _divide:
   
       Divide
     - .. image:: /images/effects_and_compositions/composition_method-divide.webp
     - | No equivalent
       | Perform an RGB[A] divide operation between the pixel sources\ [2]_ (|frei0r.divide|)
   * - .. _dodge:
   
       Dodge
     - .. image:: /images/effects_and_compositions/composition_method-dodge.webp
     - | Color Dodge
       | Perform an RGB[A] dodge operation between the pixel sources\ [3]_ (|frei0r.dodge|)
   * - .. _grain-extract:
   
       Grain Extract
     - .. image:: /images/effects_and_compositions/composition_method-grain_extract.webp
     - | No equivalent
       | Perform an RGB[A] grain-extract operation between the pixel sources (|frei0r.grain_extract|)
   * - .. _grain-merge:
   
       Grain Merge
     - .. image:: /images/effects_and_compositions/composition_method-grain_merge.webp
     - | No equivalent
       | Perform an RGB[A] grain-merge operation between the pixel sources (|frei0r.grain_merge|)
   * - .. _hardlight:
   
       Hardlight
     - .. image:: /images/effects_and_compositions/composition_method-hardlight.webp
     - | Hard light
       | Perform an RGB[A] hardlight operation between the pixel sources (|frei0r.hardlight|)
   * - .. _hue:
   
       Hue
     - .. image:: /images/effects_and_compositions/composition_method-hue.webp
     - | HSL hue
       | Perform a conversion to hue only of the source input1 using the hue of input2 (|frei0r.hue|)
   * - .. _lighten:
   
       Lighten
     - .. image:: /images/effects_and_compositions/composition_method-lighten.webp
     - | Lighten
       | Perform a lighten operation between two sources (maximum value of both sources) (|frei0r.lighten|)
   * - .. _multiply:
   
       Multiply
     - .. image:: /images/effects_and_compositions/composition_method-multiply.webp
     - | Multiply
       | Perform an RGB[A] multiply operation between the pixel sources (|frei0r.multiply|)
   * - .. _overlay:
   
       Overlay
     - .. image:: /images/effects_and_compositions/composition_method-overlay.webp
     - | Overlay
       | Perform an RGB[A] overlay operation between the pixel sources\ [4]_ (|frei0r.overlay|)
   * - .. _saturation:
   
       Saturation
     - .. image:: /images/effects_and_compositions/composition_method-saturation.webp
     - | HSL saturation
       | Perform a conversion to saturation only of the source input1 using the saturation level of input2 (|frei0r.saturation|)
   * - .. _screen:
   
       Screen
     - .. image:: /images/effects_and_compositions/composition_method-screen.webp
     - | Screen
       | Perform an RGB[A] screen operation between the pixel sources\ [5]_ effectively using black as the alpha channel (|frei0r.screen|)
   * - .. _softlight:
   
       Softlight
     - .. image:: /images/effects_and_compositions/composition_method-softlight.webp
     - | Soft light
       | Perform an RGB[A] softlight operation between the pixel sources (|frei0r.softlight|)
   * - .. _subtract:
   
       Subtract
     - .. image:: /images/effects_and_compositions/composition_method-subtract.webp
     - | No equivalent
       | Perform an RGB[A] subtract operation of the pixel source input2 from input1 (|frei0r.subtract|)


----

.. [1] It uses the generalized algorithm: :code:`D = saturation of 255 or depletion of 0, of ((255-A)*256) / (b+1)`

.. [2] Input 1 is the numerator, input 2 the denominator

.. [3] It uses the generalized algorithm: :code:`D = saturation of 255 or (A*256)/(256-B)`

.. [4] It uses using the generalized algorithm: :code:`D = A * (B + (2 * B) * (255 - A))`

.. [5] It uses using the generalized algorithm: :code:`D = 255 - (255 - A) * (255 - B)` 


.. ===========================================================================
   Link list

.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Compositions
   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. |frei0r.addition| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-addition/" target="_blank">frei0r.addition</a>

.. |frei0r.addition_alpha| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-addition_alpha/" target="_blank">frei0r.addition_alpha</a>

.. |frei0r.burn| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-burn/" target="_blank">frei0r.burn</a>

.. |frei0r.cairoaffineblend| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-cairoaffineblend/" target="_blank">frei0r.cairoaffineblend</a>

.. |frei0r.cairoblend| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-cairoblend/" target="_blank">frei0r.cairoblend</a>

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

.. |frei0r.saturation| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-saturation/" target="_blank">frei0r.saturation</a>

.. |frei0r.screen| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-screen/" target="_blank">frei0r.screen</a>

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
