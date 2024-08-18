.. meta::
   :description: Kdenlive Documentation - Compositing: Masking
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, compositing, masking

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |google_search| raw:: html

   <a href="https://www.google.com/search?q=background+remover+free" target="_blank">Google search</a>

.. |roto_mask| image:: /images/effects_and_compositions/transitions_and_compositions-masking-rotoscoping_mask.webp
   :width: 200px


Masking
=======

You create a mask with one of these effects:

* :doc:`Alpha Shapes </effects_and_filters/video_effects/alpha_mask_keying/alpha_shapes>` and :doc:`Alpha Shapes (Mask) </effects_and_filters/video_effects/alpha_mask_keying/alpha_shapes_mask>`
* :doc:`Rectangular Alpha Mask </effects_and_filters/video_effects/alpha_mask_keying/rectangular_alpha_mask>`
* :doc:`Rotoscoping </effects_and_filters/video_effects/alpha_mask_keying/rotoscoping>` and :doc:`Rotoscoping (Mask) </effects_and_filters/video_effects/alpha_mask_keying/rotoscoping_mask>`
* :doc:`Shape Alpha</effects_and_filters/video_effects/alpha_mask_keying/shape_alpha>` and :doc:`Shape Alpha (Mask)</effects_and_filters/video_effects/alpha_mask_keying/shape_alpha_mask>`

.. note:: The effects with *(Mask)* in the name need to be used in conjunction with **Mask Apply** to work. It allows to apply other effects and filters only to the masked area (can also be inverted to apply to everything but the masked area). The effects without *(Mask)* simply create an alpha channel to allow clips on lower tracks to show through.

.. rubric:: Steps to create a mask

#. Depending on your use case apply one of the masking effects.

   :Alpha Shapes:
      Creates a rectangle, ellipse, triangle, and diamond shape that can be adjusted in position, size, rotation, and :abbr:`feathering (Smoothing or blurring the edges of a feature)`. For illustration purposes, :guilabel:`Operation` **Subtract** has been selected.

      .. list-table:: 
         :widths: 25 25 25 25

         * - .. image:: /images/effects_and_compositions/masking-alpha_shapes_rec.webp
           - .. image:: /images/effects_and_compositions/masking-alpha_shapes_ell.webp
           - .. image:: /images/effects_and_compositions/masking-alpha_shapes_tri.webp
           - .. image:: /images/effects_and_compositions/masking-alpha_shapes_dia.webp

   :Rectangular Alpha Mask:
      Is a simple mask whose edges are defined in number of pixels from the edge of the frame.

   :Rotoscoping:
      Is best suited for complex shapes, for example when persons or animals or other irregular objects need to be masked.

   :Shape Alpha:
      Allows to use an image or video to be used as a mask. The resource must have an alpha channel. This is particular useful for using masks created by online background removal service like those from a |google_search|. 

#. Adjust the mask to your needs

   .. container:: clear-both

      .. figure:: /images/effects_and_compositions/transitions_and_compositions-masking-rotoscoping.gif
         :width: 360px
         :figwidth: 360px
         :align: left

         Rotoscoping (click to enlarge)

      In this example the jumping person shall be composited into the scene with the road. For this complex shape the :doc:`/effects_and_filters/video_effects/alpha_mask_keying/rotoscoping` effect is best. It creates a mask\ [1]_ outside the shape. Using the :guilabel:`Alpha Operation` the mask can be inverted.

   .. rst-class:: clear-both

   .. container:: clear-both

      .. figure:: /images/effects_and_compositions/masking-adjust_alpha_shapes_mask.webp
         :width: 360px
         :figwidth: 360px
         :align: left

         An Alpha Shapes (Mask) applied

      In this example the alpha shape rectangle has been adjusted in size, position, and transition width to cover the house in the middle. For better adjustment, :guilabel:`Operation` has been set to **Write on clear**. For the mask to work (protecting the masked area) :guilabel:`Operation` must be set to **Subtract**.

   .. rst-class:: clear-both

#. Apply the desired effect(s) to the clip and adjust as needed

   .. container:: clear-both

      .. figure:: /images/effects_and_compositions/masking-adjust_alpha_shapes_mask_gblur.webp
         :width: 360px
         :figwidth: 360px
         :align: left

         Gaussian Blur effect applied

      This will blur the rest of the image but not the part covered by the mask.

   .. rst-class:: clear-both

   .. container:: clear-both

      .. figure:: /images/effects_and_compositions/masking-adjust_alpha_shapes_mask_bw0r.webp
         :width: 360px
         :figwidth: 360px
         :align: left

         bw0r effect (b&w) applied

      This will make the rest of the image black and white but not the part covered by the mask.

   .. rst-class:: clear-both

#. Add the :doc:`Mask Apply </effects_and_filters/video_effects/alpha_mask_keying/mask_apply>` effect to the clip

   .. container:: clear-both

      .. figure:: /images/effects_and_compositions/masking-adjust_alpha_shapes_mask_result.webp
         :width: 360px
         :figwidth: 360px
         :align: left

         Result of the mask

      The masked area is protected from the effects of the two effects/filters. In this example the house in the middle stands out and is in focus.

      To adjust for camera movement, you can use keyframes in the **Mask** effect to change position, size, rotation, and other parameters.

   .. rst-class:: clear-both


You can repeat this as often as needed for the same clip or add other effects after the **Mask Apply** for affecting the entire clip.

.. rubric:: Other Examples

This is an example for using :doc:`rotoscoping </effects_and_filters/video_effects/alpha_mask_keying/rotoscoping_mask>` with keyframes to highlight an object in a video:

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/transitions_and_compositions-masking-rotoscoping_2.gif
      :width: 360px
      :figwidth: 360px
      :align: left

      Rotoscoping Mask with keyframes

   The :doc:`/effects_and_filters/video_effects/color_image_correction/colorize` effect was used to highlight the masked area.

.. rst-class:: clear-both


----

.. [1] This is the mask that the rotoscoping effect creates:

   |roto_mask|

   The black areas are now the alpha channel, allowing the clip in the track below to show through.