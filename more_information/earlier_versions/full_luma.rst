.. meta::
   :description: The Kdenlive User Manual - Notes for Earlier Versions - Full Luma
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, help, learn, easy, earlier version, full luma

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


.. attention:: This page is not maintained anymore and contains information referring to features or functions from earlier versions of Kdenlive that are deprecated or have been superseded by something else.

Full Luma
=========

The :guilabel:`Full (JPEG)` luma option refers to video sources with :term:`luma` recorded outside of the typical `broadcast`, limited 16 - 235 8-bit range.

It fixes problems when round-tripping video files with luma outside of the 16 - 235 8-bit range.

By default, when we import a video it is handled and displayed based on the 16 - 235 range. That means levels below 15 and those above 235 are compressed to 0 and 255, respectively. Thus shadows get overly dark and highlights saturated in the preview in Kdenlive for camera sources that are full range.

When we render out the project, those levels remain in the final video (compressed shadows and saturated highlights) resulting in a mismatch between the levels in the imported video and the exported video.

.. note:: This only really matters for round-tripping to an external application.

For any playback on DVDs, Blu-ray, and via the likes of Vimeo or Youtube, our video levels in the final rendered output should be in the 16 - 235 range, otherwise we see so called `gamma shifts`, `washed out` or saturated playback depending on playback handling.

However, we want to have full control of the levels adjustment in Kdenlive, i.e. 0 - 255 into 16 - 235. Full luma option changes the handling of the files and preview / scopes are based on an alternative YCbCr to RGB calculation.

By setting the full luma on, which should only be done for camera sources known to be full range 0 - 255 or even 16 - 255 such as FS100, Nex5, HV20, HV30 and probably many more consumer cameras. Canon and Nikon DSLR's too but a little more complicated, we can export video with the levels as imported, BUT and it's a big but, that is without doing any RGB operations in Kdenlive, so no effects, color correction etc. If any effects are added then the output will be restricted range again.

.. For me I use full luma all the time, it allows round-tripping a video edit and maintaining levels for grading in an external application that offers 32bit float precision. When it's necessary to otherwise happy with **Kdenlive's** SOP/SAT and scopes.


.. |kdenlive_org| raw:: html

   <a href="http://www.kdenlive.org/forum/what-does-full-luma-exactly-do#comment-18298" target="_blank">kdenlive.org</a>

**Sources**
  The original text for **Full Luma** was submitted by user *Yellow* to the now defunct Kdenlive forum. For this documentation it has been lifted from |kdenlive_org| and adapted to match the overall style.
