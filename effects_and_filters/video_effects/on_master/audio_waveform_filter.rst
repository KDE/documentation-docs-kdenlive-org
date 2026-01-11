.. meta::

   :description: Kdenlive Video Effects - Audio Waveform Filter
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, on master, audio waveform filter

.. metadata-placeholder

   :authors: - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. .. versionadded:: 22.12


Audio Waveform Filter
=====================

.. figure:: /images/effects_and_compositions/effects-audio_waveform-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Audio Waveform Filter

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      audiowaveform
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      Yes
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter is an audio visualization effect that draws an audio waveform on the image. It can be :ref:`controlled directly on the monitor <ui-monitors_effect_direct_control>`.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Fill
     - Switch
     - If checked the area below the line will be filled using the color specified with :guilabel:`Foreground Color`.
   * - Channel to draw
     - Selection
     - Defines which channels in the audio track to draw
   * - Background Color
     - Picker
     - Defines the background color to be applied to the entire frame
   * - Foreground Color
     - Picker
     - Defines the color of the waveform
   * - Line Thickness
     - Integer
     - Defines the thickness of the line in number of pixels
   * - Angle
     - Integer
     - Defines the rotation angle to be applied to the waveform
   * - X / Y / W / H / Size / Opacity
     - 
     - Defines the X and Y coordinates, Width and Height, Size and Opacity of the rectangle in which the waveform is drawn. The icons help lining up the rectangle. :guilabel:`Opacity` cannot be changed.


The following selection items are available:

:guilabel:`Channel to draw`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - All
     - default
   * - Merge
     - 
   * - 1 - 10
     - 


.. Tip:: 
   :guilabel:`Opacity` is fixed at 100%. You control the opacity/transparency of the effect by adjusting the alpha component of the :guilabel:`Foreground color`.


.. rubric:: Example

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-audio_waveform_filter_example.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   
   Example of the Audio Waveform Filter effect with default settings

..
