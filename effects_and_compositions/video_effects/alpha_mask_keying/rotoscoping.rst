.. meta::
   :description: Kdenlive Video Effects - Rotoscoping
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha, mask, keying, rotoscoping

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Roger (https://userbase.kde.org/User:Roger)
             - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Maris Stalte (https://userbase.kde.org/User:limerick)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. |no_mirror| raw:: html

   <a href="https://youtu.be/h36S-awjLBk" target="_blank">No Mirror for you!</a>

.. |arkengheist| raw:: html

   <a href="https://www.youtube.com/watch?v=IkLeGgM8-OI&t=295" target="_blank">Putting yourself in a Movie</a>

.. |text_reveal| raw:: html

   <a href="https://www.youtube.com/watch?v=I5AeSNSVCRw" target="_blank">Text Reveal</a>

.. |rotoscoping_nbtech| raw:: html

   <a href="https://www.youtube.com/watch?v=DzIt5yCt2uU" target="_blank">ROTOSCOPING</a>


Rotoscoping
===========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-rotoscoping.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-rotoscoping

.. sidebar:: |kdenlive-show-video| Rotoscoping

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      rotoscoping
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

"In the visual effects industry, the term rotoscoping refers to the technique of manually creating a matte for an element on a live-action plate so it may be composited over another background."\ [1]_

This effect\ [2]_ is used to draw a region on one clip, and everything outside/inside that region will disappear showing the video track underneath. Effectively, the region defines the matte or mask for the clip.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Mode
     - Selection
     - Defines the channel to apply rotoscoping to
   * - Alpha Operation
     - Selection
     - Determines how compositing is done
   * - Invert
     - Switch
     - Inverts the rotoscoping selection
   * - Feathering width
     - Integer
     - Determines the amount of :abbr:`feathering (Smoothing or blurring the edges of a feature)`. Default is 0 (no feathering).
   * - Feathering passes
     - Integer
     - Sets the number of passes. The more passes the finer and more accurate the :abbr:`feathering (Smoothing or blurring the edges of a feature)` will be. Default is 1.

The following selection items are available:

:guilabel:`Mode`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-simple

   * - Alpha
     - The rotoscoped area will be the alpha channel (default)
   * - Luma
     - 
   * - RGB
     - 

:guilabel:`Alpha Operation`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-simple

   * - Write on clear
     - (default)
   * - Maximum
     - 
   * - Minimum
     - 
   * - Add
     - 
   * - Subtract
     - 


.. rubric:: Screenshots

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-rotoscoping_1.webp
   :width: 90%
   :alt: kdenlive2304_effects-rotoscoping_1

   Before, during and after Rotoscoping. Note the disabled Edit Mode (bottom right)


.. rubric:: Drawing the Region

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-rotoscoping_nodes_handles.webp
   :align: left
   :width: 328px
   :figwidth: 328px
   :alt: kdenlive2304_effects-rotoscoping_nodes_handles

   Nodes and Handles

The region is drawn by adding nodes along your region. These act as edges for your rotoscope, and there is a line between each node. The line can be made into a curve\ [3]_ using "handles".

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/kdenlive2304_effects-rotoscoping_nodes.webp
      :align: left
      :width: 328px
      :figwidth: 328px
      :alt: kdenlive2304_effects-rotoscoping_nodes

      Nodes and Handles

   Add nodes to the region by left clicking the mouse. You can draw nodes outside of the active frame: Zoom out in the Project Monitor (:kbd:`Ctrl+Wheel` or by hovering over the edge of the Project Monitor until the monitor tools show up and then selecting the Zoom-out icon) and then draw nodes. This is useful if the mask is to include/exclude regions all the way to the edge(s) of the clip (like the example screenshots at the beginning of this chapter).

.. rst-class:: clear-both

Close the region by right clicking the mouse on one of the nodes. Kdenlive will draw a straight line between the first node created and the last.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-rotoscoping_insert_node.webp
   :align: left
   :width: 328px
   :figwidth: 328px
   :alt: kdenlive2304_effects-rotoscoping_insert_node

   Inserting a node for better edge control

Change the edge of the region by moving a node. You can insert a node between two existing nodes by hovering over the line connecting the two nodes until a circle appears and then double-click the mouse. The more nodes the finer the region/mask can be controlled to follow ("hug") a shape, object or scenery.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/kdenlive2304_effects-rotoscoping_handles.webp
      :align: left
      :width: 328px
      :figwidth: 328px
      :alt: kdenlive2304_effects-rotoscoping_handles

      Using handles to create curves

   Make a line curved by dragging the control "handles". These are the two dots on the ends of the straight lines that appear on the curve.

.. rst-class:: clear-both

Once the region is created (closed) you can move individual nodes, insert and delete nodes, create curves to better follow the shape you want to rotoscope out or in, and move the entire region. For the latter action grab the :guilabel:`x` in the middle of the region and drag it around.

By default, the inside of the region you created is transparent (the video track underneath is visible). Use the :guilabel:`Invert` checkbox to make the outside of the region transparent.

.. note:: The Rotoscope effect can be keyframed. In contrast to other effects, keyframes not only can be created individually on the keyframe ruler\ [4]_ but are created automatically whenever the region is changed (nodes added, deleted or moved; curves created or changed; region moved). It is therefore important to create the rotoscope region on the very first frame of the clip.


.. rubric:: Using Keyframes to Make the Region Follow the Action

.. note:: The keyframe ruler and icons\ [4]_ may be greyed out initially. They become available once the first node is created.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-rotoscoping_keyframes.webp
   :align: left
   :width: 400px
   :figwidth: 400px
   :alt: kdenlive2304_effects-rotoscoping_keyframes

   Using keyframes for Rotoscoping

Move the position in the clip by dragging the playhead on the timeline (3) or by using the keyframe ruler\ [4]_ in the Rotoscope effect (2).

Click |keyframe-add|:guilabel:`Add keyframe` (6).

Now adjust the position of the nodes in the curve to match the action.

Kdenlive will calculate a path to move the nodes from the position they were in the previous keyframe to the position you put them in at this keyframe. So you do not have to draw a curve for every frame in the clip.

To remove a keyframe select it by clicking on the keyframe symbol (diamond, circle or square), or move to the frame with the keyframe using the |keyframe-previous|:guilabel:`Go to previous keyframe` (4) or |keyframe-next|:guilabel:`Go to next keyframe` (5) and then click on |keyframe-remove| which becomes :guilabel:`Delete keyframe` (6) when you are on an existing keyframe.


.. rubric:: Examples

**Examples on YouTube of what you can do with the Rotoscoping effect**

* |no_mirror| (by Everything and Even Gaming)

* |arkengheist| (by Arkengheist)

* |text_reveal| (by TJ FREE)

* |rotoscoping_nbtech| (by NBtech)


**Example "How to use Rotoscoping for Changing Color Tone"**

.. figure:: /images/effects_and_compositions/kdenlive_effects-rotoscoping_image21.webp
   :align: left
   :width: 400px
   :figwidth: 400px
   :alt: kdenlive_effects-rotoscoping_image21

   Layout changed to Color

We will be using the :guilabel:`Color` layout. This will allow us to work with the color vectorscope. Make sure it is enabled: :menuselection:`Menu --> View --> Vectorscope`. But for now we will stay in the :guilabel:`Edit` layout.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/kdenlive_effects-rotoscoping_image13.webp
      :align: left
      :width: 400px
      :figwidth: 400px
      :alt: kdenlive_effects-rotoscoping_image13

      Selecting Rotoscoping from the list of effects

   1. In the Timeline, select the clip with the sunset. Open the effects tab, type in "Rotoscoping", then drag it over the video to see further instructions.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/kdenlive_effects-rotoscoping_image14.webp
      :align: left
      :width: 400px
      :figwidth: 400px
      :alt: kdenlive_effects-rotoscoping_image14

      Object selection

   2. Start creating the region/mask around the sun by putting nodes around it. Use :guilabel:`Mouse left-click` to create nodes. If needed, zoom into the Project Monitor by using :guilabel:`Ctrl+Wheel` or the Project Monitor controls.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/kdenlive_effects-rotoscoping_image15.webp
      :align: left
      :width: 400px
      :figwidth: 400px
      :alt: kdenlive_effects-rotoscoping_image15

      Object selection

   3. Close the region/mask by :guilabel:`Mouse right-click`. If needed make adjustments by moving, adding or deleting nodes. For round object like the sun in this example curves come in handy.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/kdenlive_effects-rotoscoping_image18.webp
      :align: left
      :width: 400px
      :figwidth: 400px
      :alt: kdenlive_effects-rotoscoping_image18

      YUV selection

   4. Switch back to the :guilabel:`Color` layout. In the vectorscope tab use the :guilabel:`Paint mode` and select YUV.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/kdenlive_effects-rotoscoping_image19.webp
      :align: left
      :width: 400px
      :figwidth: 400px
      :alt: kdenlive_effects-rotoscoping_image19

      Color balance selection

   5. In the effects tab choose Color Balance and adjust the various red, green and blue values to the color of the sun you like.

.. rst-class:: clear-both


----

.. |wiki_rotoscoping| raw:: html

   <a href="https://en.wikipedia.org/wiki/Rotoscoping" target="_blank">Rotoscoping</a>

.. |mlt_rotoscoping| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterRotoscoping/" target="_blank">MLT framework Rotoscoping</a>

.. |wiki_bezier| raw:: html

   <a href="https://en.wikipedia.org/wiki/Bézier_curve" target="_blank">Bézier curves</a>


.. [1] See this Wikipedia article about |wiki_rotoscoping|

.. [2] This is the |mlt_rotoscoping| filter

.. [3] See this Wikipedia article about |wiki_bezier|

.. [4] If there is no keyframe ruler in the Rotoscope effect panel click on the |keyframe| icon in the effect header
