.. meta::
   :description: Kdenlive Tips & Tricks - Extract Frame to Project
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, extract frame, project, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - TheDiveO
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0


Extract Frame to Project
========================

If you happen to work a lot with still images from your video source material in your Kdenlive project, then you may like the new :guilabel:`Extract Frame to Project`. Instead of the tedious mill of extract clip, thinking of a usable image filename other than :file:`adshsgfg.png`, then finding this file again to add it to your project … simply let Kdenlive propose a suitable filename, click OK, and you are set.

.. figure:: /images/tips_and_tricks/kdenlive2308_extract_frame_to_project.webp
   :align: left
   :width: 250px
   :figwidth: 250px
   :alt: kdenlive-extract-clip-to-project

   Clip and Project Monitor right-click menu item

The clip and project monitors now have a new context menu item :guilabel:`Extract Frame to Project`, in addition to the existing :guilabel:`Extract Frame`. This new menu item not only extracts the currently shown frame, but also adds it automatically to your project.

.. rst-class:: clear-both

You will still see the :guilabel:`Save Image` dialog, but there is an additional convenience: Kdenlive now proposes an image filename. This is based either (in the clip monitor) on the clip name, or (in the project monitor) on the project filename. To avoid filename clashes when extracting multiple frames from the same source clip or project, Kdenlive neatly adds the frame number. So, when extracting frames from your clip named :file:`coolclip.mp4`, the suggested image names are like :file:`coolclip-f42.png`, and so on. Of course, you can still use your own filenames as before. But you will probably soon start to like just forgetting about filenames, as it is so convenient to focus on content, not clip names.

The extracted image is immediately added to your project bin. If you use bin folders, then the image gets added to your currently selected bin folder.

On purpose, Kdenlive **does not** switch to the project bin. This way, you can focus on extracting the required still images from a source video clip, without loosing context all the time. However, the extracted frame is not copied or saved to your file system.

In contrast, the :guilabel:`Extract Frame` feature copies and saves the extracted frame to your file system so you can edit or otherwise use the image elsewhere. However, it does not add the extracted frame to your project immediately.



.. rubric:: Notes

.. |kdenlive_org| raw:: html

   <a href="https://kdenlive.org/en/project/extract-frame-to-project/" target="_blank">kdenlive.org</a>

**Sources**
  The original text was submitted by user *TheDiveO* to the now defunct kdenlive.org blog. For this documentation it has been lifted from |kdenlive_org|, updated and adapted to match the overall style.