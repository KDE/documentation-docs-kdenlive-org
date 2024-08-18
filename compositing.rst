.. meta::
   :description: Kdenlive Documentation - Compositing
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, compositing

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



############################
Transitions and Compositions
############################

Compositing is the process of combining several visual elements from different sources into a single video. It involves replacing selected parts of an image or video with other material, usually other images or videos.

To create a composite from several clips, you make parts of one or more of the clips transparent so that the other clips can show through. :doc:`Alpha shapes </effects_and_filters/video_effects/alpha_mask_keying>`, :doc:`rotoscoping </effects_and_filters/video_effects/alpha_mask_keying/rotoscoping>`, and masks are the most common features for making portions of the clips transparent.

You can use the :guilabel:`Opacity` parameter in the :doc:`Transform </effects_and_filters/video_effects/transform_distort_perspective/transform>` effect to control uniform transparency of a clip. This can be animated using :term:`keyframes <keyframe>` to fade a clip down or up over time.

Some clips may have their transparency information stored in the alpha channel. You can tell Kdenlive how to use this information during compositing.

Compositing more than two clips requires subsequent compositions between the other tracks, or the clever use of alpha channels and mattes.

In Kdenlive, you put the different sources into tracks in the **Timeline** and use **Compositions** to tell Kdenlive how to combine them. For example, the *Dissolve* composition fades out one clip while fading in another over a certain number of frames.

That is why :doc:`/compositing/compositions` are often referred to as :doc:`/compositing/transitions`.

.. note:: Alpha channels are taken into account automatically so that clips with alpha can be stacked on top of each other without the need of compositions.

.. toctree:: 
  :maxdepth: 1
  :hidden:

  compositing/alpha_channels
  compositing/blending_modes
  compositing/transitions
  compositing/compositions
  compositing/masking_and_tracking
