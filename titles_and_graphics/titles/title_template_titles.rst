.. meta::
   :description: Kdenlive Documentation - Template Titles
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, titles, title clip, text, template, placeholder

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
Template Titles
===============

**Template Titles** (not to be confused with Title Templates) allow you to create a template for other titles in your project. You create the template title with the settings that all or a considerable number of the titles in the project should have, and then base subsequent titles on that template. If you decide to change the look of your titles, you only need to change the template title, and the titles based on this template will automatically update to reflect any formatting changes you made to the template title. Apart from that, template titles behave like any other title clip.


Create a Template Title
=======================

Create a new title clip like normal, add any objects you need, and any static text. Create a new text field, and enter :code:`%s`. This will be replaced later with text you specify for each title you add to the project based on this template. Adjust the font attributes, alignment, shadow, and the :ref:`typewriter<title-text_typewriter>` effect as required. If the title needs :doc:`animation</titles_and_graphics/graphics_and_animations/title_scrolling>`, you can create that, too.

Instead of simply clicking on :guilabel:`Create title`, click on |document-save-as|\ :guilabel:`Save As`, or press :kbd:`Ctrl+S`, and save the template title. Give it a meaningful name for better recognizeability.


Use the Template Title
======================

In the Project Bin, click on |kdenlive-add-clip|\ |go-down|\ :guilabel:`Add clip or folder` and select :guilabel:`Add Template Title`, or right-click on empty space in the Project Bin, and select :guilabel:`Add Template Title`.

.. container::
   
   .. figure:: /images/titles_and_graphics/title-add_template_title.webp
      :width: 360px
      :figwidth: 360px
         :align: left

      Adding a template title

   Kdenlive opens a window with a drop-down list with all the title templates and a preview area. Select the template you just created, or in case you saved it elsewhere click the |document-open|\ :guilabel:`Open file dialog` icon, navigate to the respective folder, and open the :file:`.kdenlivetitle` file from there.

.. rst-class:: clear-both

Alternatively you can add template title inside :ref:`the title app <title-editor_load-template>`.

Kdenlive added a new title clip to the Project Bin. Right-click this clip in the Project Bin and select :guilabel:`Clip Properties`, or in case you have the :guilabel:`Clip Properties` widget available, simply open it.

.. container::
   
   .. figure:: /images/titles_and_graphics/title-use_template_title.webp
      :width: 360px
      :figwidth: 360px
         :align: left

      Using a template title

   Enter the text that this title should display into the text field in the dialog that appears.

   You can change the :guilabel:`Duration` by ticking the box and entering a new value (format is hh:mm:ss:ff).

   You can edit the template by clicking on the :guilabel:`Edit Clip` button.

   Click on :guilabel:`Apply` to create or change this title clip.

.. rst-class:: clear-both

Drag the title to the timeline.

.. container::
   
   .. figure:: /images/titles_and_graphics/title-use_template_title_2.webp
      :width: 360px
      :figwidth: 360px
         :align: left

      A template title at work

   The :code:`%s` in the template will be replaced with the text that you enter in the :guilabel:`Text` field.

.. rst-class:: clear-both

.. warning::
   A known issue with template titles is that text centering does not work correctly for text replacing the :code:`%s`.