.. meta::
   :description: Kdenlive Tips & Tricks - The Vectorscope's I and Q Lines
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, scopes, vectorscope, I and Q, editing, timeline, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Simon "Granjow" Eugster <simon.eu@gmail.com>
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |color-correct| raw:: html

   <a href="https://prolost.com/blog/2008/3/23/save-our-skins.html" target="_blank">color-correct</a>


.. _scopes-vectorscope_i_and_q_lines:

Vectorscope I and Q Lines
=========================

The Vectorscope has an option to draw I/Q lines. So you may be wondering what are they good for?

.. figure:: /images/tips_and_tricks/kdenlive2308_vectorscope_iq_01.webp
   :width: 350px

   I and Q lines in the Vectorscope

Where I/Q lines Come From
-------------------------

You may remember from the :doc:`Vectorscope chapter <vectorscope_working>` that the Vectorscope uses a color space different than RGB. In the image above it is :term:`YUV`, in the image below it is :term:`YPbPr`. They both share the property that the Y component represents :term:`Luma` only (i.e. how bright a pixel is), and the other two components represent :term:`Chroma` (colour) by expressing deviations from neutral color on the red-green and yellow-blue axis. (These are complementary colours each, so mixing them in equal parts results in neutral again - which is why they can be used for the deviation.)

YUV is the standard color space for analog PAL television. NTSC, the american analog TV standard, uses a color space I did not mention yet: :term:`YIQ`. The special thing about this color space is that the I component was chosen such that skin tones (also known as flesh tones) lie on the I line (orange-blue), and it was given more than four times as much bandwidth as the Q component (which represents the green-purple line; the human eye is also less sensitive for changes on this line).

.. figure:: /images/tips_and_tricks/kdenlive2308_vectorscope_iq_02.webp
   :width: 650px

   Vectorscope showing skin tones along the I line

Purpose of the I and the Q line
-------------------------------

Displaying the Q and especially the I line is to help with skin tones. There is a rule of thumb in post production saying that all skin tones should approximately lie on the I line. If it is not, you might want to |color-correct| your clip.

The simple reason for this is that our eyes are trained on skin tones, and if skin tones in your video do not lie in the I line they are very likely to look unnatural. There are very good picture examples in the Save our Skins article mentioned above.



.. rubric:: Notes

.. |web_archive| raw:: html

   <a href="https://web.archive.org/web/20160324111308/http://kdenlive.org/users/granjow/vectorscope-what-i-and-q-lines-are-good" target="_blank">web.archive.org</a>

**Sources**
  :download:`skin1.avi <http://granjow.net/uploads/kdenlive/samples/skin1.avi>` (720p, 5.1 MB)

  The original text was submitted by *Simon A. Eugster (Granjow)* on Fri, 11/26/2010 - 18:05 to the now defunct kdenlive.org blog. For this documentation it has been lifted from |web_archive|, updated and adapted to match the overall style.