.. meta::
   :description: The Kdenlive User Manual - Notes for Earlier Versions - The Audio Spectrum and the Spectrogram
   :keywords: KDE, Kdenlive, more information, earlier versions, scopes, audio, spectrum, spectrogram, editing, timeline, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Simon "Granjow" Eugster <simon.eu@gmail.com>
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |audio_scopes| raw:: html

   <a href="http://granjow.net/uploads/kdenlive/kdenlive-audioscopes.pdf" target="_blank">Audio Scopes for Kdenlive (PDF)</a>

.. |signalgen| raw:: html

   <a href="https://arachnoid.com/SignalGen/index.html" target="_blank">SignalGen</a>

.. |audacity| raw:: html

   <a href="https://www.audacityteam.org/" target="_blank">Audacity</a>


.. _audio_spectrum_and_spectrogram:

.. attention:: This page is not maintained anymore and contains information referring to features or functions from earlier versions of Kdenlive that are deprecated or have been superseded by something else.

The Audio Spectrum and the Spectrogram
======================================

This chapter is about audio scopes. It is also talking about audio in general (e.g. recording, perception, etc.).

.. image:: /images/earlier_versions/audiospectrum-example.png

The Scopes
----------

.. figure:: /images/earlier_versions/kdenlive-spectrogram.png

   Spectrogram screenshot

The audio scopes are documented in-depth in |audio_scopes| by Simon "Granjow" Eugster\ [#f1]_. You may skip the technical/mathematical part — it is not necessary for understanding the scope, and the maths behind it is not trivial. The rest might be interesting, though.

Nevertheless, a quick overview over the features currently available.

Audio Spectrum
~~~~~~~~~~~~~~

This scope displays the frequency spectrum for each frame. Low frequencies are on the left, high frequencies on the right. And the higher the bar, the louder this frequency.

Loudness is measured in :abbr:`decibel (Unit of measurement (dB) for sound levels)` in the spectrum\ [#f2]_. If all frequencies have equal loudness, you can adjust the range to display by dragging vertically. Simply dragging adjusts the lower threshold, :kbd:`Shift+drag` adjusts the maximum loudness to display. Horizontal dragging adjusts the maximum frequency to display samples for.

But what is this display useful for? One thing is that, as described in the PDF linked at the top, you can visually distinguish between good and bad sound quality: If there are no frequencies higher than, for example, 3 kHz, then the audio quality most likely is not too good.

.. hint:: If you have no clue how high 3 kHz are, which is nothing unusual since our ears do not deliver numerical values to our brain, you can use a program like |signalgen| or |audacity| to generate a sine wave with 3 kHz (which is 3,000 Hz).

Something else the frequency spectrum is useful for is to avoid :abbr:`clipping (A form of distortion that limits a signal once it exceeds a threshold)`. The same effect that can be seen with colors, e.g. in the :doc:`RGB parade </tips_and_tricks/scopes/waveform_and_rgb_parade>`, and actually with every signal that is digitalized. More about this below.

Spectrogram
~~~~~~~~~~~

The :abbr:`Spectrogram (Visual representation of the spectrum of frequencies of a signal as it varies with time)` does the same as the Audio Spectrum: It shows the frequency distribution with the difference, though, that the frequencies are not shown for one frame only. Similar to the :doc:`RGB Parade </tips_and_tricks/scopes/waveform_and_rgb_parade>` for colors, stronger (louder) frequencies are represented by brighter pixels; this allows to put a whole frame's spectrum in one line.

What the Scopes Might Help in as Well
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |this_review| raw:: html
   
   <a href="https://www.youtube.com/watch?app=desktop&v=ZWXU3mScCzM" target="_blank">this review</a>

Consider |this_review| about the Nikon D7000, and listen at 7:00 and 11:00. At 7:00 you can hear the reviewer loud and clear, at 11:00 you need to turn up the volume to even understand something. This should not happen. The audio scope helps to maintain equal loudness over multiple shots. 

Sound
-----

Now a few interesting details about sound.

Clipping
~~~~~~~~

.. figure:: /images/earlier_versions/Zoom_H4n_audio_levels.jpg
   :width: 40%
   :align: right

   Audio levels on a Zoom H4n

As mentioned above sound can clip as well. Everyone has heard this already. This is how it sounds (extracts from James Edwards' Greensleeves\ [#f3]_):

.. |original| raw:: html

   <a href="http://granjow.net/uploads/kdenlive/samples/James-Edwards-Greensleeves-original.ogg" target="_blank">Original</a>

.. |volume_up_24db| raw:: html

   <a href="http://granjow.net/uploads/kdenlive/samples/James-Edwards-Greensleeves-overdriven-24dB.ogg" target="_blank">Volume increased by 24 dB</a>

.. |volume_down_24db| raw:: html

   <a href="http://granjow.net/uploads/kdenlive/samples/James-Edwards-Greensleeves-overdriven-24dB-reverted.ogg" target="_blank">Volume afterwards decreased by 24 dB</a>

- |original|
  
- |volume_up_24db| - massive clipping!

- |volume_down_24db| - the clipping effect is irreversible

Clipping is also very well visible in the audio wave itself, if you e.g. open the samples above with Audacity. (If you want to reproduce the above effect with Audacity, make sure to select «allow overdrive», otherwise it will :abbr:`prevent clipping (Dynamic range compression (DRC)is an audio signal processing operation that reduces the volume of loud sounds or amplifies quiet sounds, thus reducing or compressing an audio signal's dynamic range.)`. When decreasing the volume afterwards do not use the same project since Audacity actually stores values that are bigger than the maximum amplitude value (:file:`.aup` files only). This is great for editing, and perhaps one day we will have that for color as well in Kdenlive …)

So, when may clipping occur?

1. When recording audio. The input gain can be adjusted on the audio recorder. If the gain is too high, it might record for example low talking at a good volume, but clip as soon as someone rises their voice. Therefore input gain is usually adjusted such that the mean volume and peaks do not exceed a certain limit.
   
   This limit depends on the expected dynamic audio range. A common choice is -12 dB for the mean volume and maximally -6 dB for peaks.
   
2. When editing. There are multiple volume effects in Kdenlive. If you raise the volume too much, you will experience clipping.

   To prevent clipping in kdenlive, you actually do quite the same as when recording audio. Try to keep peak values below -6 dB. If you need one cut to be really much louder than the rest and you cannot raise it any further, then you need to lower everything else.

Damping
~~~~~~~

The further away you are from the sound source, the quieter you hear it. Until finally it will be as loud as the noise floor of your microphone and audio recorder. To maintain a good :abbr:`SNR (Signal-to-Noise Ratio)` you will therefore usually try to keep your microphone as close as possible to the sound source. Such that the signal is much stronger than the noise (and with the input gain adjusted such that no clipping occurs).

But that is not everything yet. (Actually the above point was not about dampening at all but merely about wave propagation.) There is one interesting aspect, which is that higher frequencies are absorbed much stronger than low frequencies. Unlike the previous points this is not a problem but rather an interesting variable: If you record someone's voice and want to put him far away in the video (next room for example), lower the higher frequencies (using Audacity's Equalizer effect for example).

Our Ear
~~~~~~~

What is louder: A sine wave of 200 Hz or a sine wave of 4 kHz?

.. |200hz_sine| raw:: html

   <a href="http://granjow.net/uploads/kdenlive/samples/Sine-200Hz.ogg" target="_blank">200 Hz Sine</a>

.. |4000hz_sine| raw:: html

   <a href="http://granjow.net/uploads/kdenlive/samples/Sine-4000Hz.ogg" target="_blank">4,000 Hz Sine</a>

.. |hearing| raw:: html

   <a href="https://en.wikipedia.org/wiki/Hearing" target="_blank">Hearing</a>

- |200hz_sine|

- |4000hz_sine|

They have both been generated with the same amplitude (volume). But our ear is most sensible on the frequencies we talk in. To read more about our ear, the Wikipedia article about |hearing| is a good starting point.



.. rubric:: Notes

.. |web_archive| raw:: html

   <a href="https://web.archive.org/web/20160321134459/http://kdenlive.org/users/granjow/introducing-scopes-audio-spectrum-and-spectrogram" target="_blank">web.archive.org</a>

.. |james_edwards| raw:: html

   <a href="https://www.jamendo.com/artist/355390/james-edwards" target="_blank">James Edwards</a>

.. |damping| raw:: html

   <a href="https://people.ee.ethz.ch/~isistaff/courses/ak1/acoustics-sound-propagation-outdoors.pdf" target="_blank">Acoustics I - Sound Propagation Outdoors</a> 
   
.. |capturing| raw:: html

   <a href="https://vimeo.com/blog/post/capturing-good-sound" target="_blank">Capturing Good Sound</a>

.. |thread| raw:: html

   <a href="https://www.dvxuser.com/forum/filmmaking/location-sound-post-audio/208302-db-level-peaks-matter-in-this-situation" target="_blank">Thread about audio and clipping</a>
   
**Further Information and Suggested Reading**
  - |damping|, ETH Zurich

  - |capturing| at Vimeo, about microphones

  - |thread| in the forum at dvxuser.com

----

.. [#f1] The original text was submitted by *Simon A. Eugster (Granjow)* on Sat, 12/25/2010 - 12:51 to the now defunct kdenlive.org blog. For this documentation it has been lifted from |web_archive| and adapted to match the overall style.

.. [#f2] To be very precise, the unit used in the scope is :abbr:`dbFS (Decibels relative to full scale)`, so 0 dB refers to the maximum possible loudness that can be achieved with the digital input signal.

.. [#f3] |james_edwards| at Jamendo