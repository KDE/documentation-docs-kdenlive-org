.. meta::

   :description: Kdenlive Video Effects - GPS Text
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, generate, gps_text

.. metadata-placeholders

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


GPS Text
========

.. figure:: /images/effects_and_compositions/effects-gps_text-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| GPS Text

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      MLT
   :**Source filter**:
      gpstext
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter overlays GPS-related text onto the image source. **GPS Text** will search for keywords in the text to be overlaid and will replace those keywords on a frame-by-frame basis. It is based on the :doc:`/effects_and_filters/video_effects/generate/dynamic_text` effect/filter.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Text
     - String
     - The text to be displayed. You can add any other text between keywords.
   * - <select a keyword>
     - Selection
     - Select the keyword to add to the :guilabel:`Text` field. Keywords must be enclosed in '#'.
   * - GPS File
     - File
     - The full path of file containing location (GPS) data. Supported extensions are ``.gpx`` and ``.tcx``.
   * - Time offset in seconds
     - Integer
     - An offset to be added to the video file to match it to the GPS track. Most of the time this will at least need to be set to the timezone difference between the two files plus some seconds if the video recording device is not precisely set to the correct time. GPS time is always exact and in UTC\ [#]_. Use positive values if GPS is ahead of video, and negative otherwise.
   * - Smoothing level
     - Integer
     - Determines how many GPS points to smooth in order to eliminate GPS errors. A value of 0 only exposes the raw values from the file. A value of 1 does not smooth locations, it only calculates the extra fields (speed, distance, etc) it also interpolates missing values for **heart rate** and **altitude**.
   * - Updates per second
     - Integer
     - Controls how many times per second the GPS text is updated on video (interpolated). A value of 0 will only update text when a real GPS point has been recorded.

.. rst-class:: clear-both


The following keywords are available:

.. list-table::
   :width: 100%
   :widths: 30 70
   :class: table-wrap

   * - GPS latitude
     - the GPS latitude value
   * - GPS longitude
     - the GPS longitude value
   * - GPS altitude
     - the GPS altitude or elevation value
   * - GPS speed
     - GPS speed
   * - distance so far
     - Total distance so far
   * - date and time of current GPS point
     - date and time of current GPS point shown
   * - date and time of current frame in video file
     - date and time of current frame in video file
   * - heart rate
     - heart rate (if present in GPS file)
   * - current GPS_bearing
     - current GPS bearing (degrees 0-360)
   * - current GPS direction
     - current GPS direction (8 divisions: N, NE, E, etc)
   * - GPS altitude gain so far
     - total GPS altitude gain so far
   * - GPS altitude loss so far
     - total GPS altitude loss so far
   * - distance travelled uphill
     - total distance travelled uphill so far
   * - distance travelled downhill
     - total distance travelled downhill so far
   * - distance travelled on flat area
     - total distance travelled on flat area so far

Time-based keywords can include a ``strftime``\ [#]_ format string to customize the output and a number (representing seconds) preceded by '+' or '-' which will offset the actual time. For example, ``#gps_datetime_now %I:%M:%S %p +3600#`` shows only the time in 12-hour format, offset by 1 hour.

Speed and distance keywords may include an extra format keyword to convert the value to metric/imperial units. Default is meters and km/h respectively.

Supported formats:

* Distance: **m**\|\ **meter**, **km**\|\ **kilometer**, **mi**\|\ **mile**, **ft**\|\ **feet**, **nm**\|\ **nautical**
* Speed: **ms**\|\ **m/s**\|\ **meters**, **km**\|\ **km/h**\|\ **kilo**, **mih**\|\ **mi/h**\|\ **mileh**, **fts**\|\ **ft/s**\|\ **feet**, **kn**\|\ **nm/h**\|\ **knots**.

.. from the mlt filter page: Computed values are calculated since beginning of GPS file or since "gps_processing_start_time" property, if set.

The '#' may be escaped with '\\'.


----

.. |wiki_UTC| raw:: html

   <a href="https://en.wikipedia.org/wiki/Coordinated_Universal_Time" target="_blank">this article about UTC</a>

.. |possible_formats| raw:: html

   <a href="https://strftime.org/" target="_blank">possible formats</a>


.. [#] UTC is short for Coordinated Universal Time and is the primary time standard by which the world regulates clocks and time. See |wiki_UTC| on Wikipedia for more details.

.. [#] See this list of |possible_formats|.
