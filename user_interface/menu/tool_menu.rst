.. metadata~placeholder

   :authors: - Yuri Chornoivan
             - Jack (https://userbase.kde.org/User:Jack)
             - Carl Schwan <carl@carlschwan.eu>
             - Eugen Mohr
             - Bernd Jordan

   :license: Creative Commons License SA 4.0

.. _tool_menu:

Tool Menu
=========


.. figure:: /images/user_interface/menu_reference/kdenlive_tool_menu.webp
   :align: left
   :alt: kdenlive_tool_menu
   
   Tool Menu


The options on this menu provide three modes and six tools which determine how operations are performed on clips in the timeline. The same options can also be accessed from :ref:`timeline_edit_modes` and :ref:`timeline_edit_tools`. More details on their usage can be found there.

.. rst-class:: clear-both

Modes
-----

Normal Mode
~~~~~~~~~~~

Allows clips to be added to the timeline only where there is enough space to fit them in.


Overwrite Mode
~~~~~~~~~~~~~~

Allows clips to be added to the timeline anywhere overwriting that portion of clips already there.


Insert Mode
~~~~~~~~~~~

Allows clips to be added to the timeline anywhere cutting and shifting clips already there to accommodate the inserted clip


Tools
-----

.. tip:: :kbd:`ESC` will always switch from any selected timeline editing tool back to the Selection Tool.

Selection Tool
~~~~~~~~~~~~~~

Use this to select clips in the timeline. Default keyboard shortcut is :kbd:`S`.


Razor Tool
~~~~~~~~~~

Use this to cut clips in the timeline. Default keyboard shortcut is :kbd:`X`.


Spacer Tool
~~~~~~~~~~~

Use this to create or remove space in the timeline between clips. Temporarily groups clips for dragging them for this purpose. Default keyboard shortcut is :kbd:`M`.


Slip Tool
~~~~~~~~~

Use this to trim, in a single operation, the In and Out points of the clip maintaining its position and duration in the timeline.


Ripple Tool
~~~~~~~~~~~

Use this to trim one clip and shift the adjacent clip accordingly.


Multicam Tool
~~~~~~~~~~~~~

Use this to cut between several cameras/tracks while playback is running. Will switch on the :ref:`multitrack view <ui-multitrack_view>` in the project monitor.
