.. meta::
   :description: Kdenlive Documentation - Title Editor File Operations
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, titles, title clip, text, template, placeholder, file, operations

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


.. |kde_store_templates| raw:: html

   <a href="https://store.kde.org/browse?cat=335&ord=latest" target="_blank">KDE Store Kdenlive Title Template</a>


=====================
Title File Operations
=====================

There are three file operations available:

* |document-open| :guilabel:`Open document` (keyboard shortcut :kbd:`Ctrl+O`)
* |document-save-as| :guilabel:`Save as` (keyboard shortcut :kbd:`Ctrl+S`)
* |edit-download| :guilabel:`Download New Title Templates` (keyboard shortcut :kbd:`Alt+D`)

.. hint:: 
   If the title editor window is not wide enough, the file operations icons may not be displayed. Instead, a left arrow :kbd:`>` is displayed (depending on your style and icon set the arrow might be black and therefore difficult to see). Click it to get a drop-down menu with the file operation items.


Open a Title
------------

Click the |document-open| :guilabel:`Open Document` button in the title editor toolbar, or press :kbd:`Ctrl+O` to open the **Load Title** dialog window. Only files of type :file:`.kdenlivetitle` can be opened. Navigate to the respective folder in your filesystem, select the title file you want to open, and click on :guilabel:`Open`.


Save a Title
------------

Click the |document-save-as|:guilabel:`Save As` button in the tool bar, or press :kbd:`Ctrl+S` to open the **Save Title** dialog window. Navigate to the respective target folder in your filesystem, and enter a name for the title. Make sure that the title is saved in the :file:`.kdenlivetitle` format for Kdenlive to recognize it properly. For a title to be used as a template, it must be saved to this folder in your filesystem:

:Linux appimage: :file:`~/.local/share/kdenlive/titles`

:Linux Flatpak: :file:`~/.var/app/org.kde.kdenlive/data/kdenlive/titles`

:Windows: :file:`%AppData%/kdenlive/titles` (press :kbd:`Win+R` and copy **%AppData%/kdenlive/**)


Download New Title Template
---------------------------

Kdenlive can connect to the KDE Store\ [1]_ to download title templates from there. Click the |edit-download| :guilabel:`Download New Title Templates` icon on the toolbar, or press :kbd:`Alt+D`.

.. container:: clear-both

   .. figure:: /images/titles_and_graphics/title-download_template.webp
      :width: 360px
      :figwidth: 360px
      :align: left
      :alt: Kdenlive_Download_title_templates

   Once these title templates are installed, they can be accessed via the :guilabel:`Template` drop-down list (see (10) in the :ref:`layout description <title-editor_layout>`).

.. rst-class:: clear-both

The :file:`.kdenlivetitle` title template files are installed to:

:Linux: :file:`~/.local/share/kdenlive/titles`

:Flatpak: :file:`~/.var/app/org.kde.kdenlive/data/kdenlive/titles`

:Windows: :file:`%AppData%/kdenlive/titles`. Press :kbd:`Win+R` and copy **%AppData%/kdenlive/**.

If you have a title template you want to share with the community, you can upload it to the |kde_store_templates| section so that other Kdenlive users can download it through this method.


----

.. |kde_store| raw:: html

   <a href="https://store.kde.org/browse?cat=333&ord=latest" target="_blank">KDE Store</a>

.. [1] Kdenlive has a direct link to the |kde_store| from where you can download and install new title templates. If you have an active Internet connection, Kdenlive queries the KDE Store for all of the template files available and opens a dialog window.