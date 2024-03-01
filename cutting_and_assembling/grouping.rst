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
   :alt: Kdenlive_Shift_click_drag_to_multi_select


To group the selected clips select :menuselection:`Timeline --> Group Clips` or right-click the selected clips and choose :menuselection:`Group Clips` or use the shortcut :kbd:`Ctrl+G`.

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
  :alt: Kdenlive_Grouped_video_audio

.. image:: /images/kdenlive_arrow_right.png
   :align: left
   :alt: kdenlive_arrow_right

.. image:: /images/Kdenilve_Cutting_grouped_clips.png
   :align: right
   :alt: Kdenilve_Cutting_grouped_clips


.. rst-class:: clear-both


.. _ungroup_clips:

Removing clip grouping
----------------------

To remove the grouping on clips, select the group of clips and choose :menuselection:`Timeline --> Ungroup Clips` or right-click the selected clips and choose :menuselection:`Ungroup Clips` or use the shortcut :kbd:`Ctrl+Shift+G`.


FAQ
~~~

Q: How to delete sound track only?

A: Right-click on the clip and choose :menuselection:`Split Audio`. The audio will move to an audio track but be grouped with the video track.

.. image:: /images/Kdenlive_Grouped_video_audio.png
   :align: left
   :alt: Kdenlive_Grouped_video_audio

Right-click again and choose :menuselection:`Ungroup Clips`. 

Then you can delete just the audio track. 

Alternatively you can keep the audio in the clip and use the :menuselection:`Audio Correction --> Mute` effect to just mute the soundtrack on the clip.

Yet another method is to select :menuselection:`Video only` from the :ref:`clip_menu`.


