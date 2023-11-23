.. meta::

   :description: Kdenlive Video Effects - Planes Blur
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, blur and sharpen, planes blur


   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Planes Blur
===========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-planes_blur.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-planes_blur

.. sidebar:: |kdenlive-show-video| Planes Blur

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      boxblur
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect applies just to three :term:`Planes<plane>`: :term:`Luma`, :term:`Chroma` and Alpha. You define the :guilabel:`Radius` and :guilabel:`Power` to determine the strength of the effect.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - | Luma
       | Chroma
       | Alpha  Radius
     - Integer
     - Set an expression for the box radius in pixels used for blurring the corresponding input plane. Default value for :guilabel:`Luma Radius` is **2**. If not specified, :guilabel:`Chroma Radius` and :guilabel:`Alpha Radius` default to the corresponding value set for :guilabel:`Luma Radius`.
   * - | Luma
       | Chroma
       | Alpha  Power
     - Integer
     - Specify how many times the boxblur filter is applied to the corresponding plane. Default value for :guilabel:`Luma Power` is **2**. If not specified, :guilabel:`Chroma Power` and :guilabel:`Alpha Power` default to the corresponding value set for :guilabel:`Luma Power`. A value of 0 will disable the effect. 
