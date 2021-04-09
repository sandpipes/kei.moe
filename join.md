---
permalink: /join
layout: default
title: "Join Us"
fulljQuery: true
headers: |
    <script src="https://unpkg.com/masonry-layout@4/dist/masonry.pkgd.min.js"></script>
    <script src="https://unpkg.com/imagesloaded@4/imagesloaded.pkgd.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.css" />
    <script src="https://cdn.jsdelivr.net/gh/fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.js"></script>
    <link rel="stylesheet" href="/assets/css/join.css" type="text/css">
description: Karuizawa Kei banners found here.
---
<section class="mainContent">
    <div class="col text-center justify-content-center">
        <a href="https://discord.com/invite/R38FNs6">
            <img class="discord" src="{{ site.url }}/assets/images/notkei/f5uq0NV_1.png">
        </a>
        <p>Click the images for higher quality!</p>
    </div>
    <div id="content" class="container-fluid">
        <div class="images-container">
            <div class="grid row center-block">
            {%- for image in site.data.banners -%}
                <div class="col-sm-6 grid-item">
                    <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}/assets/images/gallery/{{ image.path }}'>Full Image</a>" href="{{ site.baseurl }}/assets/images/gallery/{{ image.path }}{{ image.name }}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/{{ image.path }}{{ image.name | replace: ".png", ".jpg" }}">
                    </a>
                </div>
            {%- endfor -%}
            </div>
        </div>
    </div>
</section>
<script>
$('.images-container').each( function(i, elem) {
    var $elem = $(elem);
    $elem.imagesLoaded( function() {
        $elem.masonry({
            itemSelector: '.grid-item'
        });
        $elem.fadeTo(200, 1);
        $('.grid-item .pic', $elem).each(function(n, img) {
            if (!img.complete) {
                $(img).on('load', function() {
                    $(img).fadeTo(300,1);
                });
            } else {
                $(img).fadeTo(300,1);
            }
        });

    });
});
</script>