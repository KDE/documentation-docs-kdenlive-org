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
   :widths: 22 36 42
   :header-rows: 1
   :class: table-wrap

   * - Property
     - Keyword
     - Description
   * - Time code
     - #timecode#
     - SMPTE drop-frame timecode of the frame
   * - Frame number
     - #frame#
     - Frame number of the frame
   * - File name
     - #filename#
     - Name of the file including the file suffix (e.g. :file:`my_video.mp4`)
   * - Base name
     - #basename#
     - Name of the file without the file suffix (e.g. :file:`my_video`)
   * - Path
     - #resource#
     - Full path and filename (e.g. :file:`/path/to/my_video.mp4`)
   * - File date
     - #filedate#
     - Modification date of the file (GMT)
   * - Local file date
     - #localfiledate#
     - Modification date of the file (local)
   * - Frame rate
     - #meta.media.0.stream.frame_rate#
     - Frame rate of the source video
   * - Codec
     - #meta.media.0.codec.name#
     - Codec used in the source video
   * - Bit rate
     - #meta.media.0.codec.bit_rate#
     - Bit rate of the source video
   * - Width
     - #meta.media.width#
     - Width of the source video
   * - Height
     - #meta.media.height#
     - Height of the source video
   * - Comment
     - #meta.attr.comment.markup#
     - Comment embedded in the source video

The keywords can be selected from the drop-down list or entered directly in the text field.

Timecode keywords are based on the frame rate (fps) and position of the frame. Time-based keywords can include a ``strftime``\ [#]_ format string to customize the output as long as you put some delimiter except '#' between the keyword and the format string and the keyword comes first. For example, ``#localtime %I:%M:%S %p#`` shows only the time in 12-hour format. The '#' may be escaped with '\''.

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

   .. |tools-wizard| image:: /images/icons/tools-wizard.svg
   :width: 22px
   :class: no-scaled-link
