.. meta::
   :description: Kdenlive Documentation - Title Images
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, titles, title clip, image

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



======
Images
======

Click on |insert-image|, or use the keyboard shortcut :kbd:`Alt+I`. Using the Open File dialog window select an image file to be inserted.

The image properties can be set in the **Properties** tab.

.. container:: clear-both

   .. figure:: /images/titles_and_graphics/title-image_properties.webp
      :width: 360px
      :figwidth: 360px
      :align: left

      The image properties tab

   **Note**: The selected image will be placed into the workspace using the top left corner, i.e. the top left corner of the image is put into the top left corner of the workspace. Therefore, small images may not be easy to find at first.

.. rst-class:: clear-both

:Preserve aspect ratio: Set by default, it keeps the image's aspect ratio. Deselect this, if you need to distort the image using the :guilabel:`W` and :guilabel:`H` parameters.

.. note:: 
   An image can only be scaled by entering values for the :guilabel:`W` and :guilabel:`H` parameters, or by using the :guilabel:`Zoom` parameter. You cannot grab the edges with the mouse.


.. rubric:: Object Zooming and Rotating

An object can be zoomed and rotated. 

.. container:: clear-both

   .. figure:: /images/titles_and_graphics/title-zoom_rotate.webp
      :width: 360px
      :figwidth: 360px
      :align: left


   Sometimes zooming is easier than entering new values for :guilabel:`W` and :guilabel:`H`. Enter a zoom percentage in the :guilabel:`Zoom` field.

   Rotating an object is possible by entering degrees of rotation into the :guilabel:`Rotate X`, :guilabel:`Y`, and :guilabel:`Z` fields. Note that the center of rotation is the top left corner of the object.

.. rst-class:: clear-both


.. rubric:: Object Stacking

The objects are placed on top of each other following the sequence in which they were created. If you need to bring an object/item forward that was created in the early stages, use the :guilabel:`Z-Index` field or click on the respective icon (|object-order-raise|, |object-order-lower|, |object-order-front|, |object-order-back|) in the stack toolbar. Likewise, you can also send an object/item backwards.


.. rubric:: Object Alignment

Alignment to the project dimensions is possible using the icons in the toolbar:

* |align-horizontal-left| :guilabel:`Align left` or |align-horizontal-right| :guilabel:`Align right` moves the selected object towards the left or right edge stopping at the edges of each of the safety boxes with each click on the icon.
* |align-vertical-top| :guilabel:`Align top` or |align-vertical-bottom| :guilabel:`Align bottom` moves the selected object towards the top or bottom edge stopping at the edges of each of the safety boxes with each click on the icon.
* |align-horizontal-center| :guilabel:`Align center horizontally` or |align-vertical-center| :guilabel:`Align center vertically` centers the selected object on the vertical or horizontal center axis of the outermost box.
