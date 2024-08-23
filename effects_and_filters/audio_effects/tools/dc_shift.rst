.. meta::
   :description: Kdenlive Audio Effects - DC Shift
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, audio effects, tools, dc shift
   
.. metadata-placeholder

   :authors: - Bushuev (https://userbase.kde.org/User:Bushuev)
             - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |dc_shift| raw:: html

   <a href="https://www.soundonsound.com/glossary/dc-offset" target="_blank">this article</a>


DC Shift
========

.. figure:: /images/effects_and_compositions/kdenlive2308_effects-dc_shift.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-audio| DC Shift

   :Status:
      Maintained
   :Keyframes:
      No
   :Source library:
      avfilter 
   :Available:
      |linux| |appimage| |windows| |apple|
   :On Master only:
      No
   :Known bugs:
      No

.. rst-class:: clear-both


.. rubric:: Description

This can be useful to remove a DC offset\ [1]_ (caused perhaps by a hardware problem in the recording chain) from the audio. The effect of a DC offset is reduced headroom and hence volume.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description

   * - **DC Shift**
     - Float
     - Sets the DC shift, allowed range is [-1, 1]. It indicates the amount to shift the audio.
   * - **Limiter Gain**
     - Float
     - Optional. It should have a value much less than 1 (e.g. 0.05 or 0.02) and is used to prevent clipping.


.. .. rubric:: Notes

----

.. [1] See a more detailed description of what causes a DC offset in |dc_shift| on soundonsound.com