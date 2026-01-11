.. meta::
   :description: The Kdenlive User Manual - Notes for Earlier Versions - Variable Bit Rate
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, help, learn, easy, earlier version, variable bit rate

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Nikerabbit (https://userbase.kde.org/User:Nikerabbit)
             - Simon Eugster <simon.eu@gmail.com>
             - Jean-Baptiste Mardelle <jb@kdenlive.org>
             - Earl fx (https://userbase.kde.org/User:Earl fx)
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Vincent Pinon <vpinon@kde.org>
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jessej (https://userbase.kde.org/User:Jessej)
             - Dbolton (https://userbase.kde.org/User:Dbolton)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - KGHN (https://userbase.kde.org/User:KGHN)
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _rendering-vbr:

.. attention:: This page is not maintained anymore and contains information referring to features or functions from earlier versions of Kdenlive that are deprecated or have been superseded by something else.

Variable Bit Rate
=================

.. figure:: /images/earlier_versions/Kdenlive_Render_dialog_vbr_0.9.10.png
   :width: 400px

When a variable bitrate (VBR) profile is selected, the :guilabel:`File Size` section displays a drop down for choosing the **Video quality** you want. This quality figure is a codec-dependent number representing the quality of the video that will be rendered. Generally, lower numbers mean higher quality video and larger file sizes (e.g. x264, MPEG2, VPx), but some codecs use opposite order (e.g. Theora). Profiles provided with **Kdenlive** offer these numbers ordered from best quality (almost lossless) to lower quality (still not degrading too much). The exact file size that is produced can not be predicted when using the VBR method. The idea behind this is that you specify a certain quality of video that you want through the entire video and the encoding optimizes bitrate to give you that constant quality, lowering data size for low action scenes and using more bits for high action scenes.

Example: 1min 55 seconds of 720 x 576 H.264 iPhone footage rendered at quality 15 with the H.264/AAC High Profile would produce a file size of 186 Mb. Whereas rendering the same footage at quality quality 20 produced an 83Mb file.