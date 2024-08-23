.. meta::
   :description: Kdenlive Audio Effects - De-Esser
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, audio effects, volume, dynamics, desser, dessing, de-esser, de-essing
   
.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |de-essing| raw:: html

   <a href="https://www.izotope.com/en/learn/the-dos-and-donts-of-de-essing.html" target="_blank">What Is De-essing? The Dos and Don’ts of Using a De-esser</a>


De-Esser
========

.. figure:: /images/effects_and_compositions/kdenlive2308_effects-deesser.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-audio| Deesser

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

Applies de-essing to the audio samples.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: table-wrap

   * - Parameter
     - Value
     - Description

   * - **Intensity**
     - Float
     - Set intensity for triggering de-essing. Allowed range is from 0 to 1. Default is 0.
   * - **Max deessing**
     - Float
     - Set amount of ducking on treble part of sound. Allowed range is from 0 to 1. Default is 0.5.
   * - **Frequency**
     - Float
     - How much of original frequency content to keep when de-essing. Allowed range is from 0 to 1. Default is 0.5.
   * - **Output mode**
     - Selection
     - Set the output mode

The following selections are available:

.. list-table::
   :class: table-wrap

   * - **Input**
     - Pass input unchanged
   * - **Output**
     - Pass ess filtered out (default)
   * - **Ess only**
     - Pass only ess


.. rubric:: Notes

De-essing is the process of trying to eliminate certain high frequency sounds created by the human voice when saying "s", "z", "ch", "j", and "sh". These so-called sibilances range between 2 and 10kHz and are dependent on the individual's pitch. They can cause problems and may be perceived as irritable to the ear when due to compression, microphone choice, recording technique, or simply the way the individual forms those consonants excessive sibilances are produced. For more details about this topic, and in particular how to remove it, see this article about |de-essing| on izotope.com.