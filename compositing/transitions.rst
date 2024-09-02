.. meta::
   :description: Kdenlive Documentation - Compositing: Transitions
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, compositing, transition, transitions

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



###########
Transitions
###########

Video transition is a post-production technique to connect shots (clips) and tie them together into a cohesive and polished storyline. Depending on what mood or tone you want to convey, suggest passage of time, or tell different parts of the story or even show parallel story line, different transitions can and should be used. It is part of the creative process of film making.

In Kdenlive, transitions are part of :doc:`compositions <compositions>`. After all, you are compositing two clips albeit for a different purpose. But the workflow is very similar. And because transitions are added as compositions, the two terms are often used interchangeably. Just keep in mind that they are used for different purposes in video editing.

There are two ways to transition between clips:

* :doc:`transitions/mixes`, also called **same-track transitions**, between two adjacent clips in the same track
* :doc:`transitions/composite_transitions` between overlapping clips on different tracks

Available transitions range from built-in presets to wipes with different methods and the ability to use your own greyscale images in :file:`.pgm` (Portable Grey Map) format. Most wipes (and the same applies to Dissolve and Luma) are essentially greyscale images under the hood. During the transition, the composition track\ [1]_ will be displayed in the darkest part of the wipe image first; if the wipe transition is inverted, the composition track will become visible in the brightest area of the wipe image first.

Refer to :doc:`this list <transitions/transitions_list>` of all available transitions.


.. toctree:: 
  :maxdepth: 1
  :hidden:

  transitions/mixes
  transitions/composite_transitions
  transitions/slide
  transitions/wipe
  transitions/composite
  transitions/transitions_list
  transitions/add_transitions


----

.. [1] The composition track is the one the selected clip is composited with. For example, a clip on V2 overlaps with a clip on V1, and a transition is created to dissolve from V2 to V1: V1 is the Composition Track.