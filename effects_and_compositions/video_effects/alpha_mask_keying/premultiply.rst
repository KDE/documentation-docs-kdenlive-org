.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan

   :license: Creative Commons License SA 4.0


.. |alpha_blending| raw:: html

   <a href="https://developer.nvidia.com/content/alpha-blending-pre-or-not-pre" target="_blank">Alpha Blending</a>


.. _effects-premultiply:

Premultiply or Unpremultiply
----------------------------

Multiply (or divide) each color component by the pixel's alpha value (frei0r.premultiply).

Use this effect before any alpha effects if the result of your compositions using alpha has odd-looking colors.

For more details see this article by Nvidia about |alpha_blending|.
