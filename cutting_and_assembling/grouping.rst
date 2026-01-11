.. meta::
   :description: Timeline, central part of Kdenlive video editor
   :keywords: KDE, Kdenlive, timeline, track, group clips, edit grouped clips, working, documentation, user manual, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Vincent Pinon <vpinon@kde.org>
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Eugen Mohr

   :license: Creative Commons License SA 4.0

.. _grouping:

Grouping
========


Grouping clips allows you to lock clips together so that you can move them as a group and still retain their positions relative to each element in the group. 

.. _group_clips:

How to group clips
------------------

You can select multiple clips in preparation for grouping them by holding shift and clicking the mouse and dragging in the timeline.


.. image:: /images/Kdenlive_Shift_click_drag_to_multi_select.png
   :align: left


To group the selected clips select :menuselection:`Timeline --> Group Clips` or right-click the selected clips and choose :menuselection:`Group Clips` or use the shortcut :kbd:`Ctrl+G`.

Once grouped together a click on one of the grouped clips selects the entire group.

.. rst-class:: clear-both


.. _group_clips_edit:

.. .. versionadded:: 24.02

Edit grouped clips
------------------

Select an item in a group with :kbd:`Alt+click` and it gets a red border. You can then perform on that clip following operations:

- delete (hit :kbd:`del`)
- move (drag with the mouse)



.. _group_clips_cutting:

Cutting grouped clips
---------------------

Grouping is also useful if you have separate audio and video tracks and need to cut and splice both tracks at exactly the same point (e.g. for audio sync reasons). 


If you cut the video clip using the :ref:`editing` when there is an audio clip grouped to it, then **Kdenlive** cuts the audio clip at the same point automatically.

.. image:: /images/Kdenlive_Grouped_video_audio.png
  :align: left

.. image:: /images/kdenlive_arrow_right.png
   :align: left

.. image:: /images/Kdenilve_Cutting_grouped_clips.png
   :align: right


.. rst-class:: clear-both


.. .. versionadded:: 24.05

.. _grouped_clips_effect:

Effects on grouped clips
------------------------

.. figure:: /images/kdenlive2405_effect-on-grouped_clips.webp
   :align: left


When :guilabel:`Apply effect change to all clips in the group` is enabled, adjusting a parameter for an effect will apply it to all items in the group which have this effect too.

When enabled, an orange number appears next to the effect name to indicate how many effects are found in the group and will be affected by a change of parameters.

Deleting an effect will delete it on all clips in the group.

.. figure:: /images/kdenlive2405_effect-value-on-grouped_clips.webp
   :align: left


.. rst-class:: clear-both

When :guilabel:`Apply only to effects with the same value` is enabled, only change effects that have the same parameter value.

.. _ungroup_clips:

Removing clip grouping
----------------------

To remove the grouping on clips, select the group of clips and choose :menuselection:`Timeline --> Ungroup Clips` or right-click the selected clips and choose :menuselection:`Ungroup Clips` or use the shortcut :kbd:`Ctrl+Shift+G`.


FAQ
~~~

Q: How to delete the audio part of a clip?

A: Right-click on the clip and choose :menuselection:`Ungroup Clips`. Then you can delete just the audio part of the clip. 

.. image:: /images/Kdenlive_Grouped_video_audio.png
   :align: left


Alternatively you can keep the audio in the clip and use the :guilabel:`Mute` effect to just mute the audio on the clip.
