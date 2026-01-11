.. meta::

   :description: Kdenlive Video Effects - Audio Spectrum Filter
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, on master, audio spectrum filter

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. .. versionadded:: 22.12


Audio Spectrum Filter
=====================

.. figure:: /images/effects_and_compositions/effects-audio_spectrum-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Audio Spectrum Filter

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      audiospectrum
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      Yes
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter is an audio visualization effect that draws an audio spectrum on the image. It can be :ref:`controlled directly on the monitor <ui-monitors_effect_direct_control>`.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Graph type
     - Selection
     - Select the type of graph to display the levels
   * - Fill
     - Switch
     - If checked, fills the area under the graph. Only applies to :guilabel:`Graph type` **Line**.
   * - Mirror
     - Switch
     - If checked, mirrors the spectrum on the center line of the rectangle
   * - Reverse
     - Switch
     - If checked, draws the points starting with the highest frequency
   * - Window size
     - Integer
     - The number of samples that the FFT\ [1]_ will be performed on. If :guilabel:`Window size` is less than the number of samples in a frame, extra samples will be ignored. If :guilabel:`Window size` is more than the number of samples in a frame, samples will be buffered from previous frames to fill the window. The buffering is performed as a sliding window so that the most recent samples are always transformed.
   * - Background Color
     - Picker
     - Defines the background color to be applied to the entire frame
   * - Foreground color
     - Picker
     - Defines the color of the waveform
   * - Line Thickness
     - Integer
     - Defines the thickness of the bar or line in number of pixels
   * - Angle
     - Integer
     - Defines the rotation angle to be applied to the waveform
   * - X / Y / W / H / Size / Opacity
     - 
     - Defines the X and Y coordinates, Width and Height, Size and Opacity of the rectangle in which the waveform is drawn. The icons help in lining up the rectangle.
   * - Line Tension
     - Integer
     - Affects the amount of curve in the line interpolating between points. **0** draws a straight line between points; **100** draws very curved lines between points. Values below **0** and above **100** will cause loops in the lines. Only applies to :guilabel:`Graph type` **Line**.
   * - Points
     - Integer
     - Defines the number of bands to draw in the spectrum. Each band shows up as a data point in the graph.
   * - Low Frequency
     - Integer
     - The low end of the frequency range to be used for the graph (:abbr:`Hz (Hertz)`)
   * - High Frequency
     - Integer
     - The high end of the frequency range to be used for the graph (:abbr:`Hz (Hertz)`)
   * - Level Threshold
     - Integer
     - The minimum amplitude of sound that must occur within the frequency range to cause the value to be applied (:abbr:`dB (decibel)`)

The following selection items are available:

:guilabel:`Graph type`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Line
     - 
   * - Bar
     - 


.. note:: 
   The effect is not updated in the Project Monitor during scrubbing. You need to play back the project to see this effect.

.. Tip:: 
   :guilabel:`Opacity` is fixed at 100%. You control the opacity/transparency of the effect by adjusting the alpha component of the :guilabel:`Foreground color`.


.. rubric:: Example

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-audio_spectrum_filter_example.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   
   Example of the Audio Spectrum Filter effect

* :guilabel:`Line Thickness` set to **4**

.. rst-class:: clear-both


----

.. [1] FFT := Fast Fourier Transform
