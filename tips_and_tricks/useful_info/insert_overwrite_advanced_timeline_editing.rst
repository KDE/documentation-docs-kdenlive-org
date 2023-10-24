.. meta::
   :description: Kdenlive Tips & Tricks - Insert and Overwrite: Advanced Timeline Editing
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, useful information, insert, overwrite, advanced, timeline, editing, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - TheDiveO
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0


Insert and Overwrite: Advanced Timeline Editing
===============================================

.. .. versionadded:: 15.12.0

Kdenlive offers advanced timeline editing functions. In this chapter we are looking at the **Insert** |timeline-insert| and **Overwrite** |timeline-overwrite| advanced editing functions.

When inserting or overwriting some part in the timeline with some part from a clip, we now face two zones, so how does this work out at all? We only want to deal with three points, that is, with one zone and a point (for that reason this is also sometimes called **3-Point Editing**). In consequence, there are two different insert/overwrite operations:

1. Insert/overwrite a clip zone into the timeline at some point (cursor/playhead), or
2. Insert/overwrite a clip starting at some point into a timeline zone

.. _advanced_editing-insert:

Insert Clip Zone into Timeline at Timeline Cursor
-------------------------------------------------

..    .. image:: /images/timline-use-zone.png

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_editing_01.gif
      :align: left
      :alt: kdenlive2308_editing_01.gif
      :width: 350px

      Toggle the use of the timeline zone

   As we are going to insert a clip zone into the timeline, first make sure that the switch for Using Timeline Zone |timeline-use-zone-off| is crossed out (it is *off*).

   The **timeline zone bar** is now *dimmed* and does not show the zone duration.

..   .. image:: /images/clip-monitor-with-zone.png

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_editing_insert_01.webp
      :align: left
      :alt: kdenlive2308_editing_insert_02.webp
      :width: 350px

      Setting the clip region for insertion

   Next, mark the **clip region** of the source clip you want to insert into the timeline. You do this as usual, using either the :kbd:`I` and :kbd:`O` shortcuts, or the set Zone In |zone-in| / Zone Out |zone-out| buttons of the clip monitor.

..   .. image:: /images/timline-select-position-and-track-e1477318374733.png

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_editing_insert_02.webp
      :align: left
      :alt: kdenlive2308_editing_insert_01.webp
      :width: 350px

      Setting the insertion point in the timeline

   Now **place the timeline cursor** to where you want to start with the insert.

   Also make sure to select the **correct track** using the :kbd:`Up` and :kbd:`Down` keys to navigate up and down the track list and then :kbd:`Shift+T` to mark the track as the target for the operation. The currently selected track is marked with a semi-transparent selection color (depending on your particular color theme); the **active** track is marked with a green box (see **(1)** in the screenshot)

..   .. image:: /images/timeline-insert-clip-zone-after.png

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_editing_insert_03a.webp
      :align: left
      :alt: kdenlive2308_editing_insert_03a.webp
      :width: 350px

      Clip region inserted in the timeline

   Finally press the :kbd:`V` shortcut, or click the Insert Clip Zone toolbar button |timeline-insert|, or use :menuselection:`Menu --> Timeline --> Insertion --> Insert Clip Zone in Timeline`.

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_editing_insert_03b.webp
      :align: left
      :alt: kdenlive2308_editing_insert_03a.webp
      :width: 350px

      Clip region inserted in the timeline

   Note that the insert shifted also not-active tracks to make room for the inserted clip. In order to avoid that, lock the other tracks by clicking on the |track-unlocked| icon in the track header (see **(2)** in the screenshots).

.. rst-class:: clear-both

.. note::

   * Insertion starts at the timeline cursor, and not at the timeline zone start (because we chose to ignore it in our very first step).
   * Locked tracks are unaffected, such as the topmost track in our example.
   * Unlocked tracks get affected in that whatever is at the insertion point and later in the timeline gets shifted away to make room for the insertion.

Insert Clip (from In Point) into Timeline Zone
----------------------------------------------

..   .. image:: /images/timline-use-timeline-zone.png

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_editing_01.gif
      :align: left
      :alt: kdenlive2308_editing_01.gif
      :width: 350px

   This time, we are going to insert some part of a clip to *exactly fit* into the timeline zone. So we now need to switch on Using the Timeline Zone |timeline-use-zone-on|.

   The **timeline zone bar** is now *bright* and shows the duration of the timeline zone.

..   .. image:: /images/clip-monitor-with-in-point.png

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_editing_insert_04.webp
      :align: left
      :alt: kdenlive2308_editing_insert_04.webp
      :width: 350px

      Setting the in-point in the clip for insertion

   We only need to set the **in point** for our source clip. The out point does not matter, as it will be determined automatically by the length of the timeline zone.

..   .. image:: /images/timeline-use-timeline-zone-before.png

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_editing_insert_05.webp
      :align: left
      :alt: kdenlive2308_editing_insert_05.webp
      :width: 350px

      Defining the timeline zone to be overwritten

   Now, mark (using :kbd:`I` and :kbd:`O` or |zone-in| or |zone-out| ) or place (drag the zone left or right) the **timeline zone** into which you want to insert a part of your source clip. The timeline cursor position now does not matter.

   Make sure to select the **correct track** using the :kbd:`Up` and :kbd:`Down` keys and pressing :kbd:`Shift+T` to mark the track as the target for the operation (see **(1)** in the screenshot).

..   .. image:: /images/timeline-insert-timeline-zone-after.png

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_editing_insert_06.webp
      :align: left
      :alt: kdenlive2308_editing_insert_06.webp
      :width: 350px
      :figwidth: 350px

      Timeline with clip inserted into and having overwritten the timeline zone

   Finally press the :kbd:`V` shortcut, or click the Insert Clip Zone toolbar button |timeline-insert|, or use :menuselection:`Menu --> Timeline --> Insertion --> Insert Clip Zone in Timeline`.

.. rst-class:: clear-both
   
.. note::
   
   * Overwrite starts at the beginning of the timeline zone, and not at the timeline cursor position (because we chose to enable the timeline zone in our very first step)
   * Locked tracks are unaffected, such as the top-most track in our example
   * Unlocked tracks get affected in that whatever is at the insertion point and later in the timeline gets shifted away to make room for the insertion


.. _advanced_editing-overwrite:

Overwrite Timeline with Clip Zone
---------------------------------

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_editing_01.gif
      :align: left
      :alt: kdenlive2308_editing_01.gif
      :width: 350px

      Toggle the use of the timeline zone

   As we are going to overwrite a clip zone into the timeline, first make sure that the switch for Using Timeline Zone |timeline-use-zone-off| is crossed out (it is *off*). This is also shown in the screenshot.

   The **timeline zone bar** is now *dimmed* and does not show the zone duration.

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_editing_overwrite_01.webp
      :align: left
      :alt: kdenlive2308_editing_insert_02.webp
      :width: 350px

      Setting the clip region for the operation

   Next, mark the **clip region** of the source clip you want to insert and overwrite what is in the timeline. You do this as usual, using either the :kbd:`I` and :kbd:`O` shortcuts, or the set Zone In |zone-in| / Zone Out |zone-out| buttons of the clip monitor.

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_editing_overwrite_02.webp
      :align: left
      :alt: kdenlive2308_editing_insert_01.webp
      :width: 350px

      Setting the overwrite start point in the timeline

   Now **place the timeline cursor** to where you want to start the overwrite.

   Also make sure to select the **correct track** using the :kbd:`Up` and :kbd:`Down` keys to navigate up and down the track list and pressing :kbd:`Shift+T` to mark the track as the target for the operation. The currently selected track is marked with a semi-transparent selection color (depending on your particular color theme); the **active** track is marked with a green box (see **(1)** in the screenshot)

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_editing_overwrite_03.webp
      :align: left
      :alt: kdenlive2308_editing_insert_03a.webp
      :width: 350px

      Clip region overwrote parts of the timeline

   Finally press the :kbd:`B` shortcut, or click the Overwrite Clip Zone toolbar button |timeline-overwrite|, or use :menuselection:`Menu --> Timeline --> Insertion --> Overwrite Clip Zone in Timeline`.

   .. rst-class:: clear-both

Note that the overwrite removed the same portion also in not-active tracks. In order to avoid that, lock the other tracks by clicking on the |track-unlocked| icon in the track header (see **(2)** in the screenshots).

.. note::

   * Overwrite starts at the timeline cursor, and not at the timeline zone start (because we chose to ignore it in our very first step).
   * Locked tracks are unaffected, such as the topmost track in our example.
   * Unlocked tracks get affected in that whatever is at the insertion point and later in the timeline gets removed for the duration of the clip region.


Overwrite Timeline Zone with Clip
---------------------------------

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_editing_01.gif
      :align: left
      :alt: kdenlive2308_editing_01.gif
      :width: 350px

      Toggle the use of the timeline zone

   This time, we are going to insert some part of a clip to *exactly fit* into the timeline zone and *overwrite* what is in it. So we now need to switch on Using the Timeline Zone |timeline-use-zone-on|.

   The **timeline zone bar** is now *bright* and shows the duration of the timeline zone.

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_editing_overwrite_04.webp
      :align: left
      :alt: kdenlive2308_editing_insert_04.webp
      :width: 350px

      Setting the in-point in the clip for the operation

   We only need to set the **in point** for our source clip. The out point does not matter, as it will be determined automatically by the length of the timeline zone.

..   .. image:: /images/timeline-use-timeline-zone-before.png

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_editing_overwrite_05.webp
      :align: left
      :alt: kdenlive2308_editing_overwrite_05.webp
      :width: 350px

      Defining the timeline zone for overwriting

   Now, mark (using :kbd:`I` and :kbd:`O` or |zone-in| or |zone-out| ) or place (drag the zone left or right) the **timeline zone** that you want to overwrite with part of your source clip. The timeline cursor position now does not matter.

   Make sure to select the **correct track** using the :kbd:`Up` and :kbd:`Down` keys and pressing :kbd:`Shift+T` to mark the track as the target for the operation. The currently selected track is marked with a semi-transparent selection color (depending on your particular color theme); the **active** track is marked with a green box (see **(1)** in the screenshot).

..   .. image:: /images/timeline-insert-timeline-zone-after.png

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_editing_overwrite_06.webp
      :align: left
      :alt: kdenlive2308_editing_overwrite_06.webp
      :width: 350px
      :figwidth: 350px

      Timeline with clip having overwritten the timeline zone

   Finally press the :kbd:`B` shortcut, or click the Overwrite Clip Zone toolbar button |timeline-overwrite|, or use :menuselection:`Menu --> Timeline --> Insertion --> Overwrite Clip Zone in Timeline`.

.. rst-class:: clear-both
   
.. note::
   
   * Overwrite starts at the beginning of the timeline zone, and not from the timeline cursor position (because we chose to enable the timeline zone in our very first step)
   * Locked tracks are unaffected, such as the top-most track in our example (see **(2)** in the screenshot above)
   * Unlocked tracks get affected in that whatever is at the insertion point and later in the timeline gets shifted for the duration set by the timeline zone.


.. rubric:: Notes

.. |kdenlive_org| raw:: html

   <a href="https://kdenlive.org/en/project/insert-overwrite-advanced-timeline-editing/" target="_blank">kdenlive.org</a>

**Sources**
  The original text was submitted by user *TheDiveO* to the now defunct kdenlive.org blog. For this documentation it has been lifted from |kdenlive_org|, updated, extended and adapted to match the overall style.