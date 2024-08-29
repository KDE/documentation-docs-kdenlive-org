.. meta::
   :description: Kdenlive Documentation - Title Shapes
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, titles, title clip, shapes, rectangle, ellipse

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
Shapes
======

There are only two basic shapes you can add to a title clip: a rectangle and an ellipse (a square is just a special form of rectangle, like a circle is a special form of an ellipse).

Click on |kdenlive-insert-rect|, or use the keyboard shortcut :kbd:`Alt+R`, then drag the mouse across the main workspace to create a new rectangle. To get a square, enter identical values for the :guilabel:`W` and :guilabel:`H` parameters.

Click on |draw-ellipse|, or use the keyboard shortcut :kbd:`Alt+E`, then drag the mouse across the main workspace to create a new ellipse. If you need a circle, enter :guilabel:`W` and :guilabel:`H` values that are identical.

The shape properties can be set in the **Properties** tab.

.. figure:: /images/titles_and_graphics/title-shape_properties.webp
   :width: 360px
   :figwidth: 360px

:Solid Color: Select this if you want the shape to have one color

:Color Selection: Click the color button to open the color selection dialog window

:Gradient: Select this if you want the shape to have a color gradient

:Gradient Selection: Select from the available gradients

:Gradient Editor: |document-edit| Click on this icon to open a gradient editing window. Here you can create, edit, and delete gradients.

:Border: Click this color button to select the color for the border

:Border width: A value of zero (0) means no border; higher values create a border (measured in pixel).


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
