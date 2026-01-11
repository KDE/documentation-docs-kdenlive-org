.. meta::
   :description: Kdenlive Tips & Tricks - Fixing Unwanted Slow Audio Fade-Ins
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, useful information, usb, audio, card, fixing, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - TheDiveO
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0


Fixing Unwanted Slow Audio Fade-Ins
===================================

Do you suffer from an unwanted slow audio fade-ins whenever starting playback in the timeline or in the clip monitor, while you do not have any audio fade effects applied at all? Turns out this is some odd interference between some(!) USB audio cards and the PulseAudio sound backend.

.. rubric:: ALSA to the Res-Cue

.. figure:: /images/tips_and_tricks/kdenlive2308_alsa_audio.webp
   :align: left
   :width: 350px

   Setting the audio driver to ALSA

Luckily, there is an easy remedy in case you are affected.

Go to :menuselection:`Menu --> Settings > Configure Kdenlive`, then in the configuration dialog select the :guilabel:`Playback` section. Change the :guilabel:`Audio driver` from :guilabel:`Automatic` to :guilabel:`ALSA`. Leave the Audio device set to “Default”, so your desktop audio device settings apply.

Click :guilabel:`OK`, and you are done.

.. rst-class:: clear-both

Your timeline and bin clip audio playback should now be working as expected, without any unwanted slow audio fade-ins anymore.


You will find the corresponding option in the main menu via :menuselection:`Menu --> Sequence --> Disable Timeline Effects`. This disables or re-enables all timeline effects, that is, timeline clip effects and track effects.

However, please note that prior to Kdenlive 16.08.1, track effects are not properly disabled or re-enabled by :menuselection:`Menu --> Sequence --> Disable Timeline Effects`.

Please see :doc:`/tips_and_tricks/tips_and_tricks/effects_everywhere` about how to temporarily disable bin clip effects.

.. rst-class:: clear-both



.. rubric:: Notes

.. |kdenlive_org| raw:: html

   <a href="https://kdenlive.org/en/project/fixing-unwanted-slow-audio-fade-ins-with-some-usb-audio-cards/" target="_blank">kdenlive.org</a>

**Background Information**
  Please note that the unwanted ~2 seconds audio fade-in only happens with **some** USB audio cards but not others. It was noticed when trying a Steinberg UR22mkII USB audio interface.

  Using the UR22mkII in Kdenlive using the stock audio settings was impossible, as the automatic fade-in made any voice over editing a complete and utter fail. Curiously, the UR22mkII worked beautifully when playing back audio using an Android tablet (that is a beautiful aspect of the UR22mkII: it is designed to be used with mobile devices). For comparison, a (much bulkier) Behringer QX1202USB does not exhibit the strange behavior even with the default audio settings in Kdenlive, or when using PulseAudio.

  And what is even more strange and surprising: at least some other software, such as VLC, are completely unaffected, even when using PulseAudio for audio output.

**Sources**
  The original text was submitted by user *TheDiveO* to the now defunct kdenlive.org blog. For this documentation it has been lifted from |kdenlive_org|, updated and adapted to match the overall style.