.. meta::
   :description: Render out your final Kdenlive video for distributing
   :keywords: KDE, Kdenlive, render, distribute, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Eugen Mohr
             - Bernd Jordan

   :license: Creative Commons License SA 4.0

.. _exporting:

#########
Exporting
#########

Exporting in Kdenlive means Rendering, or vice versa. Rendering turns the project's timeline with all the edited clips into the final product: a single complete video file.

Kdenlive uses *Presets* or *Rendering Profiles* to control or determine the output. You can create your own presets and profiles.

Hit :kbd:`Ctrl+Return` to open the rendering dialog or use the :menuselection:`Menu --> File --> Render` and click on the render button |media-record|.

.. figure:: /images/exporting/kdenlive2212_rendering-render_dialog.webp
   :width: 400px
   :figwidth: 400px
   :align: left
  
   Rendering dialog window

* Select the :guilabel:`Output file` location

* Select the desired :guilabel:`Presets`. MP4-H264/AAC works nearly everywhere.

* Click on :guilabel:`Render to File` button.

.. rst-class:: clear-both

Once the video is rendered you can double-click the blue banner with the file name to start playback.

.. figure:: /images/exporting/kdenlive2402_rendering-window.webp
   :width: 400px
   :figwidth: 400px
   :align: left

   Window after rendering is complete

.. rst-class:: clear-both

Or right-click on the file name to either :guilabel:`Add to current  project` or :guilabel:`Open contained folder` where the video is saved.  

.. toctree::
   :hidden:
   :glob:

   exporting/render
