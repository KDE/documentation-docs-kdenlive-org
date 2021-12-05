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

Motion tracking is the process of locating a moving object across time. Kdenlive uses `OpenCV (Open Source Computer Vision Library)<https://opencv.org/about/>`_ for motion detection.  

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

`DaSiam<https://arxiv.org/pdf/1808.06048.pdf>`
^^^^^^^
In order to use the DaSiam algorithm you need to download the AI models and place them in *$HOME/.local/share/kdenlive/opencvmodels*.

1. https://www.dropbox.com/s/rr1lk9355vzolqv/dasiamrpn_model.onnx?dl=1
2. https://www.dropbox.com/s/999cqx5zrfi7w4p/dasiamrpn_kernel_r1.onnx?dl=1
3. https://www.dropbox.com/s/qvmtszx5h339a0w/dasiamrpn_kernel_cls1.onnx?dl=1







