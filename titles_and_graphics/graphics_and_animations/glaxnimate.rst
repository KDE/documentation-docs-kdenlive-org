.. meta::
   :description: Kdenlive Documentation - Glaxnimate Animations
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, titles, title clip, animation, graphics, vector

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |glaxnimate| raw:: html

   <a href="https://glaxnimate.mattbas.org/" target="_blank">Glaxnimate</a>

.. |glaxnimate_download| raw:: html

   <a href="https://glaxnimate.mattbas.org/download/#stable-releases" target="_blank">Glaxnimate Download</a>

.. |glaxnimate_manual| raw:: html

   <a href="https://glaxnimate.mattbas.org/manual/" target="_blank">Glaxnimate Manual</a>


===========================
Integration with Glaxnimate
===========================

Kdenlive is integrated with |glaxnimate| for vector graphics and animations. It is an independently developed and maintained software, and needs to be downloaded and installed separately. Glaxnimate is available for Linux as an appimage and Deb package (both maintained by the developer), as well as a package for AUR, Snap, PyPl, FreeBSD, and FlatPak, for Windows as a ZIP file, and for MacOS as DMG. For more details refer to the |glaxnimate_download| page.

Kdenlive needs to know where to find Glaxnimate. You set up the path to Glaxnimate in :menuselection:`Menu --> Settings --> Configure Kdenlive --> Environment --> Default Apps` (default shortcut :kbd:`Ctrl+Shift+,`) under the heading :guilabel:`Animation editing`.

:Linux: Depending on your Glaxnimate installation method (appimage or package)
:Windows: Locate the executable :file:`.exe` file (usually :file:`C:\\Program Files (x86)\\glaxnimate-x86_64\\glaxnimate\\bin\\glaxnimate.exe`)


.. rubric:: Creating an Animation

In the Project Bin, click in |kdenlive-add-clip|\ |go-down|\ :guilabel:`Add Clip or folder` and select :guilabel:`Create animation`, or right-click empty space in the Project Bin and select :guilabel:`Create animation`.

.. container:: clear-both

   .. figure:: /images/titles_and_graphics/animation-create_animation.webp
      :width: 360px
      :figwidth: 360px
      :alt: animation-create_animation
      :align: left

      Create animation dialog window

   In the dialog window, enter a name for the animation. If you want to save it in a different folder, click on the |document-open|\ :guilabel:`Open file` button to open a *Save As* dialog window. Make sure you specify the :file:`.rawr` file type.

.. rst-class:: clear-both

By default, the animation duration is set to be 5 seconds long. If you need a different duration, you can enter a new :guilabel:`Animation duration` in the format :abbr:`hh:mm:ss:ff(hours:minutes:seconds:frames)`.

.. note:: 
   You can always change the duration later by dragging the right-hand edge of the animation clip in the timeline, or by right-clicking the clip in the timeline and selecting :guilabel:`Edit duration`. However, this is not passed on to Glaxnimate, and you have to adjust the duration there as well via Glaxnimate :menuselection:`Menu --> Document --> Timing`.

.. container:: clear-both

   .. figure:: /images/titles_and_graphics/animation-glaxnimate.webp
      :width: 360px
      :figwidth: 360px
      :alt: animation-glaxnimate
      :align: left

      The Glaxnimate application

   Kdenlive opens the Glaxnimate application. Please refer to the official |glaxnimate_manual| for its features, layout, tools, the keyframe system, and the layer concept.

.. rst-class:: clear-both

After the animation is done, drag the animation clip from the Project Bin to the Timeline. Once it is placed in the timeline, you can take advantage of **the** feature of the Kdenlive-Glaxnimate integration: your clip(s) as the background in Glaxnimate!

This makes it so much easier to create moving call-outs, travel routes on a map, and so on. You can have several Glaxnimate instances open but the background will only be sent to the instance opened first. If you need to see the background in another animation clip, save the animation and close all instances of Glaxnimate before you double-click the animation clip in the timeline.

.. note:: 
   This feature works only if the animation clip is opened for editing from the timeline. Otherwise Kdenlive does not know what clip to use for the background images, of course.

.. hint:: 
   Glaxnimate may not display the background the first time even after the animation clip was opened from the timeline. In that case move the Glaxnimate playhead, and the background should be displayed.

