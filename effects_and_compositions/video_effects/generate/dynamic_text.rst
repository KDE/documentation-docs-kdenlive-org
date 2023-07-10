.. meta::

   :description: Do your first steps with Kdenlive video editor, using draw grid effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, generate, draw grid

.. metadata-placeholders

   :authors: - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-dynamic_text:

Dynamic Text
============

This effect allows you to overlay specific keywords to the image source, for example the timecode that counts up relative to the start of the clip or the track it is applied to, respectively.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-dynamic_text.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-dynamic_text

   Dynamic Text effect

* **Font Family / Size / Weight** - Select the font and its attributes for the text. **Font Weight** seems to behave differently depending on the selected font family.

* **Outline Width** - Set the width of the outline in pixels to 0, 1, 2 or 3

* **Padding** - The number of pixels to pad the background rectangle beyond the edges of text

* **Horizontal / Vertical Alignment** - Set the horizontal and vertical alignment within the geometry rectangle

* **Text** - What will be displayed as the overlay. You can add any other text between keywords.

* **<Select a Keyword>** - Select the keywords to add to the text field

* **X / Y / W / H / Size / Opacity** - X and Y coordinates, Width and Height, Size and Opacity of the overlay rectangle. You can use these parameters to fine tune the position, size and :term:`opacity` of the overlay.

* **Foreground / Background / Outline Color** - Specify the colors for the text, the background rectangle defined by :guilabel:`Padding` and the outline color (if :guilabel:`Outline Width` is greater than 0).

.. rst-class:: clear-both


The following keywords are available:

.. list-table::
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

Timecode keywords are based on the frame rate (fps) and position of the frame. Time-based keywords can include a ``strftime`` format string to customize the output as long as you put some delimiter except '#' between the keyword and the format string and the keyword comes first. For example, ``#localtime %I:%M:%S %p#`` shows only the time in 12-hour format. The '#' may be escaped with '\'.

.. note:: This effect uses the clip's properties for the calculation of the keywords' values. For example, **#timecode#** will start counting at the beginning of the clip and not at the position of the clip in the timeline. **#timecode#** will reset at the start of every clip it is assigned to. In order to have **#timecode#** count across the whole length of your project you must assign it to the (main) video track.

See also the :ref:`render` option in the render dialog to add time code or frame count to the entire rendered project.

.. hint:: In order to use a semi-transparent background color, click on the color panel, click on :guilabel:`+` and use the horizontal slider to change the transparency.

.. hint:: You can add effects to entire video tracks by clicking on |tools-wizard| icon in the track header and choosing :menuselection:`Menu --> Timeline --> Add Effect`. Video tracks that have effects added to them have the white |tools-wizard|, tracks without have a grey |tools-wizard| icon. See also :ref:`effects-track_effect`.
