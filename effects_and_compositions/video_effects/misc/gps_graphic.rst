.. meta::

   :description: Do your first steps with Kdenlive video editor, using GPS graphic effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, misc, miscellaneous, GPS graphic

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |wiki_UTC| raw:: html

   <a href="https://en.wikipedia.org/wiki/Coordinated_Universal_Time" target="_blank">this article about UTC</a>


.. _effects-gps_graphic:

GPS Graphic
===========

This effect/filter overlays GPS-related graphics onto the video.

The effect has keyframes.

.. note:: This effect does not (yet) work. A bug report has been created to fix it.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-gps_graphic.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-gps_graphic

   GPS Graphic effect

* **Offset** - An offset (in seconds) to be added to the video file to match it to the GPS track. Most of the time this will at least need to be set to the timezone difference between the two files plus some seconds if the video recording device isn't precisely set to correct time. GPS time is always exact and in UTC\ [1]_. Use positive values if GPS is ahead of video and negative otherwise.

* **Smoothing level** - How many GPS points to smooth in order to eliminate GPS errors. A value of 1 does not smooth locations, it only calculates the extra fields (speed, distance, etc) it also interpolates missing values for heart rate and altitude.

* **Speed multiplier** - If the video file is a timelapse (or slow motion), use this value to set the speed up/slow down ratio. Sample values: 30 for 30x timelapse, 0.25 for 4x slow motion footage.

* **Graph data source** - What data from the GPS file is used for drawing: **0** = GPS location/track; **1** = altitude (if available); **2** = heart rate (if available); **3** = speed (always available, computed from location)

* **Graph type** - How to draw the selected data: **0** = a basic 2D map line (for location) or 1D graph per time (others); **1** = zooms in onto the map/graph and centers around the current location [2]_; **2** = draws a speedometer (available for all data sources but recommended only for speed; for the map type it represents the "percentage done" from trimmed start - end)

* **Trim start** - Trim data from the start of the GPS file (as a percentage of total). *Note*: both :guilabel:`Trim start` and :guilabel:`Trim end` are computed from the total file so trimming 50% start and 50% end will result in trimming the entire file.

* **Trim end** - Trim data from the end of the GPS file (as a reversed percentage of total, ie: 100 means no trim, 50 means half of total file, 5 means trim 95% of the file). *Note*: both :guilabel:`Trim start` and :guilabel:`Trim end` are computed from the total file so trimming 50% start and 50% end will result in trimming the entire file.

* **Crop mode horizontal** - Decides how to interpret the :guilabel:`Crop left` and :guilabel:`Crop right` values: **0** = a percentage from min..max; **1** = an absolute value (ie: it can crop between 22.2 and 22.3 degrees of longitude) [3]_

* **Crop left** - Crops data from the left side of the graph (effectively zooming in). The value is interpreted either as a percentage of total or an absolute value depending on :guilabel:`Crop mode horizontal`. In percentage mode the values are not restricted to 0-100 to allow for "zoom out" behaviour (ie: cropping -50 left will add an extra half of the total horizontal distance). Values over 100 (in % mode) will effectively not display anything. If :guilabel:`Graph type` is **speedometer**, all crop left/right values are ignored.

* **Crop right** - Same as :guilabel:`Crop left` but for the right side and percentage type is interpreted as an inverse percentage (ie: 100 = do not crop anything). Values under 0 will effectively not display anything.

* **Crop mode vertical** - Decides how to interpret the :guilabel:`Crop top` and :guilabel:`Crop bottom` values: **0** = a percentage from min..max; **1** = an absolute value (ie: it can zoom in to between 100 and 150m of altitude to show small changes in altitude between those 2 values better) [4]_

* **Crop bottom** - Crops data from the bottom side of the graph (effectively zooming in). The value is interpreted either as a percentage of total or an absolute value depending on :guilabel:`Crop mode vertical`. In percentage mode the values are not restricted to 0-100 to allow for "zoom out" behaviour (ie: cropping -50 bot will add an extra half of the total vertical distance to the bottom). Values over 100 (in % mode) will effectively not display anything. If :guilabel:`Graph type` is speedometer, this will set the minimum needle position which will clamp all values that are lower.

* **Crop top** - Same as :guilabel:`Crop bottom` but for the top side and percentage type is interpreted as an inverse percentage (ie: 100 = do not crop anything). Values under 0 will effectively not display anything.

* **Graph color style** - Chooses one of the 9 styles to draw the graph line:

  - 0 = one color -> same color and size for the entire graph
  - 1 = two colors -> same as 2 and 3 but the entire line is the same thickness
  - 2 = solid past, thin future -> from the beginning of the graph to the current position (="past") it will be drawn using the 1st color and chosen thickness, but for the "future" part of the graph it will use the 2nd color and thickness will be 2px (or 1px if main thickness is below 3)
  - 3 = solid future, thin past
  - 4 = vertical gradient -> the line will be coloured as a vertical gradient relative to the entire rect area
  - 5 = horizontal gradient
  - 6 = color by duration -> the selected colors will be used as a gradient, in chronological time (except for location source, this will effectively be a left to right gradient for 1D graphs)
  - 7 = color by altitude -> the selected colors will be used as a gradient from the minimum altitude value from file to the maximum one, not affected by crops or trim
  - 8 = color by heart rate
  - 9 = color by speed -> same as above but gradient is affected by smoothing

* **Show now dot** - Enable it to draw a disc at the current location/time over the graph line. If graph type is speedometer, this affects the needle.

* **Show now text** - Enable it to draw the current value in big white bold letters on the bottom right side of the rect. The legend_unit value will be appended at the end and it will be used as the current unit (if a valid unit is found ie: kilometers if "km" is found anywhere in the legend_unit string).

* **Rotation** - Rotate the entire graph rect. For speedometer type the text stays horizontal.

* **Thickness** - Sets the thickness of the line graph in px

* **Draw legend** - If enabled it will draw 5 horizontal (and vertical for map type) lines with small values each corresponding to the current data source value at 0%, 25%, 50%, 75% and 100% of current graph shown, affected by the legend_unit type if applicable and with the string appended to the value. For speedometer type this shows division values (but without appending unit).

* **Show dots only** - If enabled the graph will be drawn using individual dots instead of lines. This will effectively show the individual data points as affected by smoothing (ie: for location data it will display each GPS fix if smoothing is 1) and can either be used as a cool effect when zoomed in enough or to debug unexpected line jumps.

* **Background scale** - Scale the background image (relative to center) to match it to the above GPS track. Values smaller than 1 zoom into the image, values larger than 1 zoom out. 0 hides it.

* **Background opacity** - Sets the opacity of the background image

* **Colours** - Sets the colours of the graph line

* **Now dot colour** - Choose the outer circle color of the now_dot disc. The size of this circle is the same as the line thickness. The inside of the disc is always white. If the alpha value of the color is 0 (default) this will use the same colour as the nearby (or past) line (including for gradient types) thus effectively making it change color in time.

.. rst-class:: clear-both


**Notes**

.. [1] UTC is short for Coordinated Universal Time and is the primary time standard by which the world regulates clocks and time. See |wiki_UTC| on Wikipedia for more details.

.. [2] Note: for type 1 (follow centered dot): (a) crop values are only valid as a percentage and only the bottom (resp left) values will be taken into consideration as both values (ie: bot/top) will need to be equal to keep the dot centered; (b) if data source is not GPS location, the centering will only be done for horizontal axis (time), vertical axis crop will behave just like for the type 0 (it will statically keep the same min/max limit allowing the now_dot to move up and down).

.. [3] Note: for the horizontal type, absolute values are the longitude (for the location source type) and time (in milliseconds since epoch) for the rest of the data source types.

.. [4] Note: for the vertical type, absolute values are latitude degrees (for the location source type) and altitude, heart rate, speed for the others interpreted as the legend_unit type where applicable (ie: a value of 10 for altitude will be considered meters by default but if changing legend_unit to feet it will mean 10 feet).


.. Differences to the MLT documentation:

   * **GPS File/URL** - The full path of file containing location (GPS) data. Supported extensions: .gpx, .tcx.

   * **Crop top / bottom** are called Crop right / left

   * **Colours** - filter seems to support multiple colour: Multiple colours can be specified with incrementing suffixes to cause the line to be drawn in a specific way (ie: gradient or past/future). By default, the filter has 5 colors (blue, green, yellow, orange, red):
      color.1 = #ff00aaff
      color.2 = #ff00e000
      color.3 = #ffffff00
      color.4 = #ffff8c00
      color.5 = #ffff0000
   A color value is a hexadecimal representation of RGB plus alpha channel as 0xrrggbbaa. Colors can also be the words: white, black, red, green, or blue. You can also use a HTML-style color values #rrggbb or #aarrggbb.

   * **Legend unit** - Sets the unit to be used for displaying values of type altitude and speed. Default is meters and km/h respectively. The unit is matched anywhere in the string so extra spaces can be used to tweak displaying. Supported formats, distance: m|meter, km|kilometer, mi|mile, ft|feet, nm|nautical*; speed: ms|m/s|meter, km|km/h|kilometer, mi|mi/h|mile, ft|ft/s|feet, kn|nm/h|knots.

   * **Rectangle** - Defines the rectangle that the graph should be drawn in. Format is: "X Y W H". X, Y, W, H are assumed to be pixel units unless they have the suffix '%'.

   * **Background image** - If a valid image file is selected it will be used as a background for the rect area. Paths starting with the "!" character are ignored. TIP: use a map image to add context to the GPS track.

   * **GPS start time** - Date and time of the first valid GPS point

   * **Video start time** - Date and time of the video file

   * **Auto offset start** - Provides a helper offset to guarantee start of video file syncs with the start of GPS file. Correctly sets the offset if video file and GPS recording was started at the same time.

   * **Auto offset now** - Provides a helper offset to sync the first GPS point to current video time (it is updated every second). Correctly sets the offset if you video record the moment GPS starts.

   * **Map hint** - Returns the middle lat, lon coordinates of the GPS file
