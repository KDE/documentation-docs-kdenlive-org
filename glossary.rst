.. meta::
   :description: Kdenlive Video Editor - Glossary
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, glossary

.. metadata-placeholders

   :authors: - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. .. _glossary:

.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   When adding terms please observe alphabetical order. While Sphinx re-orders the glossary, editing
   it unsorted and haphazardly makes checking for an entry so much more difficult. Thanks!
   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


.. |avfilter| raw:: html

   <a href="https://www.mltframework.org/plugins/PluginsFilters/" target="_blank">avfilter</a>

.. |frei0r| raw:: html

   <a href="https://frei0r.dyne.org/" target="_blank">frei0r</a>

.. |ffprobe| raw:: html

   <a href="https://ffmpeg.org/ffprobe.html" target="_blank">ffprobe</a>

.. |store| raw:: html

   <a href="https://www.pling.com/browse?cat=333&amp;ord=latest" target="_blank">store</a>

.. |color_temp| raw:: html

   <a href="https://www.cambridgeincolour.com/tutorials/white-balance.htm" target="_blank">color temperature</a>

.. |color_space| raw:: html

   <a href="https://en.wikipedia.org/wiki/Color_space" target="_blank">color space</a>

.. |subtractive_color| raw:: html

   <a href="https://en.wikipedia.org/wiki/Subtractive_color" target="_blank">subtractive color</a>

.. |field_order| raw:: html

   <a href="https://www.kernel.org/doc/html/v4.9/media/uapi/v4l/field-order.html" target="_blank">Field Order</a>

.. |interlaced_video| raw:: html

   <a href="https://en.wikipedia.org/wiki/Interlaced_video" target="_blank">Interlaced Video</a>

.. |techsmith| raw:: html

   <a href="https://www.techsmith.com/blog/frame-rate-beginners-guide/" target="_blank">techsmith.com</a>

.. |yiq| raw:: html

   <a href="https://en.wikipedia.org/wiki/YIQ" target="_blank">YIQ</a>

.. |ypbpr| raw:: html

   <a href="https://en.wikipedia.org/wiki/YPbPr" target="_blank">YPbPr</a>

.. |ycbcr| raw:: html

   <a href="https://en.wikipedia.org/wiki/YCbCr" target="_blank">YCbCr</a>


.. _true_glossary:

========
Glossary
========

.. glossary::
   :sorted:

   Asset
      An asset is any multimedia file (video, audio, image), title clip, color clip, and animation that can be and is used in a project. All assets are listed in the :term:`Project Bin`.
   
   Audio Mixer
      A widget that displays VU meters and has sliders to control the volume of the respective audio tracks. See :ref:`effects-audio_tools`.

   Audio Track
      A track in the :term:`timeline` that holds either the audio :term:`stream` of a video clip or an audio file itself

   Bin
      See :term:`Project Bin`

   Backup
      Kdenlive creates backup files for the current project. They are stored in a special folder. See the chapter :doc:`/project_and_asset_management/file_management/backup`.

   Caret
      See :term:`Playhead`

   Chroma
   Chrominance
      The signal used in video systems to convey the color information of the picture. Chrominance is usually represented as two-color difference components: U (blue projection) = B' - Y' (blue - :term:`luma`) and V (red projection) = R' - Y' (red - luma). See also :term:`YUV`.

   Clip
      Essentially any file with video and/or audio, a simple image or any asset created through Kdenlive, e.g. title clip, color clip, animation (via Glaxnimate). A clip can be in the :term:`Project Bin` or :term:`Timeline`, or be referred to as the result of a :term:`Render<exporting>`. See chapter :doc:`/project_and_asset_management/project_bin/clips`

   CMYK
      A |subtractive_color| model based on the CMY color model used in printing. The abbreviation refers to the four ink plates used: cyan, magenta, yellow and key (black).

   Codec
      Short for coder/decoder. Is a hardware- or software-based process that compresses or decompresses large amount of data. Examples are MPEG, H.264, VP8/VP9, Apple ProRes. Not to be confused with :term:`container`.

   Color Correction
      The process of correcting color issues and making footage appear as natural as possible. The idea is to make the images look like the human eyes would see them in the real world.

   Color Grading
      The process of creating consistent color tones throughout the film in order to give it a specific aesthetic look and style.

   Color and Image Correction
      A category of effects and filters to adjust or change the color components of the clip.

   Color Matrix
      Describes the balancing of different parts of the color spectrum in order to create an accurate representation for capture. By adjusting the properties of color matrix you can do things like shifting the white balance, alter the color palette, adjusting for color anomalies in the source.

   Color Range
      A term with more significance in broadcasting. Today's video recording equipment records in full range. Each color component is 8-bit and can have a value from 0 to 255, but only when in full range. Otherwise, for allowing headroom for video processing and exposure ranges, ranges are smaller, like 16-235 for :term:`luma`, and 16-240 for :term:`chroma`.

   Color Space
      A color space is a specific organization of colors. It is a useful conceptual tool for understanding the color capabilities of a particular device or digital file. When trying to reproduce color on another device, color spaces can show whether shadow/highlight detail and color :term:`saturation` can be retained, and by how much either will be compromised. See this article about |color_space| in Wikipedia.

   Composition
      Also referred to as a transition, it combines at least two input :term:`clips<clip>` to one output clip. Compositions cannot be stacked. See chapters :doc:`/compositing/compositions` and :doc:`/compositing/transitions`.

   Container
   Container Format
      A type of file that encapsulates multiple (compressed) data :term:`streams<stream>` in one file (wrapper), usually together with metadata for identifying or further detailing the embedded streams. Examples are Matroska (.mkv), OGG (.ogg), MPEG-4 (.mp4), AVI.

   Crash
      The instance when you realize you have not saved your project for at least two hours and worked on the most difficult edits. See :term:`backup`.

   Deprecated
      Obsolete, not used anymore. Effects in the *Deprecated* category are still available but are not maintained and can lead to unwanted results.

   Dynamic Text
      An effect that can be applied to a :term:`clip`, :term:`track` or on :term:`master` to overlay the video with specific information. Available keyword are: timecode, frame, filedate, localfiledate, source frame rate, source codec, source bit rate, source width, source height, source comment

   Effect
      Also referred to as a :term:`filter`, an effect is used to change the appearance, size or position of a :term:`clip`. Most effects have :term:`keyframe` capabilities. More than one effect can be used on the same clip (stacking). In that case effects are processed top down, so sequence is important. See :ref:`effects-effect_stack`.

   Edit Mode
      A special function of the :term:`project monitor`. Needed in order to be able to use the mouse to manipulate certain aspects (e.g. size, position) of some effects (e.g. Transform, Rotoscope). Can be switched on and off using the |edit-mode| icon in the project monitor's toolbar.

   Exporting
      See :term:`Rendering`

   Field Order
      Also called *Field Dominance*. Determines in a video stream which field of an interlaced video stream comes first. See this article about |field_order|.

   Filter
      Kdenlive uses filters from |avfilter| and |frei0r| to modify frames. See :term:`effect`.

   FPS
   Frames per Second
   Frame Rate
      The frame rate expressed in frames per second or FPS is typically the frequency (rate) at which consecutive images (frames) are captured or displayed. A good frame-rate primer including a list of typical frame rates for different types of video can be found on |techsmith|.

   Gamma
   Gamma Correction
      A description of the relationship between a color value and its brightness on a particular device. Hence Gamma Correction is the nonlinear operation for encoding and decoding :term:`luminance` in video or digital images to adjust color tones to how humans see them.

   Hamburger Menu
   Sandwich Menu
      A way to reduce clutter and save screen real estate. Looks like this |application-menu|. Replaces the Kdenlive menu bar. Can be expanded with :kbd:`Ctrl+M`.

   Histogram
      Displays a frequency histogram of the luminance of the color components of the video. See :ref:`view_menu`, and in particular :doc:`/tips_and_tricks/scopes/histogram_working` for a more detailed under-the-hood view.

   Hue
      Means a degree of lightness, darkness or strength of a color. Compare :term:`saturation`, :term:`tint` and :term:`shade`.

   Icon
      A graphical representation of an action, function, option or status.

   Interlaced
   Interleave
      A technique for doubling the perceived frame rate of a video without using extra bandwidth. Compare :term:`progressive`. See this Wikipedia article about |interlaced_video|.

   In-point
      An In-point defines the beginning of a :term:`zone`. A zone can be defined in the :term:`timeline` and the :term:`project monitor` (it has the same result), or in the :term:`clip monitor` (useful to move only a certain section of a clip to the timeline). See :term:`zone` for possible usages.

   Jog Shuttle
      An external device that improves video editing by using a rotary knob to scrub through the timeline, and providing a special keyboard for actions like cutting, inserting, deleting, slip and ripple editing, etc. It can be used with Kdenlive and configured in :menuselection:`Menu --> Settings --> Configure Kdenlive -->` :doc:`JogShuttle</getting_started/configure_kdenlive/configuration_jogshuttle>`. See :doc:`Settings</getting_started/configuration>`.

   KDE Store
      An online app |store| where users can upload files like lumas for :doc:`wipes </compositing/transitions/wipe>`, :ref:`presets <exporting>` for rendering, title templates, library clips and even project files. See :ref:`effects-effects_tab` icon #7.

   Kelvin
      Kelvin is the base unit of temperature in the International System of Units (SI). It is also used as a measure of the color temperature of light sources. True story: A physicist cooled himself to -273.15C. He was 0K.

   Keyframe
      Defines the frame in a clip where something starts or changes. Most :term:`effects<effect>` have keyframes to allow changes over time. For example, the X and Y coordinates of the Transform effect can be keyframed to move a clip across the screen. See :ref:`effects-working_with_keyframes`.

   Layout
      A particular way widgets are arranged on the screen to support different workflows or tasks. Kdenlive can save different layouts for logging, editing, audio and color. See :ref:`ui-workspace_layouts`.

   Lightness
      Also called brightness, lightness is the amount of white or black mixed in with the color. Lightness is more a subjective measure of perceived light, while brightness is an absolute measure of emitted or reflected light from an object. Compare :term:`tint` and :term:`shade`.

   Luma
   Luminance
      Represents the brightness of an image or video. Luma is typically paired with :term:`chrominance`. Luma represents the achromatic (aka black-and-white) image, while the chroma components represent the color information.

   Library
      Holds assets for generic use in projects. For example, watermarks, logos, lower-thirds, intros, and so on. See the chapter :doc:`Library</project_and_asset_management/library>`.

   Lock
      Locks a track for editing. Indicated by a closed padlock icon.

   Markers
      Belong to the clip they have been created in/for and move with it. Changes to a marker apply to all copies of the clip in the timeline. See :ref:`markers`.

   Mask
      An area to block out parts of an image. Can be used to apply an effect only to the masked area (see :doc:`/effects_and_filters/video_effects/alpha_mask_keying/mask_apply`) or to have an underlying clip show through (see :doc:`/effects_and_filters/video_effects/alpha_mask_keying/rotoscoping`, :doc:`/effects_and_filters/video_effects/alpha_mask_keying/alpha_shapes`, :doc:`/effects_and_filters/video_effects/alpha_mask_keying/shape_alpha` and :doc:`/effects_and_filters/video_effects/alpha_mask_keying/rectangular_alpha_mask`).

   Master
   Master Effect
      A special effect stack that applies to all clips in all of the tracks.

   Master Audio
      The volume of all of the audio tracks when merged into one during rendering. See :ref:`effects-audio_tools`.

   Media Browser
      Allows easy browsing of the file system and previewing media clips and other assets for importing to the :term:`Project Bin`. A widget that can be switched on and off via :menuselection:`Menu --> View --> Media Browser`. See the chapter :doc:`media_browser</project_and_asset_management/media_browser>`.

   MELT
   melt
      Melt was developed as a test tool for the MLT framework. If you will, Kdenlive is a front-end for melt writing :file:`.mlt` XML files that code the edit points and transitions. It then calls melt to render the video. See :ref:`troubleshooting-faq`.

   Mixes
      See :term:`Same-track Transition`

   Monitor
      A device to display a video signal. Kdenlive uses a Clip Monitor to play clips selected in the :term:`project bin` and :term:`Project Monitor` to play clips in the :term:`timeline`. Monitor is widget that can be switched on and off via :menuselection:`Menu --> View`. See :ref:`ui-monitors`.

   MOVIT
      A library for high-quality, high-performance video filters. Is needed to enable GPU-supported preview and playback. See :doc:`Configure Playback</getting_started/configure_kdenlive/configuration_playback>` in :menuselection:`Menu --> Settings --> Configure Kdenlive`.

   Clip Monitor
      The Clip Monitor plays the clip currently selected in the :term:`Project Bin`. See :ref:`ui-monitors` and :term:`overlay`.

   Project Monitor
      The Project Monitor plays clips selected in the :term:`timeline` or simply the project.

   Opacity
      A measure of impenetrability to electromagnetic or other kinds of radiation, especially visible light. An object that does not allow any visible light to go through is fully opaque or has 100% opacity.

   Overlay
      Clip and Project Monitor can have an overlay that helps with editing. Hover the mouse over the hot zone of the respective monitor (default is the top right-hand corner) and click on the grid icon to cycle through the available patterns. Different from :term:`Dynamic Text` and :term:`video overlay`.

   Mute
      Temporarily disable a video or audio track.

   Nested Timeline
      See :term:`Sequence`

   Out-point
      An Out-point defines the end of a :term:`zone`. A zone can be defined in the :term:`timeline` and the :term:`project monitor` (it has the same result), or in the :term:`clip monitor` (useful to move only a certain section of a clip to the timeline). See :term:`zone` for possible usages.

   Video Overlay
      Additional information (e.g. timecode) that is overlayed during the render process. Can be selected in the More Options section of the :ref:`Render Dialog<render>`.

   Playhead
      The upside-down triangle in the timeline ruler. Indicates the (play) position in the timeline. During :ref:`3-point Editing<three_point_editing>` determines where a clip or clip zone will be added to the timeline. Drag it across to scrub the timeline.

   Posterize
   Posterization
      Is the conversion of a continuous gradation of tone or color to several regions of fewer tones or color, causing abrupt changes from one tone or color to the other. The term comes from the process of creating posters. The effect is most visible when a JPEG image with millions of colors is converted to the GIF format with only 256 colors.

   Preset
      Used for :term:`rendering` to determine output format (container), codec, dimensions, aspect ratio, bit rate and various other parameters. See :ref:`render_profile_parameters`.

   Progressive
      A format of displaying, storing or transmitting video in which all the lines of each frame are drawn in sequence. The 'p' in 1080p indicates that the format is using progressive scan, i.e. the frame's lines are **not** :term:`interlaced`.

   Project
      The sum of all assets, clips, tracks, effects, transitions, compositions and settings, their arrangements in the timeline, and references to all the source materials including their :term:`proxy` work copies. The project file is associated with a working directory where Kdenlive generates proxies and thumbs.

   Project Bin
      Lists all the clips and assets that are associated with the project. Referred to as the 'Project Tree' in earlier versions. See the chapter :doc:`Project Bin</project_and_asset_management/project_bin>`.

   Project Settings
      Defines the format (dimensions, aspect ratio, frames-per-second setting) of the project through the choice of profile or :term:`preset`, which working directory to use, how many video and audio tracks there are initially, and which profile to use for previews. Stores metadata for your project (e.g. title, author, copyright information). See chapter :doc:`Project Settings</project_and_asset_management/project_settings>`.

   Profile
      For rendering see :term:`preset`, for project see :term:`project settings`

   Proxy
      A light-weight version of the original clip. Used to make editing and in particular playback easier and smoother. See :ref:`make_proxy_clip`.

   Plane
      Used on :term:`color correction` and blur application to separate color components for the purpose of applying an effect only to that component. Color components are RGB (Red, Green, Blue) and YUV (luminance (Y), blue projection (U), red projection (V)) , as well as alpha (channel).

   Quality, custom
      A setting in the :term:`rendering` dialog More Options section to control the quality of the rendered video.

   Radio Button
      Used to select one option and one option only from a list of option. Like in the old days on a radio to select a pre-programmed station: press the stations' button and the previously pressed button pops out.

   RGB Parade
      An RGB parade is a video editing tool (a “scope”) that separates the red, green, and blue color channels of an image in order to analyze their levels and distribution; it is essential for color correction to detect color casts, adjust white balance (ideally, all channels should match), and ensure that no details are clipped in highlights or shadows by graphically displaying the brightness values of each color. 

   Rendering
      Also referred to as 'Exporting'. The process of saving the edited clips into a single complete video clip. See :ref:`render`.

   Rendering Profile
      See :term:`Preset`

   Ripple Tool
      Used in editing. Changes the original duration of the clip. Compare with working with old film material: The film strip is lengthened or shortened and in so doing the adjacent clips are moved back and forth. See :ref:`timeline_edit_tools`.

   Saturation
      Color saturation is a degree of intensity of a color in an image or video. As saturation increases, the color appears to be more pure. Compare :term:`hue` and :term:`tint`.

   Same-track transition
      Also known as mixes. A transition between clips on the same track. See :ref:`same_track_transition`.

   Sequence
      Introduced with version 23.04.0, a sequence is basically a timeline. Sequences are part of a project but can be rendered independently. A project can have multiple sequences (hence the alias 'nested timelines'). See :ref:`sequence`.

   Shade
      In color theory, a shade is a mixture of a color with black, increasing its darkness. Compare :term:`tint`, :term:`hue` and :term:`saturation`.

   Slip Tool
      Used in editing. Keeps the original duration of the clip. Compare with working with old film material: the film strip is slipped back and forth beneath the given "window" of the clip length. See :ref:`timeline_edit_tools`

   Snap Point
      Sections in :term:`clips<clip>` that other clips snap to when "snapping" is turned on. Snap points include markers, timeline markers, zone in-points, zone out-points, transition start points, clip edges, and cuts.

   Speed Ramping
      See :term:`Time Remapping`

   Stack
      The list of effects applied to a clip, track or master. An effect stack is processed top down, so sequence is important. See :ref:`effects-effect_stack`.

   Stream
      A part of an (encoded) media file containing either video or audio data. Use a tool like |ffprobe| to examine media files.

   Temperature
   Color Temperature
      A parameter describing the color of the visible light source. It is measured in :term:`Kelvins<kelvin>` (K). The range is from 1,000K to 10,000K where lower temperatures are considered "warm", and higher temperatures "cool". See this article about |color_temp|.

      Theme
      A set of colors, icons, fonts and other settings to change the appearance of an application or desktop. Can be set from :menuselection:`Menu --> Settings --> Color Scheme`.

   Thumbnail
      A small image representation of a much larger image. Used in the timeline at the start and end of a clip. See :ref:`timeline-show_video_thumbnails`.

   Time Remapping
      A special widget allowing to keyframe the speed of a clip to achieve effects like speed ramping. See :ref:`effects-time_remapping`.

   Timeline
      The :doc:`central part</user_interface/timeline>` of Kdenlive. This is where all the editing takes place. Keeps a chronological sequence of the clips and the relations to each other through tracks and compositions. Can be zoomed. See also :ref:`sequence` for nested timelines.

   Timeline Marker (former Guide)
      Static markings in the :term:`timeline` that do not necessarily move with clips. Not to be confused with :term:`markers`. Can be used to define regions for rendering and exported to provide chapters for YouTube videos. See :ref:`guides`.
   
   Timeline Ruler
      Sits right above the tracks and displays the time code information (default notation is hh:mm:ss:ff, can be switched to frames) as well as any currently defined timeline :term:`zone` and/or preview render zone. See :ref:`timeline_ruler`.

   Timeline Zone
      See :term:`Zone`

   Tint
      In color theory a tint is a mixture of a color with white, increasing the lightness. Compare :term:`shade`, :term:`hue` and :term:`saturation`.

   Title Bar
      Part of a :term:`widget's<widget>` window displaying additional information (e.g. name, title, action icons). You can grab a widget by the title bar and move it around. See :ref:`ui-moving_widgets`.

   Tooltip
      A small window with more information about a function that pops up when hovering the mouse over an icon or button. Press Shift to get even more details (not available for all functions).

   Track
      Holds various :term:`assets <asset>` in the timeline. Can be muted and locked individually. Can have effects in its own stack that apply to all clips in that track. Track height can be adjusted. Tracks can be inserted and deleted. Video tracks only accept clips with video, image, title, or color; audio tracks only accept pure audio clips or the audio track of a video clip. There is a relationship between video and audio tracks: A video clip with an audio :term:`stream` can only be put into a track where there is a corresponding audio track - V1/A1, V2/A2, V3/A3 and so on. See :ref:`tracks`.

   Active Track
      Can accept clips. Indicated by a highlighted track number.

   Inactive Track
      Cannot accept clips. Indicated by a greyed out track number.

   Transcode
      Converts a video or audio clip from one format to another. Is needed (and automatically proposed when loaded in to the :term:`project bin`) for files that are not in an editing-friendly format. See :ref:`transcode`.

   Tutorial
      A step-by-step instruction to use a function, tool, effect or combination of these to achieve a certain result. Often created as a video with commentary or just explanatory text. There are many tutorials for Kdenlive available via a simple Google or YouTube search.

   Transition
      A :term:`Wipe` or Dissolve :term:`composition` between two overlapping clips. See chapters :doc:`/compositing/compositions` and :doc:`/compositing/transitions`.

   Video
      An asset or file with a video :term:`stream`.

   Video Track
      A type of track that only accepts clips with video, image, title, or color. Needs a corresponding :term:`audio track` to accept a clip with video and audio :term:`stream`. See :ref:`tracks`.

   Widget
      A blend (portmanteau) of 'window' and 'gadget' coined by American playwright George S. Kaufman in 1924. A small applet as part of the :term:`layout` for a specific tool or panel that can be moved around the screen and docked in specific places in order to accommodate different workflows. See :ref:`user_interface`.

   Wipe
      A special type of :term:`composition` mostly used as a transition from one clip to another. See :doc:`Wipe </compositing/transitions/wipe>`.

   YIQ
      Color space used by the analog NTSC color TV system. For more details see the Wikipedia page about |yiq|.

   YPbPr
      A color space used in video electronics. Also written as Y'PbPr or YP\ :sub:`B`\ P\ :sub:`R`. Used in particular when referring to component video cables. For more details see the Wikipedia page about |ypbpr|.

   YCbCr
      A color space used for any digital encoding of YCbCr suited for video and image compression and transmission formats such as MPEG and JPEG. For more details refer to the Wikipedia page about |ycbcr|.

   YUV
      A color model used to encode a color image or video taking human perception into account. Y stands for the :term:`luminance`, U for blue projection and V for red projection.

   Zone
      A defined region of a clip or the timeline. Use a clip zone to bring only a portion of the clip into the timeline. Use a timeline zone to render only that portion (see :ref:`rendering-selected_zone`). Define a zone for preview rendering (see :doc:`/tips_and_tricks/tips_and_tricks/timeline_preview_rendering`). A zone is defined by setting an :term:`in-point` and an :term:`out-point`.

   Zoom
      Increase or decrease the level of detail. You can zoom the timeline by using the icons or by :kbd:`Ctrl+wheel`. Clip and Project Monitor can be zoomed by clicking on the icons in the monitor :term:`overlay` or with :kbd:`Ctrl+wheel`.
