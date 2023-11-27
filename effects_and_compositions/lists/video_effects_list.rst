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
   :widths: 20 8 20 42

   * - Effect or Filter
     - OS\ [1]_
     - Category
     - Description
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/3_point_balance` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Balances colors along with 3 points (|frei0r.three_point_balance|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/3-level_threshold` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Dynamic 3-level thresholding (|frei0r.threelay0r|)
   * - :doc:`/effects_and_compositions/video_effects/grain_and_noise/3d_fft_denoiser` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Grain and Noise
     - Denoise frames using 3D FFT (frequency domain filtering) (|avfilter.fftdnoiz|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/alpha_gradient` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - Fill the alpha channel with the specified gradient (|frei0r.alphagrad|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/alpha_operations` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - Display and manipulation of the alpha channel (|frei0r.alpha0ps|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/alpha_shapes` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - Draws simple shapes into the alpha channel (|frei0r.alphaspot|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/alpha_shapes_mask` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - This filter takes a snapshot of the frame before it draws simple shapes into the alpha channel. Use it together with the mask_apply effect, that uses a transition to composite the current frame's image over the snapshot. The typical use case is to add effects in the following sequence: this effect, zero or more effects, mask_apply. (|mask_start|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/alpha_strobing` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - Strobes the alpha channel to 0. Many other filters overwrite the alpha channel, in that case this needs to be last (|strobe|)
   * - :doc:`/effects_and_compositions/video_effects/misc/alphaextract` 
     - |appimage|\ |windows|\ |apple|
     - Misc
     - Extract an alpha channel as a grayscale image component. (|avfilter.alphaextract|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/applylut` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Apply a Look Up Table (LUT) to the video. A LUT is an easy way to correct the color of a video. Supported formats: 3dl (AfterEffects), .cube (Iridas), .dat (DaVinci), .m3d (Pandora) (|avfilter.lut3d|)
   * - :doc:`/effects_and_compositions/video_effects/on_master/audio_level_visualization_filter` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - On Master
     - An audio visualization filter that draws an audio level meter on the image. (|audiolevelgraph|)
   * - :doc:`/effects_and_compositions/video_effects/on_master/audio_spectrum_filter` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - On Master
     - An audio visualization filter that draws an audio spectrum on the image (|audiospectrum|)
   * - :doc:`/effects_and_compositions/video_effects/on_master/audio_wave` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - On Master
     - Display the audio waveform instead of the video (|audiowave|)
   * - :doc:`/effects_and_compositions/video_effects/on_master/audio_waveform_filter` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - On Master
     - An audio visualization filter that draws an audio waveform on the image. (|audiowaveform|)
   * - :doc:`/effects_and_compositions/video_effects/blur_and_sharpen/average_blur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Apply average blur filter (|avfilter.avgblur|)
   * - :doc:`/effects_and_compositions/video_effects/misc/backgroundkey` 
     - |appimage|\ |windows|\ |apple|
     - Misc
     - Turns a static background into transparency. (|avfilter.backgroundkey|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/bezier_curves` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image Correction
     - Color curves adjustment (|frei0r.curves|)
   * - :doc:`/effects_and_compositions/video_effects/blur_and_sharpen/bilateral` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Apply Bilateral filter (|avfilter.bilateral|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/binarize` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Make monochrome clip (|threshold|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/binarize_dynamically` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Dynamic thresholding (|frei0r.twolay0r|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/bluescreen0r` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - Color to alpha (blit SRCALPHA) (|frei0r.bluescreen0r|)
   * - :doc:`/effects_and_compositions/video_effects/deprecated/blur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Blur using 2D IIR filters (exponential, lowpass, gaussian) (|frei0r.IIRblur|)
   * - :doc:`/effects_and_compositions/video_effects/deprecated/box_blur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Box blur (separate horizontal and vertical blur) (|boxblur|)
   * - :doc:`/effects_and_compositions/video_effects/blur_and_sharpen/boxblur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Box blur (separate horizontal and vertical blur) (|box_blur|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/brightness` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjusts the brightness of a source image (|frei0r.brightness|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/brightness_keyframable` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Change the image |brightness| with keyframes (|brightness|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/bw0r` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Turns image Black/White (|frei0r.bw0r|)
   * - :doc:`/effects_and_compositions/video_effects/generate/cairogradient` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Draws a gradient on top of image. Filter is given gradient start and end points, colors and opacities. (|frei0r.cairogradient|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/cartoon` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Cartoonify video, do a form of edge detect (|frei0r.cartoon|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/channel_extractors` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Extracts Blue from Image (|frei0r.B|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/channel_extractors` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Extracts Green from Image (|frei0r.G|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/channel_extractors` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Extracts Red from Image (|frei0r.R|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/charcoal` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Charcoal drawing effect (|charcoal|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/chroma_hold` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Removes all color information for all colors except for a certain one (|avfilter.chromahold|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/chroma_keep` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Make image greyscale except for chosen color (|chroma_hold|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/chroma_key_advanced` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - Chroma Key with more advanced options (e.g. different color models). Use if basic chroma key is not working effectively. (|frei0r.select0r|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/chroma_key` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - Make Selected Color transparent (|chroma|)
   * - :doc:`/effects_and_compositions/video_effects/grain_and_noise/chroma_noise_reduction` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Grain and Noise
     - Reduce chrominance noise (|avfilter.chromanr|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/chroma_shift` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Shift chroma pixels horizontally and/or vertically (|avfilter.chromashift|)
   * - :doc:`/effects_and_compositions/video_effects/utility/ciescope` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - Video CIE scope (|avfilter.ciescope|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/CMYK_adjust` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Apply CMYK correction to specific color ranges (|avfilter.selectivecolor|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/color_balance` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Modify intensity of primary colors (red, green and blue) of input frames (|avfilter.colorbalance|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/color_channel_mixer` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Modifies a color channel by adding the values associated to the other channels of the same pixels (|avfilter.colorchannelmixer|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/color_contrast` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjust color contrast between RGB components. (|avfilter.colorcontrast|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/color_correct` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjust color white balance selectively for blacks and whites.This filter operates in YUV colorspace. (|avfilter.colorcorrect|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/color_distance` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Calculates the distance between the selected color and the current pixel and uses that value as a new pixel value (|frei0r.colordistance|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/color_effect` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Applies a pre-made color effect to image (|frei0r.colortap|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/color_hold` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Remove all color information all RGB colors except for certain one (|avfilter.colorhold|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/color_levels` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjust video input frames using levels (|avfilter.colorlevels|)
   * - :doc:`/effects_and_compositions/video_effects/image_adjustment/color_matrix` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Convert color matrix (|avfilter.colormatrix|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/color_overlay` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Overlay a solid color on the video stream (|avfilter.colorize|)
   * - :doc:`/effects_and_compositions/video_effects/image_adjustment/color_space` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Convert colorspace, transfer characteristics or color primaries. Input video needs to have an even size. (|avfilter.colorspace|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/color_temperature` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjust color temperature of video (|avfilter.colortemperature|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/colorize` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Colorizes image to selected hue, saturation and lightness (|frei0r.colorize|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/contrast` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjusts the contrast of a source image (|frei0r.contrast0r|)
   * - :doc:`/effects_and_compositions/video_effects/blur_and_sharpen/contrast_adaptive_sharpen` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Apply Contrast Adaptive Sharpen filter to video stream. (|avfilter.cas|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/corners` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Four corners geometry engine (|frei0r.c0rners|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/crop_padding` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - This filter crops the image to a rounded rectangle or circle by padding it with a color (|qtcrop|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/crop_scale_tilt` 
     - |linux|\ |appimage|\ |windows|
     - Transform, Distort and Perspective
     - Scales, Tilts and Crops an Image (|frei0r.scale0tilt|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/curves` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Color curves adjustment (|frei0r.curves|)
   * - :doc:`/effects_and_compositions/video_effects/on_master/dance` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - On Master
     - An audio visualization filter that moves the image around proportional to the magnitude of the audio spectrum (|dance|)
   * - :doc:`/effects_and_compositions/video_effects/utility/datascope` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - Video data analysis (|avfilter.datascope|)
   * - :doc:`/effects_and_compositions/video_effects/blur_and_sharpen/dblur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Apply Directional Blur filter. (|avfilter.dblur|)
   * - dct_denoiser
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Denoise frames using 2D DCT frequency domain filtering (|avfilter.dctdnoiz|)
   * - :doc:`/effects_and_compositions/video_effects/image_adjustment/deband` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Remove banding artifacts from input video. It works by replacing banded pixels with an average value of referenced pixels (|avfilter.deband|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/defish` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Non rectilinear lens mappings (|frei0r.defish0r|)
   * - delogo
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Perform an RGB[A] difference operation between the pixel sources (|frei0r.difference|)
   * - :doc:`/effects_and_compositions/video_effects/grain_and_noise/denoiser` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Grain and Noise
     - High Quality 3d denoiser (|frei0r.hqdn3d|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/despill` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - Remove unwanted contamination of foreground colors, caused by reflected color of greenscreen or bluescreen (|avfilter.despill|)
   * - :doc:`/effects_and_compositions/video_effects/image_adjustment/dilation` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Apply dilation effect (|avfilter.dilation|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/distort` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Plasma (|frei0r.distort0r|)
   * - :doc:`/effects_and_compositions/video_effects/deprecated/dither` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Dithers the image and reduces the number of available colors (|frei0r.dither|)
   * - :doc:`/effects_and_compositions/video_effects/generate/drawbox` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Draw a colored box on the input video (|avfilter.drawbox|)
   * - :doc:`/effects_and_compositions/video_effects/generate/drawgrid` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Draw a colored grid on the input video (|avfilter.drawgrid|)
   * - :doc:`/effects_and_compositions/video_effects/grain_and_noise/dust` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Grain and Noise
     - Add |dust| and specks to the video, as in old movies (|dust|)
   * - :doc:`/effects_and_compositions/video_effects/generate/dynamic_text` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Overlay text with keywords replaced (|dynamictext|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/edge_crop` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Trim the edges of a clip (|crop|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/edge_detection` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Detect and draw edges. The filter uses the Canny Edge Detection algorithm (|avfilter.edgedetect|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/edge_glow` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Edge glow filter (|frei0r.edgeglow|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/elastic_scale_filter` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - This is a frei0r filter which allows to scale video footage non-linearly (|frei0r.elastic_scale|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/elbg_posterizer` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Apply posterize effect, using the ELBG algorithm (|avfilter.elbg|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/emboss` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Creates embossed relief image of source image (|frei0r.emboss|)
   * - :doc:`/effects_and_compositions/video_effects/image_adjustment/epx_scaler` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Scale the input using EPX algorithm. (|avfilter.epx|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/equaliz0r` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Equalizes the intensity historgrams (|frei0r.equaliz0r|)
   * - :doc:`/effects_and_compositions/video_effects/image_adjustment/erosion` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Apply erosion effect (|avfilter.erosion|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/exposure` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjust exposure of the video stream (|avfilter.exposure|)
   * - :doc:`/effects_and_compositions/video_effects/motion/fade_in` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Motion
     - Fade video from black (|brightness|)
   * - :doc:`/effects_and_compositions/video_effects/motion/fade_out` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Motion
     - Fade video to black (|brightness|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/fft-based_fir` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Apply arbitrary expressions to samples in frequency domain (|avfilter.fftfilt|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/fill_borders` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Fill borders of the input video, without changing video stream dimensions. Sometimes video can have garbage at the four edges and you may not want to crop video input to keep size multiple of some number (|avfilter.fillborders|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/flip_horizontally` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Horizontally flip the input video (|avfilter.hflip|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/flip_vertically` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Vertically flip the input video (|avfilter.vflip|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/flippo` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Flipping X and Y axis (|frei0r.flippo|)
   * - :doc:`/effects_and_compositions/video_effects/motion/freeze` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Motion
     - Freeze video on a chosen frame (|freeze|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/gamma` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjusts the gamma value of a source image (|frei0r.gamma|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/gamma_keyframe` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Change |gamma| color value (|gamma|)
   * - :doc:`/effects_and_compositions/video_effects/blur_and_sharpen/gaussian_blur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Apply Gaussian Blur filter (|avfilter.gblur|)
   * - :doc:`/effects_and_compositions/video_effects/motion/glitch0r` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Motion
     - Adds glitches and block shifting (|frei0r.glitch0r|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/glow` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Creates a Glamorous Glow (|frei0r.glow|)
   * - :doc:`/effects_and_compositions/video_effects/misc/gps_graphic` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Misc
     - Overlay GPS-related graphics onto the video (|gpsgraphic|)
   * - :doc:`/effects_and_compositions/video_effects/generate/gps_text` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Overlay GPS-related text onto the video. (|gpstext|)
   * - :doc:`/effects_and_compositions/video_effects/grain_and_noise/gradfun` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Grain and Noise
     - Debands video quickly using gradients (|avfilter.gradfun|)
   * - :doc:`/effects_and_compositions/video_effects/deprecated/grain` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Grain over the image (|grain|)
   * - :doc:`/effects_and_compositions/video_effects/misc/grayworld` 
     - |appimage|\ |windows|\ |apple|
     - Misc
     - Adjust white balance using LAB gray world algorithm (|avfilter.grayworld|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/greyscale` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Discard color information (|greyscale|)
   * - :doc:`/effects_and_compositions/video_effects/utility/histogram` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - Compute and draw a color distribution histogram for the input video (|avfilter.histogram|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/histogram_equalizer` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - This filter applies a global color histogram equalization on a per-frame basis (|avfilter.histeq|)
   * - :doc:`/effects_and_compositions/video_effects/image_adjustment/hqx_interpolator` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Scale the input by 2, 3 or 4 using the hq*x magnification algorithm (|avfilter.hqx|)
   * - :doc:`/effects_and_compositions/video_effects/misc/hsvkey` 
     - |appimage|\ |windows|\ |apple|
     - Misc
     - Turns a certain HSV range into transparency. Operates on YUV colors. (|avfilter.hsvkey|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/hue_shift` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Shifts the hue of a source image (|frei0r.hueshift0r|)
   * - :doc:`/effects_and_compositions/video_effects/misc/huesaturation` 
     - |appimage|\ |windows|\ |apple|
     - Misc
     - Apply hue-saturation-intensity adjustments. (|avfilter.huesaturation|)
   * - :doc:`/effects_and_compositions/video_effects/misc/hsvhold` 
     - |appimage|\ |windows|\ |apple|
     - Misc
     - Turns a certain HSV range into gray. (|avfilter.hsvhold|)
   * - :doc:`/effects_and_compositions/video_effects/image_adjustment/interlace_field_order` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Transform the field order of the input video (|avfilter.fieldorder|)
   * - :doc:`/effects_and_compositions/video_effects/image_adjustment/interleave_deinterleave` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Deinterleave or interleave fields (|avfilter.il|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/invert` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Invert colors (|invert|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/invert` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Inverts all colors of a source image (|frei0r.invert0r|)
   * - :doc:`/effects_and_compositions/video_effects/deprecated/k-means_clustering` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Clusters of a source image by color and spatial distance (|frei0r.cluster|)
   * - :doc:`/effects_and_compositions/video_effects/image_adjustment/kernel_deinterlacer` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Deinterlace input video by applying Donald Graft’s adaptive kernel deinterlacing. Works on interlaced parts of a video to produce progressive frames (|avfilter.kerndeint|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/key_spill_mop_up` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - Reduces the visibility of key color spill in chroma keying (|frei0r.keyspillm0pup|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/kirsch` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Apply kirsch operator (|avfilter.kirsch|)
   * - Legacy ffmpeg deinterlacer **deprecated**
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Misc
     - Deinterlace interlaced video. (|avdeinterlace|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/lens_correction` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Allow compensation of lens distortion (|frei0r.lenscorrection|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/lens_correction_keyframe` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Correct radial lens distortion (|avfilter.lenscorrection|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/letterb0xed` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Adds black borders at the top and bottom for cinema look (|frei0r.letterb0xed|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/levels` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjust levels (|frei0r.levels|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/lift_gamma_gain` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - A simple lift/gamma/gain effect, used for color grading. (|lift_gamma_gain|)
   * - :doc:`/effects_and_compositions/video_effects/on_master/light_show` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - On Master
     - An audio visualization filter that colors the image proportional to the magnitude of the audio spectrum (|lightshow|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/limiter` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Limits the pixel components values to the specified range [min,max] (|avfilter.limiter|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/lumakey` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - This filter modifies image’s alpha channel as a function of its luma value. This is used together with a compositor to combine two images so that bright or dark areas of source image are overwritten on top of the destination image (|lumakey|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/lumaliftgammagain` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Filter can be used to apply lift gain and gamma corrections to luma values of an image (|lumaliftgammagain|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/luminance` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Creates a luminance map of the image (|frei0r.luminance|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/mask_apply` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - Apply the previous effects in the zone defined by a Mask Start effect. (|mask_apply|)
   * - :doc:`/effects_and_compositions/video_effects/grain_and_noise/median` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Grain and Noise
     - Pick median pixel from certain rectangle defined by radius. (|avfilter.median|)
   * - :doc:`/effects_and_compositions/video_effects/deprecated/medians` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Implements several median-type filters (|frei0r.medians|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/mirror` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Flip your image in any direction (|mirror|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/monochrome` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Convert video to gray using custom color filter (|avfilter.monochrome|)
   * - :doc:`/effects_and_compositions/video_effects/image_adjustment/motion_compensation_deinterlacer` 
     - |linux|
     - Image Adjustment
     - Apply motion-compensation deinterlacing (|avfilter.mcdeint|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/motion_tracker` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - Select a zone to follow its movements (|opencv.tracker|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/ndvi_filter` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - This filter creates a false image from a visible + infrared source (|frei0r.ndvi|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/negate` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Negate (invert) the input video or its alpha channel. (|avfilter.negate|)
   * - :doc:`/effects_and_compositions/video_effects/motion/nervous` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Motion
     - Flushes frames in time in a nervous way (|frei0r.nervous|)
   * - :doc:`/effects_and_compositions/video_effects/utility/nikon_d90_stairstepping_fix` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - Removes stairstepping artifacts from Nikon D90’s 720p videos. Sharp lines in videos from the Nikon D90 show steps each 8th or 9th line, assumedly due to poor downsampling. These can be smoothed out with this filter if they become too annoying (|frei0r.d90stairsteppingfix|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/normaliz0r` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Normalize (aka histogram stretch, contrast stretch) (|frei0r.normaliz0r|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/normalize_rgb_video` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Normalize RGB video (aka histogram stretching, contrast stretching). See: https://en.wikipedia.org/wiki/Normalization_(image_processing) (|avfilter.normalize|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/nosync0r` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Broken TV (|frei0r.nosync0r|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/obscure` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - Hide a region of the clip (|obscure|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/oldfilm` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Moves the Picture up and down and random brightness change (|oldfilm|)
   * - :doc:`/effects_and_compositions/video_effects/utility/oscilloscope` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - 2D Video Oscilloscope (|avfilter.oscilloscope|)
   * - :doc:`/effects_and_compositions/video_effects/utility/oscilloscope_advanced` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - 2D video oscilloscope (|frei0r.pr0file|)
   * - :doc:`/effects_and_compositions/video_effects/image_adjustment/phase` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Delay interlaced video by one field time so that the field order changes (|avfilter.phase|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/photosensitivity` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Filter out photosensitive epilepsy seizure-inducing flashes (|avfilter.photosensitivity|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/pillar_echo` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Create an echo effect (blur) outside of an area of interest (|pillar_echo|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/pixelize` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Pixelize input image (|frei0r.pixeliz0r|)
   * - :doc:`/effects_and_compositions/video_effects/misc/pixs0r` 
     - |appimage|\ |windows|\ |apple|
     - Misc
     - Glitch image shifting rows to and fro (|frei0r.pixs0r|)
   * - :doc:`/effects_and_compositions/video_effects/blur_and_sharpen/planes_blur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Set an expression for the box radius in pixels used for blurring the corresponding input plane. (|avfilter.boxblur|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/position_and_zoom` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Adjust size and position of clip (|affine|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/posterize` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Posterizes image by reducing the number of colors used in image (|frei0r.posterize|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/premultiply` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - Multiply (or divide) each color component by the pixel's alpha value (|frei0r.premultiply|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/prewitt` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Apply prewitt operator to input video stream (|avfilter.prewitt|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/primaries` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Reduce image to primary colors (|frei0r.primaries|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/rectangular_alpha_mask` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - Creates a square alpha-channel mask (|frei0r.mask0mate|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/rgb_adjustment` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Simple color adjustment (|frei0r.coloradj_RGB|)
   * - :doc:`/effects_and_compositions/video_effects/deprecated/rgbnoise` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Adds RGB noise to image (|frei0r.rgbnoise|)
   * - :doc:`/effects_and_compositions/video_effects/utility/rgb_parade` 
     - |linux|\ |appimage|\ |windows|
     - Utility
     - 
   * - :doc:`/effects_and_compositions/video_effects/stylize/rgba_shift` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Shift R/G/B/A pixels horizontally and/or vertically (|avfilter.rgbashift|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/rgbsplit0r` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - RGB splitter and shifting (|frei0r.rgbsplit0r|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/roberts` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Apply roberts cross operator to input video stream (|avfilter.roberts|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/rotate_keyframable` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Rotate clip in any 3 directions (|affine|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/rotate_and_shear` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Rotate clip in any 3 directions (|affine|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/rotoscoping` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - Keyframable vector based |rotoscoping| (|rotoscoping|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/rotoscoping_mask` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - This filter makes a snapshot of the frame before a keyframable vector based rotoscoping is applied. Use it together with the mask_apply effect, that uses a transition to composite the current frame's image over the snapshot. The typical use case is to add effects in the following sequence: this effect, zero or more effects, mask_apply. (|mask_start|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/saturation` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjusts the saturation of a source image (|frei0r.saturat0r|)
   * - :doc:`/effects_and_compositions/video_effects/generate/scanline0r` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Interlaced black lines (|frei0r.scanline0r|)
   * - :doc:`/effects_and_compositions/video_effects/misc/scharr` 
     - |appimage|\ |windows|\ |apple|
     - Misc
     - Apply scharr operator. (|avfilter.scharr|)
   * - :doc:`/effects_and_compositions/video_effects/grain_and_noise/scratchlines` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Grain and Noise
     - Scratch|lines| over the picture (|lines|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/scroll` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Pick median pixel from certain rectangle defined by radius. (|avfilter.scroll|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/secondary_color_selection_mask` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - This filter takes a snapshot of the frame before a keyframable Chroma Key selection with more advanced options (e.g. different color models) is applied. Use it together with the mask_apply effect, that uses a transition to composite the current frame's image over the snapshot. The typical use case is to add effects in the following sequence: this effect, zero or more effects, mask_apply. (|mask_start|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/sepia` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Turn clip colors to |sepia| (|sepia|)
   * - :doc:`/effects_and_compositions/video_effects/image_adjustment/set_range` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Force color range for the output video frame (|avfilter.setrange|)
   * - :doc:`/effects_and_compositions/video_effects/blur_and_sharpen/shape_adaptive_blur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Shape Adaptive Blur (|avfilter.sab|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/shape_alpha` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - Create an alpha channel (transparency) based on another resource (|shape|)
   * - :doc:`/effects_and_compositions/video_effects/blur_and_sharpen/sharp_unsharp` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Sharpen or Blur your video (|avfilter.unsharp|)
   * - :doc:`/effects_and_compositions/video_effects/deprecated/sharpen` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Unsharp masking (port from Mplayer) (|frei0r.sharpness|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/shear` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Shear transform the input image (|avfilter.shear|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/sigmoidal_transfer` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Desaturates image and creates a particular look that could be called Stamp, Newspaper, or Photocopy (|frei0r.sigmoidaltransfer|)
   * - :doc:`/effects_and_compositions/video_effects/blur_and_sharpen/smartblur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Blur the input video without impacting the outlines (|avfilter.smartblur|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/sobel` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Sobel filter (|frei0r.sobel|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/sobel_planes` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Apply sobel operators to input video stream (|avfilter.sobel|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/soft_glow` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Does softglow effect on highlights (|frei0r.softglow|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/sat` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Changes Slope, Offset, and Power of the color components, and the overall Saturation, according to the ASC CDL (Color Decision List) (|frei0r.sopsat|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/spillsuppress` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - Remove green or blue spill light from subjects shot in front of green or blue screen (|frei0r.spillsupress|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/spot_remover` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - Replace an area with interpolated pixels. The new pixel values are interpolated from the nearest pixel. (|spot_remover|)
   * - :doc:`/effects_and_compositions/video_effects/blur_and_sharpen/square_blur` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Blur and Sharpen
     - Square Blur (|frei0r.squareblur|)
   * - :doc:`/effects_and_compositions/video_effects/vr360_and_3d/stereoscopic_3d` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - VR360 and 3D
     - Convert between different stereoscopic image formats (|avfilter.stereo3d|)
   * - :doc:`/effects_and_compositions/video_effects/image_adjustment/super2xsai` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Scale the input by 2x using the Super2xSaI pixel art algorithm (|avfilter.super2xsai|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/swapuv` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Swap U and V components (|avfilter.swapuv|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/technicolor` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Oversaturate the color in video, like in old Technicolor movies (|tcolor|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/threshold` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stylize
     - Thresholds a source image (|frei0r.threshold0r|)
   * - :doc:`/effects_and_compositions/video_effects/utility/timeout_indicator` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - Timeout indicators e.g. for slides (|frei0r.timeout|)
   * - :doc:`/effects_and_compositions/video_effects/generate/timer` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Overlay a |timer| onto the video (|timer|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/tint` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Maps source image luminance between two colors specified (|frei0r.tint0r|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/transform` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Position, Scale and opacity, (|qtblend|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/transparency` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - Tunes the alpha channel (|frei0r.transparency|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/transpose` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Transpose rows with columns in the input video and optionally flip it (|avfilter.transpose|)
   * - :doc:`/effects_and_compositions/video_effects/utility/vectorscope` 
     - |linux|\ |appimage|\ |windows|
     - Utility
     - Display a vectorscope of the video data (|frei0r.vectorscope|)
   * - :doc:`/effects_and_compositions/video_effects/utility/vectorscope_advanced` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - Display 2 color component values in the two dimensional graph (which is called a vectorscope) (|avfilter.vectorscope|)
   * - :doc:`/effects_and_compositions/video_effects/motion/vertigo` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Motion
     - Alpha blending with zoomed and rotated images (|frei0r.vertigo|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/vibrance` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Boost or alter saturation.  (|avfilter.vibrance|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/video_equalizer` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjust Brightness, contrast, gamma, saturation (|avfilter.eq|)
   * - :doc:`/effects_and_compositions/video_effects/generate/video_grid` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Create a video grid (|frei0r.cairoimagegrid|)
   * - :doc:`/effects_and_compositions/video_effects/utility/video_values` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - Measure video values (|frei0r.pr0be|)
   * - :doc:`/effects_and_compositions/video_effects/utility/video_waveform_monitor` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Utility
     - The waveform monitor plots color component intensity. By default luminance only. Each column of the waveform corresponds to a column of pixels in the source video.  (|avfilter.waveform|)
   * - :doc:`/effects_and_compositions/video_effects/grain_and_noise/video_noise_generator` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Grain and Noise
     - Add noise on video input frame (|avfilter.noise|)
   * - :doc:`/effects_and_compositions/video_effects/generate/vignette` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Natural Lens vignetting effect (|frei0r.vignette|)
   * - :doc:`/effects_and_compositions/video_effects/generate/vignette_effect` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Generate
     - Adjustable Vignette (|vignette|)
   * - :doc:`/effects_and_compositions/video_effects/vr360_and_3d/vr360_equi2stereo` 
     - |appimage|
     - VR360 and 3D
     - converts an equirectangular frame (panoramic) to a rectilinear frame (what you’re used to seeing). Can be used to preview what will be shown in a 360 video viewer. Delayed frame blitting mapping on a time bitmap (|frei0r.bigsh0t_eq_to_rect|)
   * - :doc:`/effects_and_compositions/video_effects/vr360_and_3d/vr360_equi_mask` 
     - |appimage|
     - VR360 and 3D
     - Adds a black matte to the frame. Use this if you filmed using a 360 camera but only want to use part of the 360 image - for example if you and the film crew occupy the 90 degrees behind the camera (|frei0r.bigsh0t_eq_mask|)
   * - :doc:`/effects_and_compositions/video_effects/vr360_and_3d/vr360_equi2rect` 
     - |appimage|
     - VR360 and 3D
     - converts an equirectangular frame (panoramic) to a rectilinear frame (what you’re used to seeing). Can be used to preview what will be shown in a 360 video viewer. Delayed frame blitting mapping on a time bitmap (|frei0r.bigsh0t_eq_to_rect|)
   * - :doc:`/effects_and_compositions/video_effects/vr360_and_3d/vr360_rect2equi` 
     - |appimage|
     - VR360 and 3D
     - Converts a rectilinear (a normal-looking) image to an equirectangular image. Use this together with transform 360 to place “normal” footage in a 360 movie (|frei0r.bigsh0t_rect_to_eq|)
   * - :doc:`/effects_and_compositions/video_effects/vr360_and_3d/vr360_stabilize` 
     - |appimage|
     - VR360 and 3D
     - Stabilizes 360 footage. The plugin works in two phases - analysis and stabilization. When analyzing footage, it detects frame-to-frame rotation, and when stabilizing it tries to correct high-frequency motion (shake) (|frei0r.bighsh0t_stabilize_360|)
   * - :doc:`/effects_and_compositions/video_effects/vr360_and_3d/vr360_transform` 
     - |appimage|
     - VR360 and 3D
     - Rotates a panoramic image (|frei0r.bigsh0t_transform_360|)
   * - :doc:`/effects_and_compositions/video_effects/deprecated/wave` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Makes waves on your clip with keyframes (|wave|)
   * - wavelet_denoiser
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Deprecated
     - Wavelet based Denoiser (|avfilter.vaguedenoiser|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/white_balance` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Adjust the white balance / color temperature (|frei0r.balanc0r|)
   * - :doc:`/effects_and_compositions/video_effects/color_image_correction/white_balance_lms` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Color and Image correction
     - Do simple color correction, in a physically meaningful way (|frei0r.colgate|)
   * - :doc:`/effects_and_compositions/video_effects/image_adjustment/xbr_interpolator` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Image Adjustment
     - Apply the xBR high-quality magnification filter which is designed for pixel art. It follows a set of edge-detection rules, see this |xbr_tutorial| (|avfilter.xbr|)
   * - :doc:`/effects_and_compositions/video_effects/misc/xine_deinterlacer` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Misc
     - Deinterlace interlaced video. (|deinterlace|)
   * - :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/zoom_pan` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Transform, Distort and Perspective
     - Apply Zoom and Pan effect (|avfilter.zoompan|)

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

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-3-point-color-balance.html?gi-language=c" target="_blank">frei0r.three_point_balance</a>

.. |frei0r.threelay0r| raw:: html

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-threelay0r.html?gi-language=c" target="_blank">frei0r.threelay0r</a>

.. |avfilter.fftdnoiz| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#fftdnoiz" target="_blank">avfilter.fftdnoiz</a>

.. |frei0r.aech0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-aech0r/" target="_blank">frei0r.aech0r</a>

.. |frei0r.alphagrad| raw:: html

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-alphagrad.html?gi-language=c#frei0r-filter-alphagrad" target="_blank">frei0r.alphagrad</a>

.. |frei0r.alpha0ps| raw:: html

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-alpha0ps.html?gi-language=c" target="_blank">frei0r.alpha0ps</a>

.. |frei0r.alphaspot| raw:: html

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-alphaspot.html?gi-language=c" target="_blank">frei0r.alphaspot</a>

.. |frei0r.brightness| raw:: html

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-b.html?gi-language=c" target="_blank">frei0r.brightness</a>

.. |mask_start| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterMask_start/" target="_blank">mask_start</a>

.. |strobe| replace:: strobe

.. |avfilter.alphaextract| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-lut3d/" target="_blank">avfilter.alphaextract</a>

.. |avfilter.lut3d| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAudiolevelgraph/" target="_blank">avfilter.lut3d</a>

.. |audiolevelgraph| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAudiospectrum/" target="_blank">audiolevelgraph</a>

.. |audiospectrum| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAudiowave/" target="_blank">audiospectrum</a>

.. |audiowave| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-avgblur/" target="_blank">audiowave</a>

.. |audiowaveform| replace:: audiowaveform

.. |avfilter.avgblur| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-bilateral/" target="_blank">avfilter.avgblur</a>

.. |avfilter.backgroundkey| replace:: avfilter.backgroundkey

.. |frei0r.curves| raw:: html

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-twolay0r.html?gi-language=c" target="_blank">frei0r.curves</a>

.. |avfilter.bilateral| raw:: html

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-bluescreen0r.html?gi-language=c" target="_blank">avfilter.bilateral</a>

.. |threshold| raw:: html

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-iir-blur.html?gi-language=c" target="_blank">threshold</a>

.. |frei0r.twolay0r| replace:: frei0r.twolay0r

.. |avfilter.blockdetect| replace:: avfilter.blockdetect

.. |frei0r.bluescreen0r| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-brightness/" target="_blank">frei0r.bluescreen0r</a>

.. |frei0r.IIRblur| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-brightness/" target="_blank">frei0r.IIRblur</a>

.. |avfilter.blurdetect| raw:: html

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-bw0r.html?gi-language=c" target="_blank">avfilter.blurdetect</a>

.. |boxblur| raw:: html

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-cairogradient.html?gi-language=c" target="_blank">boxblur</a>

.. |box_blur| raw:: html

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-cartoon.html?gi-language=c" target="_blank">box_blur</a>

.. |frei0r.b| raw:: html

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-b.html?gi-language=c" target="_blank">frei0r.b</a>

.. |frei0r.g| raw:: html

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-g.html?gi-language=c" target="_blank">frei0r.b</a>

.. |frei0r.bw0r| raw:: html

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-r.html?gi-language=c" target="_blank">frei0r.bw0r</a>

.. |frei0r.cairogradient| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterCharcoal/" target="_blank">frei0r.cairogradient</a>

.. |frei0r.cartoon| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#chromahold" target="_blank">frei0r.cartoon</a>

.. |frei0r.B| replace:: frei0r.B

.. |frei0r.G| raw:: html

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-select0r.html?gi-language=c" target="_blank">frei0r.G</a>

.. |frei0r.R| replace:: frei0r.R

.. |charcoal| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#chromanr" target="_blank">charcoal</a>

.. |avfilter.chromahold| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#chromashift" target="_blank">avfilter.chromahold</a>

.. |chroma_hold| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#ciescope" target="_blank">chroma_hold</a>

.. |frei0r.select0r| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#selectivecolor-1" target="_blank">frei0r.select0r</a>

.. |chroma| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#colorbalance" target="_blank">chroma</a>

.. |avfilter.chromanr| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#colorchannelmixer" target="_blank">avfilter.chromanr</a>

.. |avfilter.chromashift| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#colorcontrast" target="_blank">avfilter.chromashift</a>

.. |avfilter.ciescope| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#colorcorrect" target="_blank">avfilter.ciescope</a>

.. |avfilter.selectivecolor| raw:: html

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-color-distance.html?gi-language=c" target="_blank">avfilter.selectivecolor</a>

.. |avfilter.colorbalance| raw:: html

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-colortap.html?gi-language=c" target="_blank">avfilter.colorbalance</a>

.. |avfilter.colorchannelmixer| replace:: avfilter.colorchannelmixer

.. |avfilter.colorcontrast| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#colorlevels" target="_blank">avfilter.colorcontrast</a>

.. |avfilter.colorcorrect| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#colormatrix" target="_blank">avfilter.colorcorrect</a>

.. |frei0r.colordistance| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#colorize" target="_blank">frei0r.colordistance</a>

.. |frei0r.colortap| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#colorspace" target="_blank">frei0r.colortap</a>

.. |avfilter.colorhold| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#colortemperature" target="_blank">avfilter.colorhold</a>

.. |avfilter.colorlevels| replace:: avfilter.colorlevels

.. |avfilter.colormatrix| raw:: html

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-contrast0r.html?gi-language=c" target="_blank">avfilter.colormatrix</a>

.. |avfilter.colorize| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#cas" target="_blank">avfilter.colorize</a>

.. |avfilter.colorspace| raw:: html

   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-c0rners.html?gi-language=c" target="_blank">avfilter.colorspace</a>

.. |avfilter.colortemperature| replace:: avfilter.colortemperature

.. |frei0r.colorize| replace:: frei0r.colorize

.. |frei0r.contrast0r| replace:: frei0r.contrast0r

.. |avfilter.cas| replace:: avfilter.cas

.. |frei0r.c0rners| replace:: frei0r.c0rners

.. |qtcrop| replace:: qtcrop

.. |frei0r.scale0tilt| replace:: frei0r.scale0tilt

.. |dance| replace:: dance

.. |avfilter.datascope| replace:: avfilter.datascope

.. |avfilter.dblur| replace:: avfilter.dblur

.. |avfilter.dctdnoiz| replace:: avfilter.dctdnoiz

.. |avfilter.deband| replace:: avfilter.deband

.. |frei0r.defish0r| replace:: frei0r.defish0r

.. |frei0r.difference| replace:: frei0r.difference

.. |frei0r.hqdn3d| replace:: frei0r.hqdn3d

.. |avfilter.despill| replace:: avfilter.despill

.. |avfilter.dilation| replace:: avfilter.dilation

.. |frei0r.distort0r| replace:: frei0r.distort0r

.. |frei0r.dither| replace:: frei0r.dither

.. |avfilter.dnn_classify| replace:: avfilter.dnn_classify

.. |avfilter.dnn_detect| replace:: avfilter.dnn_detect

.. |avfilter.drawbox| replace:: avfilter.drawbox

.. |avfilter.drawgrid| replace:: avfilter.drawgrid

.. |dust| replace:: dust

.. |dynamictext| replace:: dynamictext

.. |crop| replace:: crop

.. |avfilter.edgedetect| replace:: avfilter.edgedetect

.. |frei0r.edgeglow| replace:: frei0r.edgeglow

.. |frei0r.elastic_scale| replace:: frei0r.elastic_scale

.. |avfilter.elbg| replace:: avfilter.elbg

.. |frei0r.emboss| replace:: frei0r.emboss

.. |avfilter.epx| replace:: avfilter.epx

.. |frei0r.equaliz0r| replace:: frei0r.equaliz0r

.. |avfilter.erosion| replace:: avfilter.erosion

.. |avfilter.exposure| replace:: avfilter.exposure

.. |frei0r.facebl0r| replace:: frei0r.facebl0r

.. |frei0r.facedetect| replace:: frei0r.facedetect

.. |brightness| replace:: brightness

.. |avcolor_space| replace:: avcolor_space

.. |swscale| replace:: swscale

.. |avfilter.fftfilt| replace:: avfilter.fftfilt

.. |avfilter.fillborders| replace:: avfilter.fillborders

.. |avfilter.hflip| replace:: avfilter.hflip

.. |avfilter.vflip| replace:: avfilter.vflip

.. |frei0r.flippo| replace:: frei0r.flippo

.. |freeze| replace:: freeze

.. |frei0r.gamma| replace:: frei0r.gamma

.. |gamma| replace:: gamma

.. |avfilter.gblur| replace:: avfilter.gblur

.. |frei0r.glitch0r| replace:: frei0r.glitch0r

.. |frei0r.glow| replace:: frei0r.glow

.. |gpsgraphic| replace:: gpsgraphic

.. |gpstext| replace:: gpstext

.. |avfilter.gradfun| replace:: avfilter.gradfun

.. |grain| replace:: grain

.. |avfilter.grayworld| replace:: avfilter.grayworld

.. |greyscale| replace:: greyscale

.. |avfilter.histogram| replace:: avfilter.histogram

.. |avfilter.histeq| replace:: avfilter.histeq

.. |avfilter.hqx| replace:: avfilter.hqx

.. |avfilter.hsvkey| replace:: avfilter.hsvkey

.. |frei0r.hueshift0r| replace:: frei0r.hueshift0r

.. |avfilter.huesaturation| replace:: avfilter.huesaturation

.. |avfilter.hsvhold| replace:: avfilter.hsvhold

.. |avfilter.fieldorder| replace:: avfilter.fieldorder

.. |avfilter.il| replace:: avfilter.il

.. |invert| replace:: invert

.. |frei0r.invert0r| replace:: frei0r.invert0r

.. |frei0r.cluster| replace:: frei0r.cluster

.. |avfilter.kerndeint| replace:: avfilter.kerndeint

.. |frei0r.keyspillm0pup| replace:: frei0r.keyspillm0pup

.. |avfilter.kirsch| replace:: avfilter.kirsch

.. |avfilter.latency| replace:: avfilter.latency

.. |avdeinterlace| replace:: avdeinterlace

.. |frei0r.lenscorrection| replace:: frei0r.lenscorrection

.. |avfilter.lenscorrection| replace:: avfilter.lenscorrection

.. |frei0r.letterb0xed| replace:: frei0r.letterb0xed

.. |frei0r.levels| replace:: frei0r.levels

.. |lift_gamma_gain| replace:: lift_gamma_gain

.. |lightshow| replace:: lightshow

.. |avfilter.limiter| replace:: avfilter.limiter

.. |lumakey| replace:: lumakey

.. |lumaliftgammagain| replace:: lumaliftgammagain

.. |frei0r.luminance| replace:: frei0r.luminance

.. |mask_apply| replace:: mask_apply

.. |avfilter.median| replace:: avfilter.median

.. |frei0r.medians| replace:: frei0r.medians

.. |mirror| replace:: mirror

.. |avfilter.monochrome| replace:: avfilter.monochrome

.. |avfilter.mcdeint| replace:: avfilter.mcdeint

.. |opencv.tracker| replace:: opencv.tracker

.. |frei0r.ndvi| replace:: frei0r.ndvi

.. |avfilter.negate| replace:: avfilter.negate

.. |frei0r.nervous| replace:: frei0r.nervous

.. |frei0r.d90stairsteppingfix| replace:: frei0r.d90stairsteppingfix

.. |frei0r.normaliz0r| replace:: frei0r.normaliz0r

.. |avfilter.normalize| replace:: avfilter.normalize

.. |frei0r.nosync0r| replace:: frei0r.nosync0r

.. |obscure| replace:: obscure

.. |oldfilm| replace:: oldfilm

.. |avfilter.oscilloscope| replace:: avfilter.oscilloscope

.. |frei0r.pr0file| replace:: frei0r.pr0file

.. |avfilter.phase| replace:: avfilter.phase

.. |avfilter.photosensitivity| replace:: avfilter.photosensitivity

.. |pillar_echo| replace:: pillar_echo

.. |frei0r.pixeliz0r| replace:: frei0r.pixeliz0r

.. |avfilter.pixelize| replace:: avfilter.pixelize

.. |frei0r.pixs0r| replace:: frei0r.pixs0r

.. |avfilter.boxblur| replace:: avfilter.boxblur

.. |affine| replace:: affine

.. |frei0r.posterize| replace:: frei0r.posterize

.. |frei0r.premultiply| replace:: frei0r.premultiply

.. |avfilter.prewitt| replace:: avfilter.prewitt

.. |frei0r.primaries| replace:: frei0r.primaries

.. |frei0r.mask0mate| replace:: frei0r.mask0mate

.. |rescale| replace:: rescale

.. |frei0r.coloradj_RGB| replace:: frei0r.coloradj_RGB

.. |frei0r.rgbnoise| replace:: frei0r.rgbnoise

.. |avfilter.rgbashift| replace:: avfilter.rgbashift

.. |frei0r.rgbsplit0r| replace:: frei0r.rgbsplit0r

.. |avfilter.roberts| replace:: avfilter.roberts

.. |rotoscoping| replace:: rotoscoping

.. |frei0r.saturat0r| replace:: frei0r.saturat0r

.. |frei0r.scanline0r| replace:: frei0r.scanline0r

.. |avfilter.scdet| replace:: avfilter.scdet

.. |avfilter.scharr| replace:: avfilter.scharr

.. |lines| replace:: lines

.. |avfilter.scroll| replace:: avfilter.scroll

.. |sepia| replace:: sepia

.. |avfilter.setrange| replace:: avfilter.setrange

.. |avfilter.sab| replace:: avfilter.sab

.. |shape| replace:: shape

.. |avfilter.unsharp| replace:: avfilter.unsharp

.. |frei0r.sharpness| replace:: frei0r.sharpness

.. |avfilter.shear| replace:: avfilter.shear

.. |frei0r.sigmoidaltransfer| replace:: frei0r.sigmoidaltransfer

.. |avfilter.siti| replace:: avfilter.siti

.. |avfilter.smartblur| replace:: avfilter.smartblur

.. |frei0r.sobel| replace:: frei0r.sobel

.. |avfilter.sobel| replace:: avfilter.sobel

.. |frei0r.softglow| replace:: frei0r.softglow

.. |frei0r.sopsat| replace:: frei0r.sopsat

.. |frei0r.spillsupress| replace:: frei0r.spillsupress

.. |spot_remover| replace:: spot_remover

.. |frei0r.squareblur| replace:: frei0r.squareblur

.. |avfilter.stereo3d| replace:: avfilter.stereo3d

.. |avfilter.super2xsai| replace:: avfilter.super2xsai

.. |avfilter.swapuv| replace:: avfilter.swapuv

.. |tcolor| replace:: tcolor

.. |frei0r.threshold0r| replace:: frei0r.threshold0r

.. |frei0r.timeout| replace:: frei0r.timeout

.. |timer| replace:: timer

.. |frei0r.tint0r| replace:: frei0r.tint0r

.. |avfilter.tonemap_vaapi| replace:: avfilter.tonemap_vaapi

.. |qtblend| replace:: qtblend

.. |frei0r.transparency| replace:: frei0r.transparency

.. |avfilter.transpose| replace:: avfilter.transpose

.. |typewriter| replace:: typewriter

.. |frei0r.vectorscope| replace:: frei0r.vectorscope

.. |avfilter.vectorscope| replace:: avfilter.vectorscope

.. |frei0r.vertigo| replace:: frei0r.vertigo

.. |avfilter.vibrance| replace:: avfilter.vibrance

.. |avfilter.eq| replace:: avfilter.eq

.. |frei0r.cairoimagegrid| replace:: frei0r.cairoimagegrid

.. |frei0r.pr0be| replace:: frei0r.pr0be

.. |avfilter.waveform| replace:: avfilter.waveform

.. |avfilter.noise| replace:: avfilter.noise

.. |frei0r.vignette| replace:: frei0r.vignette

.. |vignette| replace:: vignette

.. |avfilter.vpp_qsv| replace:: avfilter.vpp_qsv

.. |frei0r.bigsh0t_eq_to_rect| replace:: frei0r.bigsh0t_eq_to_rect

.. |frei0r.bigsh0t_eq_mask| replace:: frei0r.bigsh0t_eq_mask

.. |freior.bigsh0t_hemi_to_eq| replace:: freior.bigsh0t_hemi_to_eq

.. |frei0r.bigsh0t_rect_to_eq| replace:: frei0r.bigsh0t_rect_to_eq

.. |frei0r.bighsh0t_stabilize_360| replace:: frei0r.bighsh0t_stabilize_360

.. |frei0r.bigsh0t_transform_360| replace:: frei0r.bigsh0t_transform_360

.. |wave| replace:: wave

.. |avfilter.vaguedenoiser| replace:: avfilter.vaguedenoiser

.. |frei0r.balanc0r| replace:: frei0r.balanc0r

.. |frei0r.colgate| replace:: frei0r.colgate

.. |avfilter.xbr| replace:: avfilter.xbr

.. |deinterlace| replace:: deinterlace

.. |avfilter.zoompan| replace:: avfilter.zoompan


----

.. [1] |linux|: available in installed version; |appimage|: available in the appimage; |windows|: available in Windows; |apple|: available on MacOS (Intel only)


.. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   To be done
   ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Video
   ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   * - :doc:`/effects_and_compositions/video_effects/misc/scdet` |linux|\ |appimage|\ |windows|\ |apple|
     - Misc
     - Detect video scene change (|avfilter.scdet|)
   * - :doc:`/effects_and_compositions/video_effects/misc/siti` |appimage|\ |windows|\ |apple|
     - Misc
     - Calculate spatial information (SI) and temporal information (TI). (|avfilter.siti|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/typewriter`|windows|\ |apple|
     - Stylize
     - Typewriter effect v0.3.3 To be applied on title clips only. (|typewriter|)
   * - :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/shape_alpha_mask` |linux|\ |appimage|\ |windows|\ |apple|
     - Alpha, Mask and Keying
     - This filter makes a snapshot of the frame before an alpha channel (transparency) is created based on another resource. Use it together with the mask_apply effect, that uses a transition to composite the current frame's image over the snapshot. The typical use case is to add effects in the following sequence: this effect, zero or more effects, mask_apply. (|mask_start|)
   * - :doc:`/effects_and_compositions/video_effects/image_adjustment/rescale` |appimage|
     - Image Adjustment
     - Scale the producer video frames size to match the consumer. This filter is designed for use as a normaliser for the loader producer (|rescale|)
   * - :doc:`/effects_and_compositions/video_effects/misc/pixelize` |appimage|\ |windows|\ |apple|
     - Misc
     - Pixelize video. (|avfilter.pixelize|)
   * - :doc:`/effects_and_compositions/video_effects/misc/latency` |appimage|\ |windows|\ |apple|
     - Misc
     - Report video filtering latency. (|avfilter.latency|)
   * - :doc:`/effects_and_compositions/video_effects/misc/face_blur` |appimage|\ |windows|\ |apple|
     - Misc
     - Automatically detect and blur a face using OpenCV (|frei0r.facebl0r|)
   * - :doc:`/effects_and_compositions/video_effects/misc/face_detect` |appimage|\ |windows|\ |apple|
     - Misc
     - Detect faces and draw shapes on them using OpenCV (|frei0r.facedetect|)
   * - :doc:`/effects_and_compositions/video_effects/misc/ffmeg_image_converter` |linux|\ |appimage|\ |windows|\ |apple|
     - Misc
     - Converts the colorspace and pixel format. (|avcolor_space|)
   * - :doc:`/effects_and_compositions/video_effects/misc/ffmeg_image_scaler` |linux|\ |appimage|\ |windows|\ |apple|
     - Misc
     - Change the resolution of an image. (|swscale|)
   * - :doc:`/effects_and_compositions/video_effects/misc/dnn_classify` |appimage|\ |windows|\ |apple|
     - Misc
     - Apply DNN classify filter to the input. (|avfilter.dnn_classify|)
   * - :doc:`/effects_and_compositions/video_effects/misc/dnn_detect` |appimage|\ |windows|\ |apple|
     - Misc
     - Apply DNN detect filter to the input. (|avfilter.dnn_detect|)
   * - :doc:`/effects_and_compositions/video_effects/misc/blurdetect` |appimage|\ |windows|\ |apple|
     - Misc
     - Blurdetect filter. (|avfilter.blurdetect|)
   * - :doc:`/effects_and_compositions/video_effects/misc/blockdetect` |appimage|\ |windows|\ |apple|
     - Misc
     - Blockdetect filter. (|avfilter.blockdetect|)
   * - :doc:`/effects_and_compositions/video_effects/stylize/aech0r` |appimage|\ |windows|\ |apple|
     - Stylize
     - analog video echo (|frei0r.aech0r|)
