.. meta::
   :description: Kdenlive Documentation - Project Bin - Create Animation
   :keywords: KDE, Kdenlive, add clips, animation, editing, timeline, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Gallaecio (https://userbase.kde.org/User:Gallaecio)
             - Simon Eugster <simon.eu@gmail.com>
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Carl Schwan <carl@carlschwan.eu>
             - Eugen Mohr
             - Tenzen (https://userbase.kde.org/User:Tenzen)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

     
.. |glaxnimate| raw:: html

   <a href="https://glaxnimate.mattbas.org/" target="_blank">Glaxnimate</a>


Create Animation
================

.. .. versionadded:: 22.08

Right-click on empty space in the project bin, or click the |kdenlive-add-clip|\ |go-down|\ :guilabel:`Add Clip` icon on the project bin toolbar, and select :guilabel:`Create Animation`.

.. note:: 
   This requires |glaxnimate| to be installed and the path to it configured in Kdenlive's :doc:`settings</user_interface/menu/settings_menu/configure_kdenlive>`.

.. figure:: /images/project_and_asset_management/project_bin_create_animation.webp
   :width: 206px
   :figwidth: 206px
   :align: left
   :alt: project_bin_create_animation

   Creating an animation

This opens a dialog window to enter a name for the :file:`.rawr` file Kdenlive creates before opening Glaxnimate.

If Glaxnimate is not configured, you are presented with a dialog box to enter the path to Glaxnimate.

.. rst-class:: clear-both

You can edit the animation in Glaxnimate by double-clicking on the animation in the project bin, or by right-clicking and selecting :guilabel:`Edit Clip`.

For further details about editing an animation see the chapter :doc:`/titles_and_graphics/graphics_and_animations/glaxnimate`. 

Kdenlive supports the :file:`Json` (Lottie animations) and :file:`rawr` (Glaxnimate animation) file formats.

:file:`Json` and :file:`rawr` files contain an alpha channel, so the imported animations can be overlayed over other clips in the timeline.

For Glaxnimate installation see the chapter about :ref:`default_apps`.
