.. meta::

   :description: Do your first steps with Kdenlive video editor, using speed effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, motion, speed

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)

   :license: Creative Commons License SA 4.0

.. _speed:

Speed
=====

.. attention::

   .. deprecated:: 21.04
      Is not available anymore. Use :ref:`change_speed` instead




Make clip play faster or slower. Use of this effect mutes the audio of the clip.

.. figure:: /images/effects_and_compositions/Kdenlive_Motion_speed_effect.png
   :align: left
   
The *Stroboscope* setting defines the number frames the effect skips when playing back. For example, if *Stroboscope* is set to 5 then the effect will only show every fifth frame but will show these frames for five times as long, producing a jumpy, stroboscopic effect.

It has been reported that the **Speed** effect does not work very well on H.264-formatted source video. It is recommended to transcode your source material into the DNxHD format and apply the **Speed** effect to that. 
