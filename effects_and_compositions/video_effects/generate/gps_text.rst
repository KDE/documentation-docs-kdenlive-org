.. meta::

   :description: Do your first steps with Kdenlive video editor, using gps_text effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, generate, gps_text

.. metadata-placeholders

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |wiki_UTC| raw:: html

   <a href="https://en.wikipedia.org/wiki/Coordinated_Universal_Time" target="_blank">this article about UTC</a>


.. _effects-gps_text:

GPS Text
========

This effect/filter overlays GPS-related text onto the image source. **GPS Text** will search for keywords in the text to be overlaid and will replace those keywords on a frame-by-frame basis. It is based on the :ref:`effects-dynamic_text` effect/filter.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-gps_text.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-gps_text

   GPS Text effect

* **Text** - The text to be displayed. You can add any other text between keywords.

* **<select a keyword>** - Select the keyword to add to the :guilabel:`Text` field. Keywords must be enclosed in '#'.

* **GPS File** - The full path of file containing location (GPS) data. Supported extensions are ``.gpx`` and ``.tcx``.

* **Time offset in seconds** - An offset to be added to the video file to match it to the GPS track. Most of the time this will at least need to be set to the timezone difference between the two files plus some seconds if the video recording device is not precisely set to the correct time. GPS time is always exact and in UTC\ [1]_. Use positive values if GPS is ahead of video, and negative otherwise.

* **Smoothing level** - Determines how many GPS points to smooth in order to eliminate GPS errors. A value of 0 only exposes the raw values from the file. A value of 1 does not smooth locations, it only calculates the extra fields (speed, distance, etc) it also interpolates missing values for **heart rate** and **altitude**.

* **Updates per second** - Controls how many times per second the GPS text is updated on video (interpolated). A value of 0 will only update text when a real GPS point has been recorded.

.. rst-class:: clear-both


The following keywords are available:

.. list-table::
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

Time-based keywords can include a ``strftime`` format string to customize the output and a number (representing seconds) preceeded by '+' or '-' which will offset the actual time. For example, ``#gps_datetime_now %I:%M:%S %p +3600#`` shows only the time in 12-hour format, offset by 1 hour.

Speed and distance keywords may include an extra format keyword to convert the value to metric/imperial units. Default is meters and km/h respectively.

Supported formats:

* Distance: m|meter, km|kilometer, mi|mile, ft|feet, nm|nautical
* Speed: ms|m/s|meter, km|km/h|kilo, mi|mi/h|mile, ft|ft/s|feet, kn|nm/h|knots.

.. from the mlt filter page: Computed values are calculated since beginning of GPS file or since "gps_processing_start_time" property, if set.

The '#' may be escaped with '\\'.


**Notes**

.. [1] UTC is short for Coordinated Universal Time and is the primary time standard by which the world regulates clocks and time. See |wiki_UTC| on Wikipedia for more details.
