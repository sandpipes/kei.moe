---
permalink: /join
layout: gallery
title: "Join Us"
description: Karuizawa Kei banners found here.
---
<section class="mainContent join-page">
    <div class="col text-center justify-content-center">
        <a href="https://discord.gg/xudkGPVAss">
            <img class="discord" src="{{ site.url }}/assets/images/notkei/f5uq0NV_1.png">
        </a>
        <p class="join-page">Click the images for higher quality!</p>
    </div>
    <div id="content" class="container-fluid">
        <div class="images-container">
            <div class="grid row center-block">
            {%- for image in site.data.banners -%}
                <div class="col-sm-6 grid-item">
                    <div class="shadow mr-2 mb-2 rounded paperImage">
                        <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}/assets/images/gallery/{{ image.path }}'>Full Image</a>" href="{{ site.baseurl }}/assets/images/gallery/{{ image.path }}{{ image.name }}">
                            <img class="pic lazyload" data-src="{{ site.baseurl }}/assets/images/gallery/thumbnails/{{ image.path }}{{ image.name | replace: ".png", ".jpg" }}">
                        </a>
                    </div>
                </div>
            {%- endfor -%}
            </div>
        </div>
    </div>
</section>