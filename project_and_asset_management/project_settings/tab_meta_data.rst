.. meta::
   :description: Kdenlive Documentation - Project Metadata
   :keywords: KDE, Kdenlive, project, setup, settings, metadata, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Jean-Baptiste Mardelle <jb@kdenlive.org>
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Vincent Pinon <vpinon@kde.org>
             - Jack (https://userbase.kde.org/User:Jack)
             - Tenzen (https://userbase.kde.org/User:Tenzen)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


   
Project Metadata
================

This tab stores metadata about your project. By default, there are fields for **Title**, **Author**, **Copyright** and **Year**. You can add as many other fields as you need.

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/project_settings_metadata.webp
      :width: 360px
      :figwidth: 360px
      :align: left
   
      The Project Settings Metadata dialog window

Double-click an existing field to enter text.

|list-add|\ :guilabel:`Add field`: Adds a new field. In the dialog box enter the name of the field.

|list-remove|\ :guilabel:`Remove field`: Removes the selected field. You can remove the default fields.

.. rst-class:: clear-both

The data set up here will be written to the rendered files if :guilabel:`Export metadata` is checked in :doc:`/exporting/render` dialog window under :guilabel:`More Options`.

You can check the metadata in the rendered video by entering this in a terminal window:

.. code-block:: bash

  $ ffprobe <your_video>