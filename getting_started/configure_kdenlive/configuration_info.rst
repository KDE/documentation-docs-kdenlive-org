.. meta::
   :description: Kdenlive Documentation - Configuration Information
   :keywords: KDE, Kdenlive, documentation, user manual, install, installation, configuration, preferences, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Configuration Information
-------------------------

Kdenlive's application-wide persistent settings are stored in the following locations, depending on your platform. 

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 33 32 35
   :class: table-wrap

   * - File / Folder
     - Location
     - Description
   * - :file:`kdenliverc`
     - | |linux|: :file:`~/.config/`
       | |windows|: :file:`%LocalAppData%\\`
     - General settings of the application. Delete this and restart Kdenlive to reset the application to "factory" settings
   * - :file:`kdenlive-appimagerc`
     - | |linux|: :file:`~/.config/`
     - Linux AppImage only: contains the general settings of the application
   * - :file:`kdenlive_*`
     - | |linux|: :file:`~/.config/session/`
     - temporary session info
   * - | |linux|: :file:`~/.cache/kdenlive/`
       | |windows|: :file:`%LocalAppData%\\kdenlive\\`
     - 
     - Audio and video thumbnails, proxy clips, user defined titles, LUTS, lumas, shortcuts
   * - | |linux|: :file:`~/.local/share/kdenlive/`
       | |windows|: :file:`%AppData%\\kdenlive\\`
     - 
     - Contains downloaded effects, export, library, opencv models, profiles, speech models, and titles
   * - | |linux|: :file:`~/.local/share/kdenlive/ lumas/`
       | |windows|: :file:`%LocalAppData%\\kdenlive\\ lumas\\`
     - 
     - Contains the files used for :doc:`wipes </compositing/transitions/wipe>`
   * - | |linux|: :file:`~/.local/share/kdenlive/ .backup/`
       | |windows|: :file:`%AppData%\\kdenlive\\ .backup\\`
     - 
     - Auto Save Recovery files
   * - | |linux|: :file:`~/.config/share/kdenlive/ layouts/`
       | |windows|: :file:`%LocalAppData%\\kdenlive\\ layouts\\`
     -
     - Contains the different layout files saved by the user
   * - | :file:`kdenliveui.rc`
     - | |linux|: :file:`~/.local/share/kxmlgui5/ kdenlive/`
       | |windows|: :file:`%LocalAppData%\\kxmlgui5\\ kdenlive\\`
     - Contains UI configuration. If your UI is broken, delete this file.
   * - | :file:`knewstuff3`
     - | |linux|: :file:`~/.local/share/`
       | |windows|: :file:`%LocalAppData%\\`
     - Contains LUT definition
   * - | |linux|: :file:`~/.local/share/kdenlive/ speechmodels/`
       | |windows|: :file:`%AppData%\\kdenlive\\ speechmodels\\`
     - 
     - Contains the downloaded VOSK models
   * - | |linux|: :file:`~/.local/share/kdenlive/ opencvmodels/`
       | |windows|: :file:`%AppData%\\kdenlive\\ pencvmodels\\`
     - 
     - Contains the downloaded OpenCV models 
   * - | |linux|: :file:`~/.local/share/kdenlive/ venv/`
       | |windows|: :file:`%LocalAppData%\\kdenlive\\ venv\\`
     - 
     - Contains the Python virtual environment (venv)
   * - | |windows|: :file:`$HOME/.cache/huggingface`
     - 
     - Contains the SeamlessM4T models for Whisper  

   
Windows
   To reach the above folders: :kbd:`Windows+R` then copy above path into the window.
