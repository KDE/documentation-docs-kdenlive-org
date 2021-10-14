.. metadata-placeholder

   :authors: - Roger (https://userbase.kde.org/User:Roger)

   :license: Creative Commons License SA 4.0

.. _historical_install_information:



Historical Info on  Installation
================================

.. contents::




The information on this page may be of interest for historical reasons but you should visit the `download <https://kdenlive.org/download/>`_ page of the Kdenlive Web site for up to date information on installing **Kdenlive**.  (Aug 2017)


Install binary packages
-----------------------



Most linux distributions provide recent binary packages of **Kdenlive** that can be installed from your Package Manager. However, in some cases you can find more recent versions in private repositories. 


`This <http://www.kdenlive.org/download>`_ page at the **Kdenlive** home has instructions on how to source these more recent versions, depending on which flavour of Linux you run.   Instructions for Debian, Fedora, Gentoo, OpenSUSE, Slackware and Ubuntu are available.


As of May 2015, obtaining and installing the latest version of **Kdenlive** has gotten a little complicated.  
Development of **Kdenlive** up to this point has used a technology known as KDE Frameworks 4. And the last stable release using this technology is version  `0.9.10 <http://kdenlive.org/discover/0.9.10>`_, released 25th September 2014.

To use this you need to have recent versions of frei0r, **Kdenlive** , mlt and  libvidstab,
e.g.: 


* frei0r = 1.4.0+git20140826.72e51041  


* **Kdenlive** = 0.9.10  


* mlt = 0.9.3+git20141005.22abed67 


* libvidstab=2:0.98b


As of June 2015, `this <https://launchpad.net/~sunab/+archive/ubuntu/kdenlive-release-old>`_ PPA has version 0.9.10 of **Kdenlive** , 1.4.0 of Frei0r and 0.9.3 of melt.


Development of **Kdenlive** has now switched to a new version of the KDE Frameworks called KF5 (KDE Frameworks 5).  To install versions of **Kdenlive** using this underlying technology, you need to be on a Linux distribution which supports KF5. Ubuntu and its derivatives versioned 15.04 and higher support KF5.   It is not possible to install KF5 on distributions earlier than 15.04 (except by *chroot*ing your system).
Versions using KF5 are distributed by the `Kubuntu-CI Team <https://launchpad.net/~kubuntu-ci>`_. The sunab ppa (see below) now also distributes KF5 versions. 

Version numbers of the KF5 flavour start at 15.04.0. 

This author recommends using the  sunab ppa to install Kdenlive rather than the  Kubuntu-CI Team because the Kubuntu-CI Team PPA has many other packages in it which will attempt to uprade all sorts of things on your system–with the potential of breaking it.


Debian
~~~~~~



* Debian* project has been shipping **Kdenlive** packages since the "squeeze" (6.0) release. However, to benefit from recent updates and bugfixes, you might consider upgrading to a "testing" release or even "sid".


Once your package management tool is pointed at an appropriate release, a simple ``apt install kdenlive`` should then work.


Sunab's PPA (see below) is not recommended for Debian because *Debian uses a different lib layout for multiarch* (reference: this `post <https://forum.kde.org/viewtopic.php?f=269&amp;t=123425#p322708>`_ from vpinon).


Ubuntu and derivatives
~~~~~~~~~~~~~~~~~~~~~~



* Ubuntu* also has offered **Kdenlive** since "gutsy" (7.10). However, to benefit from recent updates and bugfixes, you should consider upgrading to the latest release.


`ppa:kdenlive/kdenlive-master <https://launchpad.net/~kdenlive/+archive/ubuntu/kdenlive-master>`_ is the development branch, with the very latest features additions.


`ppa:kdenlive/kdenlive-testing <https://launchpad.net/~kdenlive/+archive/ubuntu/kdenlive-testing>`_ is the feature-frozen branch, starting from the first beta, with bugfix updates as soon as solutions are found


`ppa:kdenlive/kdenlive-stable <https://launchpad.net/~kdenlive/+archive/ubuntu/kdenlive-stable>`_ is the last robust official release


Not all the packages in the ppa are necessary. Install or upgrade the following to get a 15.04 release
(version numbers as at 13 July 2015)


* kdenlive   (15.04.2-0ubuntu0-~sunab~vivid4)     


* kdenlive-data    (15.04.2-0ubuntu0-~sunab~vivid4)    


* libmlt++3    (0.9.6-0ubuntu0~sunab~vivid1)     


* libmlt-data  (0.9.6-0ubuntu0~sunab~vivid1)    


* libmlt6   (0.9.6-0ubuntu0~sunab~vivid1)           


* libvidstab1.0   (2:0.98b-0ubuntu0~sunab~vivid1)  


* melt           ( 0.9.6-0ubuntu0~sunab~vivid1)  


Non-Kubuntu users will need to install the kde-runtime package to fix missing buttons and icons.


Fedora, RedHat and derivatives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



RPM packages are not yet maintained in an official branch, so you must go through an unofficial repository such as  `RPM Fusion <http://rpmfusion.org/>`_ or `packman <http://packman.links2linux.de/package/kdenlive>`_ (Has ver 15.12.0 29 Dec 2015). Follow the site's recommendations to make them available and end with ``yum install kdenlive``.


Gentoo, Arch, BSD ports
~~~~~~~~~~~~~~~~~~~~~~~



Building scripts are ready for up-to-date systems, so run respectively ``emerge kdenlive`` or ``pacman -S kdenlive`` or ``pkg_add kdenlive``, etc.


Windows
~~~~~~~



The first Windows version of Kdenlive (v16.12.1) is available for download `here <https://kdenlive.org/download/>`_. Read the installation instructions for Windows.


Alternatively you could try and use some virtualized :ref:`what_is_a_distribution` to run **Kdenlive** on **Windows**. Some advice can be found on `this page <http://www.kdenlive.org/forum/kdenlive-windows>`_.


There is also the `kdenlive on win <http://sourceforge.net/projects/kdenlive-on-win/>`_ project on SourceForge which "consists of an Ubuntu VirtualBox image that is preconfigured to run **Kdenlive**". The project was last updated 2012-08-09.


MacOS
~~~~~



* *Kdenlive** and **MLT** can compile and run under Mac OS X. Packages are available from the `MacPorts <http://www.macports.org/>`_ project.


MacPorts is a source-based system – there is not a binary app bundle for **Kdenlive**. Therefore, **Kdenlive** and all of its numerous dependencies, including multimedia libraries, KDE, and Qt, must be compiled. This can take a long time and much disk space! Furthermore, it is not unusual for something not to build correctly; it is definitely not something for the novice, impatient, or "faint of heart".


You may have some success getting support for the MacPort of **Kdenlive** on the Mac Ports forum on `MacOS Forge <http://mac-os-forge.2317878.n4.nabble.com/MacPorts-f3.html>`_.


Installing from source
----------------------



If you want to test latest committed code or your personal patches, you will have to build **Kdenlive** (and probably **MLT**) on your own.


Details on how to compile and install **Kdenlive** from source are available on the `Community wiki <https://community.kde.org/Kdenlive/Development/KF5>`_.


You can use your distribution's package building procedure to use its software management system to install/upgrade/remove the binaries and data, and eventually share your builds (and even contribute to package maintenance - refer to the respective distribution manual).


If you prefer you can build &  install **Kdenlive** to a local area (preferably not :file:`/usr`, but rather :file:`/usr/local` or :file:`$HOME/my_local_builds/kdenlive-last-release` or similar).
You could try using  `this <https://community.kde.org/Kdenlive/Development/KF5#A_build_script>`_ build script to build the latest version from the sources. Or you could use the `this <http://www.mltframework.org/twiki/bin/view/MLT/BuildScripts#Kdenlive>`_ build script to build kdenlive ver 0.9.10  [1]_  (Follow the instructions under "show kdenlive". These instructions will build **Kdenlive** and its dependancies [e.g. melt, ffmpeg] in a "sandbox").


Installing from pre-built binary packages
-----------------------------------------



* *Kdenlive** now offers pre-build binary packages deployed using Appimage technology - see Appimage section on the `download page <https://kdenlive.org/download/>`_  of the Kdenlive web site.


These install files are hosted at http://files.kde.org/kdenlive/  where you will find a release folder and an unstable folder
The release folder contains binary builds of the current stable version of **Kdenlive**.


Windows Versions are in 7zip format archives with file names of the form 


Kdenlive-17.04.0-2-w64.7z


For installation instructions for windows see the `download page <https://kdenlive.org/download/>`_.


Linux Appimage versions are in file names of the form 


Kdenlive-17.04.1b-x86_64.AppImage


To run the AppImage versions simply make the downloaded file executable (chmod +x) and run it (./Kdenlive-17.04.1b-x86_64.AppImage)


Pre-built binary packages are often an easy solution if you are having troubles with your install and can be preferable to building your own because you don't need to install a build environment.


The pre-built AppImage version and your main version of **Kdenlive** can live simultaneously on your machine so you can test new and possibly unstable versions without breaking the main version of **Kdenlive** on your system.


A downside is that these packages have been built with a version of ffmpeg that only has the free video codecs.  The type of files you can render your video to is limited.  Choosing the **Theora** profile in the **Web Sites** rendering destination does work.


* *Kdenlive** pre built binaries currently only supports 64 bit operating systems 


.. [1] on distributions older than *Debian 6* or *Ubuntu 10.04* and derivatives, you need to set ``ENABLE_SWFDEC=0`` in the config variables of the script. Modify the INSTALL_DIR in the script to  something like ``INSTALL_DIR="$HOME/my_local_builds/kdenlive-last-release"`` to make it match where you want this local build to install. 
