.. meta::
   :description: Kdenlive Audio Effects - Crusher
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, audio effects, tools, crusher
   
.. metadata-placeholder

   :authors: - Bushuev (https://userbase.kde.org/User:Bushuev)
             - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Crusher
=======

.. figure:: /images/effects_and_compositions/kdenlive2308_effects-crusher.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-audio| Crusher

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

This filter is a bit crusher with enhanced functionality.

A bit crusher is used to audibly reduce number of bits an audio signal is sampled with. This does not change the bit depth at all, it just produces the effect. Material reduced in bit depth sounds more harsh and "digital". This filter is able to even round to continuous values instead of discrete bit depths. Additionally it has a :guilabel:`DC` offset which results in different crushing of the lower and the upper half of the signal. An :guilabel:`Anti-aliasing` setting is able to produce "softer" crushing sounds.

Another feature of this filter is the logarithmic mode. This setting switches from linear distances between bits to logarithmic ones. The result is a much more "natural" sounding crusher which does not gate low signals for example. The human ear has a logarithmic perception, so this kind of crushing is much more pleasant. Logarithmic crushing is also able to get anti-aliased. 


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description

   * - **Input gain**
     - Float
     - Sets level in
   * - **Output gain**
     - Float
     - Sets level out
   * - **Limit**
     - Float
     - 
   * - **Bit reduction**
     - Integer
     - Sets bit reduction (range is from 1 to 64 bit; default is 8 bits)
   * - **Mix**
     - Float
     - Sets mixing amount
   * - **Mode**
     - Selection
     - Sets filtering mode (Linear or Logarithmic; default is Linear)
   * - **DC**
     - Float
     - Sets DC
   * - **Anti-aliasing**
     - Float
     - Sets anti-aliasing
   * - **Sample reduction**
     - Integer
     - Sets sample reduction (range is from 1 to 250; default is 1)
   * - **Enable LFO**
     - Switch
     - Enables :abbr:`LFO (Low-Frequency Oscillation)` (default is disabled)
   * - **LFO depth**
     - Integer
     - Sets LFO depth
   * - **LFO rate**
     - Float
     - Sets LFO rate


.. .. rubric:: Notes