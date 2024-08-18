.. meta::
   :description: Kdenlive Audio Effects - Volume and Dynamics
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, audio effects, volume, dynamics
   
.. metadata-placeholders

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |ffmpeg_filter| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html" target="_blank">ffmpeg filter</a>


Volume and Dynamics
=========================

This category consists of effects and filters like compressors, expanders, for normalization and volume adjustment.

The following filters and effects are available and documented here in detail:

.. toctree::
   :maxdepth: 1

   compressor_expander
   deesser
   fade_in
   fade_out
   gain
   limiter
   mute
   normalize
   normalize_2pass
   volume_keyframable

The following filters are more geared towards further processing of the audio streams with potential extra hardware required, and are not documented here. Please refer to the |ffmpeg_filter| documentation (section *8 Audio Filter*).

* asoftclip
* simple_compressor_expander
* sox_gain
