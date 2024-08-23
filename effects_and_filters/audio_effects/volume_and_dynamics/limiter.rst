.. meta::
   :description: Kdenlive Audio Effects - Limiter
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, audio effects, volume, dynamics, limiter
   
.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Limiter
=======

.. figure:: /images/effects_and_compositions/kdenlive2308_effects-limiter.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-audio| Limiter

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

The limiter prevents an input signal from rising over a desired threshold. This limiter uses lookahead technology to prevent your signal from distorting. It means that there is a small delay after the signal is processed. Keep in mind that the delay it produces is the attack time you set. 


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: table-wrap

   * - Parameter
     - Value
     - Description

   * - **Input gain**
     - Float
     - Set input gain. Default is 1.
   * - **Output gain**
     - Float
     - Set output gain. Default is 1.
   * - **Limit**
     - Float
     - Do not let signals above this level pass the limiter. Default is 1.
   * - **Attack**
     - Float
     - The limiter will reach its attenuation level in this amount of time in milliseconds. Default is 5 milliseconds.
   * - **Release**
     - Integer
     - Come back from limiting to attenuation 1.0 in this amount of milliseconds. Default is 50 milliseconds.
   * - **Enable ASC**
     - Switch
     - When gain reduction is always needed ASC takes care of releasing to an average reduction level rather than reaching a reduction of 0 in the release time.
   * - **ASC level**
     - Float
     - Select how much the release time is affected by ASC, 0 means nearly no changes in release time while 1 produces higher release times.
   * - **Normalize to 0dB**
     - Switch
     - Auto level output signal. Default is enabled. This normalizes audio back to 0dB if enabled.
