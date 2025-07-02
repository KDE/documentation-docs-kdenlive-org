.. meta::
   :description: Kdenlive Documentation - Compositing: Tracking
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, compositing, tracking

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



Tracking
========

Use the :doc:`Motion Tracker </effects_and_filters/video_effects/alpha_mask_keying/motion_tracker>` effect to track your object.

.. note:: The **Motion Tracker** effect comes with its own basic blur types which can be used for blurring or pixelating areas quickly and in one go. This section about tracking is about using the motion tracker to generate keyframes to be used in other effects, such as :doc:`Transform </effects_and_filters/video_effects/transform_distort_perspective/transform>` to move texts or images around the screen.

.. rubric:: Steps to track an object and make a text follow it

#. Apply the Motion Tracker effect to the clip with the object

   You may want to cut the clip such that the object is clearly visible over the tracking period or for the duration of the special effect.

#. Select the area with the object you want to track

   .. container:: clear-both

      .. figure:: /images/effects_and_compositions/transitions_and_compositions-tracking_1.gif
         :width: 360px
         :figwidth: 360px
         :align: left

         Selecting the area for tracking

      Select an area with high contrast and that is on screen for the duration of the tracking. The algorithms are not that good if the area leaves the screen and comes back.

   .. rst-class:: clear-both

#. Adjust the parameters for optimal tracking

   The defaults work for most cases but you may need to play around with them to get the best results. For more details about the different algorithms see :ref:`this page <tracking algorithms>`.

#. Click on the :guilabel:`Analyze` button to start the analysis

   .. container:: clear-both

      .. figure:: /images/effects_and_compositions/transitions_and_compositions-tracking_2.gif
         :width: 360px
         :figwidth: 360px
         :align: left

         Analyzing the video

      Kdenlive generates keyframes according to :guilabel:`Keyframes spacing` parameter and displays them in the keyframe ruler and as a track in the project monitor.

   .. rst-class:: clear-both

#. Copy the keyframes from the tracker

   .. container:: clear-both

      .. figure:: /images/effects_and_compositions/transitions_and_compositions-tracking_3.gif
         :width: 360px
         :figwidth: 360px
         :align: left

         Copying the keyframes

      | 

   .. rst-class:: clear-both

#. Delete the motion tracker effect

   You may want to keep it in case you need to run another pass, or you need the keyframes again after you copied something else (unless you have a clipboard manager, of course).

#. Add the other effect you need, and paste the keyframes from the motion tracker

   .. container:: clear-both

      .. figure:: /images/effects_and_compositions/transitions_and_compositions-tracking_4.gif
         :width: 360px
         :figwidth: 360px
         :align: left

         Applying the tracking information to the Transform effect

      The keyframes for the X coordinates are depicted in red, the one for Y in green.
      
      You can add an offset for the X and Y position, but using another **Transform** effect is more efficient and easier.

   .. rst-class:: clear-both

#. Adjust other parameters or add other effects as needed

   .. container:: clear-both

      .. figure:: /images/effects_and_compositions/transitions_and_compositions-tracking_5.gif
         :width: 360px
         :figwidth: 360px
         :align: left

         Adding another Transform effect for fine tuned positioning of the text

      It is important to keep the sequence in mind when adding other effects. Kdenlive processes effects top down. This is particular important for effects that transform a clip, like :doc:`Transform </effects_and_filters/video_effects/transform_distort_perspective/transform>`, :doc:`Position and Zoom </effects_and_filters/video_effects/transform_distort_perspective/position_and_zoom>`, :doc:`Rotate and Shear </effects_and_filters/video_effects/transform_distort_perspective/shear>`, or :doc:`Crop, Scale and Tilt </effects_and_filters/video_effects/transform_distort_perspective/crop_scale_tilt>`.

   .. rst-class:: clear-both

For more details, refer to the :doc:`Motion Tracker </effects_and_filters/video_effects/alpha_mask_keying/motion_tracker>` effect section in this documentation.