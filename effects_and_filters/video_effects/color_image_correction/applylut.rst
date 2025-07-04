.. meta::

   :description: Kdenlive Video Effects - Apply LUT
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, apply LUT

   :authors: - Mmaguire (https://userbase.kde.org/User:Mmaguire)
             - Maris (https://userbase.kde.org/User:limerick)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. |freshLUTs| raw:: html

   <a href="https://freshluts.com/" target="_blank">freshluts.com</a>

.. |smallhd| raw:: html

   <a href="https://smallhd.com/blogs/community/movie-looks-download" target="_blank">smallhd.com</a>

.. |what_is_a_lut| raw:: html

   <a href="https://filmlifestyle.com/what-is-a-lut/" target="_blank">What is a LUT?</a>

.. |kde_store| raw:: html

   <a href="https://www.pling.com/browse?cat=644&ord=latest" target="_blank">KDE Store</a>


Apply LUT
=========

.. figure:: /images/effects_and_compositions/effects-apply_lut-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-apply_lut-2504.webp

.. sidebar:: |kdenlive-show-video| Apply LUT

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      lut3d
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect applies a 3D Look Up Table (LUT)\ [1]_ to the clip. A LUT is an easy way to adjust the color tone of a video, and therefore is mostly used for :term:`color grading`. It is important to note that if your clips do not match from clip to clip or shot to shot, are not properly exposed or not (yet) color corrected, applying a LUT will not work the way one hoped it would.

**Supported formats**

- .3dl (AfterEffects)
- .cube (Iridas)
- .dat (DaVinci)
- .m3d (Pandora)


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - LUT file to apply
     - File selection
     - File containing the LUT to be applied. Select **Custom...** to open a file dialog window to browse for additional LUT files. You can also download LUT files from the |kde_store| directly from here by clicking on the |edit-download| icon. See the `Notes <lut_notes>`_ section below.
   * - Interpolation Mode
     - Selection
     - Selects the mode for interpolation


The following selection items are available:

:guilabel:`Interpolation Mode`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Nearest
     - 
   * - Trilinear
     - 
   * - Tetrahedral
     - (default)

.. rst-class:: clear-both

.. _effects-example_lut:

.. rubric:: Example

For the example we are using the :download:`Tahoe.cube </files/Tahoe.cube>` LUT file. You can download LUTs from many places on the internet, like |freshLUTs| or |smallhd|. Put the downloaded files in a directory or folder that can be reached easily from within Kdenlive. For example, you may have a media stock folder and want to create a similar one for your LUT files.

This is the *after* and *before* view:

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-apply_lut_example_3.webp
   :width: 700px
   :figwidth: 700px
   :align: left
   :alt: kdenlive2304_effects-apply_lut_example_3

   Project Monitor showing the clip with LUT applied, Clip Monitor the unaltered clip

To apply the LUT follow these simple steps:

1. In the :guilabel:`Effects` tab open the **Color and Image Correction** category and select the **Apply LUT** effect. Assign it to the clip in the timeline
2. Open the :guilabel:`LUT file to apply` drop-down and select :guilabel:`Custom`
3. Navigate to the folder with the LUT file(s) you downloaded
4. Select the LUT file you want and click :guilabel:`Open`

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-apply_lut_example_1.webp
   :width: 700px
   :figwidth: 700px
   :align: left
   :alt: kdenlive2304_effects-apply_lut_example_1

   Apply LUT effect with default settings\ [2]_

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-apply_lut_example_2.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-apply_lut_example_2

   Apply LUT file selection dialog

Note that this example shows an individual video editing directory structure with a folder for stock media containing a folder for LUTs. Your mileage may vary ...

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-apply_lut_example_4.webp
   :width: 700px
   :figwidth: 700px
   :align: left
   :alt: kdenlive2304_effects-apply_lut_example_4

   Apply LUT effect with Tahoe.cube LUT file applied\ [2]_

.. rst-class:: clear-both


Of course, you can add other effects from the *Color and Image Correction* category to further adjust or correct the colors. A good rule of thumb is "*less is more*".

You can find more about color correction and color grading in the Tutorial section of the documentation.


.. _lut_notes:

.. rubric:: Notes

Kdenlive has a direct connection to the |kde_store| to download LUT files other users uploaded there. Of course it requires a working Internet connection.

Click on the |edit-download| icon and a window opens listing all available LUT files.

.. figure:: /images/effects_and_compositions/effects-apply_lut_store_1-2504.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: effects-apply_lut_store_1-2504.webp

   LUT files available in the |kde_store|

You can use filters (|view-filter|) to select all available LUTs, installed ones, and those for which an update is available.

Use |view-sort| to sort by name, rating, downloads (default), or release date.

Use the :kbd:`Search` field to search for a LUT file by name.

Click on :kbd:`Install` to install the selected LUT file(s).

Click on the highlighted tile to get more information about the selected LUT.

.. figure:: /images/effects_and_compositions/effects-apply_lut_store_2-2504.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: effects-apply_lut_store_2-2504.webp

   More details about the selected LUT

Here you see more details and some examples (provided the author has uploaded images).

Clicking the link opens a browser and the respective |kde_store| page for the LUT file. 

Click on :kbd:`Install` to download and install the selected LUT file.

.. rst-class:: clear-both


----

.. [1] A good explanation of and examples for how to use LUTs for color grading are available on the filmlifestyle.com |what_is_a_lut| page.

.. [2] The screenshot is showing the old effect/filter layout/design
