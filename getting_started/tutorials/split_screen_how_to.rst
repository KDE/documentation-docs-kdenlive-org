.. metadata-placeholder

   :authors: - Roger (https://userbase.kde.org/User:Roger)
             - Smolyaninov (https://userbase.kde.org/User:Smolyaninov)

   :license: Creative Commons License SA 4.0

.. _split_screen_how_to:

How To Do Split Screen Effect
=============================

.. contents::




This effect is also known as picture in picture effect or PIP.


In this example we will see how to have 4 screens playing at once in the video.


`Example - 4 screens in one(YouTube) <https://youtu.be/YRs5UDuCVJg>`_


To create this effect you need 4 video tracks on the time line.  Add extra tracks to the time line from the  :ref:`tracks` menu.


You create a project/timeline like that shown in Figure 1 and described in detail below.


.. image:: /images/Kdenlive_4pip_overview.png
   :align: left
   :width: 400px
   :alt: Figure 1. - Time Line Setup


Video 1 (appears in bottom left in the result) has no effects added to it.  


.. image:: /images/Kdenlive_4pip_transition1.png
   :width: 200px
   :align: left
   :alt: Figure 2. - Transition 1


Video 2 (appears top left in result) has a :ref:`pan_and_zoom` effect added to it (See Figure 3).  This effect has a sizing and positioning effect as part of it that causes the Video on Video Track 2 to be scaled down 50% and be positioned in the top left corner.


.. image:: /images/Kdenlive_4pip_vid2_pan_and_zoom.png
   :width: 200px
   :align: left
   :alt: Figure 3 - Effect on Video 2


There is a standard composite transition between Video track 2 and Video track 3 - see Figure 4.


.. image:: /images/Kdenlive_4pip_transition2.png
   :width: 200px
   :align: left
   :alt: Figure 4 - Transition between Video 2 and Video 3


Video 3 (appears top right in result) has a pan and zoom effect added to it (See Figure 5).  This effect has a sizing and positioning effect as part of it that causes the Video on Video Track 3 to be scaled down 50% and be positioned in the top right corner.


.. image:: /images/Kdenlive_4pip_vid3_pan_and_zoom.png
   :width: 200px
   :align: left
   :alt: Figure 5 - Effect on Video 3


There is a standard composite transition between Video track 3 and Video track 4 - see Figure 6.


.. image:: /images/Kdenlve_4pip_transition3.png
   :width: 200px
   :align: left
   :alt: Figure 6 - Transition between Video 3 and Video 4


Video 4 (appears bottom right in result) has a pan and zoom effect added to it (See Figure 7).  This effect has a sizing and positioning effect as part of it that causes the Video on Video Track 4 to be scaled down 50% and be positioned in the bottom right corner.


.. image:: /images/Kdenlive_4pip_vid4_pan_and_zoom.png
   :width: 200px
   :align: left
   :alt: Figure 7 - Effect on Video 4


