.. meta::

   :description: Kdenlive Video Effects - Audio Level Visualization
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, on master, audio level visualization

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. .. versionadded:: 22.12


Audio Level Visualization Filter
================================

.. figure:: /images/effects_and_compositions/effects-audio_level_visualization-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-audio_level_visualization-2504.webp

.. sidebar:: |kdenlive-show-video| Audio Level Visualization Filter

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      audiolevelgraph
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      Yes
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter is an audio visualization effect that draws an audio level meter on the image. It can be :ref:`controlled directly on the monitor <ui-monitors_effect_direct_control>`.


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
   * - Mirror
     - Switch
     - If checked, mirrors the spectrum on the center line of the rectangle
   * - Reverse
     - Switch
     - If checked, draws the points starting with the right channel
   * - Gradient Orientation
     - Selection
     - Sets the direction of the color gradient
   * - Background Color
     - Picker
     - Defines the background color to be applied to the entire frame
   * - Gradient Color 1 / 2 / 3
     - Picker
     - Defines color of the waveform gradient. Color 1 defines the top, 2 the middle and 3 the bottom of the gradient
   * - Line Thickness
     - Integer
     - Defines the thickness of the bar or segments in number of pixels
   * - Angle
     - Integer
     - Defines the rotation angle to be applied to the waveform
   * - X / Y / W / H / Size / Opacity
     - 
     - Defines the X and Y coordinates, Width and Height, Size and Opacity of the rectangle in which the waveform is drawn. The icons help lining up the rectangle.
   * - Channels
     - Integer
     - Defines the number of channels to show
   * - Segment Gap
     - Integer
     - Defines the space in pixels between segments

The following selection items are available:

:guilabel:`Graph type`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Bar
     - Default
   * - Segment
     - 


:guilabel:`Gradient Orientation`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Vertical
     - Default
   * - Horizontal
     - 


.. rubric:: Example

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-audio_level_visualization_filter_example.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-audio_level_visualization_filter_example

   Example of the Audio Level Visualization Filter effect

* :guilabel:`Line Thickness` set to **8**

* :guilabel:`Gradient Color 1 / 2 / 3` set to different colors for demonstration purposes
