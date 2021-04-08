---
permalink: /gallery
layout: default
title: Gallery
fulljQuery: true
headers: |
    <script src="https://unpkg.com/masonry-layout@4/dist/masonry.pkgd.min.js"></script>
    <script src="https://unpkg.com/imagesloaded@4/imagesloaded.pkgd.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.css" />
    <script src="https://cdn.jsdelivr.net/gh/fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.js"></script>
    <link rel="stylesheet" href="/assets/css/gallery.css" type="text/css">
description: The best place for Kei Karuizawa images found here. Includes official, edited official and fan artworks. Along with translated comics when available. Gallery is updated frequently when possible.
---
<section class="msetup mcontent" id="gallery-d">
    <div id="content" class="container-fluid">
        {% include gallery-official-component.html %}
        {% include gallery-ln-component.html %}
        {% include gallery-edits-component.html %}
        {% include gallery-comics-component.html %}
        {% include gallery-fanart-component.html %}
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