.. meta::

   :description: Kdenlive Video Effects - Dynamic Text
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, generate, draw grid

.. metadata-placeholders

   :authors: - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             - Eugen Mohr

   :license: Creative Commons License SA 4.0


Dynamic Text
============

.. figure:: /images/effects_and_compositions/effects-dynamic_text-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-dynamic_text-2504.webp

.. sidebar:: |kdenlive-show-video| Dynamic Text

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      dynamictext
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect allows you to overlay specific keywords to the image source, for example the timecode that counts up relative to the start of the clip or the track it is applied to, respectively. It can be :ref:`controlled directly on the monitor <ui-monitors_effect_direct_control>`.

.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Font Family / Size / Weight
     - Selection / Integer
     - Select the font and its attributes for the text. **Font Weight** seems to behave differently depending on the selected font family.
   * - Outline Width
     - Integer
     - Set the width of the outline in pixels to 0, 1, 2 or 3
   * - Padding
     - Integer
     - The number of pixels to pad the background rectangle beyond the edges of text
   * - Horizontal / Vertical Alignment
     - Selection
     - Set the horizontal and vertical alignment within the geometry rectangle
   * - Text
     - String
     - What will be displayed as the overlay. You can add any other text between keywords.
   * - <Select a Keyword>
     - Selection
     - Select the keywords to add to the text field
   * - X / Y / W / H / Size / Opacity
     - 
     - X and Y coordinates, Width and Height, Size and Opacity of the overlay rectangle. You can use these parameters to fine tune the position, size and :term:`opacity` of the overlay.
   * - Foreground / Background / Outline Color
     - Picker
     - Specify the colors for the text, the background rectangle defined by :guilabel:`Padding` and the outline color (if :guilabel:`Outline Width` is greater than 0).


The following selection items are available:

:guilabel:`Horizontal Alignment` :guilabel:`Vertical Alignment`

.. list-table::
   :width: 100%
   :widths: 22 78
   :class: table-wrap

   * - Left
     - Default
   * - Center
     - 
   * - Right
     - 


.. rst-class:: clear-both


The following keywords are available:

.. list-table::
   :width: 100%
   :widths: 22 78
   :class: table-wrap

   * - timecode
     - SMPTE drop-frame timecode of the frame
   * - frame
     - frame number of the frame
   * - file date
     - modification date of the file (GMT)
   * - local file date
     - modification date of the file (local)
   * - source frame rate
     - frame rate of the source video
   * - source codec
     - codec used in the source video
   * - source bit rate
     - bit rate of the source video
   * - source width
     - width of the source video
   * - source height
     - height of the source video
   * - source comment
     - comment embedded in the source video

Timecode keywords are based on the frame rate (fps) and position of the frame. Time-based keywords can include a ``strftime``\ [#]_ format string to customize the output as long as you put some delimiter except '#' between the keyword and the format string and the keyword comes first. For example, ``#localtime %I:%M:%S %p#`` shows only the time in 12-hour format. The '#' may be escaped with '\'.

.. note:: 
  This effect uses the clip's properties for the calculation of the keywords' values. For example, **#timecode#** will start counting at the beginning of the clip and not at the position of the clip in the timeline. **#timecode#** will reset at the start of every clip it is assigned to. In order to have **#timecode#** count across the whole length of your project you must assign the effect to the (main) video track or the Master.

.. seealso::
  :ref:`Render` option in the render dialog to add time code or frame count to the entire rendered project.

.. hint:: 
  In order to use a semi-transparent background color, click on the color panel, click on :guilabel:`+` and use the horizontal slider to change the transparency.

.. hint:: 
  You can add effects to entire video tracks by clicking on the |tools-wizard| icon in the track header and choosing :menuselection:`Menu --> Sequence --> Add Effect`. Video tracks that have effects added to them have the white |tools-wizard|, tracks without have a grey |tools-wizard| icon. See also :ref:`effects-track_effect`.


----

.. |possible_formats| raw:: html

   <a href="https://strftime.org/" target="_blank">possible formats</a>


.. [#] See this list of |possible_formats|.


.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Icons used here (remove comment indent to enable them for this document)
   
   .. |linux| image:: /images/icons/linux.png
   :width: 14px
   :alt: Linux
   :class: no-scaled-link

   .. |appimage| image:: /images/icons/kdenlive-appimage_3.svg
   :width: 14px
   :alt: appimage
   :class: no-scaled-link

   .. |windows| image:: /images/icons/windows.png
   :width: 14px
   :alt: Windows
   :class: no-scaled-link

   .. |apple| image:: /images/icons/apple.png
   :width: 14px
   :alt: MacOS
   :class: no-scaled-link

   .. |tools-wizard| image:: /images/icons/tools-wizard.svg
   :width: 22px
   :class: no-scaled-link
