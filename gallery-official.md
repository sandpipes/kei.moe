---
permalink: /gallery-official
layout: gallery
title: Official Artwork Gallery
description: Official Kei Karuizawa artwork found here.
---
<h1 class="title">Official Manga/Anime/Other Artwork</h1>
<div class="images-container">
    <div class="grid row center-block" id="officialRow">
    {%- for image in site.static_files -%}
    {%- if image.path contains "assets/images/gallery/official" -%}
        <div class="col-sm-3 grid-item">
            <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}{{ image.path }}'>Full Image</a>" href="{{ site.baseurl }}{{ image.path}}">
                <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/official/{{ image.basename | append: ".jpg" }}">
            </a>
        </div>
    {%- endif -%}
    {%- endfor -%}
    </div>
</div>