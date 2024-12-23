.. meta::
   :description: Kdenlive Documentation - Using the Project Bin - Tags
   :keywords: KDE, Kdenlive, project bin, working, using, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Carl Schwan <carl@carlschwan.eu>
             - Eugen Mohr
             - Smolyaninov (https://userbase.kde.org/User:Smolyaninov)
             - Tenzen (https://userbase.kde.org/User:Tenzen)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. ====================================================================================================
   This file is being .. include(d):: in project_bin_use.rst and the chapter title designation follows the structure of the parent file. Hence the use of --- and ~~~ as chapter designation
   ====================================================================================================

.. _project_bin_using_tags:

Using Tags
----------

Tags are a good way to stay organized as they give you a quick overview of the nature of your assets. You can create as many tags as you need, assign different colors, and change the default tags. After you assigned tags to your assets you can then quickly filter by tags making it much easier to assemble the clips in the timeline and building your story.

.. attention:: 
   Kdenlive adjusts the width of the project bin widget to accommodate all tags and their description. It is recommended to keep the number of tags and the length of the description as small as possible to conserve valuable screen real estate for other widgets (in particular the timeline and monitors). If you have multiple monitors at your disposal consider undocking some of the widgets and moving them off the main screen used for editing.

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/project_bin_toolbar_tags.webp
      :width: 360px
      :figwidth: 360px
      :align: left
      :alt: project_bin_toolbar_tags
      
      Enabling the tags panel

   Click on the |tag|\ :guilabel:`Tags Panel` icon in the project bin toolbar to enable the panel.

.. rst-class:: clear-both


Assigning Tags
~~~~~~~~~~~~~~

.. .. versionadded:: 20.04.0

Assigning tags is as simple as selecting a clip and then clicking the appropriate tag in the panel. 

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/project_bin_tags_assign.gif
      :width: 334px
      :figwidth: 334px
      :align: left
      :alt: project_bin_tags_assign
   
      Assigning tags to clips

   A clip can have more than one tag.
   
   Click the tag again to remove it from the clip

.. rst-class:: clear-both


.. .. versionadded:: 22.08

Editing Tags
~~~~~~~~~~~~

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/project_bin_tags_edit.gif
      :width: 334px
      :figwidth: 334px
      :align: left
      :alt: project_bin_tags_edit

      Editing tags
      
   You can change the description and color of existing tags.

   Click on |edit-delete|\ :guilabel:`Delete` to delete a tag.

   Click on |tag-add|\ :guilabel:`Add tag` to add a new tag.

   Make sure to click |document-save|\ :guilabel:`Save` to save the changes.

.. rst-class:: clear-both

.. hint::
   You can change the order of the tags in the panel by simply grabbing a tag and dragging it to the desired place in the panel.


Filtering by Tags
~~~~~~~~~~~~~~~~~

You can filter the project bin list using tags.

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/project_bin_tags_filter.gif
      :width: 334px
      :align: left
      :alt: project_bin_tags_filter

      Filtering using tags

   Note how the background of the |view-filter|\ icon changes as soon as filter criteria have been selected.

   Filter criteria within the same category (like *tag* or *rating*) are applied in an OR fashion, meaning that all clips with any of the selected criteria will be listed (red OR green *tag*).

   Filter criteria across different categories are applied in an AND fashion, meaning that clips with criteria from both categories will be listed (red OR green *tag* AND with four OR five *stars*)

   For more details refer to the chapter about :doc:`using filters</project_and_asset_management/project_bin/project_bin_use_filters>`.

.. rst-class:: clear-both

|