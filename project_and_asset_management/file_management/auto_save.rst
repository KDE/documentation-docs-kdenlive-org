.. meta::
   :description: Kdenlive Documentation - File Management - Auto Saves
   :keywords: KDE, Kdenlive, project bin, working, file, management, auto save, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Julius Künzel <jk.kdedev@smartlab.uber.space 
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



Auto Save
=========

Autosaves are generated three seconds after the user performs an action that cannot be undone, **BUT** only if no another action is performed within these three seconds.

You can switch it on or off in :menuselection:`Menu --> Settings --> Configure Kdenlive -->` :doc:`Misc</getting_started/configure_kdenlive/configuration_misc>`

Autosaves are offered the first time after you open the project again in case the autosave is newer than the last saved project version.

Autosaves are stored in stale files, not in normal :file:`.kdenlive` files.
