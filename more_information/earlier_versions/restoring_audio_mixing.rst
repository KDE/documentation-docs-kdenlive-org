.. meta::
   :description: Kdenlive Tips & Tricks - Restoring Audio Mixing
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, restore, audio mixing, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - TheDiveO
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0

.. moved from https://kdenlive.org/en/project/cure-projects-with-odd-audio-mixing-behavior/


.. attention:: This page is not maintained anymore and contains information referring to features or functions from earlier versions of Kdenlive that are deprecated or have been superseded by something else.

Restoring Audio Mixing
======================

.. .. versionadded:: 16.08

Nobody is perfect. So yes, once in a while you may experience unexpected odd audio mixing in Kdenlive projects. While audio from some tracks will mix properly, audio from certain other tracks mutes all remaining tracks. Rejoice! Kdenlive 16.08 now comes to your rescue.

Restoring proper audio mixing is easy:

1. **Load your project** into Kdenlive
2. **Add a new track** to your timeline; whether it is an audio or video track does not matter
3. Then you may **delete** this track again, if you do not plan to use it anyway
4. Check playback
5. **Save** your project

This may sound exactly like clueless support advice but it works. If you now play your project in the timeline, automatic audio mixing across all timeline tracks should work again normally.

.. note::

   This upgrades your Kdenlive projects to the most recent project version. So you will not be able to edit it again in an older or ancient Kdenlive version.



.. rubric:: Notes

.. |kdenlive_org| raw:: html
   
   <a href="https://kdenlive.org/en/project/adding-meta-data-to-mp4-video/" target="_blank">kdenlive.org</a>

**Sources**
  The original text was submitted by user *TheDiveO* to the now defunct kdenlive.org blog. For this documentation it has been lifted from |kdenlive_org| and adapted to match the overall style.