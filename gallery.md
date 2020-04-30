---
layout: default
title: Gallery
---
<section class="msetup mcontent" id="gallery-d">
    <div id="content" class="container-fluid">
        <h3>Official LN/Manga/Anime Artwork</h3>
        <div class="images-container">
            <div class="grid row center-block" id="officialRow">
            {%- for image in site.static_files -%}
            {%- if image.path contains "assets/images/gallery/official" -%}
                <div class="col-sm-3 grid-item">
                    <a data-fancybox="gallery" href="{{ site.baseurl }}{{ image.path}}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/official/{{ image.name | replace: ".png", ".jpg" }}">
                    </a>
                </div>
            {%- endif -%}
            {%- endfor -%}
            </div>
        </div>
        <h3>Edited Official LN/Manga/Anime Artwork</h3>
        <div class="images-container">
            <div class="grid row center-block" id="officialRow">
            {%- for image in site.static_files -%}
            {%- if image.path contains "assets/images/gallery/edits" -%}
                <div class="col-sm-3 grid-item">
                    <a data-fancybox="gallery" href="{{ site.baseurl }}{{ image.path}}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/edits/{{ image.name | replace: ".png", ".jpg" }}">
                    </a>
                </div>
            {%- endif -%}
            {%- endfor -%}
            </div>
        </div>
        <h3>Fanart</h3>
        <div class="images-container">
            <div class="grid row center-block" id="fanartRow">
            {%- for image in site.static_files -%}
            {%- if image.path contains "assets/images/gallery/fanart" -%}
                {%- assign has_source = false -%}
                {%- assign source = image -%}
                {%- for s in site.data.fanart_sources -%}
                    {%- if image.path contains s.name -%}
                        {%- assign source = s -%}
                        {%- assign has_source = true -%}
                    {%- endif -%}
                {%- endfor -%}
                <div class="col-sm-3 grid-item">
                    {%- if has_source -%}
                    <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ source.link }}'>Source</a>" href="{{ site.baseurl }}{{ image.path }}">
                    {% else %}
                    <a data-fancybox="gallery" href="{{ site.baseurl }}{{ image.path }}">
                    {%- endif -%}
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/fanart/{{ image.name | replace: ".png", ".jpg" }}">
                    </a>
                </div>
            {%- endif -%}
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