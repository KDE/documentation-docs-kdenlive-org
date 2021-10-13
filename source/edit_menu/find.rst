.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)

   :license: Creative Commons License SA 4.0

.. _find:


Edit Menu - Find
================

.. contents::




This feature can be used to quickly locate a clip or clips in the timeline. In order to use it, you must be in **Project Monitor** mode. Clicking :menuselection:`Edit --> Find` (or the default shortcut **/**) turns on "find text as you type" for five seconds or so. As you type, an incremental search is performed which attempts to match any part of a clip name to the characters you are typing. For instance, in the example shown below, as you type "0", the timeline cursor would move to the first clip on the timeline because that is the first clip that has a "0" in its name. After you've typed "00", the cursor has not moved because that clip is still a match. However, once you've typed "005", the cursor jumps to the clip shown since it's the first one that has a match for all three characters. The results of your search are displayed in the left corner of the status bar. If you pause typing for more than five seconds, the "find text as you type" timer will expire. See :ref:`find_next` for how to find additional occurrences of matching clips.



.. image:: /images/Kdenlive_Edit_find.png


There is also a find window at the top of the :ref:`project_tree`. Typing text in here causes the list of clips in the project tree to be filtered.


.. image:: /images/Clip_filter.png


This clip filtering is independent of the :menuselection:`Edit --> Find` menu item.


