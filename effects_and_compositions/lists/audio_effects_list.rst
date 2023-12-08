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
   :widths: 20 8 20 42

   * - Effect or Filter
     - OS\ [1]_
     - Category
     - Description
   * - :doc:`4 x 4 pole allpass </effects_and_compositions/audio_effects/swh_plugins/index>`
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1218|)
   * - :doc:`Adecorrelate </effects_and_compositions/audio_effects/audio/index>`
     - |appimage|\ |windows|\ |apple|\ |linux|
     - Audio
     - Apply decorrelation to input audio. (|avfilter.adecorrelate|)
   * - :doc:`Adenorm </effects_and_compositions/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Remedy denormals by adding extremely low-level noise. (|avfilter.adenorm|)
   * - :doc:`Aderivative </effects_and_compositions/audio_effects/tools/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Tools
     - Compute derivative of input audio (|avfilter.aderivative|)
   * - :doc:`Adrc </effects_and_compositions/audio_effects/audio/index>` 
     - |windows|\ |apple|
     - Audio
     - Audio Spectral Dynamic Range Controller. (|avfilter.adrc|)
   * - :doc:`Adynamicequalizer </effects_and_compositions/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Apply Dynamic Equalization of input audio. (|avfilter.adynamicequalizer|)
   * - :doc:`Adynamicsmooth </effects_and_compositions/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Apply Dynamic Smoothing of input audio. (|avfilter.adynamicsmooth|)
   * - :doc:`Aexciter </effects_and_compositions/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Enhance high frequency part of audio (|avfilter.aexciter|)
   * - :doc:`Afreqshift </effects_and_compositions/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Apply frequency shifting to input audio (|avfilter.afreqshift|)
   * - :doc:`Afwtdn </effects_and_compositions/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Denoise audio stream using Wavelets. (|avfilter.afwtdn|)
   * - :doc:`Aintegral </effects_and_compositions/audio_effects/tools/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Tools
     - Compute integral of input audio (|avfilter.aintegral|)
   * - :doc:`Alatency </effects_and_compositions/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Report audio filtering latency. (|avfilter.alatency|)
   * - :doc:`Aliasing </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1407|)
   * - :doc:`Allpass </effects_and_compositions/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - EQ and Filters
     - Apply a two-pole all-pass filter (|avfilter.allpass|)
   * - :doc:`Allpass delay line, cubic spline interpolation </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1897|)
   * - :doc:`Allpass delay line, linear interpolation </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1896|)
   * - :doc:`Allpass delay line, noninterpolating </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1895|)
   * - :doc:`AM pitchshifter </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1433|)
   * - :doc:`Ambisonic Decoder </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Various applications: B-Format to Cube (|ladspa.1092|), B-Format to Quad (|ladspa.1091|), B-Format to Stereo (|ladspa.1090|), FMH-Format to Octagon (|ladspa.1093|)
   * - :doc:`Ambisonic Encoder </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Various applications: B-Format (|ladspa.1087|), FMH-Format (|ladspa.1088|),
   * - :doc:`Ambisonic Rotation </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Various applications: B-Format Rotation (Horizontal) (|ladspa.1094|), FMH-Format Rotation (Horizontal) (|ladspa.1095|)
   * - :doc:`Amplifier (Mono) </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Amplifier (Mono). (|ladspa.1067|)
   * - :doc:`Amplifier (Stereo) </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Amplifier (Stereo). (|ladspa.1068|)
   * - :doc:`Amplitude Modulator </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Amplitude Modulator. (|ladspa.1070|)
   * - :doc:`Aphaseshift </effects_and_compositions/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Apply phase shifting to input audio (|avfilter.aphaseshift|)
   * - :doc:`Apsyclip </effects_and_compositions/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Audio Psychoacoustic Clipper. (|avfilter.apsyclip|)
   * - :doc:`Arndn </effects_and_compositions/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Reduce noise from speech using recurrent Neural Networks (|avfilter.arnndn|)
   * - :doc:`Artificial latency </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1914|)
   * - :doc:`Asoftclip </effects_and_compositions/audio_effects/volume_and_dynamics/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Audio soft clipper (|avfilter.asoftclip|)
   * - :doc:`Aspectralstats </effects_and_compositions/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Show frequency domain statistics about audio frames. (|avfilter.aspectralstats|)
   * - :doc:`Asr </effects_and_compositions/audio_effects/audio/index>` 
     - |linux|
     - Audio
     - Automatic Speech Recognition. (|avfilter.asr|)
   * - :doc:`Asubboost </effects_and_compositions/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Show time domain statistics about audio frames (|avfilter.astats|)
   * - :doc:`Asubcut </effects_and_compositions/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Cut subwoofer frequencies (|avfilter.asubcut|)
   * - :doc:`Asupercut </effects_and_compositions/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Cut super frequencies (|avfilter.asupercut|)
   * - :doc:`Asuperpass </effects_and_compositions/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Apply high order Butterworth band-pass filter (|avfilter.asuperpass|)
   * - :doc:`Asuperstop </effects_and_compositions/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Apply high order Butterworth band-stop filter (|avfilter.asuperstop|)
   * - :doc:`Atilt </effects_and_compositions/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Apply spectral tilt to audio. (|avfilter.atilt|)
   * - :doc:`Audio Divider (Suboctave Generator) </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1186|)
   * - :doc:`Audio Equalizer_(avfilter) </effects_and_compositions/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - EQ and Filters
     - Apply two-pole peaking equalization (EQ) filter (|avfilter.equalizer|)
   * - :doc:`Audio Levels </effects_and_compositions/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Compute the audio amplitude (|audiolevel|)
   * - :doc:`/effects_and_compositions/audio_effects/channels/audio_pan` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Channels
     - Pan an audio channel, adjust balance, or adjust fade (|panner|)
   * - :doc:`/effects_and_compositions/audio_effects/channels/audiomap` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Channels
     - |audiomap| (|audiomap|)
   * - :doc:`Auto phaser </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1219|)
   * - :doc:`/effects_and_compositions/audio_effects/channels/balance` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Channels
     - Adjust the left/right balance (|panner|)
   * - :doc:`Band-pass </effects_and_compositions/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - EQ and Filters
     - Apply a two-pole band-pass filter (|avfilter.bandpass|)
   * - :doc:`Band-Reject </effects_and_compositions/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - EQ and Filters
     - Apply a two-pole Butterworth band-reject filter (|avfilter.bandreject|)
   * - :doc:`Barry’s Satan Maximiser </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1408|)
   * - :doc:`Bass </effects_and_compositions/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - EQ and Filters
     - Boost or cut lower frequencies (|avfilter.bass|)
   * - :doc:`Bode frequency shifter </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1431|)
   * - :doc:`Bode frequency shifter (CV) </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1432|)
   * - :doc:`Canyon Delay </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - A deep stereo crossdelay with built-in low pass filters. (|ladspa.1225|)
   * - :doc:`Chebyshev distortion </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1430|)
   * - :doc:`Comb delay line cubic, spline interpolation </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1888|)
   * - :doc:`Comb delay line, linear interpolation </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1887|)
   * - :doc:`Comb delay line, noninterpolating </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1889|)
   * - :doc:`Comb Filter </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1190|)
   * - :doc:`Comb Splitter </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1411|)
   * - :doc:`Compensation Delay </effects_and_compositions/audio_effects/reverb_echo_delays/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Reverb, Echo and Delays
     - Audio Compensation Delay Line (|avfilter.compensationdelay|)
   * - :doc:`/effects_and_compositions/audio_effects/volume_and_dynamics/compressor_expander` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Compress or expand the audio’s dynamic range. (|avfilter.compand|)
   * - :doc:`Constant Signal Generator </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1909|)
   * - :doc:`/effects_and_compositions/audio_effects/channels/copy_channels_to_stereo` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Channels
     - Copy one audio channel to another (|channelcopy|)
   * - :doc:`Crossfade </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1915|)
   * - :doc:`Crossfade (4 outs) </effects_and_compositions/audio_effects/ladspa_plugins/index>` 
     - |linux|
     - LADSPA Plugins
     - LADSPA Plugin (|ladspa.1917|)
   * - :doc:`Crossfeed </effects_and_compositions/audio_effects/stereo_and_binaural_images/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stereo and Binaural Images
     - Apply headphone crossfeed filter (|avfilter.crossfeed|)
   * - :doc:`Crossover distortion </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1404|)
   * - :doc:`/effects_and_compositions/audio_effects/tools/crusher` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Tools
     - Reduce audio bit resolution. (|avfilter.acrusher|)
   * - :doc:`/effects_and_compositions/audio_effects/tools/crystalizer` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Tools
     - Simple audio noise sharpening filter (|avfilter.crystalizer|)
   * - :doc:`Dc Offset Remover </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1207|)
   * - :doc:`/effects_and_compositions/audio_effects/tools/dc_shift` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Tools
     - Apply a DC shift to the audio. This can be useful to remove a DC offset (caused perhaps by a hardware problem in the recording chain) from the audio. The effect of a DC offset is reduced headroom and hence volume. The astats filter can be used to determine if a signal has a DC offset. (|avfilter.dcshift|)
   * - :doc:`Decimator </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1202|)
   * - :doc:`Declipper </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1195|)
   * - :doc:`/effects_and_compositions/audio_effects/volume_and_dynamics/deesser` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Apply a de-essing to the audio (|avfilter.deesser|)
   * - :doc:`Delayorama </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1402|)
   * - :doc:`Dialoguenhance </effects_and_compositions/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Apply a flanging effect to the audio (|avfilter.flanger|)
   * - :doc:`Diode Processor </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1185|)
   * - :doc:`Disintegrator </effects_and_compositions/audio_effects/ladspa_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - LADSPA Plugins
     - LADSPA plugin (|ladspa.1846|)
   * - :doc:`Dj Eq </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1901|)
   * - :doc:`Dj Eq (Mono) </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1907|)
   * - :doc:`Dj Flanger </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1438|)
   * - :doc:`Dynamic Sledgehammer </effects_and_compositions/audio_effects/ladspa_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - LADSPA Plugins
     - LADSPA plugin (|ladspa.1848|)
   * - :doc:`Dyson Compressor </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1403|)
   * - :doc:`Echo Delay Line </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Echo Delay Line with max delays of 0.01s, 0.1s, 1s, 5s, 60s. No feedback is provided.
   * - :doc:`Exponential Signal Decay </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1886|)
   * - :doc:`Extrastereo </effects_and_compositions/audio_effects/stereo_and_binaural_images/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stereo and Binaural Images
     - Increase difference between stereo audio channels (|avfilter.extrastereo|)
   * - :doc:`/effects_and_compositions/audio_effects/volume_and_dynamics/fade_in` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Fade in audio track (|volume|)
   * - :doc:`/effects_and_compositions/audio_effects/volume_and_dynamics/fade_out` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Fade out audio track (|volume|)
   * - :doc:`Fast Lookahead Imiter </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1913|)
   * - :doc:`Fast Overdrive </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1196|)
   * - :doc:`Feedback Delay Line </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Feedback Delay Line with max delays of 0.01s, 0.1s, 1s, 5s, 60s. No feedback is provided.
   * - :doc:`Ffmpeg Audio Resampler </effects_and_compositions/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Apply a flanging effect to the audio (|avfilter.flanger|)
   * - :doc:`JACK </effects_and_compositions/audio_effects/audio/index>` 
     - |linux|
     - Audio
     - Process audio using JACK. (|jack|)
   * - :doc:`Flanger </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1191|)
   * - :doc:`Flanger </effects_and_compositions/audio_effects/modulators/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Modulators
     - Apply a flanging effect to the audio.  (|avfilter.flanger|)
   * - :doc:`Fm Oscillator </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1415|)
   * - :doc:`FMH-Format to V-Format </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|
     - CMT Plugins
     - This plugin simply discards the R, S, T, U and V channels but is included for clarity. (|ladspa.1089|)
   * - :doc:`Foldover Distortion </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1213|)
   * - :doc:`Fractionally Addressed Delay Line </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1192|)
   * - :doc:`FMH-Format to B-Format (Discard RSTUV Channels) </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |windows|\ |apple|
     - CMT Plugins
     - LADSPA plugin (|ladspa.1089|)
   * - :doc:`Freeverb (Version 3) </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - This reverb unit is a direct port of the free public domain source code available from Jezar at Dreampoint. (|ladspa.1123|)
   * - :doc:`Frequency Tracker </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1418|)
   * - :doc:`/effects_and_compositions/audio_effects/volume_and_dynamics/gain` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Adjust the audio |volume| without keyframes (|volume|)
   * - :doc:`Gate </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1410|)
   * - :doc:`Giant Flange </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1437|)
   * - :doc:`Glame Bandpass Analog Filter </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1893|)
   * - :doc:`Glame Bandpass Filter </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1892|)
   * - :doc:`Glame Butterworth Highpass </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1904|)
   * - :doc:`Glame Butterworth Lowpass </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1903|)
   * - :doc:`Glame Butterworth X-Over Filter </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1902|)
   * - :doc:`Glame Highpass Filter </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1890|)
   * - :doc:`Glame Lowpass Filter </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1891|)
   * - :doc:`Gong Beater </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1439|)
   * - :doc:`Gong Model </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1424|)
   * - :doc:`Granular Scattering Processor </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - This plugin generates an output audio stream by scattering short `grains` of sound from an input stream. It is possible to control the length and envelope of these grains, how far away from their source time grains may be scattered and the density (grains/sec) of the texture produced. (|ladspa.1096|)
   * - :doc:`GSM Simulator </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1215|)
   * - :doc:`Gverb </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1216|)
   * - :doc:`Haas Stereo Enhancer </effects_and_compositions/audio_effects/stereo_and_binaural_images/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stereo and Binaural Images
     - Apply Haas Stereo Enhancer (|avfilter.haas|)
   * - :doc:`Hard Gate </effects_and_compositions/audio_effects/ladspa_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - LADSPA Plugins
     - LADSPA plugin (|ladspa.1845|)
   * - :doc:`Hard Limiter </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1413|)
   * - :doc:`Harmonic Generator </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1220|)
   * - :doc:`Hermes Filter </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1200|)
   * - :doc:`High Pass Filter (One Pole) </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - High Pass Filter (One Pole). (|ladspa.1052|)
   * - :doc:`High-Pass </effects_and_compositions/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - EQ and Filters
     - Apply a high-pass filter with 3dB point frequency (|avfilter.highpass|)
   * - :doc:`High-Shelf </effects_and_compositions/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - EQ and Filters
     - Apply a high shelf filter (|avfilter.highshelf|)
   * - :doc:`Higher Quality Pitch Scaler </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1194|)
   * - :doc:`Hilbert Transformer </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1440|)
   * - :doc:`Identity </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Identity (Audio). (|ladspa.1098|)
   * - :doc:`Impulse Convolver </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1199|)
   * - :doc:`Inverter </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1429|)
   * - :doc:`Karaoke </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1409|)
   * - :doc:`L/C/R Delay </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1436|)
   * - :doc:`LFO Phaser </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1217|)
   * - :doc:`/effects_and_compositions/audio_effects/volume_and_dynamics/limiter` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Audio lookahead limiter (|avfilter.alimiter|)
   * - :doc:`Lo Fi </effects_and_compositions/audio_effects/ladspa_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - LADSPA Plugins
     - LADSPA plugin (|ladspa.1227|)
   * - :doc:`Low Pass Filter (One Pole) </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Low Pass Filter (One Pole). (|ladspa.1051|)
   * - :doc:`Low-Pass </effects_and_compositions/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - EQ and Filters
     - Apply a low-pass filter with 3dB point frequency (|avfilter.lowpass|)
   * - :doc:`Low-Shelf </effects_and_compositions/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - EQ and Filters
     - Apply a low shelf filter (|avfilter.lowshelf|)
   * - :doc:`LS Filter </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1908|)
   * - :doc:`Mag’s Notch Filter </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1894|)
   * - :doc:`Matrix Spatialiser </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1422|)
   * - :doc:`Matrix: MS To Stereo </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1421|)
   * - :doc:`Matrix: Stereo To MS </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1420|)
   * - :doc:`/effects_and_compositions/audio_effects/channels/mixdown` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Channels
     - Mix all channels of audio into a |mono| signal and output it as N channels (|mono|)
   * - :doc:`Mixer (Stereo to Mono) </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Mixer (Stereo to Mono). (|ladspa.1071|)
   * - :doc:`Modulatable delay </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1419|)
   * - :doc:`Mono To Stereo Splitter </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1406|)
   * - :doc:`Multiband EQ </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1197|)
   * - :doc:`Multivoice Chorus </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1201|)
   * - :doc:`/effects_and_compositions/audio_effects/volume_and_dynamics/mute` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Mute clip (|volume|)
   * - :doc:`Noise Suppressor for Voice </effects_and_compositions/audio_effects/ladspa_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - LADSPA Plugins
     - Microphone background noise removal filter (|ladspa.9354877|)
   * - :doc:`/effects_and_compositions/audio_effects/volume_and_dynamics/normalize` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Dynamically correct audio loudness as recommended by EBU R128 (|dynamic_loudness|)
   * - :doc:`/effects_and_compositions/audio_effects/volume_and_dynamics/normalize_2pass` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Correct audio |loudness| as recommended by EBU R128 (|loudness|)
   * - :doc:`/effects_and_compositions/audio_effects/channels/pan` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Channels
     - Adjust the left/right spread of a channel (|panner|)
   * - :doc:`Phaser </effects_and_compositions/audio_effects/modulators/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Modulators
     - Add a phasing effect to the audio (|avfilter.aphaser|)
   * - :doc:`Pitch Scaler </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1193|)
   * - :doc:`Plate reverb </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1423|)
   * - :doc:`Pointer cast distortion </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1910|)
   * - :doc:`Pulsator </effects_and_compositions/audio_effects/modulators/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Modulators
     - Audio Pulsator (|avfilter.apulsator|)
   * - :doc:`Rate Shifter </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1417|)
   * - :doc:`Retro Flanger </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (ladspa.1208)
   * - :doc:`Reverse Delay (5s Max) </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1605|)
   * - :doc:`Ringmod with LFO </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1189|)
   * - :doc:`Ringmod with two inputs </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1188|)
   * - :doc:`Rubberband Octave Shift </effects_and_compositions/audio_effects/pitch_and_time/index>` 
     - |linux|\ |appimage|\ |windows|
     - Pitch and Time
     - Adjust the audio pitch using the Rubberband library (|rbpitch|)
   * - :doc:`Rubberband Pitch Scale </effects_and_compositions/audio_effects/pitch_and_time/index>` 
     - |linux|\ |appimage|\ |windows|
     - Pitch and Time
     - Adjust the audio pitch using the Rubberband library. (|rbpitch|)
   * - :doc:`SC1 </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1425|)
   * - :doc:`SC2 </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (ladspa.1426)
   * - :doc:`SC3 </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1427|)
   * - :doc:`SC4 </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1882|)
   * - :doc:`SC4 mono </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1916|)
   * - :doc:`SE4 </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1883|)
   * - :doc:`Signal sifter </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1210|)
   * - :doc:`Simple amplifier </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1181|)
   * - :doc:`Simple compressor (peak envelope tracking) </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Simple Compressor (Peak Envelope Tracking). (|ladspa.1072|)
   * - :doc:`Simple compressor (rms envelope tracking) </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Simple Compressor (RMS Envelope Tracking). (|ladspa.1073|)
   * - :doc:`Simple compressor/expander </effects_and_compositions/audio_effects/audio/index>` 
     - |linux|
     - Audio
     - Simple audio dynamic range compression/expansion filter. (|avfiler.acontrast|)
   * - :doc:`Simple delay line, cubic spline interpolation </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1900|)
   * - :doc:`Simple delay line, linear interpolation </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1899|)
   * - :doc:`Simple delay line, noninterpolating </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (ladspa.1898)
   * - :doc:`Simple expander (peak  envelope tracking) </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Simple Expander (Peak Envelope Tracking). (|ladspa.1074|)
   * - :doc:`Simple expander (rms envelope tracking) </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Simple Expander (RMS Envelope Tracking). (|ladspa.1075|)
   * - :doc:`Simple limiter (peak envelope tracking) </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Simple Limiter (Peak Envelope Tracking). (|ladspa.1076|)
   * - :doc:`Simple limiter (rms  envelope tracking) </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Simple Limiter (RMS Envelope Tracking). (|ladspa.1077|)
   * - :doc:`Sine oscillator (freq:audio, amp:audio) </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Sine Oscillator. Frequency input is audio, Amplitude input is audio. (|ladspa.1063|)
   * - :doc:`Sine oscillator (freq:audio, amp:control) </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Sine Oscillator. Frequency input is audio, Amplitude input is control. (|ladspa.1064|)
   * - :doc:`Sine oscillator (freq:control, amp:audio) </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Sine Oscillator. Frequency input is control, Amplitude input is audio. (|ladspa.1065|)
   * - :doc:`Single band parametric </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1203|)
   * - :doc:`Sinus wavewrapper </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1198|)
   * - :doc:`Smooth Decimator </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1414|)
   * - :doc:`SoX </effects_and_compositions/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|
     - Audio
     - Process audio using a SoX effect (|sox|)
   * - :doc:`Sox Band </effects_and_compositions/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|
     - EQ and Filters
     - Sox band audio effect (|sox|)
   * - :doc:`Sox Bass </effects_and_compositions/audio_effects/eq_and_filters/index>` 
     - |linux|\ |appimage|\ |windows|
     - EQ and Filters
     - Sox bass audio effect (|sox|)
   * - :doc:`Sox Echo </effects_and_compositions/audio_effects/reverb_echo_delays/index>` 
     - |linux|\ |appimage|\ |windows|
     - Reverb, Echo and Delays
     - Sox echo audio effect (|sox|)
   * - :doc:`Sox Flanger </effects_and_compositions/audio_effects/modulators/index>` 
     - |linux|\ |appimage|\ |windows|
     - Modulators
     - Sox flanger audio effect (|sox|)
   * - :doc:`/effects_and_compositions/audio_effects/volume_and_dynamics/compressor_expander` 
     - |windows|\ |apple|
     - Volume and Dynamics
     - Simple audio dynamic range compression/expansion filter. (|avfilter.acontrast|)
   * - :doc:`/effects_and_compositions/audio_effects/volume_and_dynamics/gain` 
     - |linux|\ |appimage|\ |windows|
     - Volume and Dynamics
     - Sox gain audio effect (|sox|)
   * - :doc:`Sox Phaser </effects_and_compositions/audio_effects/modulators/index>` 
     - |linux|\ |appimage|\ |windows|
     - Modulators
     - Sox phaser audio effect (|sox|)
   * - :doc:`Sox Stretch </effects_and_compositions/audio_effects/pitch_and_time/index>` 
     - |linux|\ |appimage|\ |windows|
     - Pitch and Time
     - Sox stretch audio effect (|sox|)
   * - :doc:`Speechnorm </effects_and_compositions/audio_effects/audio/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Audio
     - Speech Normalizer (|avfilter.speechnorm|)
   * - :doc:`State Variable Filter </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1214|)
   * - :doc:`Step Demuxer </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1212|)
   * - :doc:`/effects_and_compositions/audio_effects/channels/stereo_to_mono` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Channels
     - Copy one channel to another (|channelcopy|)
   * - :doc:`SOFAlizer </effects_and_compositions/audio_effects/stereo_and_binaural_images/index>` 
     - |linux|
     - Stereo and Binaural Images
     - SOFAlizer uses head-related transfer functions (HRTFs) to create virtual loudspeakers around the user for binaural listening via headphones (audio formats up to 9 channels supported). The HRTFs are stored in SOFA files (see http://www.sofacoustics.org/ for a database). SOFAlizer is developed at the Acoustics Research Institute (ARI) of the Austrian Academy of Sciences.  (|avfilter.sofalizer|)
   * - :doc:`Stereo to binaural </effects_and_compositions/audio_effects/stereo_and_binaural_images/index>` 
     - |linux|
     - Stereo and Binaural Images
     - Bauer stereo to binaural transformation. (|avfilter.bs2b|)
   * - :doc:`Stereo Tools </effects_and_compositions/audio_effects/stereo_and_binaural_images/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stereo and Binaural Images
     - This filter has some handy utilities to manage stereo signals, for converting M/S stereo recordings to L/R signal while having control over the parameters or spreading the stereo image of master track.  (|avfilter.stereotools|)
   * - :doc:`Stereo Widener </effects_and_compositions/audio_effects/stereo_and_binaural_images/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Stereo and Binaural Images
     - This filter enhance the stereo effect by suppressing signal common to both channels and by delaying the signal of left into right and vice versa, thereby widening the stereo effect. (|avfilter.stereowiden|)
   * - :doc:`Surround matrix encoder </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1401|)
   * - :doc:`/effects_and_compositions/audio_effects/channels/swap_channels` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Channels
     - Move the left channel to the right and the right-to-left (|channelswap|)
   * - :doc:`Tap Autopanner </effects_and_compositions/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2146|)
   * - :doc:`Tap Chrous/Flanger </effects_and_compositions/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2159|)
   * - :doc:`Tap Deesser </effects_and_compositions/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2147|)
   * - :doc:`Tap Dynamics (M) </effects_and_compositions/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2152|)
   * - :doc:`Tap Dynamics (St) </effects_and_compositions/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2153|)
   * - :doc:`Tap Equalizer </effects_and_compositions/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2141|)
   * - :doc:`Tap Equalizer/Bw </effects_and_compositions/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2151|)
   * - :doc:`Tap Fractal Doubler </effects_and_compositions/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2156|)
   * - :doc:`Tap Pink/Fractal Noise </effects_and_compositions/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2155|)
   * - :doc:`Tap Pitch Shifter </effects_and_compositions/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2150|)
   * - :doc:`Tap Reflector </effects_and_compositions/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2154|)
   * - :doc:`Tap Reverberator </effects_and_compositions/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2142|)
   * - :doc:`Tap Rotary Speaker </effects_and_compositions/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2149|)
   * - :doc:`Tap Scaling Limiter </effects_and_compositions/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2145|)
   * - :doc:`Tap Sigmoid Booster </effects_and_compositions/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2157|)
   * - :doc:`Tap Stereo Echo </effects_and_compositions/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2143|)
   * - :doc:`Tap Tremolo </effects_and_compositions/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (ladspa.2144)
   * - :doc:`Tap Tubewarmth </effects_and_compositions/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2158|)
   * - :doc:`Tap Vibrato </effects_and_compositions/audio_effects/tap_plugins/index>` 
     - |appimage|\ |windows|
     - TAP Plugins
     - LADSPA plugin (|ladspa.2148|)
   * - :doc:`Tape Delay Simulation </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1211|)
   * - :doc:`Tiltshelf </effects_and_compositions/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Apply a tilt shelf filter. (|avfilter.tiltshelf|)
   * - :doc:`Transient mangler </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1206|)
   * - :doc:`Treble </effects_and_compositions/audio_effects/modulators/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Modulators
     - Boost or cut upper frequencies (|avfilter.treble|)
   * - :doc:`Triple band parametric with shelves </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1204|)
   * - :doc:`Valve rectifier </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1405|)
   * - :doc:`Valve saturation </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1209|)
   * - :doc:`VCF 303 </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - A TB-303 resonant filter clone. (|ladspa.1224|)
   * - :doc:`Vibrato </effects_and_compositions/audio_effects/modulators/index>` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Modulators
     - Vibrato effect. (|avfilter.vibrato|)
   * - :doc:`Virtualbass </effects_and_compositions/audio_effects/audio/index>` 
     - |appimage|\ |windows|\ |apple|
     - Audio
     - Audio Virtual Bass. (|avfilter.virtualbass|)
   * - :doc:`Vocoder </effects_and_compositions/audio_effects/ladspa_plugins/index>` 
     - |linux|\ |appimage|
     - LADSPA Plugins
     - LADSPA plugin (|ladspa.1337|)
   * - :doc:`/effects_and_compositions/audio_effects/volume_and_dynamics/volume_keyframable` 
     - |linux|\ |appimage|\ |windows|\ |apple|
     - Volume and Dynamics
     - Adjust the audio |volume| with keyframes (|volume|)
   * - :doc:`VyNil (Vinyl Effect) </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1905|)
   * - :doc:`Wave shaper </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1187|)
   * - :doc:`Wave Shaper (Sine-Based) </effects_and_compositions/audio_effects/cmt_plugins/index>` 
     - |appimage|\ |windows|\ |apple|
     - CMT Plugins
     - Wave Shaper (Sine-Based). (|ladspa.1097|)
   * - :doc:`Wave Terrain Oscillator </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1412|)
   * - :doc:`Z-1 </effects_and_compositions/audio_effects/swh_plugins/index>` 
     - |linux|
     - SWH plugins
     - LADSPA plugin (|ladspa.1428|)


.. Link list

.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   External
   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. |xbr_tutorial| raw:: html
   
   <a href="https://forums.libreto.com/t/xbr-algorithm-tutorial/123" target="_blank">xbr-algorithm-tutorial</a>

.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Audio
   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. |ladspa.1218| replace:: ladspa.1218

.. |avfilter.adecorrelate| replace:: avfilter.adecorrelate

.. |avfilter.adenorm| replace:: avfilter.adenorm

.. |avfilter.aderivative| replace:: avfilter.aderivative

.. |avfilter.adrc| replace:: avfilter.adrc

.. |avfilter.adynamicequalizer| replace:: avfilter.adynamicequalizer

.. |avfilter.adynamicsmooth| replace:: avfilter.adynamicsmooth

.. |avfilter.aexciter| replace:: avfilter.aexciter

.. |avfilter.afreqshift| replace:: avfilter.afreqshift

.. |avfilter.afwtdn| replace:: avfilter.afwtdn

.. |avfilter.aintegral| replace:: avfilter.aintegral

.. |avfilter.alatency| replace:: avfilter.alatency

.. |ladspa.1407| replace:: ladspa.1407

.. |avfilter.allpass| replace:: avfilter.allpass

.. |ladspa.1897| replace:: ladspa.1897

.. |ladspa.1896| replace:: ladspa.1896

.. |ladspa.1895| replace:: ladspa.1895

.. |ladspa.1433| replace:: ladspa.1433

.. |ladspa.1092| replace:: ladspa.1092

.. |ladspa.1091| replace:: ladspa.1091

.. |ladspa.1090| replace:: ladspa.1090

.. |ladspa.1093| replace:: ladspa.1093

.. |ladspa.1087| replace:: ladspa.1087

.. |ladspa.1088| replace:: ladspa.1088

.. |ladspa.1094| replace:: ladspa.1094

.. |ladspa.1095| replace:: ladspa.1095

.. |ladspa.1067| replace:: ladspa.1067

.. |ladspa.1068| replace:: ladspa.1068

.. |ladspa.1070| replace:: ladspa.1070

.. |avfilter.aphaseshift| replace:: avfilter.aphaseshift

.. |avfilter.apsyclip| replace:: avfilter.apsyclip

.. |avfilter.arnndn| replace:: avfilter.arnndn

.. |ladspa.1914| replace:: ladspa.1914

.. |avfilter.asoftclip| replace:: avfilter.asoftclip

.. |avfilter.aspectralstats| replace:: avfilter.aspectralstats

.. |avfilter.asr| replace:: avfilter.asr

.. |avfilter.astats| replace:: avfilter.astats

.. |avfilter.asubcut| replace:: avfilter.asubcut

.. |avfilter.asupercut| replace:: avfilter.asupercut

.. |avfilter.asuperpass| replace:: avfilter.asuperpass

.. |avfilter.asuperstop| replace:: avfilter.asuperstop

.. |avfilter.atilt| replace:: avfilter.atilt

.. |ladspa.1186| replace:: ladspa.1186

.. |avfilter.equalizer| replace:: avfilter.equalizer

.. |audiolevel| replace:: audiolevel

.. |panner| replace:: panner

.. |audiomap| replace:: audiomap

.. |ladspa.1219| replace:: ladspa.1219

.. |avfilter.bandpass| replace:: avfilter.bandpass

.. |avfilter.bandreject| replace:: avfilter.bandreject

.. |ladspa.1408| replace:: ladspa.1408

.. |avfilter.bass| replace:: avfilter.bass

.. |ladspa.1431| replace:: ladspa.1431

.. |ladspa.1432| replace:: ladspa.1432

.. |ladspa.1225| replace:: ladspa.1225

.. |ladspa.1430| replace:: ladspa.1430

.. |ladspa.1888| replace:: ladspa.1888

.. |ladspa.1887| replace:: ladspa.1887

.. |ladspa.1889| replace:: ladspa.1889

.. |ladspa.1190| replace:: ladspa.1190

.. |ladspa.1411| replace:: ladspa.1411

.. |avfilter.compensationdelay| replace:: avfilter.compensationdelay

.. |avfilter.compand| replace:: avfilter.compand

.. |ladspa.1909| replace:: ladspa.1909

.. |channelcopy| replace:: channelcopy

.. |ladspa.1915| replace:: ladspa.1915

.. |ladspa.1917| replace:: ladspa.1917

.. |avfilter.crossfeed| replace:: avfilter.crossfeed

.. |ladspa.1404| replace:: ladspa.1404

.. |avfilter.acrusher| replace:: avfilter.acrusher

.. |avfilter.crystalizer| replace:: avfilter.crystalizer

.. |ladspa.1207| replace:: ladspa.1207

.. |avfilter.dcshift| replace:: avfilter.dcshift

.. |ladspa.1202| replace:: ladspa.1202

.. |ladspa.1195| replace:: ladspa.1195

.. |avfilter.deesser| replace:: avfilter.deesser

.. |ladspa.1402| replace:: ladspa.1402

.. |avfilter.flanger| replace:: avfilter.flanger

.. |ladspa.1185| replace:: ladspa.1185

.. |ladspa.1846| replace:: ladspa.1846

.. |ladspa.1901| replace:: ladspa.1901

.. |ladspa.1907| replace:: ladspa.1907

.. |ladspa.1438| replace:: ladspa.1438

.. |ladspa.1848| replace:: ladspa.1848

.. |ladspa.1403| replace:: ladspa.1403

.. |ladspa.1053| replace:: ladspa.1053

.. |ladspa.1054| replace:: ladspa.1054

.. |ladspa.1055| replace:: ladspa.1055

.. |ladspa.1056| replace:: ladspa.1056

.. |ladspa.1057| replace:: ladspa.1057

.. |ladspa.1886| replace:: ladspa.1886

.. |avfilter.extrastereo| replace:: avfilter.extrastereo

.. |ladspa.1913| replace:: ladspa.1913

.. |ladspa.1196| replace:: ladspa.1196

.. |ladspa.1058| replace:: ladspa.1058

.. |ladspa.1059| replace:: ladspa.1059

.. |ladspa.1060| replace:: ladspa.1060

.. |ladspa.1061| replace:: ladspa.1061

.. |ladspa.1062| replace:: ladspa.1062

.. |jack| replace:: jack

.. |ladspa.1191| replace:: ladspa.1191

.. |ladspa.1415| replace:: ladspa.1415

.. |ladspa.1089| replace:: ladspa.1089

.. |ladspa.1213| replace:: ladspa.1213

.. |ladspa.1192| replace:: ladspa.1192

.. |ladspa.1123| replace:: ladspa.1123

.. |ladspa.1418| replace:: ladspa.1418

.. |ladspa.1410| replace:: ladspa.1410

.. |ladspa.1437| replace:: ladspa.1437

.. |ladspa.1893| replace:: ladspa.1893

.. |ladspa.1892| replace:: ladspa.1892

.. |ladspa.1904| replace:: ladspa.1904

.. |ladspa.1903| replace:: ladspa.1903

.. |ladspa.1902| replace:: ladspa.1902

.. |ladspa.1890| replace:: ladspa.1890

.. |ladspa.1891| replace:: ladspa.1891

.. |ladspa.1439| replace:: ladspa.1439

.. |ladspa.1424| replace:: ladspa.1424

.. |ladspa.1096| replace:: ladspa.1096

.. |ladspa.1215| replace:: ladspa.1215

.. |ladspa.1216| replace:: ladspa.1216

.. |avfilter.haas| replace:: avfilter.haas

.. |ladspa.1845| replace:: ladspa.1845

.. |ladspa.1413| replace:: ladspa.1413

.. |ladspa.1220| replace:: ladspa.1220

.. |ladspa.1200| replace:: ladspa.1200

.. |ladspa.1052| replace:: ladspa.1052

.. |avfilter.highpass| replace:: avfilter.highpass

.. |avfilter.highshelf| replace:: avfilter.highshelf

.. |ladspa.1194| replace:: ladspa.1194

.. |ladspa.1440| replace:: ladspa.1440

.. |ladspa.1098| replace:: ladspa.1098

.. |ladspa.1199| replace:: ladspa.1199

.. |ladspa.1429| replace:: ladspa.1429

.. |ladspa.1409| replace:: ladspa.1409

.. |ladspa.1436| replace:: ladspa.1436

.. |ladspa.1217| replace:: ladspa.1217

.. |avfilter.alimiter| replace:: avfilter.alimiter

.. |ladspa.1227| replace:: ladspa.1227

.. |ladspa.1051| replace:: ladspa.1051

.. |avfilter.lowpass| replace:: avfilter.lowpass

.. |avfilter.lowshelf| replace:: avfilter.lowshelf

.. |ladspa.1908| replace:: ladspa.1908

.. |ladspa.1894| replace:: ladspa.1894

.. |ladspa.1422| replace:: ladspa.1422

.. |ladspa.1421| replace:: ladspa.1421

.. |ladspa.1420| replace:: ladspa.1420

.. |mono| replace:: mono

.. |ladspa.1071| replace:: ladspa.1071

.. |ladspa.1419| replace:: ladspa.1419

.. |ladspa.1406| replace:: ladspa.1406

.. |ladspa.1197| replace:: ladspa.1197

.. |ladspa.1201| replace:: ladspa.1201

.. |volume| replace:: volume

.. |ladspa.9354877| replace:: ladspa.9354877

.. |dynamic_loudness| replace:: dynamic_loudness

.. |loudness| replace:: loudness

.. |avfilter.aphaser| replace:: avfilter.aphaser

.. |ladspa.1193| replace:: ladspa.1193

.. |ladspa.1423| replace:: ladspa.1423

.. |ladspa.1910| replace:: ladspa.1910

.. |avfilter.apulsator| replace:: avfilter.apulsator

.. |ladspa.1417| replace:: ladspa.1417

.. |ladspa.1605| replace:: ladspa.1605

.. |ladspa.1189| replace:: ladspa.1189

.. |ladspa.1188| replace:: ladspa.1188

.. |rbpitch| replace:: rbpitch

.. |ladspa.1425| replace:: ladspa.1425

.. |ladspa.1426| replace:: ladspa.1426

.. |ladspa.1427| replace:: ladspa.1427

.. |ladspa.1882| replace:: ladspa.1882

.. |ladspa.1916| replace:: ladspa.1916

.. |ladspa.1883| replace:: ladspa.1883

.. |ladspa.1210| replace:: ladspa.1210

.. |ladspa.1181| replace:: ladspa.1181

.. |ladspa.1072| replace:: ladspa.1072

.. |ladspa.1073| replace:: ladspa.1073

.. |avfiler.acontrast| replace:: avfiler.acontrast

.. |ladspa.1900| replace:: ladspa.1900

.. |ladspa.1899| replace:: ladspa.1899

.. |ladspa.1898| replace:: ladspa.1898

.. |ladspa.1074| replace:: ladspa.1074

.. |ladspa.1075| replace:: ladspa.1075

.. |ladspa.1076| replace:: ladspa.1076

.. |ladspa.1077| replace:: ladspa.1077

.. |ladspa.1063| replace:: ladspa.1063

.. |ladspa.1064| replace:: ladspa.1064

.. |ladspa.1065| replace:: ladspa.1065

.. |ladspa.1203| replace:: ladspa.1203

.. |ladspa.1198| replace:: ladspa.1198

.. |ladspa.1414| replace:: ladspa.1414

.. |sox| replace:: sox

.. |avfilter.acontrast| replace:: avfilter.acontrast

.. |avfilter.speechnorm| replace:: avfilter.speechnorm

.. |avfilter.smartblur| replace:: avfilter.smartblur

.. |ladspa.1214| replace:: ladspa.1214

.. |ladspa.1212| replace:: ladspa.1212

.. |avfilter.sofalizer| replace:: avfilter.sofalizer

.. |avfilter.bs2b| replace:: avfilter.bs2b

.. |avfilter.stereotools| replace:: avfilter.stereotools

.. |avfilter.stereowiden| replace:: avfilter.stereowiden

.. |ladspa.1401| replace:: ladspa.1401

.. |channelswap| replace:: channelswap

.. |ladspa.2146| replace:: ladspa.2146

.. |ladspa.2159| replace:: ladspa.2159

.. |ladspa.2147| replace:: ladspa.2147

.. |ladspa.2152| replace:: ladspa.2152

.. |ladspa.2153| replace:: ladspa.2153

.. |ladspa.2141| replace:: ladspa.2141

.. |ladspa.2151| replace:: ladspa.2151

.. |ladspa.2156| replace:: ladspa.2156

.. |ladspa.2155| replace:: ladspa.2155

.. |ladspa.2150| replace:: ladspa.2150

.. |ladspa.2154| replace:: ladspa.2154

.. |ladspa.2142| replace:: ladspa.2142

.. |ladspa.2149| replace:: ladspa.2149

.. |ladspa.2145| replace:: ladspa.2145

.. |ladspa.2157| replace:: ladspa.2157

.. |ladspa.2143| replace:: ladspa.2143

.. |ladspa.2144| replace:: ladspa.2144

.. |ladspa.2158| replace:: ladspa.2158

.. |ladspa.2148| replace:: ladspa.2148

.. |ladspa.1211| replace:: ladspa.1211

.. |avfilter.tiltshelf| replace:: avfilter.tiltshelf

.. |ladspa.1206| replace:: ladspa.1206

.. |avfilter.treble| replace:: avfilter.treble

.. |ladspa.1204| replace:: ladspa.1204

.. |ladspa.1405| replace:: ladspa.1405

.. |ladspa.1209| replace:: ladspa.1209

.. |ladspa.1224| replace:: ladspa.1224

.. |avfilter.vibrato| replace:: avfilter.vibrato

.. |avfilter.virtualbass| replace:: avfilter.virtualbass

.. |ladspa.1337| replace:: ladspa.1337

.. |ladspa.1905| replace:: ladspa.1905

.. |ladspa.1187| replace:: ladspa.1187

.. |ladspa.1097| replace:: ladspa.1097

.. |ladspa.1412| replace:: ladspa.1412

.. |ladspa.1428| replace:: ladspa.1428


----

.. [1] |linux|: available in installed version; |appimage|: available in the appimage; |windows|: available in Windows; |apple|: available on MacOS (Intel only)


.. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   To be done
   ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Audio
   ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   * - :doc:`Giant Flange </effects_and_compositions/audio_effects/stylize/index>` |appimage|
     - Stylize
     - LADSPA plugin (|ladspa.1437|)
