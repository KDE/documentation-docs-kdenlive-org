.. meta::

   :description: Kdenlive Video Effects - Object Mask
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha gradient

.. metadata-placeholder

   :authors: - Eugen Mohr

   :license: Creative Commons License SA 4.0

Object Mask
===========

.. figure:: /images/effects_and_compositions/kdenlive2504_effects-object_mask.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-show-video| Object Mask

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      Meta Research
   :**Source filter**:
      SAM2
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect relies on (SAM2)\ [1]_ object segmentation. Its purpose is to isolate an object in images or videos like rotoscoping. 

Before Object Mask can be used, it must be properly configured and models installed. Please refer to the chapter :doc:`Configure Object Detection</getting_started/configure_kdenlive/configuration_plugins>`.

.. warning:: The effect works only on the selected clips in the project bin.

There are two ways to use Object Mask:

.. figure:: /images/effects_and_compositions/kdenlive2504_effects-alpha_object-mask.webp
   :align: left
   :width: 90%
   :alt: kdenlive2504_effects-alpha_object-mask

   Object Mask in the effect stack when a clip is selected

.. rst-class:: clear-both

1. Click on |create-object-mask| :guilabel:`Create an Object mask`
2. Use :guilabel:`Remove Background` when the built-in effects are enabled

.. rubric:: Steps to create an Object Mask

.. figure:: /images/effects_and_compositions/kdenlive2504_effects-alpha_object-mask-creation.webp
   :align: left
   :width: 90%
   :alt: kdenlive2504_effects-alpha_object-mask-creation

.. rst-class:: clear-both

1.	Add a clip to the project bin
2.	Select in the clip monitor a zone by setting in/out points **(3)** where the background should be removed
3.	Click on |create-object-mask| :guilabel:`Create an Object mask` or :guilabel:`Remove Background`

.. figure:: /images/effects_and_compositions/kdenlive2504_effects-alpha_object-mask-create-new-mask.webp
   :align: left
   :width: 90%
   :alt: kdenlive2504_effects-alpha_object-mask-create-new-mask

.. rst-class:: clear-both

4. click on |list-add| :guilabel:`Create New Mask` **(4)**
5. Click in the clip monitor to select an object by either dragging a rectangle **(5)** and :kbd:`LMB` **(6)** to define the object inside the rectangle or by :kbd:`Shift+click` **(6)** to add another part, or :kbd:`CTRL+click` to exclude a zone
6. The mask can be inverted |edit-select-invert| **(7)** or the opacity |edit-opacity| **(8)** of the mask can be changed in 25% steps
7.	Click on |media-record| :guilabel:`Generate Mask` **(9)**
8. Wait until the mask is generated.
9. The process can be canceled by clicking on the minus icon **(10)**

.. figure:: /images/effects_and_compositions/kdenlive2504_effects-alpha_object-mask-apply.webp
   :align: left
   :width: 90%
   :alt: kdenlive2504_effects-alpha_object-mask-apply

.. rst-class:: clear-both

10. Once the mask is created, select it **(11)**
11. You can preview the mask **(12)** or edit the mask **(13)** as you like
12. :guilabel:`Apply Mask` **(14)** opens the effect :doc:`Shape Alpha</effects_and_filters/video_effects/alpha_mask_keying/shape_alpha_mask>` and the mask get applied
13. You can |edit-delete| delete the selected mask **(16)** or you can |document-import| import the mask **(15)** into the project bin as a new clip
14. Right click on the mask **(11)** and you can open the containing folder

.. figure:: /images/effects_and_compositions/kdenlive2504_effects-alpha_object-mask-applied.webp
   :align: left
   :width: 90%
   :alt: kdenlive2504_effects-alpha_object-mask-applied

.. rst-class:: clear-both


----

.. |facebookresearch_sam2| raw:: html

   <a href="https://github.com/facebookresearch/sam2" target="_blank">Segment Anything in Images and Videos</a>

.. [1] For more details about this effect refer to the github entry about |facebookresearch_sam2|.
