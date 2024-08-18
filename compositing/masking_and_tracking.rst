.. meta::
   :description: Kdenlive Documentation - Compositing: Masking and Tracking
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, compositing, masking, tracking

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



Masking and Tracking
====================

Compositing in video editing or film making often involves making certain parts of a clip transparent or cover it (making it obscure), as well as track objects. :abbr:`VFX(Visual Effects)` are unthinkable without these techniques.

Kdenlive has limited but nonetheless powerful features for masking and tracking. For more elaborate effects they can be combined, for example a clip can be superimposed on a framed picture on a wall in another clip giving the impression it is played withing the picture frame, and that even though the camera is moving along that wall. This requires a lot of manual effort using keyframes but it is doable.

Masks are stored in alpha channels. Areas that are black in the mask are editable in the sense that other effects can be applied or that clips in lower tracks show through, the other areas are protected, meaning they are not affected by effects or filter and obscure clips on lower tracks.

The following effects are used for masking:

* :doc:`Alpha Shapes (Mask) </effects_and_filters/video_effects/alpha_mask_keying/alpha_shapes_mask>`
* :doc:`Rectangular Alpha Mask </effects_and_filters/video_effects/alpha_mask_keying/rectangular_alpha_mask>`
* :doc:`Rotoscoping (Mask) </effects_and_filters/video_effects/alpha_mask_keying/rotoscoping_mask>`
* :doc:`Shape Alpha (Mask)</effects_and_filters/video_effects/alpha_mask_keying/shape_alpha_mask>`

The following effects are used for creating an alpha channel:

* :doc:`Alpha Shapes</effects_and_filters/video_effects/alpha_mask_keying/alpha_shapes>`
* :doc:`Chroma Key</effects_and_filters/video_effects/alpha_mask_keying/chroma_key>`
* :doc:`Chroma Key (Advanced)</effects_and_filters/video_effects/alpha_mask_keying/chroma_key_advanced>`
* :doc:`Rotoscoping</effects_and_filters/video_effects/alpha_mask_keying/rotoscoping>`
* :doc:`Shape Alpha </effects_and_filters/video_effects/alpha_mask_keying/shape_alpha>`



.. toctree:: 
  :maxdepth: 1
  :hidden:

  masking_and_tracking/masking
  masking_and_tracking/tracking
