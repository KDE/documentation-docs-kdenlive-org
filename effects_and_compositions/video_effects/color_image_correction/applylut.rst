.. meta::

   :description: Do your first steps with Kdenlive video editor, using the apply LUT effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, apply LUT

   :authors: - Mmaguire (https://userbase.kde.org/User:Mmaguire)
             - Maris (https://userbase.kde.org/User:limerick)
             - Bernd Jordan

   :license: Creative Commons License SA 4.0

.. |freshLUTs| raw:: html

   <a href="https://freshluts.com/" target="_blank">freshluts.com</a>

.. |smallhd| raw:: html

   <a href="https://smallhd.com/blogs/community/movie-looks-download" target="_blank">smallhd.com</a>

.. |what_is_a_lut| raw:: html

   <a href="https://filmlifestyle.com/what-is-a-lut/" target="_blank">What is a LUT?</a>


.. _effects-apply_lut:

Apply LUT
=========

This effect applies a 3D Look Up Table (LUT)\ [1]_ to the clip. A LUT is an easy way to adjust the color tone of a video, and therefore is mostly used for color grading. It is important to note that if your clips do not match from clip to clip or shot to shot, is not properly exposed or not (yet) color corrected, that applying a LUT will not work the way one hoped it would.

**Supported formats:**

* .3dl (AfterEffects)
* .cube (Iridas)
* .dat (DaVinci)
* .m3d (Pandora)

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-apply_lut.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-apply_lut

   Apply LUT effect

* **LUT file to apply** - File containing the LUT to be applied. Select *Custom...* to open a file dialog window to browse for LUT files.

* **Interpolation Mode** - Select from Nearest, Trilinear or Tetrahedral (default)

.. rst-class:: clear-both

.. _effects-example_lut:

**LUT Filter Example**

For the example we are using the :download:`Tahoe.cube </files/Tahoe.cube>` LUT file. You can download LUTs from many places on the internet, like |freshLUTs| or |smallhd|. Put the downloaded files in a directory or folder that can be reached easily from with Kdenlive. For example, you may have a media stock folder and want to create a similar one for your LUT files.

This is the *after* and *before* view:

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-apply_lut_example_3.webp
   :width: 700px
   :figwidth: 700px
   :align: left
   :alt: kdenlive2304_effects-apply_lut_example_3

   Project Monitor showing the clip with LUT applied, Clip Monitor the unaltered clip

To apply the LUT follow these simple steps:

1. In the :guilabel:`Effects` tab open the *Color and Image Correction* category and select the *Apply LUT* effect. Assign it to the clip in the timeline
2. Open the :guilabel:`LUT file to apply` drop-down and select :guilabel:`Custom`
3. Navigate to the folder with the LUT file(s) you downloaded
4. Select the LUT file you want and click :guilabel:`Open`

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-apply_lut_example_1.webp
   :width: 700px
   :figwidth: 700px
   :align: left
   :alt: kdenlive2304_effects-apply_lut_example_1

   Apply LUT effect with default settings

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

   Apply LUT effect with Tahoe.cube LUT file applied

.. rst-class:: clear-both


Of course, you can add other effects from the *Color and Image Correction* category to further adjust or correct the colors. A good rule of thumb is "*less is more*".

You can find more about color correction and color grading in the Tutorial section of the documentation.

**Notes**

.. [1] A good explanation of and examples for how to use LUTs for color grading are available on the filmlifestyle.com |what_is_a_lut| page.
