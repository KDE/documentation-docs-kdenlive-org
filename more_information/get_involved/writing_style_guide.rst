.. meta::
   :description: Kdenlive Manual - Writing Style Guide
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, manual, documentation, writing, style, guide, style guide

.. metadata-placeholder

   :authors: - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

..  See also KDE Typographical Guidelines: https://userbase.kde.org/Typographical_Guidelines


.. _writing_style_guide:

*******************
Writing Style Guide
*******************


.. _goals:

Goals
=====

User Focused
   The manual shall be kept understandable by beginners to video editing.


Complete
   All features, options and tools of **Kdenlive** should be described.
   The manual should provide information on what a feature is, its purpose, and how to use it.


Concise
   Keep the text short and concise and relevant to the topic you describe.


Maintainable
   Write content that will not have to be redone the moment some small change is made in **Kdenlive**.


.. _guidelines:

Guidelines
==========

Content
-------

* Use American English (e.g: modeling and not modelling, color and not colour) also for formatting numbers (e.g: 2,718.28 and not 2 718,28).

* Use spell checking.

* Take care about grammar, appropriate wording and use simple English.

* Think of what could be interesting for a video editor.

* Describe in general and not in full depth, so you don't have to adapt the documentation with each new **Kdenlive** version.

* Do not describe bugs, no actual state.

* Including why or how an option might be useful. Example :ref:`sequence_advantage`.

* If you are unsure about how a feature works, ask someone else or find out who developed it and ask them.

* You can add comment (which is not shown in the HTML page, but useful for other editors): ``.. TODO, How to choose the correct output format and bit rate? Ask advanced user.``


Style
-----

* Keep sentences short and clear, use verbs and less noun. Resulting in text that is easy to read, objective and to the point. Rule of thumb (but not only!): 20 words or 120 letters per sentence.

* Be specific: Do not write *input device* when you mean the *mouse*.

* Be entertaining: Each sentence describes something new.

* Use bold text to highlight: **Program names**

* Use italic text to emphasize: *Words or phrases as in general writing*, *Titles when referencing other works*, *The first use of an unfamiliar word*

* Combined Bold and Italic Text: In restructured text this is only possible with additional code.


Putting a definition first
   .. code-block:: bash

      Sequence
      Using sequences you can make your project clearer.

   better

   .. code-block:: bash

      Sequence
      A sequence is basically a timeline.

   Then explain what it does and how you can use it. Example: :ref:`sequence`

..

Avoiding the immediate repetition of the term
   .. code-block:: bash

      The Properties Tab
      The Properties Tab displays the settings for the effects on the currently selected clip.

   better

   .. code-block:: bash

      The Properties Tab
      The settings for the effects on the currently selected clip are shown the properties tab.


Avoiding the “it is”
   .. code-block:: bash

      Binarize
      It is an effect to make he image black and white.

   better

   .. code-block:: bash

      Binarize
      Creates a black and white image.


Images
------

Only ``.. figure::`` should be used to place images.

Use the **Kdenlive** dark theme when making screenshots.

Use .webp for images.

Use animated .gif or .mp4 files if that explains the feature/task better.

Try to avoid having a lot of images. Use a single image that shows all of the relevant areas placed at the top of the section. Numbering the features and then explain the features in that order. Like this :ref:`example <project_tree>`.


Further information
-------------------

Check the :ref:`template <template>` for how to use the rst commands.
