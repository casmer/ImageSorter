# ImageSorter
I have thousands of pictures on my One Drive account, and wanted to sort them. New images get sorted by Year and Month by the app these days, but the rest of my older pictures do not. So I wrote script based off of the the one i found here: https://github.com/vitords/sort-images 
I used the file names to sort if possible because it works faster as most of my files are on a NAS on my home network. I don't keep a full local copy on my laptop.
 - sorts images by year and month.
 - uses the file name if it can, falls back to exif data if possible.
 - Puts images with FB_IMG and not exif data in a seperate folder.
 - renames files that were download from internet and saved as .webp as jpeg

This could do a lot more, I just add to it as I use it.