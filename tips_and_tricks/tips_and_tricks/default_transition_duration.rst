.. meta::
   :description: Kdenlive Tips & Tricks - Configuring the Default Transition Duration
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, configuring, default, transition, duration, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - TheDiveO
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0


Configuring the Default Transition Duration
===========================================

You can configure the default duration for all newly created transitions. In versions prior to 16.08, all new transitions were always 65 frames long - and this translated to varying default durations, depending on a project's frame rate. This new configuration option should appeal to all those users who work a lot with transitions.

.. .. image:: /images/config-transition-duration.png

.. figure:: /images/tips_and_tricks/kdenlive2308_config_default_transition_duration.webp
   :align: left
   :width: 350px
   
   :menuselection:`Menu --> Settings --> Configure Kdenlive`

Go to :menuselection:`Menu --> Settings --> Configure Kdenlive --> Misc`. Under the heading :guilabel:`Default Durations` you will find the option to configure the default duration for newly created transitions. Enter a duration in the usual format :abbr:`hh:mm:ss:ff (hours:minutes:seconds:frames)`.

Please note that the frames (**ff**) field element will be interpreted on the basis of the current project's framerate. In contrast, the other field elements (**hh:mm:ss**) are independent of the framerate.

.. rst-class:: clear-both
   

.. rubric:: Notes

.. |kdenlive_org| raw:: html

   <a href="https://kdenlive.org/en/project/configuring-the-default-transition-duration/" target="_blank">kdenlive.org</a>

**Sources**
  The original text was submitted by user *TheDiveO* to the now defunct kdenlive.org blog. For this documentation it has been lifted from |kdenlive_org| and adapted to match the overall style.