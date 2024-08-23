.. meta::
   :description: Alphabetical list of all audio effects in Kdenlive
   :keywords: KDE, Kdenlive, audio effects, plugins, composition, transition

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
Audio Effects
=============

.. note::
   The effects and compositions included will differ depending on the available plug-ins on the specific packaging on each operating system. Kdenlive will auto-detect and make available any supported LADSPA plug-in packages from your distribution. For the greatest compatibility, please use the AppImage version of Kdenlive.


.. list-table::  
   :class: table-wrap
   :header-rows: 1
   :width: 100%
   :widths: 23 8 20 49

   * - Effect or Filter
     - OS\ [1]_
     - Category
     - Description
   * - :doc:`4 x 4 pole allpass </effects_and_filters/audio_effects/swh_plugins/index>`
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1218|)
   * - :doc:`Adecorrelate </effects_and_filters/audio_effects/audio/index>`
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Apply decorrelation to input audio. (|avfilter.adecorrelate|)
   * - :doc:`Adenorm </effects_and_filters/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Remedy denormals by adding extremely low-level noise. (|avfilter.adenorm|)
   * - :doc:`Aderivative </effects_and_filters/audio_effects/tools/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Tools
     - Compute derivative of input audio (|avfilter.aderivative|)
   * - :doc:`Adrc </effects_and_filters/audio_effects/audio/index>` 
     - |windows|\ |apple|
     - Audio
     - Audio Spectral Dynamic Range Controller. (|avfilter.adrc|)
   * - :doc:`Adynamicequalizer </effects_and_filters/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Apply Dynamic Equalization of input audio. (|avfilter.adynamicequalizer|)
   * - :doc:`Adynamicsmooth </effects_and_filters/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Apply Dynamic Smoothing of input audio. (|avfilter.adynamicsmooth|)
   * - :doc:`Aexciter </effects_and_filters/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Enhance high frequency part of audio (|avfilter.aexciter|)
   * - :doc:`Afreqshift </effects_and_filters/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Apply frequency shifting to input audio (|avfilter.afreqshift|)
   * - :doc:`Afwtdn </effects_and_filters/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Denoise audio stream using Wavelets. (|avfilter.afwtdn|)
   * - :doc:`Aintegral </effects_and_filters/audio_effects/tools/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Tools
     - Compute integral of input audio (|avfilter.aintegral|)
   * - :doc:`Alatency </effects_and_filters/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Report audio filtering latency. (|avfilter.alatency|)
   * - :doc:`Aliasing </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1407|)
   * - :doc:`Allpass </effects_and_filters/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - EQ and Filters
     - Apply a two-pole all-pass filter (|avfilter.allpass|)
   * - :doc:`Allpass delay line, cubic spline interpolation </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1897|)
   * - :doc:`Allpass delay line, linear interpolation </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1896|)
   * - :doc:`Allpass delay line, noninterpolating </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1895|)
   * - :doc:`AM pitchshifter </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1433|)
   * - :doc:`Ambisonic Decoder </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Various applications: B-Format to Cube (|ladspa.1092|), B-Format to Quad (|ladspa.1091|), B-Format to Stereo (|ladspa.1090|), FMH-Format to Octagon (|ladspa.1093|)
   * - :doc:`Ambisonic Encoder </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Various applications: B-Format (|ladspa.1087|), FMH-Format (|ladspa.1088|),
   * - :doc:`Ambisonic Rotation </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Various applications: B-Format Rotation (Horizontal) (|ladspa.1094|), FMH-Format Rotation (Horizontal) (|ladspa.1095|)
   * - :doc:`Amplifier (Mono) </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Amplifier (Mono). (|ladspa.1067|)
   * - :doc:`Amplifier (Stereo) </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Amplifier (Stereo). (|ladspa.1068|)
   * - :doc:`Amplitude Modulator </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Amplitude Modulator. (|ladspa.1070|)
   * - :doc:`Aphaseshift </effects_and_filters/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Apply phase shifting to input audio (|avfilter.aphaseshift|)
   * - :doc:`Apsyclip </effects_and_filters/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Audio Psychoacoustic Clipper. (|avfilter.apsyclip|)
   * - :doc:`Arndn </effects_and_filters/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Reduce noise from speech using recurrent Neural Networks (|avfilter.arnndn|)
   * - :doc:`Artificial latency </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1914|)
   * - :doc:`Asoftclip </effects_and_filters/audio_effects/volume_and_dynamics/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Audio soft clipper (|avfilter.asoftclip|)
   * - :doc:`Aspectralstats </effects_and_filters/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Show frequency domain statistics about audio frames. (|avfilter.aspectralstats|)
   * - :doc:`Asr </effects_and_filters/audio_effects/audio/index>` 
     - |linux|
     - Audio
     - Automatic Speech Recognition. (|avfilter.asr|)
   * - :doc:`Asubboost </effects_and_filters/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Show time domain statistics about audio frames (|avfilter.astats|)
   * - :doc:`Asubcut </effects_and_filters/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Cut subwoofer frequencies (|avfilter.asubcut|)
   * - :doc:`Asupercut </effects_and_filters/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Cut super frequencies (|avfilter.asupercut|)
   * - :doc:`Asuperpass </effects_and_filters/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Apply high order Butterworth band-pass filter (|avfilter.asuperpass|)
   * - :doc:`Asuperstop </effects_and_filters/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Apply high order Butterworth band-stop filter (|avfilter.asuperstop|)
   * - :doc:`Atilt </effects_and_filters/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Apply spectral tilt to audio. (|avfilter.atilt|)
   * - :doc:`Audio Divider (Suboctave Generator) </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1186|)
   * - :doc:`Audio Equalizer_(avfilter) </effects_and_filters/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - EQ and Filters
     - Apply two-pole peaking equalization (EQ) filter (|avfilter.equalizer|)
   * - :doc:`Audio Levels </effects_and_filters/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Compute the audio amplitude (|audiolevel|)
   * - :doc:`/effects_and_filters/audio_effects/channels/audio_pan` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Channels
     - Pan an audio channel, adjust balance, or adjust fade (|panner|)
   * - :doc:`/effects_and_filters/audio_effects/channels/audiomap` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Channels
     - |audiomap| (|audiomap|)
   * - :doc:`Auto phaser </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1219|)
   * - :doc:`/effects_and_filters/audio_effects/channels/balance` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Channels
     - Adjust the left/right balance (|panner|)
   * - :doc:`Band-pass </effects_and_filters/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - EQ and Filters
     - Apply a two-pole band-pass filter (|avfilter.bandpass|)
   * - :doc:`Band-Reject </effects_and_filters/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - EQ and Filters
     - Apply a two-pole Butterworth band-reject filter (|avfilter.bandreject|)
   * - :doc:`Barry’s Satan Maximiser </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1408|)
   * - :doc:`Bass </effects_and_filters/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - EQ and Filters
     - Boost or cut lower frequencies (|avfilter.bass|)
   * - :doc:`Bode frequency shifter </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1431|)
   * - :doc:`Bode frequency shifter (CV) </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1432|)
   * - :doc:`Canyon Delay </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - A deep stereo crossdelay with built-in low pass filters. (|ladspa.1225|)
   * - :doc:`Chebyshev distortion </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1430|)
   * - :doc:`Comb delay line cubic, spline interpolation </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1888|)
   * - :doc:`Comb delay line, linear interpolation </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1887|)
   * - :doc:`Comb delay line, noninterpolating </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1889|)
   * - :doc:`Comb Filter </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1190|)
   * - :doc:`Comb Splitter </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1411|)
   * - :doc:`Compensation Delay </effects_and_filters/audio_effects/reverb_echo_delays/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Reverb, Echo and Delays
     - Audio Compensation Delay Line (|avfilter.compensationdelay|)
   * - :doc:`/effects_and_filters/audio_effects/volume_and_dynamics/compressor_expander` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Compress or expand the audio’s dynamic range. (|avfilter.compand|)
   * - :doc:`Constant Signal Generator </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1909|)
   * - :doc:`/effects_and_filters/audio_effects/channels/copy_channels_to_stereo` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Channels
     - Copy one audio channel to another (|channelcopy|)
   * - :doc:`Crossfade </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1915|)
   * - :doc:`Crossfade (4 outs) </effects_and_filters/audio_effects/ladspa_plugins/index>` 
     - |linux|
     - LADSPA Plugins
     - LADSPA Plugin (|ladspa.1917|)
   * - :doc:`Crossfeed </effects_and_filters/audio_effects/stereo_and_binaural_images/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stereo and Binaural Images
     - Apply headphone crossfeed filter (|avfilter.crossfeed|)
   * - :doc:`Crossover distortion </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1404|)
   * - :doc:`/effects_and_filters/audio_effects/tools/crusher` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Tools
     - Reduce audio bit resolution. (|avfilter.acrusher|)
   * - :doc:`/effects_and_filters/audio_effects/tools/crystalizer` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Tools
     - Simple audio noise sharpening filter (|avfilter.crystalizer|)
   * - :doc:`Dc Offset Remover </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1207|)
   * - :doc:`/effects_and_filters/audio_effects/tools/dc_shift` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Tools
     - Apply a DC shift to the audio. This can be useful to remove a DC offset (caused perhaps by a hardware problem in the recording chain) from the audio. The effect of a DC offset is reduced headroom and hence volume. The astats filter can be used to determine if a signal has a DC offset. (|avfilter.dcshift|)
   * - :doc:`Decimator </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1202|)
   * - :doc:`Declipper </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1195|)
   * - :doc:`/effects_and_filters/audio_effects/volume_and_dynamics/deesser` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Apply a de-essing to the audio (|avfilter.deesser|)
   * - :doc:`Delayorama </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1402|)
   * - :doc:`Dialoguenhance </effects_and_filters/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Apply a flanging effect to the audio (|avfilter.flanger|)
   * - :doc:`Diode Processor </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1185|)
   * - :doc:`Disintegrator </effects_and_filters/audio_effects/ladspa_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - LADSPA Plugins
     - LADSPA plugin (|ladspa.1846|)
   * - :doc:`Dj Eq </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1901|)
   * - :doc:`Dj Eq (Mono) </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1907|)
   * - :doc:`Dj Flanger </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1438|)
   * - :doc:`Dynamic Sledgehammer </effects_and_filters/audio_effects/ladspa_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - LADSPA Plugins
     - LADSPA plugin (|ladspa.1848|)
   * - :doc:`Dyson Compressor </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1403|)
   * - :doc:`Echo Delay Line </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Echo Delay Line with max delays of 0.01s, 0.1s, 1s, 5s, 60s. No feedback is provided.
   * - :doc:`Exponential Signal Decay </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1886|)
   * - :doc:`Extrastereo </effects_and_filters/audio_effects/stereo_and_binaural_images/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stereo and Binaural Images
     - Increase difference between stereo audio channels (|avfilter.extrastereo|)
   * - :doc:`/effects_and_filters/audio_effects/volume_and_dynamics/fade_in` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Fade in audio track (|volume|)
   * - :doc:`/effects_and_filters/audio_effects/volume_and_dynamics/fade_out` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Fade out audio track (|volume|)
   * - :doc:`Fast Lookahead Imiter </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1913|)
   * - :doc:`Fast Overdrive </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1196|)
   * - :doc:`Feedback Delay Line </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Feedback Delay Line with max delays of 0.01s, 0.1s, 1s, 5s, 60s. No feedback is provided.
   * - :doc:`Ffmpeg Audio Resampler </effects_and_filters/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Apply a flanging effect to the audio (|avfilter.flanger|)
   * - :doc:`JACK </effects_and_filters/audio_effects/audio/index>` 
     - |linux|
     - Audio
     - Process audio using JACK. (|jack|)
   * - :doc:`Flanger </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1191|)
   * - :doc:`Flanger </effects_and_filters/audio_effects/modulators/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Modulators
     - Apply a flanging effect to the audio.  (|avfilter.flanger|)
   * - :doc:`Fm Oscillator </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1415|)
   * - :doc:`FMH-Format to V-Format </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|
     - CMT Plugins
     - This plugin simply discards the R, S, T, U and V channels but is included for clarity. (|ladspa.1089|)
   * - :doc:`Foldover Distortion </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1213|)
   * - :doc:`Fractionally Addressed Delay Line </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1192|)
   * - :doc:`FMH-Format to B-Format (Discard RSTUV Channels) </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |windows|\ |apple|
     - CMT Plugins
     - LADSPA plugin (|ladspa.1089|)
   * - :doc:`Freeverb (Version 3) </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - This reverb unit is a direct port of the free public domain source code available from Jezar at Dreampoint. (|ladspa.1123|)
   * - :doc:`Frequency Tracker </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1418|)
   * - :doc:`/effects_and_filters/audio_effects/volume_and_dynamics/gain` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Adjust the audio |volume| without keyframes (|volume|)
   * - :doc:`Gate </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1410|)
   * - :doc:`Giant Flange </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1437|)
   * - :doc:`Glame Bandpass Analog Filter </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1893|)
   * - :doc:`Glame Bandpass Filter </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1892|)
   * - :doc:`Glame Butterworth Highpass </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1904|)
   * - :doc:`Glame Butterworth Lowpass </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1903|)
   * - :doc:`Glame Butterworth X-Over Filter </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1902|)
   * - :doc:`Glame Highpass Filter </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1890|)
   * - :doc:`Glame Lowpass Filter </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1891|)
   * - :doc:`Gong Beater </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1439|)
   * - :doc:`Gong Model </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1424|)
   * - :doc:`Granular Scattering Processor </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - This plugin generates an output audio stream by scattering short `grains` of sound from an input stream. It is possible to control the length and envelope of these grains, how far away from their source time grains may be scattered and the density (grains/sec) of the texture produced. (|ladspa.1096|)
   * - :doc:`GSM Simulator </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1215|)
   * - :doc:`Gverb </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1216|)
   * - :doc:`Haas Stereo Enhancer </effects_and_filters/audio_effects/stereo_and_binaural_images/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stereo and Binaural Images
     - Apply Haas Stereo Enhancer (|avfilter.haas|)
   * - :doc:`Hard Gate </effects_and_filters/audio_effects/ladspa_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - LADSPA Plugins
     - LADSPA plugin (|ladspa.1845|)
   * - :doc:`Hard Limiter </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1413|)
   * - :doc:`Harmonic Generator </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1220|)
   * - :doc:`Hermes Filter </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1200|)
   * - :doc:`High Pass Filter (One Pole) </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - High Pass Filter (One Pole). (|ladspa.1052|)
   * - :doc:`High-Pass </effects_and_filters/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - EQ and Filters
     - Apply a high-pass filter with 3dB point frequency (|avfilter.highpass|)
   * - :doc:`High-Shelf </effects_and_filters/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - EQ and Filters
     - Apply a high shelf filter (|avfilter.highshelf|)
   * - :doc:`Higher Quality Pitch Scaler </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1194|)
   * - :doc:`Hilbert Transformer </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1440|)
   * - :doc:`Identity </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Identity (Audio). (|ladspa.1098|)
   * - :doc:`Impulse Convolver </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1199|)
   * - :doc:`Inverter </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1429|)
   * - :doc:`Karaoke </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1409|)
   * - :doc:`L/C/R Delay </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1436|)
   * - :doc:`LFO Phaser </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1217|)
   * - :doc:`/effects_and_filters/audio_effects/volume_and_dynamics/limiter` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Audio lookahead limiter (|avfilter.alimiter|)
   * - :doc:`Lo Fi </effects_and_filters/audio_effects/ladspa_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - LADSPA Plugins
     - LADSPA plugin (|ladspa.1227|)
   * - :doc:`Low Pass Filter (One Pole) </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Low Pass Filter (One Pole). (|ladspa.1051|)
   * - :doc:`Low-Pass </effects_and_filters/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - EQ and Filters
     - Apply a low-pass filter with 3dB point frequency (|avfilter.lowpass|)
   * - :doc:`Low-Shelf </effects_and_filters/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - EQ and Filters
     - Apply a low shelf filter (|avfilter.lowshelf|)
   * - :doc:`LS Filter </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1908|)
   * - :doc:`Mag’s Notch Filter </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1894|)
   * - :doc:`Matrix Spatialiser </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1422|)
   * - :doc:`Matrix: MS To Stereo </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1421|)
   * - :doc:`Matrix: Stereo To MS </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1420|)
   * - :doc:`/effects_and_filters/audio_effects/channels/mixdown` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Channels
     - Mix all channels of audio into a |mono| signal and output it as N channels (|mono|)
   * - :doc:`Mixer (Stereo to Mono) </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Mixer (Stereo to Mono). (|ladspa.1071|)
   * - :doc:`Modulatable delay </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1419|)
   * - :doc:`Mono To Stereo Splitter </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1406|)
   * - :doc:`Multiband EQ </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1197|)
   * - :doc:`Multivoice Chorus </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1201|)
   * - :doc:`/effects_and_filters/audio_effects/volume_and_dynamics/mute` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Mute clip (|volume|)
   * - :doc:`Noise Suppressor for Voice </effects_and_filters/audio_effects/ladspa_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - LADSPA Plugins
     - Microphone background noise removal filter (|ladspa.9354877|)
   * - :doc:`/effects_and_filters/audio_effects/volume_and_dynamics/normalize` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Dynamically correct audio loudness as recommended by EBU R128 (|dynamic_loudness|)
   * - :doc:`/effects_and_filters/audio_effects/volume_and_dynamics/normalize_2pass` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Correct audio |loudness| as recommended by EBU R128 (|loudness|)
   * - :doc:`/effects_and_filters/audio_effects/channels/pan` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Channels
     - Adjust the left/right spread of a channel (|panner|)
   * - :doc:`Phaser </effects_and_filters/audio_effects/modulators/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Modulators
     - Add a phasing effect to the audio (|avfilter.aphaser|)
   * - :doc:`Pitch Scaler </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1193|)
   * - :doc:`Plate reverb </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1423|)
   * - :doc:`Pointer cast distortion </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1910|)
   * - :doc:`Pulsator </effects_and_filters/audio_effects/modulators/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Modulators
     - Audio Pulsator (|avfilter.apulsator|)
   * - :doc:`Rate Shifter </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1417|)
   * - :doc:`Retro Flanger </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (ladspa.1208)
   * - :doc:`Reverse Delay (5s Max) </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1605|)
   * - :doc:`Ringmod with LFO </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1189|)
   * - :doc:`Ringmod with two inputs </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1188|)
   * - :doc:`Rubberband Octave Shift </effects_and_filters/audio_effects/pitch_and_time/index>` 
     - |linux|\ |appimage|\ |windows|
     - Pitch and Time
     - Adjust the audio pitch using the Rubberband library (|rbpitch|)
   * - :doc:`Rubberband Pitch Scale </effects_and_filters/audio_effects/pitch_and_time/index>` 
     - |linux|\ |appimage|\ |windows|
     - Pitch and Time
     - Adjust the audio pitch using the Rubberband library. (|rbpitch|)
   * - :doc:`SC1 </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1425|)
   * - :doc:`SC2 </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (ladspa.1426)
   * - :doc:`SC3 </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1427|)
   * - :doc:`SC4 </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1882|)
   * - :doc:`SC4 mono </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1916|)
   * - :doc:`SE4 </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1883|)
   * - :doc:`Signal sifter </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1210|)
   * - :doc:`Simple amplifier </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1181|)
   * - :doc:`Simple compressor (peak envelope tracking) </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Simple Compressor (Peak Envelope Tracking). (|ladspa.1072|)
   * - :doc:`Simple compressor (rms envelope tracking) </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Simple Compressor (RMS Envelope Tracking). (|ladspa.1073|)
   * - :doc:`Simple compressor/expander </effects_and_filters/audio_effects/audio/index>` 
     - |linux|
     - Audio
     - Simple audio dynamic range compression/expansion filter. (|avfiler.acontrast|)
   * - :doc:`Simple delay line, cubic spline interpolation </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1900|)
   * - :doc:`Simple delay line, linear interpolation </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1899|)
   * - :doc:`Simple delay line, noninterpolating </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (ladspa.1898)
   * - :doc:`Simple expander (peak  envelope tracking) </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Simple Expander (Peak Envelope Tracking). (|ladspa.1074|)
   * - :doc:`Simple expander (rms envelope tracking) </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Simple Expander (RMS Envelope Tracking). (|ladspa.1075|)
   * - :doc:`Simple limiter (peak envelope tracking) </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Simple Limiter (Peak Envelope Tracking). (|ladspa.1076|)
   * - :doc:`Simple limiter (rms  envelope tracking) </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Simple Limiter (RMS Envelope Tracking). (|ladspa.1077|)
   * - :doc:`Sine oscillator (freq:audio, amp:audio) </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Sine Oscillator. Frequency input is audio, Amplitude input is audio. (|ladspa.1063|)
   * - :doc:`Sine oscillator (freq:audio, amp:control) </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Sine Oscillator. Frequency input is audio, Amplitude input is control. (|ladspa.1064|)
   * - :doc:`Sine oscillator (freq:control, amp:audio) </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Sine Oscillator. Frequency input is control, Amplitude input is audio. (|ladspa.1065|)
   * - :doc:`Single band parametric </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1203|)
   * - :doc:`Sinus wavewrapper </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1198|)
   * - :doc:`Smooth Decimator </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1414|)
   * - :doc:`SoX </effects_and_filters/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|
     - Audio
     - Process audio using a SoX effect (|sox|)
   * - :doc:`Sox Band </effects_and_filters/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|
     - EQ and Filters
     - Sox band audio effect (|sox|)
   * - :doc:`Sox Bass </effects_and_filters/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|
     - EQ and Filters
     - Sox bass audio effect (|sox|)
   * - :doc:`Sox Echo </effects_and_filters/audio_effects/reverb_echo_delays/index>` 
     - |linux|\ |appimage|\ |windows|
     - Reverb, Echo and Delays
     - Sox echo audio effect (|sox|)
   * - :doc:`Sox Flanger </effects_and_filters/audio_effects/modulators/index>` 
     - |linux|\ |appimage|\ |windows|
     - Modulators
     - Sox flanger audio effect (|sox|)
   * - :doc:`/effects_and_filters/audio_effects/volume_and_dynamics/compressor_expander` 
     - |windows|\ |apple|
     - Volume and Dynamics
     - Simple audio dynamic range compression/expansion filter. (|avfilter.acontrast|)
   * - :doc:`/effects_and_filters/audio_effects/volume_and_dynamics/gain` 
     - |linux|\ |appimage|\ |windows|
     - Volume and Dynamics
     - Sox gain audio effect (|sox|)
   * - :doc:`Sox Phaser </effects_and_filters/audio_effects/modulators/index>` 
     - |linux|\ |appimage|\ |windows|
     - Modulators
     - Sox phaser audio effect (|sox|)
   * - :doc:`Sox Stretch </effects_and_filters/audio_effects/pitch_and_time/index>` 
     - |linux|\ |appimage|\ |windows|
     - Pitch and Time
     - Sox stretch audio effect (|sox|)
   * - :doc:`Speechnorm </effects_and_filters/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Speech Normalizer (|avfilter.speechnorm|)
   * - :doc:`State Variable Filter </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1214|)
   * - :doc:`Step Demuxer </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1212|)
   * - :doc:`/effects_and_filters/audio_effects/channels/stereo_to_mono` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Channels
     - Copy one channel to another (|channelcopy|)
   * - :doc:`SOFAlizer </effects_and_filters/audio_effects/stereo_and_binaural_images/index>` 
     - |linux|
     - Stereo and Binaural Images
     - SOFAlizer uses head-related transfer functions (HRTFs) to create virtual loudspeakers around the user for binaural listening via headphones (audio formats up to 9 channels supported). The HRTFs are stored in SOFA files (see http://www.sofacoustics.org/ for a database). SOFAlizer is developed at the Acoustics Research Institute (ARI) of the Austrian Academy of Sciences.  (|avfilter.sofalizer|)
   * - :doc:`Stereo to binaural </effects_and_filters/audio_effects/stereo_and_binaural_images/index>` 
     - |linux|
     - Stereo and Binaural Images
     - Bauer stereo to binaural transformation. (|avfilter.bs2b|)
   * - :doc:`Stereo Tools </effects_and_filters/audio_effects/stereo_and_binaural_images/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stereo and Binaural Images
     - This filter has some handy utilities to manage stereo signals, for converting M/S stereo recordings to L/R signal while having control over the parameters or spreading the stereo image of master track.  (|avfilter.stereotools|)
   * - :doc:`Stereo Widener </effects_and_filters/audio_effects/stereo_and_binaural_images/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stereo and Binaural Images
     - This filter enhance the stereo effect by suppressing signal common to both channels and by delaying the signal of left into right and vice versa, thereby widening the stereo effect. (|avfilter.stereowiden|)
   * - :doc:`Surround matrix encoder </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1401|)
   * - :doc:`/effects_and_filters/audio_effects/channels/swap_channels` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Channels
     - Move the left channel to the right and the right-to-left (|channelswap|)
   * - :doc:`Tap Autopanner </effects_and_filters/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2146|)
   * - :doc:`Tap Chrous/Flanger </effects_and_filters/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2159|)
   * - :doc:`Tap Deesser </effects_and_filters/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2147|)
   * - :doc:`Tap Dynamics (M) </effects_and_filters/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2152|)
   * - :doc:`Tap Dynamics (St) </effects_and_filters/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2153|)
   * - :doc:`Tap Equalizer </effects_and_filters/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2141|)
   * - :doc:`Tap Equalizer/Bw </effects_and_filters/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2151|)
   * - :doc:`Tap Fractal Doubler </effects_and_filters/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2156|)
   * - :doc:`Tap Pink/Fractal Noise </effects_and_filters/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2155|)
   * - :doc:`Tap Pitch Shifter </effects_and_filters/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2150|)
   * - :doc:`Tap Reflector </effects_and_filters/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2154|)
   * - :doc:`Tap Reverberator </effects_and_filters/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2142|)
   * - :doc:`Tap Rotary Speaker </effects_and_filters/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2149|)
   * - :doc:`Tap Scaling Limiter </effects_and_filters/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2145|)
   * - :doc:`Tap Sigmoid Booster </effects_and_filters/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2157|)
   * - :doc:`Tap Stereo Echo </effects_and_filters/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2143|)
   * - :doc:`Tap Tremolo </effects_and_filters/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (ladspa.2144)
   * - :doc:`Tap Tubewarmth </effects_and_filters/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2158|)
   * - :doc:`Tap Vibrato </effects_and_filters/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2148|)
   * - :doc:`Tape Delay Simulation </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1211|)
   * - :doc:`Tiltshelf </effects_and_filters/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Apply a tilt shelf filter. (|avfilter.tiltshelf|)
   * - :doc:`Transient mangler </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1206|)
   * - :doc:`Treble </effects_and_filters/audio_effects/modulators/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Modulators
     - Boost or cut upper frequencies (|avfilter.treble|)
   * - :doc:`Triple band parametric with shelves </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1204|)
   * - :doc:`Valve rectifier </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1405|)
   * - :doc:`Valve saturation </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1209|)
   * - :doc:`VCF 303 </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - A TB-303 resonant filter clone. (|ladspa.1224|)
   * - :doc:`Vibrato </effects_and_filters/audio_effects/modulators/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Modulators
     - Vibrato effect. (|avfilter.vibrato|)
   * - :doc:`Virtualbass </effects_and_filters/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Audio Virtual Bass. (|avfilter.virtualbass|)
   * - :doc:`Vocoder </effects_and_filters/audio_effects/ladspa_plugins/index>` 
     - |linux|\ |appimage|
     - LADSPA Plugins
     - LADSPA plugin (|ladspa.1337|)
   * - :doc:`/effects_and_filters/audio_effects/volume_and_dynamics/volume_keyframable` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Adjust the audio |volume| with keyframes (|volume|)
   * - :doc:`VyNil (Vinyl Effect) </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1905|)
   * - :doc:`Wave shaper </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1187|)
   * - :doc:`Wave Shaper (Sine-Based) </effects_and_filters/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Wave Shaper (Sine-Based). (|ladspa.1097|)
   * - :doc:`Wave Terrain Oscillator </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1412|)
   * - :doc:`Z-1 </effects_and_filters/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1428|)


----

.. [1] |linux|: available in the installed version; |appimage|: available in the appimage; |windows|: available in the Windows version; |apple|: available in the MacOS (Intel only) version


.. Link list

.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   External
   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. |xbr_tutorial| raw:: html
   
   <a href="https://forums.libreto.com/t/xbr-algorithm-tutorial/123" target="_blank">xbr-algorithm-tutorial</a>

.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Audio
   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. |ladspa.1218| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1218/" target="_blank">ladspa.1218</a>

.. |avfilter.adecorrelate| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-adecorrelate/" target="_blank">avfilter.adecorrelate</a>

.. |avfilter.adenorm| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-adenorm/" target="_blank">avfilter.adenorm</a>

.. |avfilter.aderivative| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-aderivative/" target="_blank">avfilter.aderivative</a>

.. |avfilter.adrc| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-adrc/" target="_blank">avfilter.adrc</a>

.. |avfilter.adynamicequalizer| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-adynamicequalizer/" target="_blank">avfilter.adynamicequalizer</a>

.. |avfilter.adynamicsmooth| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-adynamicsmooth/" target="_blank">avfilter.adynamicsmooth</a>

.. |avfilter.aexciter| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-aexciter/" target="_blank">avfilter.aexciter</a>

.. |avfilter.afreqshift| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-afreqshift/" target="_blank">avfilter.afreqshift</a>

.. |avfilter.afwtdn| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-afwtdn/" target="_blank">avfilter.afwtdn</a>

.. |avfilter.aintegral| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-aintegral/" target="_blank">avfilter.aintegral</a>

.. |avfilter.alatency| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-alatency/" target="_blank">avfilter.alatency</a>

.. |ladspa.1407| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1407/" target="_blank">ladspa.1407</a>

.. |avfilter.allpass| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-allpass/" target="_blank">avfilter.allpass</a>

.. |ladspa.1897| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1897/" target="_blank">ladspa.1897</a>

.. |ladspa.1896| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1896/" target="_blank">ladspa.1896</a>

.. |ladspa.1895| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1895/" target="_blank">ladspa.1895</a>

.. |ladspa.1433| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1433/" target="_blank">ladspa.1433</a>

.. |ladspa.1092| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1092/" target="_blank">ladspa.1092</a>

.. |ladspa.1091| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1091/" target="_blank">ladspa.1091</a>

.. |ladspa.1090| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1090/" target="_blank">ladspa.1090</a>

.. |ladspa.1093| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1093/" target="_blank">ladspa.1093</a>

.. |ladspa.1087| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1087/" target="_blank">ladspa.1087</a>

.. |ladspa.1088| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1088/" target="_blank">ladspa.1088</a>

.. |ladspa.1094| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1094/" target="_blank">ladspa.1094</a>

.. |ladspa.1095| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1095/" target="_blank">ladspa.1095</a>

.. |ladspa.1067| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1067/" target="_blank">ladspa.1067</a>

.. |ladspa.1068| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1068/" target="_blank">ladspa.1068</a>

.. |ladspa.1070| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1070/" target="_blank">ladspa.1070</a>

.. |avfilter.aphaseshift| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-aphaseshift/" target="_blank">avfilter.aphaseshift</a>

.. |avfilter.apsyclip| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-apsyclip/" target="_blank">avfilter.apsyclip</a>

.. |avfilter.arnndn| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-arnndn/" target="_blank">avfilter.arnndn</a>

.. |ladspa.1914| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1914/" target="_blank">ladspa.1914</a>

.. |avfilter.asoftclip| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-asoftclip/" target="_blank">avfilter.asoftclip</a>

.. |avfilter.aspectralstats| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-aspectralstats/" target="_blank">avfilter.aspectralstats</a>

.. |avfilter.asr| replace:: avfilter.asr

.. |avfilter.astats| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-astats/" target="_blank">avfilter.astats</a>

.. |avfilter.asubcut| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-asubcut/" target="_blank">avfilter.asubcut</a>

.. |avfilter.asupercut| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-asupercut/" target="_blank">avfilter.asupercut</a>

.. |avfilter.asuperpass| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-asuperpass/" target="_blank">avfilter.asuperpass</a>

.. |avfilter.asuperstop| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-asuperstop/" target="_blank">avfilter.asuperstop</a>

.. |avfilter.atilt| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-atilt/" target="_blank">avfilter.atilt</a>

.. |ladspa.1186| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1186/" target="_blank">ladspa.1186</a>

.. |avfilter.equalizer| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-equalizer/" target="_blank">avfilter.equalizer</a>

.. |audiolevel| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAudiolevel/" target="_blank">audiolevel</a>

.. |panner| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterPanner/" target="_blank">panner</a>

.. |audiowaveform| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAudiowaveform/" target="_blank">audiowaveform</a>

.. |audiomap| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAudiomap/" target="_blank">audiomap</a>

.. |ladspa.1219| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1219/" target="_blank">ladspa.1219</a>

.. |avfilter.bandpass| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-bandpass/" target="_blank">avfilter.bandpass</a>

.. |avfilter.bandreject| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-bandreject/" target="_blank">avfilter.bandreject</a>

.. |ladspa.1408| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1408/" target="_blank">ladspa.1408</a>

.. |avfilter.bass| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-bass/" target="_blank">avfilter.bass</a>

.. |ladspa.1431| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1431/" target="_blank">ladspa.1431</a>

.. |ladspa.1432| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1432/" target="_blank">ladspa.1432</a>

.. |ladspa.1225| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1225/" target="_blank">ladspa.1225</a>

.. |ladspa.1430| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1430/" target="_blank">ladspa.1430</a>

.. |ladspa.1888| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1888/" target="_blank">ladspa.1888</a>

.. |ladspa.1887| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1887/" target="_blank">ladspa.1887</a>

.. |ladspa.1889| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1889/" target="_blank">ladspa.1889</a>

.. |ladspa.1190| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1190/" target="_blank">ladspa.1190</a>

.. |ladspa.1411| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1411/" target="_blank">ladspa.1411</a>

.. |avfilter.compensationdelay| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-compensationdelay/" target="_blank">avfilter.compensationdelay</a>

.. |avfilter.compand| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-compand/" target="_blank">avfilter.compand</a>

.. |ladspa.1909| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1909/" target="_blank">ladspa.1909</a>

.. |channelcopy| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterChannelcopy/" target="_blank">channelcopy</a>

.. |ladspa.1915| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1915/" target="_blank">ladspa.1915</a>

.. |ladspa.1917| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1917/" target="_blank">ladspa.1917</a>

.. |avfilter.crossfeed| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-crossfeed/" target="_blank">avfilter.crossfeed</a>

.. |ladspa.1404| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1404/" target="_blank">ladspa.1404</a>

.. |avfilter.acrusher| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-acrusher/" target="_blank">avfilter.acrusher</a>

.. |avfilter.crystalizer| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-crystalizer/" target="_blank">avfilter.crystalizer</a>

.. |ladspa.1207| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1207/" target="_blank">ladspa.1207</a>

.. |avfilter.dcshift| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-dcshift/" target="_blank">avfilter.dcshift</a>

.. |ladspa.1202| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1202/" target="_blank">ladspa.1202</a>

.. |ladspa.1195| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1195/" target="_blank">ladspa.1195</a>

.. |avfilter.deesser| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-deesser/" target="_blank">avfilter.deesser</a>

.. |ladspa.1402| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1402/" target="_blank">ladspa.1402</a>

.. |avfilter.flanger| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-flanger/" target="_blank">avfilter.flanger</a>

.. |ladspa.1185| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1185/" target="_blank">ladspa.1185</a>

.. |ladspa.1846| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1846/" target="_blank">ladspa.1846</a>

.. |ladspa.1901| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1901/" target="_blank">ladspa.1901</a>

.. |ladspa.1907| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1907/" target="_blank">ladspa.1907</a>

.. |ladspa.1438| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1438/" target="_blank">ladspa.1438</a>

.. |ladspa.1848| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1848/" target="_blank">ladspa.1848</a>

.. |ladspa.1403| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1403/" target="_blank">ladspa.1403</a>

.. |ladspa.1053| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1053/" target="_blank">ladspa.1053</a>

.. |ladspa.1054| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1054/" target="_blank">ladspa.1054</a>

.. |ladspa.1055| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1055/" target="_blank">ladspa.1055</a>

.. |ladspa.1056| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1056/" target="_blank">ladspa.1056</a>

.. |ladspa.1057| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1057/" target="_blank">ladspa.1057</a>

.. |ladspa.1886| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1886/" target="_blank">ladspa.1886</a>

.. |avfilter.extrastereo| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-extrastereo/" target="_blank">avfilter.extrastereo</a>

.. |volume| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterVolume/" target="_blank">volume</a>

.. |ladspa.1913| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1913/" target="_blank">ladspa.1913</a>

.. |ladspa.1196| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1196/" target="_blank">ladspa.1196</a>

.. |ladspa.1058| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1058/" target="_blank">ladspa.1058</a>

.. |ladspa.1059| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1059/" target="_blank">ladspa.1059</a>

.. |ladspa.1060| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1060/" target="_blank">ladspa.1060</a>

.. |ladspa.1061| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1061/" target="_blank">ladspa.1061</a>

.. |ladspa.1062| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1062/" target="_blank">ladspa.1062</a>

.. |jack| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterJack/" target="_blank">jack</a>

.. |ladspa.1191| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1191/" target="_blank">ladspa.1191</a>

.. |ladspa.1415| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1415/" target="_blank">ladspa.1415</a>

.. |ladspa.1089| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1089/" target="_blank">ladspa.1089</a>

.. |ladspa.1213| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1213/" target="_blank">ladspa.1213</a>

.. |ladspa.1192| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1192/" target="_blank">ladspa.1192</a>

.. |ladspa.1123| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1123/" target="_blank">ladspa.1123</a>

.. |ladspa.1418| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1418/" target="_blank">ladspa.1418</a>

.. |ladspa.1410| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1410/" target="_blank">ladspa.1410</a>

.. |ladspa.1437| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1437/" target="_blank">ladspa.1437</a>

.. |ladspa.1893| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1893/" target="_blank">ladspa.1893</a>

.. |ladspa.1892| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1892/" target="_blank">ladspa.1892</a>

.. |ladspa.1904| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1904/" target="_blank">ladspa.1904</a>

.. |ladspa.1903| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1903/" target="_blank">ladspa.1903</a>

.. |ladspa.1902| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1902/" target="_blank">ladspa.1902</a>

.. |ladspa.1890| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1890/" target="_blank">ladspa.1890</a>

.. |ladspa.1891| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1891/" target="_blank">ladspa.1891</a>

.. |ladspa.1439| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1439/" target="_blank">ladspa.1439</a>

.. |ladspa.1424| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1424/" target="_blank">ladspa.1424</a>

.. |ladspa.1096| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1096/" target="_blank">ladspa.1096</a>

.. |ladspa.1215| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1215/" target="_blank">ladspa.1215</a>

.. |ladspa.1216| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1216/" target="_blank">ladspa.1216</a>

.. |avfilter.haas| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-haas/" target="_blank">avfilter.haas</a>

.. |ladspa.1845| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1845/" target="_blank">ladspa.1845</a>

.. |ladspa.1413| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1413/" target="_blank">ladspa.1413</a>

.. |ladspa.1220| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1220/" target="_blank">ladspa.1220</a>

.. |ladspa.1200| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1200/" target="_blank">ladspa.1200</a>

.. |ladspa.1052| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1052/" target="_blank">ladspa.1052</a>

.. |avfilter.highpass| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-highpass/" target="_blank">avfilter.highpass</a>

.. |avfilter.highshelf| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-highshelf/" target="_blank">avfilter.highshelf</a>

.. |ladspa.1194| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1194/" target="_blank">ladspa.1194</a>

.. |ladspa.1440| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1440/" target="_blank">ladspa.1440</a>

.. |ladspa.1098| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1098/" target="_blank">ladspa.1098</a>

.. |ladspa.1199| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1199/" target="_blank">ladspa.1199</a>

.. |ladspa.1429| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1429/" target="_blank">ladspa.1429</a>

.. |ladspa.1409| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1409/" target="_blank">ladspa.1409</a>

.. |ladspa.1436| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1436/" target="_blank">ladspa.1436</a>

.. |ladspa.1217| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1217/" target="_blank">ladspa.1217</a>

.. |avfilter.alimiter| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-alimiter/" target="_blank">avfilter.alimiter</a>

.. |ladspa.1227| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1227/" target="_blank">ladspa.1227</a>

.. |ladspa.1051| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1051/" target="_blank">ladspa.1051</a>

.. |avfilter.lowpass| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-lowpass/" target="_blank">avfilter.lowpass</a>

.. |avfilter.lowshelf| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-lowshelf/" target="_blank">avfilter.lowshelf</a>

.. |ladspa.1908| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1908/" target="_blank">ladspa.1908</a>

.. |ladspa.1894| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1894/" target="_blank">ladspa.1894</a>

.. |ladspa.1422| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1422/" target="_blank">ladspa.1422</a>

.. |ladspa.1421| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1421/" target="_blank">ladspa.1421</a>

.. |ladspa.1420| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1420/" target="_blank">ladspa.1420</a>

.. |mono| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterMono/" target="_blank">mono</a>

.. |ladspa.1071| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1071/" target="_blank">ladspa.1071</a>

.. |ladspa.1419| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1419/" target="_blank">ladspa.1419</a>

.. |ladspa.1406| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1406/" target="_blank">ladspa.1406</a>

.. |ladspa.1197| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1197/" target="_blank">ladspa.1197</a>

.. |ladspa.1201| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1201/" target="_blank">ladspa.1201</a>

.. |ladspa.9354877| replace:: ladspa.9354877

.. |dynamic_loudness| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterDynamic_loudness/" target="_blank">dynamic_loudness</a>

.. |loudness| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLoudness/" target="_blank">loudness</a>

.. |avfilter.aphaser| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-aphaser/" target="_blank">avfilter.aphaser</a>

.. |ladspa.1193| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1193/" target="_blank">ladspa.1193</a>

.. |ladspa.1423| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1423/" target="_blank">ladspa.1423</a>

.. |ladspa.1910| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1910/" target="_blank">ladspa.1910</a>

.. |avfilter.apulsator| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-apulsator/" target="_blank">avfilter.apulsator</a>

.. |ladspa.1417| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1417/" target="_blank">ladspa.1417</a>

.. |ladspa.1208| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1208/" target="_blank">ladspa.1208</a>

.. |ladspa.1605| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1605/" target="_blank">ladspa.1605</a>

.. |ladspa.1189| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1189/" target="_blank">ladspa.1189</a>

.. |ladspa.1188| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1188/" target="_blank">ladspa.1188</a>

.. |rbpitch| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterRbpitch/" target="_blank">rbpitch</a>

.. |ladspa.1425| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1425/" target="_blank">ladspa.1425</a>

.. |ladspa.1426| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1426/" target="_blank">ladspa.1426</a>

.. |ladspa.1427| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1427/" target="_blank">ladspa.1427</a>

.. |ladspa.1882| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1882/" target="_blank">ladspa.1882</a>

.. |ladspa.1916| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1916/" target="_blank">ladspa.1916</a>

.. |ladspa.1883| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1883/" target="_blank">ladspa.1883</a>

.. |ladspa.1210| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1210/" target="_blank">ladspa.1210</a>

.. |ladspa.1181| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1181/" target="_blank">ladspa.1181</a>

.. |ladspa.1072| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1072/" target="_blank">ladspa.1072</a>

.. |ladspa.1073| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1073/" target="_blank">ladspa.1073</a>

.. |avfiler.acontrast| replace:: avfiler.acontrast

.. |ladspa.1900| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1900/" target="_blank">ladspa.1900</a>

.. |ladspa.1899| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1899/" target="_blank">ladspa.1899</a>

.. |ladspa.1898| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1898/" target="_blank">ladspa.1898</a>

.. |ladspa.1074| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1074/" target="_blank">ladspa.1074</a>

.. |ladspa.1075| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1075/" target="_blank">ladspa.1075</a>

.. |ladspa.1076| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1076/" target="_blank">ladspa.1076</a>

.. |ladspa.1077| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1077/" target="_blank">ladspa.1077</a>

.. |ladspa.1063| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1063/" target="_blank">ladspa.1063</a>

.. |ladspa.1064| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1064/" target="_blank">ladspa.1064</a>

.. |ladspa.1065| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1065/" target="_blank">ladspa.1065</a>

.. |ladspa.1203| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1203/" target="_blank">ladspa.1203</a>

.. |ladspa.1198| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1198/" target="_blank">ladspa.1198</a>

.. |ladspa.1414| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1414/" target="_blank">ladspa.1414</a>

.. |sox| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterSox/" target="_blank">sox</a>

.. |avfilter.acontrast| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-acontrast/" target="_blank">avfilter.acontrast</a>

.. |avfilter.speechnorm| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-speechnorm/" target="_blank">avfilter.speechnorm</a>

.. |ladspa.1214| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1214/" target="_blank">ladspa.1214</a>

.. |ladspa.1212| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1212/" target="_blank">ladspa.1212</a>

.. |avfilter.sofalizer| replace:: avfilter.sofalizer

.. |avfilter.bs2b| replace:: avfilter.bs2b

.. |avfilter.stereotools| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-stereotools/" target="_blank">avfilter.stereotools</a>

.. |avfilter.stereowiden| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-stereowiden/" target="_blank">avfilter.stereowiden</a>

.. |ladspa.1401| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1401/" target="_blank">ladspa.1401</a>

.. |channelswap| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterChannelswap/" target="_blank">channelswap</a>

.. |ladspa.2146| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-2146/" target="_blank">ladspa.2146</a>

.. |ladspa.2159| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-2159/" target="_blank">ladspa.2159</a>

.. |ladspa.2147| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-2147/" target="_blank">ladspa.2147</a>

.. |ladspa.2152| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-2152/" target="_blank">ladspa.2152</a>

.. |ladspa.2153| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-2153/" target="_blank">ladspa.2153</a>

.. |ladspa.2141| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-2141/" target="_blank">ladspa.2141</a>

.. |ladspa.2151| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-2151/" target="_blank">ladspa.2151</a>

.. |ladspa.2156| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-2156/" target="_blank">ladspa.2156</a>

.. |ladspa.2155| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-2155/" target="_blank">ladspa.2155</a>

.. |ladspa.2150| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-2150/" target="_blank">ladspa.2150</a>

.. |ladspa.2154| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-2154/" target="_blank">ladspa.2154</a>

.. |ladspa.2142| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-2142/" target="_blank">ladspa.2142</a>

.. |ladspa.2149| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-2149/" target="_blank">ladspa.2149</a>

.. |ladspa.2145| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-2145/" target="_blank">ladspa.2145</a>

.. |ladspa.2157| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-2157/" target="_blank">ladspa.2157</a>

.. |ladspa.2143| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-2143/" target="_blank">ladspa.2143</a>

.. |ladspa.2144| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-2144/" target="_blank">ladspa.2144</a>

.. |ladspa.2158| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-2158/" target="_blank">ladspa.2158</a>

.. |ladspa.2148| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-2148/" target="_blank">ladspa.2148</a>

.. |ladspa.1211| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1211/" target="_blank">ladspa.1211</a>

.. |avfilter.tiltshelf| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-tiltshelf/" target="_blank">avfilter.tiltshelf</a>

.. |ladspa.1206| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1206/" target="_blank">ladspa.1206</a>

.. |avfilter.treble| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-treble/" target="_blank">avfilter.treble</a>

.. |ladspa.1204| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1204/" target="_blank">ladspa.1204</a>

.. |ladspa.1405| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1405/" target="_blank">ladspa.1405</a>

.. |ladspa.1209| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1209/" target="_blank">ladspa.1209</a>

.. |ladspa.1224| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1224/" target="_blank">ladspa.1224</a>

.. |avfilter.vibrato| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-vibrato/" target="_blank">avfilter.vibrato</a>

.. |avfilter.virtualbass| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-virtualbass/" target="_blank">avfilter.virtualbass</a>

.. |ladspa.1337| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1337/" target="_blank">ladspa.1337</a>

.. |ladspa.1905| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1905/" target="_blank">ladspa.1905</a>

.. |ladspa.1187| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1187/" target="_blank">ladspa.1187</a>

.. |ladspa.1097| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1097/" target="_blank">ladspa.1097</a>

.. |ladspa.1412| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1412/" target="_blank">ladspa.1412</a>

.. |ladspa.1428| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterLadspa-1428/" target="_blank">ladspa.1428</a>


.. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   To be done
   ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Audio
   ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   * - :doc:`Giant Flange </effects_and_filters/audio_effects/stylize/index>` |appimage|
     - Stylize
     - LADSPA plugin (|ladspa.1437|)
