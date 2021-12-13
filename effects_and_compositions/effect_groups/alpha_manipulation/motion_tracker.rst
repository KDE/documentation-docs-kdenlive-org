.. metadata-placeholder

   :authors: - frdbr (https://userbase.kde.org/User:frdbr)

   :license: Creative Commons License SA 4.0

.. _motion_tracker:

Motion Tracker
==============
.. versionadded:: 19.04.0

.. contents::

What is Motion Tracking?
------------------------

Motion tracking is the process of locating a moving object across time. Kdenlive uses `OpenCV (Open Source Computer Vision Library) <https://opencv.org/about/>`_ for motion detection.  

   -- `Wikipedia <https://en.wikipedia.org/wiki/Video_tracking>`_

.. image:: /images/motion_tracker.png
   :alt: motion tracker

How to track a region of a video? 
---------------------------------

The basic workflow for tracking a region consists of:

* Select the desired region to track on the Project Monitor. 
* Choose a tracking algorithm.
* Click on the Analyse button.

.. image:: /images/motion_tracking_face.png
   :alt: motion tracking face

.. image:: /images/motion-tracker-copy-keyframe.png
   :align: right
   :alt: motion-tracker-copy-keyframe

* When Analyse is done you can export the keyframes to the clipboard by click on |application-menu| and choose :menuselection:`Copy keyframes to clipboard`. See: :ref:`exchange_keyframes_across_effects`

.. rst-class:: clear-both

Tracking algorithms?
--------------------
KCF
^^^
soon

CSRT
^^^^
soon

MOSSE
^^^^^
soon

MIL
^^^
soon

MedianFlow
^^^^^^^^^^
soon

`DaSiam <https://arxiv.org/pdf/1808.06048.pdf>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In order to use the DaSiam algorithm you need to download the AI models and place them in: 

   **Linux**

   *$HOME/.local/share/kdenlive/opencvmodels*.

   **Windows**

   *%AppData%/kdenlive/opencvmodels*

   Press :kbd:`Win + R` (:kbd:`Windows` key and :kbd:`R` key simultaneously) and copy **%AppData%/kdenlive/**. Then create the folder `opencvmodels`



1. https://files.kde.org/kdenlive/motion-tracker/DaSiamRPN/dasiamrpn_kernel_cls1.onnx
2. https://files.kde.org/kdenlive/motion-tracker/DaSiamRPN/dasiamrpn_kernel_r1.onnx
3. https://files.kde.org/kdenlive/motion-tracker/DaSiamRPN/dasiamrpn_model.onnx







