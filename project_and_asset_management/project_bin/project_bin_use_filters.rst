.. meta::
   :description: Kdenlive Documentation - Using the Project Bin - Filters
   :keywords: KDE, Kdenlive, project bin, filter, using, documentation, user manual, video editor, open source, free, learn, easy

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


.. |filter-on| image:: /images/project_and_asset_management/project_bin_filter_on.webp

.. |filter-off| image:: /images/project_and_asset_management/project_bin_filter_off.webp


.. ====================================================================================================
   This file is being .. include(d):: in project_bin_use.rst and the chapter title designation follows the structure of the parent file. Hence the use of --- and ~~~ as chapter designation
   ====================================================================================================


Using Filters
-------------

Filters are an easy way to quickly narrow down assets by tag, rating, type, or whether or not they are being used in the timeline.

.. .. versionchanged:: 23.1

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/project_bin_filter.webp
      :width: 334px
      :figwidth: 334px
      :align: left
   
      Filtering options
      
   :1: Category *Tags*

   :2: Category *Rating*

   :3: Category *Usage*

   :4: Category *Type*

.. rst-class:: clear-both


Filters are applied in an OR way between objects of the same category, and in an AND way between different categories.

.. rubric:: Example

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/project_bin_filter_example.webp
      :width: 334px
      :figwidth: 334px
      :align: left
   
      Filtering options
      
   This filter setting shows all assets that have a *red* OR *blue* tag, AND have a rating of *4 stars*, AND are *unused*, AND are an *AV Clip* (file with video and audio streams) OR a *Mute Video* (file with only a video stream).

.. rst-class:: clear-both

If filter criteria have been set, the filter icon in the project bin toolbar changes background color. Filter **on**: |filter-on| - filter **off**: |filter-off|