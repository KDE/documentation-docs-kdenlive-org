.. meta::

   :description: Do your first steps with Kdenlive video editor, using the dance effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, on master, dance

.. metadata-placeholder

   :authors: - Roger (https://userbase.kde.org/User:Roger)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-dance:

Dance
=====

This effect/filter is an audio visualization effect that zooms, moves and rotates the image proportional to the magnitude of the audio spectrum.

Using the :guilabel:`Zoom` alone creates a cool pump effect in sync with the beats.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-dance.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-dance

   Dance effect

* **Low Frequency** - The low end of the frequency range to be used to influence the image motion

* **High Frequency** - The high end of the frequency range to be used to influence the image motion

* **Level Threshold** - The minimum amplitude of sound that must occur within the frequency range to cause the image to move

* **Oscillation** - Oscillation can be useful to make the image move back and forth during long periods of sound. A value of 0 specifies no oscillation.

.. rst-class:: clear-both

* **Initial Zoom** - The amount to zoom the image before any motion occurs. This can be used to avoid black on the sides of the image when it moves.

  * 100% = no zoom
  * < 100% = zoom out (make the image smaller)
  * > 100% = zoom in (make the image larger)

* **Zoom** - The amount that the audio affects the zoom of the image.

  * < 0% = Image will zoom out (get smaller) with more sound
  *   0% = no zoom
  * > 0% = Image will zoom in (get larger) with more sound

* **Left / Right** - The amount that the audio affects the left / right offset of the image.

  * 0% = no offset
  * > 0% = Image will move left / right with more sound

* **Up / Down** - The amount that the audio affects the up / down offset of the image.

  * 0% = no offset
  * > 0% = Image will move up / down with more sound

* **Clockwise / Counter Clockwise** - The amount that the audio affects the rotation of the image.

  * 0 = no rotation
  * > 0 = Image will rotate with more sound

* **Window Size** - The number of samples that the FFT\ [1]_ will be performed on. If :guilabel:`Window Size` is less than the number of samples in a frame, extra samples will be ignored. If :guilabel:`Window Size` is more than the number of samples in a frame, samples will be buffered from previous frames to fill the window. The buffering is performed as a sliding window so that the most recent samples are always transformed.

.. rst-class:: clear-both


**Notes**

.. [1] FFT := Fast Fourier Transform


.. https://youtu.be/gqxU1nvh6JI

