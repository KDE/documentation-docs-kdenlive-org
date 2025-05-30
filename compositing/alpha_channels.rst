.. meta::
   :description: Kdenlive Documentation - Compositing: Alpha Channels
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, compositing, alpha channel

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _compositing-alpha_channels:

==============
Alpha Channels
==============

The alpha channel is an additional channel inside a video clip or an image that contains information about transparency (or opacity) of the image. The following file formats may contain an alpha channel:

:Image file formats:
    EXR, PNG, APNG, TIFF, GIF, SVG, JXL
    
:Video file formats:
   MOV, HEVC, WEBM

The alpha channel is essentially a mask that specifies how the image should be combined (or composited) with another image when the two are overlaid. The alpha channel can have a value from 0 (black) to 255 (white). Normally, black is fully transparent, meaning the image below shows through completely, while white means that the image below is blocked (or masked). You could say the alpha channel determines which parts of the image are transparent or semi-transparent or not transparent at all (opaque), allowing or preventing the image below to show through. This is very useful in compositing and special effects work, such as adding fire, explosions, or rain to your video.

Kdenlive automatically recognizes the alpha channel of video or image files. When placed in the timeline, clips with an alpha channel allow clips in lower tracks to show through.

The following effects and filters manipulate or use the alpha channel:

.. .. hlist::
      :columns: 2

* :doc:`/effects_and_filters/video_effects/alpha_mask_keying/alpha_gradient`
* :doc:`/effects_and_filters/video_effects/alpha_mask_keying/alpha_operations`
* :doc:`/effects_and_filters/video_effects/alpha_mask_keying/alpha_strobing`
* :doc:`/effects_and_filters/video_effects/alpha_mask_keying/lumakey`
* :doc:`/effects_and_filters/video_effects/misc/alphaextract`
* :doc:`/effects_and_filters/video_effects/misc/alphamerge`
* :doc:`/effects_and_filters/video_effects/alpha_mask_keying/backgroundkey`
* :doc:`Premultiply </effects_and_filters/video_effects/alpha_mask_keying/premultiply>`
* :doc:`/effects_and_filters/video_effects/alpha_mask_keying/transparency`

The following effects and filters create an alpha channel:

.. .. hlist::
      :columns: 2

* :doc:`/effects_and_filters/video_effects/alpha_mask_keying/alpha_shapes`
* :doc:`/effects_and_filters/video_effects/alpha_mask_keying/bluescreen0r`
* :doc:`/effects_and_filters/video_effects/alpha_mask_keying/chroma_key`
* :doc:`/effects_and_filters/video_effects/alpha_mask_keying/chroma_key_advanced`
* :doc:`Rect. Alpha Mask </effects_and_filters/video_effects/alpha_mask_keying/rectangular_alpha_mask>`
* :doc:`/effects_and_filters/video_effects/alpha_mask_keying/rotoscoping`
* :doc:`/effects_and_filters/video_effects/alpha_mask_keying/shape_alpha`
* :doc:`/effects_and_filters/video_effects/alpha_mask_keying/hsvkey`