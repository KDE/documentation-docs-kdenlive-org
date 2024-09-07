<?php

// This script is intended to handle requests for files that do not exist
// This may occur because:
// 1) It is a language-free URL and we need to send the user to the most language appropriate version for them
// 2) The page has moved elsewhere and we need to send them to the appropriate page
// 3) The request is for a legacy page that existed on the older Mediawiki based setup, in which case we need to once again send them to the most appropriate page

// Our list of supported languages
$supported_languages = array(
    "en",
    "ca",
    "cs",
    "de",
    "fr",
    "it",
    "nl",
    "es",
    //"tr", // disabled because 0% translation coverage
    //"da", // disabled because 0% translation coverage
    "pl",
    //"pt_BR", // disabled because 0% translation coverage
    //"ru", // disabled because 0% translation coverage
    //"sk", // disabled because 0% translation coverage
    "sl",
    //"sv", // disabled because broken translation
    "uk_UA",
    "zh_CN",
    "zh_TW",
    "ja",
    "ko"
);

// List of page redirect rules
// These should always be free of the language code, as this will be automatically added on when formulating the URL to forward the user on to
$redirect_rules = array(
    // Default front page
    "^$" => "index.html",

    // Effects short links
    // These short links are use inside Kdenlive in the effects list to link to the documentation.
    // The pattern is https://docs.kdenlive.org/effect_link/EFFECTID where dots in EFFECTID are replaced by -
    "^effect_link\/affine" => "effects_and_filters/video_effects/transform_distort_perspective/rotate_and_shear.html",
    "^effect_link\/affinerotate" => "effects_and_filters/video_effects/transform_distort_perspective/rotate_keyframable.html",
    "^effect_link\/audiolevelgraph" => "effects_and_filters/video_effects/on_master/audio_level_visualization_filter.html",
    "^effect_link\/audiospectrum" => "effects_and_filters/video_effects/on_master/audio_spectrum_filter.html",
    "^effect_link\/audiowave" => "effects_and_filters/video_effects/on_master/audio_wave.html",
    "^effect_link\/audiowaveform" => "effects_and_filters/video_effects/on_master/audio_waveform_filter.html",
    "^effect_link\/avfilter.boxblur" => "effects_and_filters/video_effects/deprecated/box_blur.html",
    "^effect_link\/avfilter.cas" => "effects_and_filters/video_effects/blur_and_sharpen/contrast_adaptive_sharpen.html",
    "^effect_link\/avfilter.drawbox" => "effects_and_filters/video_effects/generate/drawbox.html",
    "^effect_link\/avfilter.drawgrid" => "effects_and_filters/video_effects/generate/drawgrid.html",
    "^effect_link\/avfilter.fftdnoiz" => "effects_and_filters/video_effects/grain_and_noise/3d_fft_denoiser.html",
    "^effect_link\/avfilter.histogram" => "effects_and_filters/video_effects/utility/histogram.html",
    "^effect_link\/avfilter.lenscorrection" => "effects_and_filters/video_effects/transform_distort_perspective/lens_correction.html",
    "^effect_link\/avfilter.lut3d" => "effects_and_filters/video_effects/color_image_correction/applylut.html",
    "^effect_link\/avfilter.oscilloscope" => "effects_and_filters/video_effects/utility/oscilloscope.html",
    "^effect_link\/avfilter.sobel" => "effects_and_filters/video_effects/stylize/sobel_planes.html",
    "^effect_link\/avfilter.vectorscope" => "effects_and_filters/video_effects/utility/vectorscope_advanced.html",
    "^effect_link\/boxblur" => "effects_and_filters/video_effects/deprecated/box_blur.html",
    "^effect_link\/brightness" => "effects_and_filters/video_effects/color_image_correction/brightness_keyframable.html",
    "^effect_link\/charcoal" => "effects_and_filters/video_effects/stylize/charcoal.html",
    "^effect_link\/chroma" => "effects_and_filters/video_effects/alpha_mask_keying/chroma_key.html",
    "^effect_link\/chroma_hold" => "effects_and_filters/video_effects/color_image_correction/chroma_hold.html",
    "^effect_link\/crop" => "effects_and_filters/video_effects/transform_distort_perspective/edge_crop.html",
    "^effect_link\/dance" => "effects_and_filters/video_effects/on_master/dance.html",
    "^effect_link\/dust" => "effects_and_filters/video_effects/grain_and_noise/dust.html",
    "^effect_link\/dynamictext" => "effects_and_filters/video_effects/generate/dynamic_text.html",
    "^effect_link\/fade_from_black" => "effects_and_filters/video_effects/motion/fade_in.html",
    "^effect_link\/fade_to_black" => "effects_and_filters/video_effects/motion/fade_out.html",
    "^effect_link\/freeze" => "effects_and_filters/video_effects/motion/freeze.html",
    "^effect_link\/frei0r.alpha0ps" => "effects_and_filters/video_effects/alpha_mask_keying/alpha_operations.html",
    "^effect_link\/frei0r.alphagrad" => "effects_and_filters/video_effects/alpha_mask_keying/alpha_gradient.html",
    "^effect_link\/frei0r.alphaspot" => "effects_and_filters/video_effects/alpha_mask_keying/alpha_shapes.html",
    "^effect_link\/frei0r.balanc0r" => "effects_and_filters/video_effects/color_image_correction/white_balance.html",
    "^effect_link\/frei0r.brightness" => "effects_and_filters/video_effects/color_image_correction/brightness.html",
    "^effect_link\/frei0r.c0rners" => "effects_and_filters/video_effects/transform_distort_perspective/corners.html",
    "^effect_link\/frei0r.cairogradient" => "effects_and_filters/video_effects/generate/cairogradient.html",
    "^effect_link\/frei0r.cairoimagegrid" => "effects_and_filters/video_effects/generate/video_grid.html",
    "^effect_link\/frei0r.cartoon" => "effects_and_filters/video_effects/stylize/cartoon.html",
    "^effect_link\/frei0r.cluster" => "effects_and_filters/video_effects/deprecated/k-means_clustering.html",
    "^effect_link\/frei0r.colgate" => "effects_and_filters/video_effects/color_image_correction/white_balance_lms.html",
    "^effect_link\/frei0r.coloradj_RGB" => "effects_and_filters/video_effects/color_image_correction/rgb_adjustment.html",
    "^effect_link\/frei0r.colordistance" => "effects_and_filters/video_effects/stylize/color_distance.html",
    "^effect_link\/frei0r.colortap" => "effects_and_filters/video_effects/stylize/color_effect.html",
    "^effect_link\/frei0r.curves" => "effects_and_filters/video_effects/color_image_correction/bezier_curves.html",
    "^effect_link\/frei0r.curves" => "effects_and_filters/video_effects/color_image_correction/curves.html",
    "^effect_link\/frei0r.defish0r" => "effects_and_filters/video_effects/transform_distort_perspective/defish.html",
    "^effect_link\/frei0r.distort0r" => "effects_and_filters/video_effects/stylize.html",
    "^effect_link\/frei0r.dither" => "effects_and_filters/video_effects/deprecated/dither.html",
    "^effect_link\/frei0r.edgeglow" => "effects_and_filters/video_effects/stylize/edge_glow.html",
    "^effect_link\/frei0r.equaliz0r" => "effects_and_filters/video_effects/color_image_correction/equaliz0r.html",
    "^effect_link\/frei0r.gamma" => "effects_and_filters/video_effects/color_image_correction/gamma.html",
    "^effect_link\/frei0r.glow" => "effects_and_filters/video_effects/stylize/glow.html",
    "^effect_link\/frei0r.hqdn3d" => "effects_and_filters/video_effects/grain_and_noise/denoiser.html",
    "^effect_link\/frei0r.hueshift0r" => "effects_and_filters/video_effects/color_image_correction/hue_shift.html",
    "^effect_link\/frei0r.IIRblur" => "effects_and_filters/video_effects/deprecated/blur.html",
    "^effect_link\/frei0r.keyspillm0pup" => "effects_and_filters/video_effects/alpha_mask_keying/key_spill_mop_up.html",
    "^effect_link\/frei0r.lenscorrection" => "effects_and_filters/video_effects/transform_distort_perspective/lens_correction_keyframe.html",
    "^effect_link\/frei0r.letterb0xed" => "effects_and_filters/video_effects/transform_distort_perspective/letterb0xed.html",
    "^effect_link\/frei0r.levels" => "effects_and_filters/video_effects/color_image_correction/levels.html",
    "^effect_link\/frei0r.luminance" => "effects_and_filters/video_effects/color_image_correction/luminance.html",
    "^effect_link\/frei0r.mask0mate" => "effects_and_filters/video_effects/alpha_mask_keying/rectangular_alpha_mask.html",
    "^effect_link\/frei0r.medians" => "effects_and_filters/video_effects/deprecated/medians.html",
    "^effect_link\/frei0r.ndvi" => "effects_and_filters/video_effects/stylize/ndvi_filter.html",
    "^effect_link\/frei0r.nervous" => "effects_and_filters/video_effects/motion/nervous.html",
    "^effect_link\/frei0r.nosync0r" => "effects_and_filters/video_effects/transform_distort_perspective/nosync0r.html",
    "^effect_link\/frei0r.pixeliz0r" => "effects_and_filters/video_effects/stylize/pixelize.html",
    "^effect_link\/frei0r.pr0be" => "effects_and_filters/video_effects/utility/video_values.html",
    "^effect_link\/frei0r.pr0file" => "effects_and_filters/video_effects/utility/oscilloscope_advanced.html",
    "^effect_link\/frei0r.primaries" => "effects_and_filters/video_effects/stylize/primaries.html",
    "^effect_link\/frei0r.rgbnoise" => "effects_and_filters/video_effects/deprecated/rgbnoise.html",
    "^effect_link\/frei0r.rgbsplit0r" => "effects_and_filters/video_effects/stylize/rgbsplit0r.html",
    "^effect_link\/frei0r.saturat0r" => "effects_and_filters/video_effects/color_image_correction/saturation.html",
    "^effect_link\/frei0r.scale0tilt" => "effects_and_filters/video_effects/transform_distort_perspective/crop_scale_tilt.html",
    "^effect_link\/frei0r.scanline0r" => "effects_and_filters/video_effects/generate/scanline0r.html",
    "^effect_link\/frei0r.select0r" => "effects_and_filters/video_effects/alpha_mask_keying/chroma_key_advanced.html",
    "^effect_link\/frei0r.sharpness" => "effects_and_filters/video_effects/deprecated/sharpen.html",
    "^effect_link\/frei0r.sigmoidaltransfer" => "effects_and_filters/video_effects/stylize/sigmoidal_transfer.html",
    "^effect_link\/frei0r.sobel" => "effects_and_filters/video_effects/stylize/sobel.html",
    "^effect_link\/frei0r.softglow" => "effects_and_filters/video_effects/stylize/soft_glow.html",
    "^effect_link\/frei0r.sopsat" => "effects_and_filters/video_effects/color_image_correction/sat.html",
    "^effect_link\/frei0r.spillsupress" => "effects_and_filters/video_effects/alpha_mask_keying/spillsuppress.html",
    "^effect_link\/frei0r.squareblur" => "effects_and_filters/video_effects/blur_and_sharpen/square_blur.html",
    "^effect_link\/frei0r.three_point_balance" => "effects_and_filters/video_effects/color_image_correction/3_point_balance.html",
    "^effect_link\/frei0r.threshold0r" => "effects_and_filters/video_effects/stylize/threshold.html",
    "^effect_link\/frei0r.timeout" => "effects_and_filters/video_effects/utility/timeout_indicator.html",
    "^effect_link\/frei0r.tint0r" => "effects_and_filters/video_effects/color_image_correction/tint.html",
    "^effect_link\/frei0r.vectorscope" => "effects_and_filters/video_effects/utility/vectorscope.html",
    "^effect_link\/frei0r.vignette" => "effects_and_filters/video_effects/generate/vignette.html",
    "^effect_link\/gain" => "effects_and_filters/audio_effects/volume_and_dynamics/gain.html",
    "^effect_link\/grain" => "effects_and_filters/video_effects/deprecated/grain.html",
    "^effect_link\/greyscale" => "effects_and_filters/video_effects/color_image_correction/greyscale.html",
    "^effect_link\/invert" => "effects_and_filters/video_effects/color_image_correction/invert.html",
    "^effect_link\/lift_gamma_gain" => "effects_and_filters/video_effects/color_image_correction/lift_gamma_gain.html",
    "^effect_link\/lightshow" => "effects_and_filters/video_effects/on_master/light_show.html",
    "^effect_link\/lines" => "effects_and_filters/video_effects/grain_and_noise/scratchlines.html",
    "^effect_link\/lumakey" => "effects_and_filters/video_effects/alpha_mask_keying/lumakey.html",
    "^effect_link\/mirror" => "effects_and_filters/video_effects/transform_distort_perspective/mirror.html",
    "^effect_link\/mute" => "effects_and_filters/audio_effects/volume_and_dynamics/mute.html",
    "^effect_link\/obscure" => "effects_and_filters/video_effects/alpha_mask_keying/obscure.html",
    "^effect_link\/oldfilm" => "effects_and_filters/video_effects/stylize/oldfilm.html",
    "^effect_link\/opencv.tracker" => "effects_and_filters/video_effects/alpha_mask_keying/motion_tracker.html",
    "^effect_link\/pan_zoom" => "effects_and_filters/video_effects/transform_distort_perspective/position_and_zoom.html",
    "^effect_link\/qtblend" => "effects_and_filters/video_effects/transform_distort_perspective/transform.html",
    "^effect_link\/rotoscoping" => "effects_and_filters/video_effects/alpha_mask_keying/rotoscoping.html",
    "^effect_link\/sepia" => "effects_and_filters/video_effects/color_image_correction/sepia.html",
    "^effect_link\/tcolor" => "effects_and_filters/video_effects/color_image_correction/technicolor.html",
    "^effect_link\/threshold" => "effects_and_filters/video_effects/stylize/binarize.html",
    "^effect_link\/typewriter" => "titles_and_graphics/titles/title_text.html#title-text-typewriter",
    "^effect_link\/vignette" => "effects_and_filters/video_effects/generate/vignette_effect.html",
    "^effect_link\/volume" => "effects_and_filters/audio_effects/volume_and_dynamics/volume_keyframable.html",
    "^effect_link\/wave" => "effects_and_filters/video_effects/deprecated/wave.html",
    "^transition_link\/composite" => "compositing/transitions/composite.html",
    "^transition_link\/frei0r.addition" => "compositing/blending_modes.html",
    "^transition_link\/frei0r.addition_alpha" => "compositing/blending_modes.html",
    "^transition_link\/frei0r.alphain" => "compositing/compositions/alpha_operations.html",
    "^transition_link\/frei0r.alphaout" => "compositing/compositions/alpha_operations.html",
    "^transition_link\/frei0r.alphaover" => "compositing/compositions/alpha_operations.html",
    "^transition_link\/frei0r.alphaatop" => "compositing/compositions/alpha_operations.html",
    "^transition_link\/frei0r.alphaxor" => "compositing/compositions/alpha_operations.html",
    "^transition_link\/frei0r.hue" => "compositing/blending_modes.html",
    "^transition_link\/frei0r.screen" => "compositing/blending_modes.html",
    "^transition_link\/wipe" => "compositing/transitions//wipe.html",

    // Unknown effect short link, redirect to effects overview
    "^effect_link" => "effects_and_filters/effects_and_filters_list.html"
    // Unknown transition short link, redirect to transition overview
    "^transition_link" => "compositing.html"

);

//// SETTINGS END
//// CHANGES SHOULD NOT BE NEEDED TO THE BELOW

// Helper function to determine the most appropriate language for the user
// Parameters:
// $request              The web path that the user is trying to reach
// $browser_languages    The languages accepted by the user browser, in Accept-Language format
// $supported_languages  Array of languages that we support - in ISO language code format
function determine_appropriate_language( $request, $browser_languages, $supported_languages )
{
    // First we start by looking at the request we have received
    // If this contains a language code, then we should be using that as the user has chosen to use that language explicitly
    // We assume that this language is supported
    if( preg_match( '/^([a-z][a-z](_[A-Z][A-Z])?)\//', $request, $result ) ) {
        // Then the user has specified a language - let's use that!
        return $result[1];
    }

    // Now that we know that the URL has not specified a language we can move on to looking at Accept-Language
    // First split the list up by the language separator
    $browser_requested_languages = explode( ",", $browser_languages );

    // Now go through each browser requested language in turn
    foreach( $browser_requested_languages as $language ) {
        // First as this might have a weighting value on it, we need to rip that off
        // Safest way to do this is just to split again by the appropriate separator for that
        $components = explode(";", $language);
        $language = $components[0];

        if( preg_match( '/^zh(-han[ts])?(-[a-z]{2})?$/i', $language, $result, PREG_UNMATCHED_AS_NULL ) ) {
            // Handle Chinese as a special case. Chinese lang tags may carry
            // a `Hant` or `Hans` script subtag, and/or a region subtag.
            // As long as a translation for `zh_HK` isn't available, this
            // matching is sufficient.
            if( strcasecmp($result[1], "-hant") === 0 ) {
                $language = "zh_TW";
            } else if( strcasecmp($result[1], "-hans") === 0 ) {
                $language = "zh_CN";
            } else if( strcasecmp($result[2], "-tw") === 0 || strcasecmp($result[2], "-hk") === 0 || strcasecmp($result[2], "-mo") === 0 ) {
                $language = "zh_TW";
            } else {
                // Note this also matches `zh` without script or region subtag.
                $language = "zh_CN";
            }
        } else {
            // Browsers use dashes to seperate language variants
            // But KDE translation systems use underscores for this so ensure we are consistent here
            $language = str_replace("-", "_", $language);
        }

        // Is this one of our supported languages?
        if( in_array($language, $supported_languages) ) {
            // Then we have a winner!
            return $language;
        }
    }

    // Finally if we found nothing we fallback to English
    return 'en';
}

// Start - Retrieve the values we need to work with here
$requested_url = $_SERVER['REQUEST_URI'];
$requested_languages = $_SERVER["HTTP_ACCEPT_LANGUAGE"];

// Before we can do anything else we need to clean up the URL we have received to remove the leading slash
$requested_url = substr($requested_url, 1);

// Now determine the language we should be sending the user to
$language = determine_appropriate_language( $requested_url, $requested_languages, $supported_languages );

// Split out the content part of the URL
// We will need this for the matching we are about to do above
if( !preg_match( '/^([a-z][a-z](_[A-Z][A-Z])?\/)?(.*)/', $requested_url, $result ) ) {
    // This shouldn't happen...
    // But in case it does, serve a 404 and bail
    http_response_code(404);
    include("../$language/404.html");
    exit();
}

// Save our result...
$requested_page = $result[3];

// First do a local check and see if $language/$requested_page exists..
// This allows for urls such as https://docs.krita.org/user_manual/getting_started/starting_krita.html to work
if( file_exists("../$language/$requested_page") ) {
    // Then redirect them there
    header("HTTP/1.1 301 Moved Permanently");
    header("Location: /$language/$requested_page");
    exit();
}

// Go across all of our redirect rules now and see if we have any matches
foreach( $redirect_rules as $rule => $replacement ) {
    // Try to match it...
    if( !preg_match( "/$rule/", $requested_page, $result ) ) {
        // Then we need to try another one...
        continue;
    }

    // We have a winner!
    // Perform the redirect
    header("HTTP/1.1 301 Moved Permanently"); 
    header("Location: /$language/$replacement"); 
    exit();
}

// Alas it looks like we have no match :(
// Send a 404
http_response_code(404);
include("../$language/404.html");
exit();

?>
