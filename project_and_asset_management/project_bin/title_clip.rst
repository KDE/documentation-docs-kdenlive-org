.. meta::
   :description: Kdenlive Documentation - Project Bin - Add Title Clip
   :keywords: KDE, Kdenlive, add clips, title clip, editing, timeline, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Gallaecio (https://userbase.kde.org/User:Gallaecio)
             - Simon Eugster <simon.eu@gmail.com>
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Carl Schwan <carl@carlschwan.eu>
             - Eugen Mohr
             - Tenzen (https://userbase.kde.org/User:Tenzen)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |grog| raw:: html

   <a href="https://discuss.kde.org/u/Grog" target="_blank">Grog</a>
     
.. |post| raw:: html

   <a href="https://discuss.kde.org/t/i-made-a-script-to-upgrade-subtitles-to-titles/21340" target="_blank">post</a>
     

Add Title Clip
==============

Right-click on empty space in the project bin, or click the |kdenlive-add-clip|\ |go-down|\ :guilabel:`Add Clip` icon on the project bin toolbar, and select :guilabel:`Add Title Clip`.

.. figure:: /images/project_and_asset_management/project_bin_add_title.webp
   :width: 206px
   :figwidth: 206px
   :align: left
   :alt: project_bin_add_title

   Adding a title clip

This opens the built-in Title Editor.

See :doc:`/titles_and_graphics/titles/titles` for more details.

.. rst-class:: clear-both

Here is a script courtesy of |grog| (see his |post| for more details and how to use it in Windows) that turns subtitles into titles that can be further edited in the Title Editor:

.. code-block:: bash
   :linenos:
   :emphasize-lines: 30, 34

   #!/bin/bash

   read -p "frame rate:"$'\n' frate
   [ "$frate" = "" ] && frate=60
   echo "..."

   [ -d ./Kden_Titles/ ] && rm -r ./Kden_Titles
   mkdir -p Kden_Titles

   readarray -t frm < <( (sed -n '2~4p' ./*.srt) )
   readarray -t sub < <( (sed -n '3~4p' ./*.srt) )

   n=1
   w=$(bc<<<"length(${#sub[@]}*2)")

   for i in "${!frm[@]}"; do
	
	   b=$(date -d "${frm[i]:0:12}" "+%S.%3N")
	   e=$(date -d "${frm[i]:17:12}" "+%S.%3N")
	   ee=$(date -d "${frm[i-1]:17:12}" "+%S.%3N")

	   if [ "$i" -eq 0 ]; then ee=0; fi
	   if [ "$(bc<<<"$b<$ee && $i!=0")" -eq 1 ]; then b="$(bc<<<"$b+60")"; fi
	   if [ "$(bc<<<"$e<$b")" -eq 1 ]; then e="$(bc<<<"$e+60")"; fi

	   blank="$(bc <<< "($b*$frate+0.5)/1-($ee*$frate+0.5)/1")"
	   duration="$(bc <<< "($e*$frate+0.5)/1-($b*$frate+0.5)/1")"

	   if [ "$blank" -gt 0 ]; then	
	   sed -e "s/30/$blank/" -e "s/%s//" ./*.kdenlivetitle* > ./Kden_Titles/"$(printf "%0*d" "$w" "$n")"_.kdenlivetitle
	   ((n++))
	   fi

	   sed -e "s/30/$duration/" -e "s/%s/${sub[i]}/" ./*.kdenlivetitle* > ./Kden_Titles/"$(printf "%0*d" "$w" "$n")".kdenlivetitle
	   ((n++))

   done

   sleep 1
   echo "Titles in $PWD/Kden_Titles"$'\n'
   touch ./Kden_Titles/*_*

   $SHELL

The highlighted lines point out the :code:`%s` variable (the same used as the standard placeholder for template titles). You can change that to anything you prefer, like :code:`placeholder`, for example.

Here is the same script but for Powershell in Windows (save it as :file:`.ps1`):

.. code-block:: powershell

   # Prompt for frame rate
   $frate = Read-Host "frame rate"
   if (-not $frate) { $frate = 60 }
   Write-Host "..."

   # Remove existing Kden_Titles directory if it exists
   if (Test-Path -Path "./Kden_Titles/") { Remove-Item -Path "./Kden_Titles/" -Recurse -Force }
   New-Item -ItemType Directory -Path "Kden_Titles"

   # Read frames and subtitles from SRT files
   $frm = Get-Content -Path '*.srt' | Select-Object -Skip 1 | ForEach-Object -Begin {$i=0} -Process {if ($i++ % 4 -eq 0) {$_}}
   $sub = Get-Content -Path '*.srt' | Select-Object -Skip 2 | ForEach-Object -Begin {$i=0} -Process {if ($i++ % 4 -eq 0) {$_}}
   # output File name width / counter
   $w = [math]::Ceiling($sub.Count * 2)
   $w = "$w".length
   $n = 1
   # Template file placeholders
   [regex] $p_1='30'
   [regex] $p_2='%s'

   for ($i = 0; $i -lt $frm.Count; $i++) {
       # Timing
      $b = [datetime]::ParseExact($frm[$i].Substring(0, 12), "hh:mm:ss,fff", $null).ToString("ss.fff")
      $e = [datetime]::ParseExact($frm[$i].Substring(17, 12), "hh:mm:ss,fff", $null).ToString("ss.fff")
      $ee = if ($i -gt 0) { [datetime]::ParseExact($frm[$i - 1].Substring(17, 12), "hh:mm:ss,fff", $null).ToString("ss.fff") } else { 0 }
      # Add 60s if necessary
      if ($i -eq 0) { $ee = 0 }
      if ($b -lt $ee -and $i -ne 0) { $b = [math]::Round([double]$b + 60, 3) }
      if ($e -lt $b) { $e = [math]::Round([double]$e + 60, 3) }
      # Clip length / padding
      $blank = [math]::Round([decimal]$b * $frate + 0.1) - [math]::Round([decimal]$ee * $frate + 0.1)
      $duration = [math]::Round([decimal]$e * $frate + 0.1) - [math]::Round([decimal]$b * $frate + 0.1)
      # Replace placeholders
      if ($blank -gt 0) {
         Get-Content -Path ./*.kdenlivetitle* |
	      ForEach-Object { $p_1.replace("$_", "$blank", 1) } | 
	      ForEach-Object { $p_2.replace("$_", '',1) } |
         Set-Content -Path "./Kden_Titles/$($n.ToString("D$w"))_.kdenlivetitle"
         $n++
      }
      Get-Content -Path ./*.kdenlivetitle* |
      ForEach-Object { $p_1.replace("$_", "$duration", 1) } |
      ForEach-Object { $p_2.replace("$_", $sub[$i],1) } | 
      Set-Content -Path "./Kden_Titles/$($n.ToString("D$w")).kdenlivetitle"
      $n++
   }

   Start-Sleep -Seconds 1
   Write-Host "`nTitles in $PWD\Kden_Titles`n"
   # Set date modified for blank clips
   (Get-ChildItem -Path ./Kden_Titles/*_*) | % {$_.LastWriteTime = (Get-Date)}