.. meta::
   :description: Kdenlive Documentation - Project Bin - Image Sequence
   :keywords: KDE, Kdenlive, add clips, image, image sequence, title clip, editing, timeline, documentation, user manual, video editor, open source, free, learn, easy

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

     

Image Sequence
==============

Image sequence clips are clips created from a series of still images. The feature can be used to make an animation from a collection of still images or to create a slideshow of still images. To create the former, use a short frame duration; to create the latter, use a long frame duration.

Right-click on empty space in the project bin, or click the |kdenlive-add-clip|\ |go-down|\ :guilabel:`Add Clip` icon on the project bin toolbar, and select :guilabel:`Add Image Sequence`.

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/project_bin_add_image_sequence.webp
      :align: left
      :width: 206px
      :figwidth: 206px
      :alt: project_bin_add_image_sequence

      Adding an image sequence

   This opens a dialog window to specify further details.

.. rst-class:: clear-both

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/project_bin_image_sequence.webp
      :align: left
      :width: 360px
      :figwidth: 360px
      :alt: project_bin_image_sequence

      Image sequence details

.. rst-class:: clear-both

:guilabel:`Name`: Enter the name of the image sequence. You can change it later from within the project bin.

:guilabel:`MIME Type`: When enabled, the images get imported in ascending order using a simple alphabetic sorting method. It is recommended to get the images into the right order before adding the image sequence. 

:guilabel:`Filename pattern`:  When enabled, you can point to the first image you like to import. The remaining images get imported in ascending order.

:guilabel:`Folder`: Browse to the location of the images which will make up your image sequence and select the first image. The subsequent images that are to be used in the slide show will be selected based on some sort of filename algorithm that predicts what the next image file name should be.

:guilabel:`Frame Duration`: Enter the duration for each image to be displayed. Select the format you want to use from the drop-down list. By default, the :abbr:`hh:mm:ss:ff(hours:minutes:seconds:frames)` format is used; alternatively you can use frames.

:guilabel:`Loop`: When enabled, you can lengthen the image sequence clip in the timeline by dragging. Otherwise the image sequence clip is only as long as the number of images times the frame duration.

:guilabel:`Center Crop`: When enabled, it automatically fills the output video frame with the images while maintaining their aspect ratio by zooming the image and cropping equal amounts from each edge until they fill the full frame. Without this option, the images will not be zoomed, but black bars will appear when the photo orientation or aspect ratio does not match the project settings.

:guilabel:`Dissolve`: When enabled, you can adjust the length of the dissolve (format depends on the selection of format at :guilabel:`Frame duration`), choose the type of :guilabel:`Wipe`, and adjust it with the :guilabel:`Softness` slider.

:guilabel:`Animation`: When enabled, it adds preset slow smooth pan and zoom effects also known as the Ken Burns Effect\ [1]_. You can choose :guilabel:`None` (no animation), :guilabel:`Pan`, :guilabel:`Pan and Zoom`, or :guilabel:`Zoom`. Each option also has a low pass filter to reduce the noise in the images that may occur during this operation. Low pass filtering is much slower, so you should preview without it, and then enable it for the final render.

The box a the bottom of the window shows the files that will be included in the image sequence. Check :guilabel:`Show thumbnails` to switch on thumbnails for the files.

When you press :guilabel:`OK`, a video file made up of all the images you selected will be added to the project bin.

You can then drag this video to the timeline.

To edit the slideshow parameters and to switch on :guilabel:`Low pass`, either double-click the image sequence in the project bin or right-click and choose :guilabel:`Clip Properties`.


----

.. |ken_burns_effect| raw:: html

   <a href="https://en.wikipedia.org/wiki/Ken_Burns_effect" target="_blank">Ken Burns Effect</a>
   

.. [1] The Ken Burns Effect describes a technique used extensively by American documentary maker Ken Burns that turns still images into something moving. Essentially, it applies a pan and zoom over an image giving it the impression of movement. See the Wikipedia article about the |ken_burns_effect|.