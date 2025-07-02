.. meta::
  
   :description: Alphabetical list of all video effects in Kdenlive
   :keywords: KDE, Kdenlive, video effects, plugins, composition, transition

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Roger (https://userbase.kde.org/User:Roger)
             - ChristianW (https://userbase.kde.org/User:ChristianW)
             - Tenzen (https://userbase.kde.org/User:Tenzen)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


=============
Video Effects
=============

.. note::
   The effects and compositions included will differ depending on the available plug-ins on the specific packaging on each operating system. Kdenlive will auto-detect and make available any supported LADSPA plug-in packages from your distribution. For the greatest compatibility, please use the AppImage version of Kdenlive.


.. list-table::  
   :class: table-wrap
   :header-rows: 1
   :width: 100%
   :widths: 22 8 20 50

   * - Effect or Filter
     - OS\ [1]_
     - Category
     - Description
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/3_point_balance` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Balances colors along with 3 points (|frei0r.three_point_balance|)
   * - :doc:`/effects_and_filters/video_effects/stylize/3-level_threshold` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Dynamic 3-level thresholding (|frei0r.threelay0r|)
   * - :doc:`/effects_and_filters/video_effects/grain_and_noise/3d_fft_denoiser` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Grain and Noise
     - Denoise frames using 3D FFT (frequency domain filtering) (|avfilter.fftdnoiz|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/alpha_gradient` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Fill the alpha channel with the specified gradient (|frei0r.alphagrad|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/alpha_operations` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Display and manipulation of the alpha channel (|frei0r.alpha0ps|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/alpha_shapes` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Draws simple shapes into the alpha channel (|frei0r.alphaspot|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/alpha_shapes_mask` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - This filter takes a snapshot of the frame before it draws simple shapes into the alpha channel. Use it together with the mask_apply effect, that uses a transition to composite the current frame's image over the snapshot. The typical use case is to add effects in the following sequence: this effect, zero or more effects, mask_apply. (|mask_start|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/alpha_strobing` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Strobes the alpha channel to 0. Many other filters overwrite the alpha channel, in that case this needs to be last (|strobe|)
   * - :doc:`/effects_and_filters/video_effects/misc/alphaextract` 
     - |appimage|\ |windows|\ |apple|
     - Misc
     - Extract an alpha channel as a grayscale image component. (|avfilter.alphaextract|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/applylut` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Apply a Look Up Table (LUT) to the video. A LUT is an easy way to correct the color of a video. Supported formats: 3dl (AfterEffects), .cube (Iridas), .dat (DaVinci), .m3d (Pandora) (|avfilter.lut3d|)
   * - :doc:`/effects_and_filters/video_effects/on_master/audio_level_visualization_filter` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - On Master
     - An audio visualization filter that draws an audio level meter on the image. (|audiolevelgraph|)
   * - :doc:`/effects_and_filters/video_effects/on_master/audio_spectrum_filter` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - On Master
     - An audio visualization filter that draws an audio spectrum on the image (|audiospectrum|)
   * - :doc:`/effects_and_filters/video_effects/on_master/audio_wave` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - On Master
     - Display the audio waveform instead of the video (|audiowave|)
   * - :doc:`/effects_and_filters/video_effects/on_master/audio_waveform_filter` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - On Master
     - An audio visualization filter that draws an audio waveform on the image. (|audiowaveform|)
   * - :doc:`/effects_and_filters/video_effects/blur_and_sharpen/average_blur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Apply average blur filter (|avfilter.avgblur|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/backgroundkey` 
     - |appimage|\ |windows|\ |apple|
     - Misc
     - Turns a static background into transparency. (|avfilter.backgroundkey|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/bezier_curves` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image Correction
     - Color curves adjustment (|frei0r.curves|)
   * - :doc:`/effects_and_filters/video_effects/blur_and_sharpen/bilateral` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Apply Bilateral filter (|avfilter.bilateral|)
   * - :doc:`/effects_and_filters/video_effects/stylize/binarize` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Make monochrome clip (|threshold|)
   * - :doc:`/effects_and_filters/video_effects/stylize/binarize_dynamically` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Dynamic thresholding (|frei0r.twolay0r|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/bluescreen0r` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Color to alpha (blit SRCALPHA) (|frei0r.bluescreen0r|)
   * - :doc:`/effects_and_filters/video_effects/deprecated/blur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Blur using 2D IIR filters (exponential, lowpass, gaussian) (|frei0r.IIRblur|)
   * - :doc:`/effects_and_filters/video_effects/deprecated/box_blur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Box blur (separate horizontal and vertical blur) (|boxblur|)
   * - :doc:`/effects_and_filters/video_effects/blur_and_sharpen/boxblur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Box blur (separate horizontal and vertical blur) (|box_blur|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/brightness` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjusts the brightness of a source image (|frei0r.brightness|)
   * - :doc:`/effects_and_filters/video_effects/stylize/burning_tv` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Simulates burning TV pixels (|burningtv|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/bw0r` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Turns image Black/White (|frei0r.bw0r|)
   * - :doc:`/effects_and_filters/video_effects/generate/cairogradient` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Draws a gradient on top of image. Filter is given gradient start and end points, colors and opacities. (|frei0r.cairogradient|)
   * - :doc:`/effects_and_filters/video_effects/stylize/cartoon` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Cartoonify video, do a form of edge detect (|frei0r.cartoon|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/channel_extractors` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Extracts Blue, Green, or Red from the image (|frei0r.B|)
   * - :doc:`/effects_and_filters/video_effects/stylize/charcoal` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Charcoal drawing effect (|charcoal|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/chroma_hold` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Removes all color information for all colors except for a certain one (|avfilter.chromahold|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/chroma_keep` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Make image greyscale except for chosen color (|chroma_hold|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/chroma_key_advanced` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Chroma Key with more advanced options (e.g. different color models). Use if basic chroma key is not working effectively. (|frei0r.select0r|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/chroma_key` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Make Selected Color transparent (|chroma|)
   * - :doc:`/effects_and_filters/video_effects/grain_and_noise/chroma_noise_reduction` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Grain and Noise
     - Reduce chrominance noise (|avfilter.chromanr|)
   * - :doc:`/effects_and_filters/video_effects/stylize/chroma_shift` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Shift chroma pixels horizontally and/or vertically (|avfilter.chromashift|)
   * - :doc:`/effects_and_filters/video_effects/utility/ciescope` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - Video CIE scope (|avfilter.ciescope|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/CMYK_adjust` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Apply CMYK correction to specific color ranges (|avfilter.selectivecolor|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/color_balance` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Modify intensity of primary colors (red, green and blue) of input frames (|avfilter.colorbalance|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/color_channel_mixer` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Modifies a color channel by adding the values associated to the other channels of the same pixels (|avfilter.colorchannelmixer|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/color_contrast` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjust color contrast between RGB components. (|avfilter.colorcontrast|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/color_correct` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjust color white balance selectively for blacks and whites.This filter operates in YUV colorspace. (|avfilter.colorcorrect|)
   * - :doc:`/effects_and_filters/video_effects/stylize/color_distance` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Calculates the distance between the selected color and the current pixel and uses that value as a new pixel value (|frei0r.colordistance|)
   * - :doc:`/effects_and_filters/video_effects/stylize/color_effect` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Applies a pre-made color effect to image (|frei0r.colortap|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/color_hold` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Remove all color information all RGB colors except for certain one (|avfilter.colorhold|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/color_levels` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjust video input frames using levels (|avfilter.colorlevels|)
   * - :doc:`/effects_and_filters/video_effects/image_adjustment/color_matrix` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Convert color matrix (|avfilter.colormatrix|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/color_overlay` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Overlay a solid color on the video stream (|avfilter.colorize|)
   * - :doc:`/effects_and_filters/video_effects/image_adjustment/color_space` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Convert colorspace, transfer characteristics or color primaries. Input video needs to have an even size. (|avfilter.colorspace|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/color_temperature` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjust color temperature of video (|avfilter.colortemperature|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/colorize` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Colorizes image to selected hue, saturation and lightness (|frei0r.colorize|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/contrast` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjusts the contrast of a source image (|frei0r.contrast0r|)
   * - :doc:`/effects_and_filters/video_effects/blur_and_sharpen/contrast_adaptive_sharpen` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Apply Contrast Adaptive Sharpen filter to video stream. (|avfilter.cas|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/corners` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Four corners geometry engine (|frei0r.c0rners|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/crop_padding` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - This filter crops the image to a rounded rectangle or circle by padding it with a color (|qtcrop|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/crop_scale_tilt` 
     - |linux|\ |appimage|\ |windows|
     - Transform, Distort, and Perspective
     - Crops, scales, and tilts an Image (|frei0r.scale0tilt|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/curves` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Color curves adjustment (|frei0r.curves|)
   * - :doc:`/effects_and_filters/video_effects/on_master/dance` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - On Master
     - An audio visualization filter that moves the image around proportional to the magnitude of the audio spectrum (|dance|)
   * - :doc:`/effects_and_filters/video_effects/utility/datascope` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - Video data analysis (|avfilter.datascope|)
   * - :doc:`/effects_and_filters/video_effects/blur_and_sharpen/dblur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Apply Directional Blur filter. (|avfilter.dblur|)
   * - dct_denoiser
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Denoise frames using 2D DCT frequency domain filtering (|avfilter.dctdnoiz|)
   * - :doc:`/effects_and_filters/video_effects/image_adjustment/deband` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Remove banding artifacts from input video. It works by replacing banded pixels with an average value of referenced pixels (|avfilter.deband|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/defish` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Non rectilinear lens mappings (|frei0r.defish0r|)
   * - delogo
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Remove logo from input video (|avfilter.delogo|)
   * - :doc:`/effects_and_filters/video_effects/grain_and_noise/denoise_hqdn3d` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Grain and Noise
     - High Quality 3d denoiser (|frei0r.denoise_hqdn3d|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/despill` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Remove unwanted contamination of foreground colors, caused by reflected color of greenscreen or bluescreen (|avfilter.despill|)
   * - :doc:`/effects_and_filters/video_effects/image_adjustment/dilation` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Apply dilation effect (|avfilter.dilation|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/distort` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Plasma (|frei0r.distort0r|)
   * - :doc:`/effects_and_filters/video_effects/grain_and_noise/dither` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Grain and Noise
     - Dithers the image and reduces the number of available colors (|frei0r.dither|)
   * - :doc:`/effects_and_filters/video_effects/generate/drawbox` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Draw a colored box on the input video (|avfilter.drawbox|)
   * - :doc:`/effects_and_filters/video_effects/generate/drawgrid` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Draw a colored grid on the input video (|avfilter.drawgrid|)
   * - :doc:`/effects_and_filters/video_effects/generate/drop_shadow` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Creates a shadow effect for the clip (|dropshadow|)
   * - :doc:`/effects_and_filters/video_effects/grain_and_noise/dust` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Grain and Noise
     - Add |dust| and specks to the video, as in old movies (|dust|)
   * - :doc:`/effects_and_filters/video_effects/generate/dynamic_text` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Overlay text with keywords replaced (|dynamictext|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/edge_crop` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Trim the edges of a clip (|crop|)
   * - :doc:`/effects_and_filters/video_effects/stylize/edge_detection` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Detect and draw edges. The filter uses the Canny Edge Detection algorithm (|avfilter.edgedetect|)
   * - :doc:`/effects_and_filters/video_effects/stylize/edge_glow` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Edge glow filter (|frei0r.edgeglow|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/elastic_scale_filter` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - This is a frei0r filter which allows to scale video footage non-linearly (|frei0r.elastic_scale|)
   * - :doc:`/effects_and_filters/video_effects/stylize/emboss` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Creates embossed relief image of source image (|frei0r.emboss|)
   * - :doc:`/effects_and_filters/video_effects/image_adjustment/epx_scaler` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Scale the input using EPX algorithm. (|avfilter.epx|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/equaliz0r` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Equalizes the intensity historgrams (|frei0r.equaliz0r|)
   * - :doc:`/effects_and_filters/video_effects/image_adjustment/erosion` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Apply erosion effect (|avfilter.erosion|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/exposure` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjust exposure of the video stream (|avfilter.exposure|)
   * - :doc:`/effects_and_filters/video_effects/motion/fade_in` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Motion
     - Fade video from black (|brightness|)
   * - :doc:`/effects_and_filters/video_effects/motion/fade_out` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Motion
     - Fade video to black (|brightness|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/fft-based_fir` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Apply arbitrary expressions to samples in frequency domain (|avfilter.fftfilt|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/fill_borders` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Fill borders of the input video, without changing video stream dimensions. Sometimes video can have garbage at the four edges and you may not want to crop video input to keep size multiple of some number (|avfilter.fillborders|)
   * - :doc:`/effects_and_filters/video_effects/grain_and_noise/filmgrain` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Grain and Noise
     - Adds film-like grain and softens the picture. This gives the video an old film look. (|frei0r.filmgrain|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/flip_horizontally` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Horizontally flip the input video (|avfilter.hflip|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/flip_vertically` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Vertically flip the input video (|avfilter.vflip|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/flippo` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Flipping X and Y axis (|frei0r.flippo|)
   * - :doc:`/effects_and_filters/video_effects/motion/freeze` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Motion
     - Freeze video on a chosen frame (|freeze|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/gamma` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjusts the gamma value of a source image (|frei0r.gamma|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/gamma_keyframe` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Change |gamma| color value (|gamma|)
   * - :doc:`/effects_and_filters/video_effects/blur_and_sharpen/gaussian_blur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Apply Gaussian Blur filter (|avfilter.gblur|)
   * - :doc:`/effects_and_filters/video_effects/motion/gate_weave` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Motion
     - Randomly moves frame around to simulate film gate weave (|frei0r.gateweave|)
   * - :doc:`/effects_and_filters/video_effects/motion/glitching_glitch0r` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Motion
     - Adds glitches and block shifting (|frei0r.glitch0r|)
   * - :doc:`/effects_and_filters/video_effects/motion/glitching_pixs0r` 
     - |appimage|\ |windows|\ |apple|
     - Misc
     - Glitch image shifting rows to and fro (|frei0r.pixs0r|)
   * - :doc:`/effects_and_filters/video_effects/stylize/glow` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Creates a Glamorous Glow (|frei0r.glow|)
   * - :doc:`/effects_and_filters/video_effects/generate/gps_graphic` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Overlay GPS-related graphics onto the video (|gpsgraphic|)
   * - :doc:`/effects_and_filters/video_effects/generate/gps_text` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Overlay GPS-related text onto the video. (|gpstext|)
   * - :doc:`/effects_and_filters/video_effects/grain_and_noise/gradfun` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Grain and Noise
     - Debands video quickly using gradients (|avfilter.gradfun|)
   * - :doc:`/effects_and_filters/video_effects/deprecated/grain` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Grain over the image (|grain|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/grayworld` 
     - |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjust white balance using LAB gray world algorithm (|avfilter.grayworld|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/greyscale` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Discard color information (|greyscale|)
   * - :doc:`/effects_and_filters/video_effects/utility/histogram` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - Compute and draw a color distribution histogram for the input video (|avfilter.histogram|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/histogram_equalizer` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - This filter applies a global color histogram equalization on a per-frame basis (|avfilter.histeq|)
   * - :doc:`/effects_and_filters/video_effects/image_adjustment/hqx_interpolator` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Scale the input by 2, 3 or 4 using the hq*x magnification algorithm (|avfilter.hqx|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/hsl_primaries` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjust hue, saturation and lightness for each of the three primary colors. (|hslprimaries|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/hsl_range` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjust hue, saturation and lightness for a range of hue values. (|hslrange|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/hsvhold` 
     - |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Turns a certain HSV range into gray. (|avfilter.hsvhold|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/hsvkey` 
     - |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Turns a certain HSV range into transparency. Operates on YUV colors. (|avfilter.hsvkey|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/hue_shift` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Shifts the hue of a source image (|frei0r.hueshift0r|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/huesaturation` 
     - |appimage|\ |windows|\ |apple|
     - Misc
     - Apply hue-saturation-intensity adjustments. (|avfilter.huesaturation|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/brightness_keyframable` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Change the image |brightness| with keyframes (|brightness|)
   * - :doc:`/effects_and_filters/video_effects/image_adjustment/interlace_field_order` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Transform the field order of the input video (|avfilter.fieldorder|)
   * - :doc:`/effects_and_filters/video_effects/image_adjustment/interleave_deinterleave` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Deinterleave or interleave fields (|avfilter.il|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/invert` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Invert colors (|invert|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/invert` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Inverts all colors of a source image (|frei0r.invert0r|)
   * - :doc:`/effects_and_filters/video_effects/stylize/kaleid0sc0pe` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Misc
     - Applies a kaleidoscope effect (|frei0r.kaleid0sc0pe|)
   * - :doc:`/effects_and_filters/video_effects/deprecated/k-means_clustering` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - **Abandoned due to high CPU requirements**. Clusters of a source image by color and spatial distance (|frei0r.cluster|)
   * - :doc:`/effects_and_filters/video_effects/image_adjustment/kernel_deinterlacer` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Deinterlace input video by applying Donald Graft’s adaptive kernel deinterlacing. Works on interlaced parts of a video to produce progressive frames (|avfilter.kerndeint|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/key_spill_mop_up` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Reduces the visibility of key color spill in chroma keying (|frei0r.keyspillm0pup|)
   * - :doc:`/effects_and_filters/video_effects/stylize/kirsch` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Apply kirsch operator (|avfilter.kirsch|)
   * - Legacy ffmpeg deinterlacer **deprecated**
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Misc
     - Deinterlace interlaced video. (|avdeinterlace|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/lens_correction_frei0r` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Allow compensation of lens distortion (|frei0r.lenscorrection|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/lens_correction_avfilter` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Correct radial lens distortion (|avfilter.lenscorrection|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/letterb0xed` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Adds black borders at the top and bottom for cinema look (|frei0r.letterb0xed|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/levels` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjust levels (|frei0r.levels|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/lift_gamma_gain` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - A simple lift/gamma/gain effect, used for color grading. (|lift_gamma_gain|)
   * - :doc:`/effects_and_filters/video_effects/on_master/light_show` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - On Master
     - An audio visualization filter that colors the image proportional to the magnitude of the audio spectrum (|lightshow|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/limiter` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Limits the pixel components values to the specified range [min,max] (|avfilter.limiter|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/lumakey` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - This filter modifies image’s alpha channel as a function of its luma value. This is used together with a compositor to combine two images so that bright or dark areas of source image are overwritten on top of the destination image (|lumakey|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/lumaliftgammagain` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Filter can be used to apply lift gain and gamma corrections to luma values of an image (|lumaliftgaingamma|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/luminance` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Creates a luminance map of the image (|frei0r.luminance|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/mask_apply` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Apply the previous effects in the zone defined by a Mask Start effect. (|mask_apply|)
   * - :doc:`/effects_and_filters/video_effects/grain_and_noise/median` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Grain and Noise
     - Pick median pixel from certain rectangle defined by radius. (|avfilter.median|)
   * - :doc:`/effects_and_filters/video_effects/deprecated/medians` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Implements several median-type filters (|frei0r.medians|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/mirror` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Flip your image in any direction (|mirror|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/monochrome` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Convert video to gray using custom color filter (|avfilter.monochrome|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/motion_tracker` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Select a zone to follow its movements (|opencv.tracker|)
   * - :doc:`/effects_and_filters/video_effects/stylize/ndvi_filter` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - This filter creates a false image from a visible + infrared source (|frei0r.ndvi|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/negate` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Negate (invert) the input video or its alpha channel. (|avfilter.negate|)
   * - :doc:`/effects_and_filters/video_effects/motion/nervous` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Motion
     - Flushes frames in time in a nervous way (|frei0r.nervous|)
   * - :doc:`/effects_and_filters/video_effects/utility/nikon_d90_stairstepping_fix` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - Removes stairstepping artifacts from Nikon D90’s 720p videos. Sharp lines in videos from the Nikon D90 show steps each 8th or 9th line, assumedly due to poor downsampling. These can be smoothed out with this filter if they become too annoying (|frei0r.d90stairsteppingfix|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/normaliz0r` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Normalize (aka histogram stretch, contrast stretch) (|frei0r.normaliz0r|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/normalize_rgb_video` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Normalize RGB video (aka histogram stretching, contrast stretching). See: https://en.wikipedia.org/wiki/Normalization_(image_processing) (|avfilter.normalize|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/nosync0r` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Broken TV (|frei0r.nosync0r|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/obscure` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Hide a region of the clip (|obscure|)
   * - :doc:`/effects_and_filters/video_effects/stylize/oldfilm` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Moves the Picture up and down and random brightness change (|oldfilm|)
   * - :doc:`/effects_and_filters/video_effects/utility/oscilloscope` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - 2D Video Oscilloscope (|avfilter.oscilloscope|)
   * - :doc:`/effects_and_filters/video_effects/utility/oscilloscope_advanced` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - 2D video oscilloscope (|frei0r.pr0file|)
   * - :doc:`/effects_and_filters/video_effects/image_adjustment/phase` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Delay interlaced video by one field time so that the field order changes (|avfilter.phase|)
   * - :doc:`/effects_and_filters/video_effects/stylize/photosensitivity` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Filter out photosensitive epilepsy seizure-inducing flashes (|avfilter.photosensitivity|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/pillar_echo` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Create an echo effect (blur) outside of an area of interest (|pillar_echo|)
   * - :doc:`/effects_and_filters/video_effects/stylize/pixelize` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Pixelize input image (|frei0r.pixeliz0r|)
   * - :doc:`/effects_and_filters/video_effects/blur_and_sharpen/planes_blur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Set an expression for the box radius in pixels used for blurring the corresponding input plane. (|avfilter.boxblur|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/position_and_zoom` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Adjust size and position of clip (|affine|)
   * - :doc:`/effects_and_filters/video_effects/stylize/posterize` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Posterizes image by reducing the number of colors used in image (|frei0r.posterize|)
   * - :doc:`/effects_and_filters/video_effects/stylize/posterize_elbg` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Apply posterize effect, using the ELBG algorithm (|avfilter.elbg|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/premultiply` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Multiply (or divide) each color component by the pixel's alpha value (|frei0r.premultiply|)
   * - :doc:`/effects_and_filters/video_effects/stylize/prewitt` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Apply prewitt operator to input video stream (|avfilter.prewitt|)
   * - :doc:`/effects_and_filters/video_effects/stylize/primaries` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Reduce image to primary colors (|frei0r.primaries|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/rectangular_alpha_mask` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Creates a square alpha-channel mask (|frei0r.mask0mate|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/rgb_adjustment` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Simple color adjustment (|frei0r.coloradj_RGB|)
   * - :doc:`/effects_and_filters/video_effects/deprecated/rgbnoise` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Adds RGB noise to image (|frei0r.rgbnoise|)
   * - :doc:`/effects_and_filters/video_effects/utility/rgb_parade` 
     - |linux|\ |appimage|\ |windows|
     - Utility
     - 
   * - :doc:`/effects_and_filters/video_effects/stylize/rgba_shift` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Shift R/G/B/A pixels horizontally and/or vertically (|avfilter.rgbashift|)
   * - :doc:`/effects_and_filters/video_effects/stylize/rgbsplit0r` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - RGB splitter and shifting (|frei0r.rgbsplit0r|)
   * - :doc:`/effects_and_filters/video_effects/stylize/roberts` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Apply roberts cross operator to input video stream (|avfilter.roberts|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/rotate_3_way` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Rotate clip in any 3 directions (|affine|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/rotoscoping` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Keyframable vector based |rotoscoping| (|rotoscoping|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/rotoscoping_mask` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - This filter makes a snapshot of the frame before a keyframable vector based rotoscoping is applied. Use it together with the mask_apply effect, that uses a transition to composite the current frame's image over the snapshot. The typical use case is to add effects in the following sequence: this effect, zero or more effects, mask_apply. (|mask_start|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/saturation` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjusts the saturation of a source image (|frei0r.saturat0r|)
   * - :doc:`/effects_and_filters/video_effects/generate/scanline0r` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Interlaced black lines (|frei0r.scanline0r|)
   * - :doc:`/effects_and_filters/video_effects/stylize/scharr` 
     - |appimage|\ |windows|\ |apple|
     - Misc
     - Apply scharr operator. (|avfilter.scharr|)
   * - :doc:`/effects_and_filters/video_effects/grain_and_noise/scratchlines` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Grain and Noise
     - Creates scratch lines over the picture (|lines|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/scroll` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Pick median pixel from certain rectangle defined by radius. (|avfilter.scroll|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/secondary_color_selection_mask` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - This filter takes a snapshot of the frame before a keyframable Chroma Key selection with more advanced options (e.g. different color models) is applied. Use it together with the mask_apply effect, that uses a transition to composite the current frame's image over the snapshot. The typical use case is to add effects in the following sequence: this effect, zero or more effects, mask_apply. (|mask_start|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/sepia` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Turn clip colors to |sepia| (|sepia|)
   * - :doc:`/effects_and_filters/video_effects/image_adjustment/set_range` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Force color range for the output video frame (|avfilter.setrange|)
   * - :doc:`/effects_and_filters/video_effects/blur_and_sharpen/shape_adaptive_blur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Shape Adaptive Blur (|avfilter.sab|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/shape_alpha` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Create an alpha channel (transparency) based on another resource (|shape|)
   * - :doc:`/effects_and_filters/video_effects/blur_and_sharpen/sharp_unsharp` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Sharpen or Blur your video (|avfilter.unsharp|)
   * - :doc:`/effects_and_filters/video_effects/deprecated/sharpen` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Unsharp masking (port from Mplayer) (|frei0r.sharpness|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/shear` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Shear transform the input image (|avfilter.shear|)
   * - :doc:`/effects_and_filters/video_effects/stylize/sigmoidal_transfer` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Desaturates image and creates a particular look that could be called Stamp, Newspaper, or Photocopy (|frei0r.sigmoidaltransfer|)
   * - :doc:`/effects_and_filters/video_effects/blur_and_sharpen/smartblur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Blur the input video without impacting the outlines (|avfilter.smartblur|)
   * - :doc:`/effects_and_filters/video_effects/stylize/sobel` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Sobel filter (|frei0r.sobel|)
   * - :doc:`/effects_and_filters/video_effects/stylize/sobel_planes` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Apply sobel operators to input video stream (|avfilter.sobel|)
   * - :doc:`/effects_and_filters/video_effects/stylize/soft_glow` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Does softglow effect on highlights (|frei0r.softglow|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/sat` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Changes Slope, Offset, and Power of the color components, and the overall Saturation, according to the ASC CDL (Color Decision List) (|frei0r.sopsat|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/spillsuppress` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Remove green or blue spill light from subjects shot in front of green or blue screen (|frei0r.spillsupress|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/spot_remover` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Replace an area with interpolated pixels. The new pixel values are interpolated from the nearest pixel. (|spot_remover|)
   * - :doc:`/effects_and_filters/video_effects/blur_and_sharpen/square_blur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Square Blur (|frei0r.squareblur|)
   * - :doc:`/effects_and_filters/video_effects/vr360_and_3d/stereoscopic_3d` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - VR360 and 3D
     - Convert between different stereoscopic image formats (|avfilter.stereo3d|)
   * - :doc:`/effects_and_filters/video_effects/image_adjustment/super2xsai` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Scale the input by 2x using the Super2xSaI pixel art algorithm (|avfilter.super2xsai|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/swapuv` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Swap U and V components (|avfilter.swapuv|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/technicolor` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Oversaturate the color in video, like in old Technicolor movies (|tcolor|)
   * - :doc:`/effects_and_filters/video_effects/stylize/threshold` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Thresholds a source image (|frei0r.threshold0r|)
   * - :doc:`/effects_and_filters/video_effects/utility/timeout_indicator` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - Timeout indicators e.g. for slides (|frei0r.timeout|)
   * - :doc:`/effects_and_filters/video_effects/generate/timer` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Overlay a |timer| onto the video (|timer|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/tint` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Maps source image luminance between two colors specified (|frei0r.tint0r|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/transform` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Position, Scale and opacity, (|qtblend|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/transparency` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - Tunes the alpha channel (|frei0r.transparency|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/transpose` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Transpose rows with columns in the input video and optionally flip it (|avfilter.transpose|)
   * - :doc:`/effects_and_filters/video_effects/utility/vectorscope` 
     - |linux|\ |appimage|\ |windows|
     - Utility
     - Display a vectorscope of the video data (|frei0r.vectorscope|)
   * - :doc:`/effects_and_filters/video_effects/utility/vectorscope_advanced` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - Display 2 color component values in the two dimensional graph (which is called a vectorscope) (|avfilter.vectorscope|)
   * - :doc:`/effects_and_filters/video_effects/motion/vertigo` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Motion
     - Alpha blending with zoomed and rotated images (|frei0r.vertigo|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/vibrance` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Boost or alter saturation.  (|avfilter.vibrance|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/video_equalizer` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjust Brightness, contrast, gamma, saturation (|avfilter.eq|)
   * - :doc:`/effects_and_filters/video_effects/generate/video_grid` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Create a video grid (|frei0r.cairoimagegrid|)
   * - :doc:`/effects_and_filters/video_effects/utility/video_values` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - Measure video values (|frei0r.pr0be|)
   * - :doc:`/effects_and_filters/video_effects/utility/video_waveform_monitor` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - The waveform monitor plots color component intensity. By default luminance only. Each column of the waveform corresponds to a column of pixels in the source video.  (|avfilter.waveform|)
   * - :doc:`/effects_and_filters/video_effects/grain_and_noise/video_noise_generator` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Grain and Noise
     - Add noise on video input frame (|avfilter.noise|)
   * - :doc:`/effects_and_filters/video_effects/generate/vignette` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Natural Lens vignetting effect (|frei0r.vignette|)
   * - :doc:`/effects_and_filters/video_effects/generate/vignette_effect` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Adjustable Vignette (|vignette|)
   * - :doc:`/effects_and_filters/video_effects/vr360_and_3d/vr360_cap` 
     - |appimage|
     - VR360 and 3D
     - Attempts to fill in zenith and nadir by stretching and blurring the image data. It samples a band of latitude near the start of the effect and stretches and blurs it over the pole. (|frei0r.bigsh0t_cap|)
   * - :doc:`/effects_and_filters/video_effects/vr360_and_3d/vr360_equi2stereo` 
     - |appimage|
     - VR360 and 3D
     - Converts an equirectangular frame (panoramic) to a rectilinear frame (what you’re used to seeing). Can be used to preview what will be shown in a 360 video viewer. Delayed frame blitting mapping on a time bitmap (|frei0r.bigsh0t_eq_to_rect|)
   * - :doc:`/effects_and_filters/video_effects/vr360_and_3d/vr360_equi_mask` 
     - |appimage|
     - VR360 and 3D
     - Adds a black matte to the frame. Use this if you filmed using a 360 camera but only want to use part of the 360 image - for example if you and the film crew occupy the 90 degrees behind the camera (|frei0r.bigsh0t_eq_mask|)
   * - :doc:`/effects_and_filters/video_effects/vr360_and_3d/vr360_equi2rect` 
     - |appimage|
     - VR360 and 3D
     - Converts an equirectangular frame (panoramic) to a rectilinear frame (what you’re used to seeing). Can be used to preview what will be shown in a 360 video viewer. Delayed frame blitting mapping on a time bitmap (|frei0r.bigsh0t_eq_to_rect|)
   * - :doc:`/effects_and_filters/video_effects/vr360_and_3d/vr360_rect2equi` 
     - |appimage|
     - VR360 and 3D
     - Converts a rectilinear (a normal-looking) image to an equirectangular image. Use this together with transform 360 to place “normal” footage in a 360 movie (|frei0r.bigsh0t_rect_to_eq|)
   * - :doc:`/effects_and_filters/video_effects/vr360_and_3d/vr360_stabilize` 
     - |appimage|
     - VR360 and 3D
     - Stabilizes 360 footage. The plugin works in two phases - analysis and stabilization. When analyzing footage, it detects frame-to-frame rotation, and when stabilizing it tries to correct high-frequency motion (shake) (|frei0r.bigsh0t_stabilize_360|)
   * - :doc:`/effects_and_filters/video_effects/vr360_and_3d/vr360_transform` 
     - |appimage|
     - VR360 and 3D
     - Rotates a panoramic image (|frei0r.bigsh0t_transform_360|)
   * - :doc:`/effects_and_filters/video_effects/vr360_and_3d/vr360_wrap` 
     - |appimage|
     - VR360 and 3D
     - Stretches a section of the equirectangular panorama to cover the entire VR sphere (|frei0r.bigsh0t_wrap|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/wave` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Makes waves on your clip with keyframes (|wave|)
   * - :doc:`/effects_and_filters/video_effects/grain_and_noise/vague_denoiser`
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Grain and Noise
     - Wavelet-based denoiser (|avfilter.vaguedenoiser|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/white_balance` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjust the white balance / color temperature (|frei0r.balanc0r|)
   * - :doc:`/effects_and_filters/video_effects/color_image_correction/white_balance_lms` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Do simple color correction, in a physically meaningful way (|frei0r.colgate|)
   * - :doc:`/effects_and_filters/video_effects/image_adjustment/xbr_interpolator` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Apply the xBR high-quality magnification filter which is designed for pixel art. It follows a set of edge-detection rules, see this |xbr_tutorial| (|avfilter.xbr|)
   * - :doc:`/effects_and_filters/video_effects/misc/xine_deinterlacer` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Misc
     - Deinterlace interlaced video. (|deinterlace|)
   * - :doc:`/effects_and_filters/video_effects/transform_distort_perspective/zoom_pan` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort, and Perspective
     - Apply Zoom and Pan effect (|avfilter.zoompan|)


----

.. [1] |linux|: available in the installed version; |appimage|: available in the appimage; |windows|: available in the Windows version; |apple|: available in the MacOS (Intel only) version


.. Link list

.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   External
   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. |xbr_tutorial| raw:: html
   
   <a href="https://forums.libreto.com/t/xbr-algorithm-tutorial/123" target="_blank">xbr-algorithm-tutorial</a>

.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Video
   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. |frei0r.three_point_balance| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-three_point_balance/" target="_blank">frei0r.three_point_balance</a>


.. |frei0r.threelay0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-threelay0r/" target="_blank">frei0r.threelay0r</a>


.. |avfilter.fftdnoiz| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-fftdnoiz/" target="_blank">avfilter.fftdnoiz</a>


.. |frei0r.aech0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-aech0r/" target="_blank">frei0r.aech0r</a>


.. |frei0r.alphagrad| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-alpha0ps_alphagrad/" target="_blank">frei0r.alpha0ps_alphagrad</a>


.. |frei0r.alpha0ps| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-alpha0ps_alpha0ps/" target="_blank">frei0r.alpha0ps_alpha0ps</a>


.. |frei0r.alphaspot| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-alpha0ps_alphaspot/" target="_blank">frei0r.alpha0ps_alphaspot</a>


.. |mask_start| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterMask_start/" target="_blank">mask_start</a>


.. |strobe| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterStrobe/" target="_blank">strobe</a>


.. |avfilter.alphaextract| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-alphaextract/" target="_blank">avfilter.alphaextract</a>


.. |avfilter.lut3d| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-lut3d/" target="_blank">avfilter.lut3d</a>


.. |audiolevelgraph| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAudiolevelgraph/" target="_blank">audiolevelgraph</a>


.. |audiospectrum| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAudiospectrum/" target="_blank">audiospectrum</a>


.. |audiowave| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAudiowave/" target="_blank">audiowave</a>


.. |audiowaveform| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAudiowaveform/" target="_blank">audiowaveform</a>


.. |avfilter.avgblur| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-avgblur/" target="_blank">avfilter.avgblur</a>


.. |avfilter.backgroundkey| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-backgroundkey/" target="_blank">avfilter.backgroundkey</a>


.. |frei0r.curves| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-curves/" target="_blank">frei0r.curves</a>


.. |avfilter.bilateral| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-bilateral/" target="_blank">avfilter.bilateral</a>


.. |threshold| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterThreshold/" target="_blank">threshold</a>


.. |frei0r.twolay0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-twolay0r/" target="_blank">frei0r.twolay0r</a>


.. |avfilter.blockdetect| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-blockdetect/" target="_blank">avfilter.blockdetect</a>


.. |frei0r.bluescreen0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-bluescreen0r/" target="_blank">frei0r.bluescreen0r</a>


.. |frei0r.IIRblur| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-iirblur/" target="_blank">frei0r.IIRblur</a>


.. |avfilter.blurdetect| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-blurdetect/" target="_blank">avfilter.blurdetect</a>


.. |boxblur| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterBoxblur/" target="_blank">boxblur</a>


.. |box_blur| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterBox_blur/" target="_blank">box_blur</a>


.. |frei0r.brightness| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-brightness/" target="_blank">frei0r.brightness</a>


.. |brightness| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterBrightness/" target="_blank">brightness</a>


.. |frei0r.bw0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-bw0r/" target="_blank">frei0r.bw0r</a>


.. |frei0r.cairogradient| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-cairogradient/" target="_blank">frei0r.cairogradient</a>


.. |frei0r.cartoon| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-cartoon/" target="_blank">frei0r.cartoon</a>


.. |frei0r.B| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-b/" target="_blank">frei0r.B</a>


.. |frei0r.G| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-g/" target="_blank">frei0r.G</a>


.. |frei0r.R| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-r/" target="_blank">frei0r.R</a>


.. |charcoal| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterCharcoal/" target="_blank">charcoal</a>


.. |avfilter.chromahold| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-chromahold/" target="_blank">avfilter.chromahold</a>


.. |chroma_hold| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterChroma_hold/" target="_blank">chroma_hold</a>


.. |frei0r.select0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-select0r/" target="_blank">frei0r.select0r</a>


.. |chroma| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterChroma/" target="_blank">chroma</a>


.. |avfilter.chromanr| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-chromanr/" target="_blank">avfilter.chromanr</a>


.. |avfilter.chromashift| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-chromashift/" target="_blank">avfilter.chromashift</a>


.. |avfilter.ciescope| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-ciescope/" target="_blank">avfilter.ciescope</a>


.. |avfilter.selectivecolor| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-selectivecolor/" target="_blank">avfilter.selectivecolor</a>


.. |avfilter.colorbalance| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-colorbalance/" target="_blank">avfilter.colorbalance</a>


.. |avfilter.colorchannelmixer| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-colorchannelmixer/" target="_blank">avfilter.colorchannelmixer</a>


.. |avfilter.colorcontrast| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-colorcontrast/" target="_blank">avfilter.colorcontrast</a>


.. |avfilter.colorcorrect| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-colorcorrect/" target="_blank">avfilter.colorcorrect</a>


.. |frei0r.colordistance| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-colordistance/" target="_blank">frei0r.colordistance</a>


.. |frei0r.colortap| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-colortap/" target="_blank">frei0r.colortap</a>


.. |avfilter.colorhold| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-colorhold/" target="_blank">avfilter.colorhold</a>


.. |avfilter.colorlevels| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-colorlevels/" target="_blank">avfilter.colorlevels</a>


.. |avfilter.colormatrix| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-colormatrix/" target="_blank">avfilter.colormatrix</a>


.. |avfilter.colorize| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-colorize/" target="_blank">avfilter.colorize</a>


.. |avfilter.colorspace| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-colorspace/" target="_blank">avfilter.colorspace</a>


.. |avfilter.colortemperature| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-colortemperature/" target="_blank">avfilter.colortemperature</a>


.. |frei0r.colorize| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-colorize/" target="_blank">frei0r.colorize</a>


.. |frei0r.contrast0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-contrast0r/" target="_blank">frei0r.contrast0r</a>


.. |avfilter.cas| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-cas/" target="_blank">avfilter.cas</a>


.. |frei0r.c0rners| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-c0rners/" target="_blank">frei0r.c0rners</a>


.. |qtcrop| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterQtcrop/" target="_blank">qtcrop</a>


.. |frei0r.scale0tilt| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-scale0tilt/" target="_blank">frei0r.scale0tilt</a>


.. |burningtv| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterBurningtv/" target="_blank">BurningTV</a>


.. |dance| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterDance/" target="_blank">dance</a>


.. |avfilter.datascope| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-datascope/" target="_blank">avfilter.datascope</a>


.. |avfilter.dblur| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-dblur/" target="_blank">avfilter.dblur</a>


.. |avfilter.dctdnoiz| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-dctdnoiz/" target="_blank">avfilter.dctdnoiz</a>


.. |avfilter.deband| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-deband/" target="_blank">avfilter.deband</a>


.. |frei0r.defish0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-defish0r/" target="_blank">frei0r.defish0r</a>


.. |avfilter.delogo| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-delogo/" target="_blank">avfilter.delogo</a>


.. |frei0r.denoise_hqdn3d| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-denoise_hqdn3d/" target="_blank">frei0r.denoise_hqdn3d</a>


.. |avfilter.despill| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-despill/" target="_blank">avfilter.despill</a>


.. |avfilter.dilation| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-dilation/" target="_blank">avfilter.dilation</a>


.. |frei0r.distort0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-distort0r/" target="_blank">frei0r.distort0r</a>


.. |frei0r.dither| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-dither/" target="_blank">frei0r.dither</a>


.. |avfilter.dnn_classify| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-dnn_classify/" target="_blank">avfilter.dnn_classify</a>


.. |avfilter.dnn_detect| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-dnn_detect/" target="_blank">avfilter.dnn_detect</a>


.. |avfilter.drawbox| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-drawbox/" target="_blank">avfilter.drawbox</a>


.. |avfilter.drawgrid| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-drawgrid/" target="_blank">avfilter.drawgrid</a>


.. |dropshadow| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterDropshadow/" target="_blank">dropshadow</a>


.. |dust| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterDust/" target="_blank">dust</a>


.. |dynamictext| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterDynamictext/" target="_blank">dynamictext</a>


.. |crop| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterCrop/" target="_blank">crop</a>


.. |avfilter.edgedetect| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-edgedetect/" target="_blank">avfilter.edgedetect</a>


.. |frei0r.edgeglow| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-edgeglow/" target="_blank">frei0r.edgeglow</a>


.. |frei0r.elastic_scale| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-elastic_scale/" target="_blank">frei0r.elastic_scale</a>


.. |avfilter.elbg| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-elbg/" target="_blank">avfilter.elbg</a>


.. |frei0r.emboss| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-emboss/" target="_blank">frei0r.emboss</a>


.. |avfilter.epx| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-epx/" target="_blank">avfilter.epx</a>


.. |frei0r.equaliz0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-equaliz0r/" target="_blank">frei0r.equaliz0r</a>


.. |avfilter.erosion| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-erosion/" target="_blank">avfilter.erosion</a>


.. |avfilter.exposure| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-exposure/" target="_blank">avfilter.exposure</a>


.. |frei0r.facebl0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-facebl0r/" target="_blank">frei0r.facebl0r</a>


.. |frei0r.facedetect| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-facedetect/" target="_blank">frei0r.facedetect</a>


.. |avcolor_space| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvcolor_space/" target="_blank">avcolor_space</a>


.. |swscale| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterSwscale/" target="_blank">swscale</a>


.. |avfilter.fftfilt| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-fftfilt/" target="_blank">avfilter.fftfilt</a>


.. |avfilter.fillborders| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-fillborders/" target="_blank">avfilter.fillborders</a>


.. |frei0r.filmgrain| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-filmgrain/" target="_blank">frei0r.filmgrain</a>


.. |avfilter.hflip| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-hflip/" target="_blank">avfilter.hflip</a>


.. |avfilter.vflip| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-vflip/" target="_blank">avfilter.vflip</a>


.. |frei0r.flippo| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-flippo/" target="_blank">frei0r.flippo</a>


.. |freeze| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFreeze/" target="_blank">freeze</a>


.. |frei0r.gamma| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-gamma/" target="_blank">frei0r.gamma</a>


.. |gamma| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterGamma/" target="_blank">gamma</a>


.. |avfilter.gblur| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-gblur/" target="_blank">avfilter.gblur</a>


.. |frei0r.gateweave| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-gateweave/" target="_blank">frei0r.gateweave</a>


.. |frei0r.glitch0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-glitch0r/" target="_blank">frei0r.glitch0r</a>


.. |frei0r.glow| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-glow/" target="_blank">frei0r.glow</a>


.. |gpsgraphic| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterGpsgraphic/" target="_blank">gpsgraphic</a>


.. |gpstext| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterGpstext/" target="_blank">gpstext</a>


.. |avfilter.gradfun| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-gradfun/" target="_blank">avfilter.gradfun</a>


.. |grain| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterGrain/" target="_blank">grain</a>


.. |avfilter.grayworld| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-grayworld/" target="_blank">avfilter.grayworld</a>


.. |greyscale| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterGreyscale/" target="_blank">greyscale</a>


.. |avfilter.histogram| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-histogram/" target="_blank">avfilter.histogram</a>


.. |avfilter.histeq| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-histeq/" target="_blank">avfilter.histeq</a>


.. |avfilter.hqx| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-hqx/" target="_blank">avfilter.hqx</a>


.. |avfilter.hsvhold| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-hsvhold/" target="_blank">avfilter.hsvhold</a>


.. needs updating

.. |hslprimaries| raw:: html

   <a href="https://www.mltframework.org/plugins/PluginsFilters/" target="_blank">hslprimaries</a>


.. needs updating

.. |hslrange| raw:: html

   <a href="https://www.mltframework.org/plugins/PluginsFilters/" target="_blank">hslrange</a>


.. |avfilter.hsvkey| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-hsvkey/" target="_blank">avfilter.hsvkey</a>


.. |frei0r.hueshift0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-hueshift0r/" target="_blank">frei0r.hueshift0r</a>


.. |avfilter.huesaturation| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-huesaturation/" target="_blank">avfilter.huesaturation</a>


.. |avfilter.fieldorder| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-fieldorder/" target="_blank">avfilter.fieldorder</a>


.. |avfilter.il| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-il/" target="_blank">avfilter.il</a>


.. |invert| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterInvert/" target="_blank">invert</a>


.. |frei0r.invert0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-invert0r/" target="_blank">frei0r.invert0r</a>


.. |frei0r.kaleid0sc0pe| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-kaleid0sc0pe/" target="_blank">frei0r.kaleid0sc0pe</a>


.. |frei0r.cluster| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-cluster/" target="_blank">frei0r.cluster</a>


.. |avfilter.kerndeint| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-kerndeint/" target="_blank">avfilter.kerndeint</a>


.. |frei0r.keyspillm0pup| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-keyspillm0pup/" target="_blank">frei0r.keyspillm0pup</a>


.. |avfilter.kirsch| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-kirsch/" target="_blank">avfilter.kirsch</a>


.. |avfilter.latency| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-latency/" target="_blank">avfilter.latency</a>


.. |avdeinterlace| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvdeinterlace/" target="_blank">avdeinterlace</a>


.. |frei0r.lenscorrection| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-lenscorrection/" target="_blank">frei0r.lenscorrection</a>


.. |avfilter.lenscorrection| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-lenscorrection/" target="_blank">avfilter.lenscorrection</a>


.. |frei0r.letterb0xed| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-letterb0xed/" target="_blank">frei0r.letterb0xed</a>


.. |frei0r.levels| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-levels/" target="_blank">frei0r.levels</a>


.. |lift_gamma_gain| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLift_gamma_gain/" target="_blank">lift_gamma_gain</a>


.. |lightshow| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLightshow/" target="_blank">lightshow</a>


.. |avfilter.limiter| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-limiter/" target="_blank">avfilter.limiter</a>


.. |lumakey| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLumakey/" target="_blank">lumakey</a>


.. |lumaliftgaingamma| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLumaliftgaingamma/" target="_blank">lumaliftgaingamma</a>


.. |frei0r.luminance| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-luminance/" target="_blank">frei0r.luminance</a>


.. |mask_apply| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterMask_apply/" target="_blank">mask_apply</a>


.. |avfilter.median| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-median/" target="_blank">avfilter.median</a>


.. |frei0r.medians| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-medians/" target="_blank">frei0r.medians</a>


.. |mirror| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterMirror/" target="_blank">mirror</a>


.. |avfilter.monochrome| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-monochrome/" target="_blank">avfilter.monochrome</a>


.. |opencv.tracker| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterOpencv-tracker/" target="_blank">opencv.tracker</a>


.. |frei0r.ndvi| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-ndvi/" target="_blank">frei0r.ndvi</a>


.. |avfilter.negate| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-negate/" target="_blank">avfilter.negate</a>


.. |frei0r.nervous| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-nervous/" target="_blank">frei0r.nervous</a>


.. |frei0r.d90stairsteppingfix| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-d90stairsteppingfix/" target="_blank">frei0r.d90stairsteppingfix</a>


.. |frei0r.normaliz0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-normaliz0r/" target="_blank">frei0r.normaliz0r</a>


.. |avfilter.normalize| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-normalize/" target="_blank">avfilter.normalize</a>


.. |frei0r.nosync0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-nosync0r/" target="_blank">frei0r.nosync0r</a>


.. |obscure| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterObscure/" target="_blank">obscure</a>


.. |oldfilm| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterOldfilm/" target="_blank">oldfilm</a>


.. |avfilter.oscilloscope| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-oscilloscope/" target="_blank">avfilter.oscilloscope</a>


.. |frei0r.pr0file| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-pr0file/" target="_blank">frei0r.pr0file</a>


.. |avfilter.phase| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-phase/" target="_blank">avfilter.phase</a>


.. |avfilter.photosensitivity| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-photosensitivity/" target="_blank">avfilter.photosensitivity</a>


.. |pillar_echo| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterPillar_echo/" target="_blank">pillar_echo</a>


.. |frei0r.pixeliz0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-pixeliz0r/" target="_blank">frei0r.pixeliz0r</a>


.. |avfilter.pixelize| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-pixelize/" target="_blank">avfilter.pixelize</a>


.. |frei0r.pixs0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-pixs0r/" target="_blank">frei0r.pixs0r</a>


.. |avfilter.boxblur| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-boxblur/" target="_blank">avfilter.boxblur</a>


.. |affine| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAffine/" target="_blank">affine</a>


.. |frei0r.posterize| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-posterize/" target="_blank">frei0r.posterize</a>


.. |frei0r.premultiply| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-premultiply/" target="_blank">frei0r.premultiply</a>


.. |avfilter.prewitt| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-prewitt/" target="_blank">avfilter.prewitt</a>


.. |frei0r.primaries| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-primaries/" target="_blank">frei0r.primaries</a>


.. |frei0r.mask0mate| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-mask0mate/" target="_blank">frei0r.mask0mate</a>


.. |rescale| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterRescale/" target="_blank">rescale</a>


.. |frei0r.coloradj_RGB| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-coloradj_rgb/" target="_blank">frei0r.coloradj_RGB</a>


.. |frei0r.rgbnoise| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-rgbnoise/" target="_blank">frei0r.rgbnoise</a>


.. |frei0r.rgbparade| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-rgbparade/" target="_blank">frei0r.rgbparade</a>


.. |avfilter.rgbashift| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-rgbashift/" target="_blank">avfilter.rgbashift</a>


.. |frei0r.rgbsplit0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-rgbsplit0r/" target="_blank">frei0r.rgbsplit0r</a>


.. |avfilter.roberts| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-roberts/" target="_blank">avfilter.roberts</a>


.. |rotoscoping| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterRotoscoping/" target="_blank">rotoscoping</a>


.. |frei0r.saturat0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-saturat0r/" target="_blank">frei0r.saturat0r</a>


.. |frei0r.scanline0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-scanline0r/" target="_blank">frei0r.scanline0r</a>


.. |avfilter.scdet| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-scdet/" target="_blank">avfilter.scdet</a>


.. |avfilter.scharr| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-scharr/" target="_blank">avfilter.scharr</a>


.. |lines| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLines/" target="_blank">lines</a>


.. |avfilter.scroll| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-scroll/" target="_blank">avfilter.scroll</a>


.. |sepia| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterSepia/" target="_blank">sepia</a>


.. |avfilter.setrange| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-setrange/" target="_blank">avfilter.setrange</a>


.. |avfilter.sab| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-sab/" target="_blank">avfilter.sab</a>


.. |shape| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterShape/" target="_blank">shape</a>


.. |avfilter.unsharp| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-unsharp/" target="_blank">avfilter.unsharp</a>


.. |frei0r.sharpness| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-sharpness/" target="_blank">frei0r.sharpness</a>


.. |avfilter.shear| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-shear/" target="_blank">avfilter.shear</a>


.. |frei0r.sigmoidaltransfer| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-sigmoidaltransfer/" target="_blank">frei0r.sigmoidaltransfer</a>


.. |avfilter.siti| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-siti/" target="_blank">avfilter.siti</a>


.. |avfilter.smartblur| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-smartblur/" target="_blank">avfilter.smartblur</a>


.. |frei0r.sobel| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-sobel/" target="_blank">frei0r.sobel</a>


.. |avfilter.sobel| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-sobel/" target="_blank">avfilter.sobel</a>


.. |frei0r.softglow| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-softglow/" target="_blank">frei0r.softglow</a>


.. |frei0r.sopsat| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-sopsat/" target="_blank">frei0r.sopsat</a>


.. |frei0r.spillsupress| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-spillsupress/" target="_blank">frei0r.spillsupress</a>


.. |spot_remover| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterSpot_remover/" target="_blank">spot_remover</a>


.. |frei0r.squareblur| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-squareblur/" target="_blank">frei0r.squareblur</a>


.. |avfilter.stereo3d| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-stereo3d/" target="_blank">avfilter.stereo3d</a>


.. |avfilter.super2xsai| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-super2xsai/" target="_blank">avfilter.super2xsai</a>


.. |avfilter.swapuv| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-swapuv/" target="_blank">avfilter.swapuv</a>


.. |tcolor| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterTcolor/" target="_blank">tcolor</a>


.. |frei0r.threshold0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-threshold0r/" target="_blank">frei0r.threshold0r</a>


.. |frei0r.timeout| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-timeout/" target="_blank">frei0r.timeout</a>


.. |timer| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterTimer/" target="_blank">timer</a>


.. |frei0r.tint0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-tint0r/" target="_blank">frei0r.tint0r</a>


.. |avfilter.tonemap_vaapi| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-tonemap_vaapi/" target="_blank">avfilter.tonemap_vaapi</a>


.. |qtblend| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterQtblend/" target="_blank">qtblend</a>


.. |frei0r.transparency| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-transparency/" target="_blank">frei0r.transparency</a>


.. |avfilter.transpose| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-transpose/" target="_blank">avfilter.transpose</a>


.. |typewriter| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterTypewriter/" target="_blank">typewriter</a>


.. |frei0r.vectorscope| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-vectorscope/" target="_blank">frei0r.vectorscope</a>


.. |avfilter.vectorscope| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-vectorscope/" target="_blank">avfilter.vectorscope</a>


.. |frei0r.vertigo| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-vertigo/" target="_blank">frei0r.vertigo</a>


.. |avfilter.vibrance| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-vibrance/" target="_blank">avfilter.vibrance</a>


.. |avfilter.eq| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-eq/" target="_blank">avfilter.eq</a>


.. |frei0r.cairoimagegrid| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-cairoimagegrid/" target="_blank">frei0r.cairoimagegrid</a>


.. |frei0r.pr0be| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-pr0be/" target="_blank">frei0r.pr0be</a>


.. |avfilter.waveform| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-waveform/" target="_blank">avfilter.waveform</a>


.. |avfilter.noise| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-noise/" target="_blank">avfilter.noise</a>


.. |frei0r.vignette| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-vignette/" target="_blank">frei0r.vignette</a>


.. |vignette| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterVignette/" target="_blank">vignette</a>


.. |frei0r.bigsh0t_cap| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-bigsh0t_eq_cap/" target="_blank">frei0r.bigsh0t_eq_cap</a>


.. |frei0r.bigsh0t_eq_to_rect| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-bigsh0t_eq_to_rect/" target="_blank">frei0r.bigsh0t_eq_to_rect</a>


.. |frei0r.bigsh0t_eq_mask| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-bigsh0t_eq_mask/" target="_blank">frei0r.bigsh0t_eq_mask</a>


.. |frei0r.bigsh0t_hemi_to_eq| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-bigsh0t_hemi_to_eq/" target="_blank">frei0r.bigsh0t_hemi_to_eq</a>


.. |frei0r.bigsh0t_rect_to_eq| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-bigsh0t_rect_to_eq/" target="_blank">frei0r.bigsh0t_rect_to_eq</a>


.. |frei0r.bigsh0t_stabilize_360| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-bigsh0t_stabilize_360/" target="_blank">frei0r.bigsh0t_stabilize_360</a>


.. |frei0r.bigsh0t_transform_360| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-bigsh0t_transform_360/" target="_blank">frei0r.bigsh0t_transform_360</a>


.. |frei0r.bigsh0t_wrap| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-bigsh0t_eq_wrap/" target="_blank">frei0r.bigsh0t_eq_wrap</a>


.. |wave| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterWave/" target="_blank">wave</a>


.. |avfilter.vaguedenoiser| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-vaguedenoiser/" target="_blank">avfilter.vaguedenoiser</a>


.. |frei0r.balanc0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-balanc0r/" target="_blank">frei0r.balanc0r</a>


.. |frei0r.colgate| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-colgate/" target="_blank">frei0r.colgate</a>


.. |avfilter.xbr| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-xbr/" target="_blank">avfilter.xbr</a>


.. |deinterlace| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterDeinterlace/" target="_blank">deinterlace</a>


.. |avfilter.zoompan| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-zoompan/" target="_blank">avfilter.zoompan</a>


.. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   To be done
   ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Video
   ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   * - :doc:`/effects_and_filters/video_effects/misc/scdet` |linux|\ |appimage|\ |windows|\ |apple|
     - Misc
     - Detect video scene change (|avfilter.scdet|)
   * - :doc:`/effects_and_filters/video_effects/misc/siti` |appimage|\ |windows|\ |apple|
     - Misc
     - Calculate spatial information (SI) and temporal information (TI). (|avfilter.siti|)
   * - :doc:`/effects_and_filters/video_effects/stylize/typewriter`|windows|\ |apple|
     - Stylize
     - Typewriter effect v0.3.3 To be applied on title clips only. (|typewriter|)
   * - :doc:`/effects_and_filters/video_effects/alpha_mask_keying/shape_alpha_mask` |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask, and Keying
     - This filter makes a snapshot of the frame before an alpha channel (transparency) is created based on another resource. Use it together with the mask_apply effect, that uses a transition to composite the current frame's image over the snapshot. The typical use case is to add effects in the following sequence: this effect, zero or more effects, mask_apply. (|mask_start|)
   * - :doc:`/effects_and_filters/video_effects/image_adjustment/rescale` |appimage|
     - Image Adjustment
     - Scale the producer video frames size to match the consumer. This filter is designed for use as a normaliser for the loader producer (|rescale|)
   * - :doc:`/effects_and_filters/video_effects/misc/pixelize` |appimage|\ |windows|\ |apple|
     - Misc
     - Pixelize video. (|avfilter.pixelize|)
   * - :doc:`/effects_and_filters/video_effects/misc/latency` |appimage|\ |windows|\ |apple|
     - Misc
     - Report video filtering latency. (|avfilter.latency|)
   * - :doc:`/effects_and_filters/video_effects/misc/face_blur` |appimage|\ |windows|\ |apple|
     - Misc
     - Automatically detect and blur a face using OpenCV (|frei0r.facebl0r|)
   * - :doc:`/effects_and_filters/video_effects/misc/face_detect` |appimage|\ |windows|\ |apple|
     - Misc
     - Detect faces and draw shapes on them using OpenCV (|frei0r.facedetect|)
   * - :doc:`/effects_and_filters/video_effects/misc/ffmeg_image_converter` |linux|\ |appimage|\ |windows|\ |apple|
     - Misc
     - Converts the colorspace and pixel format. (|avcolor_space|)
   * - :doc:`/effects_and_filters/video_effects/misc/ffmeg_image_scaler` |linux|\ |appimage|\ |windows|\ |apple|
     - Misc
     - Change the resolution of an image. (|swscale|)
   * - :doc:`/effects_and_filters/video_effects/misc/dnn_classify` |appimage|\ |windows|\ |apple|
     - Misc
     - Apply DNN classify filter to the input. (|avfilter.dnn_classify|)
   * - :doc:`/effects_and_filters/video_effects/misc/dnn_detect` |appimage|\ |windows|\ |apple|
     - Misc
     - Apply DNN detect filter to the input. (|avfilter.dnn_detect|)
   * - :doc:`/effects_and_filters/video_effects/misc/blurdetect` |appimage|\ |windows|\ |apple|
     - Misc
     - Blurdetect filter. (|avfilter.blurdetect|)
   * - :doc:`/effects_and_filters/video_effects/misc/blockdetect` |appimage|\ |windows|\ |apple|
     - Misc
     - Blockdetect filter. (|avfilter.blockdetect|)
   * - :doc:`/effects_and_filters/video_effects/stylize/aech0r` |appimage|\ |windows|\ |apple|
     - Stylize
     - analog video echo (|frei0r.aech0r|)
   * - :doc:`/effects_and_filters/video_effects/image_adjustment/motion_compensation_deinterlacer` 
     - |linux|
     - Image Adjustment
     - Apply motion-compensation deinterlacing (|avfilter.mcdeint|)
