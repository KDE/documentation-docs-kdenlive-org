.. meta::
   :description: Kdenlive Documentation - User Interface Toolbars
   :keywords: KDE, Kdenlive, use, using, toolbars, documentation, user manual, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Eugen Mohr

   :license: Creative Commons License SA 4.0

.. _toolbars:

Toolbars
========


.. _menubar:

Menubar
-------

.. image:: /images/Kdenlive_menubar.png
   :alt: Kdenlive_Menubar_bar

Not really a toolbar but it shows the :ref:`Menu` and :ref:`ui-workspace_layouts`.

It can be switched on/off in :menuselection:`Settings --> Show Menubar` or by :kbd:`Ctrl+M`.

.. .. versionadded:: 22.12

This switches between having a menubar or having a hamburger menu button in the main toolbar showing the menu items.

.. image:: /images/Kdenlive_menubar_off.png
   :alt: Kdenlive_Menubar_off

If the main tool bar is switched off you get a warning:

.. image:: /images/Kdenlive_menubar_warning.png
   :alt: Kdenlive_Menubar_off



.. _main_toolbar:

Main Toolbar
------------

.. image:: /images/Kdenlive_Main_tool_bar.png
   :alt: Kdenlive_Main_tool_bar

The main toolbar can be configured in :menuselection:`Settings --> Configure Toolbars` or right-click on the toolbar and choose :guilabel:`Configure Toolbars...`. It can be switched on/off in :menuselection:`Settings --> Toolbars Shown`.


.. _extra_toolbar:

Extra Toolbar
-------------

.. image:: /images/Kdenlive_extra_toolbar.png
   :alt: Kdenlive_extra_toolbar

The extra toolbar contains by default the **Render** button. The extra toolbar can be configured in :menuselection:`Settings --> Configure Toolbars` or right-click on the toolbar and choose :guilabel:`Configure Toolbars...`. It can be switched on/off in :menuselection:`Settings --> Toolbars Shown`.


.. _timeline_toolbar3:

Timeline Toolbar
----------------

.. image:: /images/Kdenlive_timeline_toolbar.png
   :alt: Kdenlive_timeline_toolbar

The timeline toolbar can be configured in :menuselection:`Settings --> Configure Toolbars` or right-click on the toolbar and choose :guilabel:`Configure Toolbars...`. It cannot be switched off.



.. _status_toolbar:

Statusbar
---------

.. image:: /images/Kdenlive_statusbar.png
   :align: left
   :alt: kdenlive_bottom_toolbar01

Not really a toolbar but the statusbar shows on the left hints what you can do, and on the right has switches and the zoom slider. It can be switched on and off in :menuselection:`Settings --> Show Statusbar`.

For more info on the statusbar see :ref:`editing`, :ref:`status_bar` .


.. _configuring_the_toolbars:

Configuring the Toolbars
------------------------

The tools and actions/commands that are available in the toolbars are defined in :menuselection:`Settings --> Configure Toolbars`. Alternatively, right-click anywhere in a toolbar and select :guilabel:`Configure Toolbars...`.


.. image:: /images/kdenlive_configure_toolbars.webp
   :alt: Configure Toolbars Dialogue Window

:1: Select which toolbar you want to configure

:2: List of available actions/commands/tools. You can search for them in the :guilabel:`Filter` field. Select the item you want to add to the toolbar and click on the right-arrow in (**4**)

:3: List of actions/commands/tools already available in the selected toolbar. You can search for items in the ':guilabel:`Filter` field. Select the item you want to process and click on an arrow in (**4**). Arrows up and down move the selected item up or down in the list. Arrow left deletes it from the list.

:4: Arrows to move items around in the list (up or down) and into or out of the lists (left or right).

.. tip:: If you are running out of screen space because you have many tracks it is a good idea to move commands or actions from the menu to the Extra or Timeline Toolbar, and also from the Status Bar to the Timeline Toolbar. Then switch off the menu bar in :menuselection:`Menu --> Settings --> Show Menubar` or with :kbd:`Ctrl+M` and the Status Bar in :menuselection:`Menu --> Settings --> Show Statusbar`. Please note that with the Status Bar off you will not get any keybinding information.



Hiding and Showing the Toolbars
-------------------------------

You can also control this from the :ref:`toolbars_shown` menu item in the :menuselection:`Settings` menu.
