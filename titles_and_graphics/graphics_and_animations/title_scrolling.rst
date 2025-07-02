.. meta::
   :description: Kdenlive Documentation - Title Scrolling
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, titles, title clip, text, scrolling, scroll, horizontal, vertical

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Vincent Pinon <vpinon@kde.org>
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Carl Schwan <carl@carlschwan.eu>
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



===============
Title Scrolling
===============

The title editor has a built-in animation function, albeit rather rudimentary. It allows scrolling titles in basically any direction in a linear motion. This is enough for something like closing credits, but for more elaborate motion it is recommended to use effects like :doc:`/effects_and_filters/video_effects/transform_distort_perspective/transform`, :doc:`/effects_and_filters/video_effects/transform_distort_perspective/rotate_3_way`, or :doc:`/effects_and_filters/video_effects/transform_distort_perspective/shear`.

The animation feature works by defining a start viewport and an end viewport covering none or some of the title workspace. The position of the viewports determines the direction of the animation:

:Start viewport above end viewport: Title contents are moving upwards

:Start viewport below end viewport: Title contents are moving downwards

:Start viewport left of end viewport: Title contents are moving to the left

:Start viewport right of end viewport: Title contents are moving to the right

It is possible to have any conceivable combination between these four basic scenarios. Essentially, this allows a title animation in any direction within a 360 degree circle.

.. container:: clear-both

   .. figure:: /images/titles_and_graphics/title-text_scrolling.gif
      :width: 360px
      :figwidth: 360px
      :align: left

      Creating a scrolling title

   Enter your text into a :doc:`text object</titles_and_graphics/titles/title_text>`. You can copy and paste from other sources. Adjust the text's properties as needed and align it as required.

   Select the :guilabel:`Animation` tab and click the :guilabel:`Edit start viewport` button. Now drag the start rectangle to above the viewable area. Alternatively, you can keep the start rectangle where it is and move the text and any other object outside (below) the viewable area.

   Click the :guilabel:`Edit end viewport` button and drag the end rectangle to below the viewable area. If you want the text to scroll all the way out of the screen, put the end rectangle below the text field.

   You may need to zoom the workspace for better visibility and easier positioning of the viewports. Drag the zoom slider in the bottom left of the editor window, or use :kbd:`Ctrl+MW` to zoom in and out.

   Press the :guilabel:`Create Title` or :guilabel:`Update Title` button.

.. rst-class:: clear-both
   
The text in the above title scrolls up the screen. It is as if the camera starts on the start rectangle and then pans down to the end rectangle.

To make the text scroll faster, set the :guilabel:`Duration:` field to a smaller value. To make the text scroll slower, set it to a larger value.

.. warning::
   Changing the length (or duration) of the title clip in the timeline does not change the length of the animation and thus the scrolling speed. If the duration of the clip in the timeline is greater than the duration specified in the title editor, the scrolling will stop after the time specified in the title editor is up and the title will stay paused on the screen until the end of the clip.

   Likewise, if the length (or duration) of the title clip in the timeline is shorter than the duration specified in the title editor, the scrolling will not complete before the title clip finishes.

.. note:: 
   You cannot delete an animation per se. If you don't want or need the animation, simply move the start and end viewports back to their original position by entering a value of 0 into the :guilabel:`X` and :guilabel:`Y` parameters.