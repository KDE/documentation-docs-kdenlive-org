.. meta::
   :description: Kdenlive Tips & Tricks - Transitions
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, useful information, transitions, timeline, editing, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - TheDiveO
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0


.. To Do:
   + Update screenshots
   + Correct/update *Affine*
   + Move images to new folder
  

.. |gimp| raw:: html

   <a href="https://www.gimp.org/" target="_blank">GIMP</a>


Kdenlive Transitions
====================

Depending on their background in video editing, users may find Kdenlive **Transitions** somewhat confusing. Hopefully, this article clears up this confusion surrounding Kdenlive transitions, at least to some degree.


Kdenlive Transitions: 3-in-1
----------------------------

In Kdenlive, **Transitions** can roughly be classified into three different types as follows:

.. list-table:: 
   :header-rows: 1
   :width: 100
   :widths: 30 70
   :class: table-wrap

   * - Type of Transition
     - Description
   * - Clip-to-Clip Transition
     - Gradually replaces one clip by another clip. Has exactly two implicit keyframes, one for start and one for end. This is what many users usually understand transitions to be.
   * - Dynamic Compositing
     - For combining two clips, and the way of combination may vary with time. Supports user-defined keyframes that allow to control at least certain parameters. 
   * - Layer Compositing
     - For combining two clips in a constant, static way: much like layer compositing in image tools. As keyframes are not supported, this type of compositing is static, thus invariant of time.

Historically, Kdenlive borrows the term **transition** with its 3-fold meaning directly from the `multimedia engine MLT <https://mltframework.org/>`_. :abbr:`MLT (Media Lovin' Toolkit - An open source software multimedia framework designed and developed for tv broadcasting)` that does all the video and audio processing according to your timeline. In the MLT universe, transitions basically «merge» video frames from upper tracks with video frames from lower tracks, producing result frames.

In contrast, many users experienced in video editing have come to know transitions as a mechanism to transition between to adjacent clips. As of version 21.08 Kdenlive does support such in-track (or same-track) transitions as :ref:`Mixes <same_track_transition>`.


.. _clip_to_clip_transition:

Clip-to-Clip Transitions
------------------------

Let's start with those **standard transitions** most users would probably expect when they hear the word *transition*: the dissolve, slide, and wipe transitions.

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_clip_to_clip_dissolve.webp
      :align: left
      :alt: kdenlive2308_clip_to_clip_dissolve.webp
      :width: 350px

   **Dissolve**: gradually transitions from one clip to another. So it is kind of fading between the two clips. (See also the Wikipedia article on `Dissolve. <https://en.wikipedia.org/wiki/Dissolve_%28filmmaking%29>`_) 

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_clip_to_clip_slide.webp
      :align: left
      :alt: kdenlive2308_clip_to_clip_slide.webp
      :width: 350px

   **Slide**: gradually replaces one clip by another clip, by traveling from one side of the frame to another (See also the Wikipedia article on `Wipe <https://en.wikipedia.org/wiki/Wipe_%28transition%29>`_.)

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_clip_to_clip_wipe.webp
      :align: left
      :alt: kdenlive2308_clip_to_clip_wipe.webp
      :width: 350px

   **Wipe**: one clip gradually replaces another clip, often in form of some shape. (See also the Wikipedia article on `Wipe <https://en.wikipedia.org/wiki/Wipe_%28transition%29>`_.)

.. rst-class:: clear-both

These three transitions do not offer any (user-) keyframes. Instead, their *start* and *end* keyframes are *implicit* and fixed to the *start* and *end* of the transition respectively.

.. note:: When using two separate tracks for transitions, as time moves forward in the timeline, these transitions change (or kind of fade) from the clip on the upper track to the clip on the lower track. The somewhat strangely named transition parameter :guilabel:`Reverse` allows you to switch the track roles: if :guilabel:`Reverse` is checked, then these transitions change from the lower track to the upper track, as time progresses. Simply put: ▼ :guilabel:`Reverse` **off**: transition from upper track to ▼ lower track; ▲ :guilabel:`Reverse` **on**: transition from lower track to ▲ upper track instead.


.. _dynamic_compositing_transition:

Dynamic Compositing Transitions
-------------------------------

.. image:: /images/transition-compositing-galore.png
      :alt: transition-compositing-galore

To some degree, Kdenlive supports (simple) compositing in its timeline. Actually, even this simple compositing can get you a long way in many projects (as the above screenshot may hint at). Kdenlive currently offers the following (keyframable) compositing transitions:


:Affine:
   Allows to size, rotate, skew, and position. Together with keyframes, this transition is really versatile. Its only drawbacks are that it is slower than other complex transitions (due to the affine transformation), and it does not support wipes (which only **Composite** and **Region** support in this class of transitions).

:Cairo Blend:
   A simple compositing transition, supporting several compositing modes. In addition, the opacity of the upper frames can be controlled. This transition also supports keyframes.

:Cairo Affine Blend:
   This has the functionality of both **Affine** and **Composite**: position, rotate (you can even control the center of rotation!), and finally skew. And all this is keyframable.

:Composite:
   Allows keyframed dissolves, wipes, and swipes; and all this in the same transition. In contrast to **Affine**, it does not support rotation or skewing. The downsides of Composite are: :term:`luma` bleed, and less precise position control. When compared to **Affine**, the **Composite** transition is much faster, albeit at the cost of luma bleed.

:Composite & Transform:
   This is a rather new transition that made its debut with Kdenlive 16.04. It allows to easily composite clips onto each other (supported several compositing modes), as well as to move the upper track clips. However, there is neither support for scaling nor for rotation, but for dynamic opacity. And keyframes are supported. In those situations, use **Affine** or **Cairo Affine Blend** instead.

:Region:
   Like **Composite**, but restricted to a region in form of a matte. In the **Region** transition properties, this matte is called the **Transparency clip**.


Admittedly, MLT and Kdenlive offer a lot of choice here; probably too much choice. A non-representative poll in our official Kdenlive G+ community showed that **Composite** is used the most, followed by **Composite & Transform** and **Affine**.


.. _composite_with_transparency:

Compositing with Transparency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Composite & Transform** is Kdenlive's new darling, as it will make life much easier for many, if not most Kdenlive users. When compared to **Affine**, this new transition is also faster in the standard compositing cases. Moreover, **Composite & Transform** defaults to the alpha (transparency) compositing mode (paint) *over* - which is what probably most users need when compositing. In contrast, **Affine** uses the atop alpha compositing strategy that can drive unexpected users mad.

.. container:: clear-both

   .. image:: /images/composite-transition-over.png
      :align: left
      :alt: composite-transition-over
      :width: 350px

   **Composite & Transform** - whatever semi or non-transparent is in the frame from the upper track, it will be painted over the frame from the lower track. Hence the name of this compositing mode: over. Please note: in the transition properties, this mode is to be found as **Compositing**: **Alpha Blend** instead.

   In addition, **Composite**, **Cairo Blend**, and **Cairo Affine Blend** also use the same over compositing strategy, as Composite & Transform does. For **Cairo Blend** and **Cairo Affine Blend** this **Blend mode** is called **Normal** instead.

.. container:: clear-both

   .. image:: /images/affine-transition-atop.png
      :align: left
      :alt: affine-transition-atop
      :width: 350px

   **Affine** - as the simple rule of thumb, transparency is solely controlled by the *lower* track. Any transparency information from the upper track simply gets completely ignored. In consequence, if your lower frame has regions of full transparency, whatever falls within them on the upper frame will be invisible! You can see this result also in the screenshot.

   At least at this time, **Composite & Transform** does not support this alpha handling as **Affine** does.

.. rst-class:: clear-both


.. _layer_compositing:

Layer Compositing
-----------------

This third kind of Kdenlive/MLT transitions mostly work similar to layer modes in image editors, such as |gimp|, for example. These static layer compositing transitions do not have any parameters at all. This category actually has the most Kdenlive transitions to offer:

Layer Compositing
~~~~~~~~~~~~~~~~~

.. hlist::
   :columns: 3

   * Addition
   * Addition Alpha
   * Burn
   * Color Only
   * Darken
   * Difference
   * Divide
   * Dodge
   * Grain Handling: Extract / Merge
   * Hardlight / Overlay
   * Hue
   * Lighten
   * Multiply
   * Overlay / Hardlight
   * Saturation
   * Screen
   * Softlight
   * Substract
   * UV Map
   * Value
   * Video Quality Management

Alpha Compositing
~~~~~~~~~~~~~~~~~

.. hlist::
   :columns: 1

   * Alpha atop
   * Alpha in
   * Alpha out
   * Alpha over
   * Alpha XOR
   * Matte

.. note::

   Kdenlive's (or, :abbr:`MLT (Media Lovin' Toolkit - An open source software multimedia framework designed and developed for tv broadcasting)`'s) fixed compositing transitions do not have a transparency parameter. To some extent, you may substitute the **Cairo Blend** transition, which has an opacity parameter.



.. rubric:: Notes

.. |kdenlive_org| raw:: html

   <a href="https://kdenlive.org/en/project/kdenlive-transitions/" target="_blank">kdenlive.org</a>

**Sources**
  The original text was submitted by user *TheDiveO* to the now defunct kdenlive.org blog. For this documentation it has been lifted from |kdenlive_org|, updated and adapted to match the overall style.