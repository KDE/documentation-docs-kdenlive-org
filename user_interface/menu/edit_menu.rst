.. meta::
   :description: Edit menu in Kdenlive video editor
   :keywords: KDE, Kdenlive, edit, menu, undo, redo, copy, paste, effect, documentation, user manual, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Carl Schwan <carl@carlschwan.eu>
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Jack (https://userbase.kde.org/User:Jack
             - Yuri Chornoivan
             - Annew (https://userbase.kde.org/User:Annew)
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Eugen Mohr
             - Bernd Jordan


   :license: Creative Commons License SA 4.0


.. _edit_menu:

Edit Menu
=========


Undo
----

:menuselection:`Edit --> Undo` is used to reverse the last change you made or operation you performed in Kdenlive.  If you have made multiple changes to your project, **Undo** can be used repeatedly to rollback each of the changes in the reverse order they were performed. **Undo** can also be executed from the icon on the **Extra Toolbar** (:menuselection:`Settings --> Toolbars Shown`) or by using the default keyboard shortcut :kbd:`Ctrl + Z`.

To view a navigable list of all the changes which can be undone, see :ref:`Undo_History`.

Redo
----

:menuselection:`Edit --> Redo` reverses the previous `Undo`_ operation. The default keyboard shortcut is :kbd:`Ctrl + Shift + Z`.

Copy
----

Copies a clip selected in the timeline to the clipboard. The default keyboard shortcut is :kbd:`Ctrl + C`. It also copies the effects attached to the clip to the clipboard. Use `Paste`_ to paste the clip into a different spot on the timeline. Use `Paste Effects`_ to paste just the effects from the copied clip onto a different clip or group of clips.

Paste
-----

Pastes an existing clip in the clipboard into a different spot on the timeline (where the playhead is, to be exact). The default keyboard shortcut is :kbd:`Ctrl + V`.

.. _paste_effects:

Paste Effects
-------------

You need to have selected a clip and copied it first. Then select another clip or a group of clips. **Paste Effects** then pastes just the effects from the previously selected clip to the newly selected clip or group of clips.
