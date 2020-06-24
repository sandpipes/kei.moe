---
layout: default
title: Gallery
---
<section class="msetup mcontent" id="gallery-d">
    <div id="content" class="container-fluid">
        <h3>Official Manga/Anime/Other Artwork</h3>
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
        <h3>Official Light Novel Illustrations</h3>
        <h4>Volume 2</h4>
        <div class="images-container">
            <div class="grid row center-block" id="officialRow">
            {%- for image in site.static_files -%}
            {%- if image.path contains "assets/images/gallery/LN_v2" -%}
                <div class="col-sm-3 grid-item">
                    <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}{{ image.path }}'>Full Image</a>" href="{{ site.baseurl }}{{ image.path}}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/LN_v2/{{ image.basename | append: ".jpg" }}">
                    </a>
                </div>
            {%- endif -%}
            {%- endfor -%}
            </div>
        </div>
        <h4>Volume 4</h4>
        <div class="images-container">
            <div class="grid row center-block" id="officialRow">
            {%- for image in site.static_files -%}
            {%- if image.path contains "assets/images/gallery/LN_v4.0" -%}
                <div class="col-sm-3 grid-item">
                    <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}{{ image.path }}'>Full Image</a>" href="{{ site.baseurl }}{{ image.path}}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/LN_v4.0/{{ image.basename | append: ".jpg" }}">
                    </a>
                </div>
            {%- endif -%}
            {%- endfor -%}
            </div>
        </div>
        <h4>Volume 4.5</h4>
        <div class="images-container">
            <div class="grid row center-block" id="officialRow">
            {%- for image in site.static_files -%}
            {%- if image.path contains "assets/images/gallery/LN_v4.5" -%}
                <div class="col-sm-3 grid-item">
                    <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}{{ image.path }}'>Full Image</a>" href="{{ site.baseurl }}{{ image.path}}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/LN_v4.5/{{ image.basename | append: ".jpg" }}">
                    </a>
                </div>
            {%- endif -%}
            {%- endfor -%}
            </div>
        </div>
        <h4>Volume 5</h4>
        <div class="images-container">
            <div class="grid row center-block" id="officialRow">
            {%- for image in site.static_files -%}
            {%- if image.path contains "assets/images/gallery/LN_v5" -%}
                <div class="col-sm-3 grid-item">
                    <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}{{ image.path }}'>Full Image</a>" href="{{ site.baseurl }}{{ image.path}}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/LN_v5/{{ image.basename | append: ".jpg" }}">
                    </a>
                </div>
            {%- endif -%}
            {%- endfor -%}
            </div>
        </div>
        <h4>Volume 6</h4>
        <div class="images-container">
            <div class="grid row center-block" id="officialRow">
            {%- for image in site.static_files -%}
            {%- if image.path contains "assets/images/gallery/LN_v6" -%}
                <div class="col-sm-3 grid-item">
                    <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}{{ image.path }}'>Full Image</a>" href="{{ site.baseurl }}{{ image.path}}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/LN_v6/{{ image.basename | append: ".jpg" }}">
                    </a>
                </div>
            {%- endif -%}
            {%- endfor -%}
            </div>
        </div>
        <h4>Volume 7</h4>
        <div class="images-container">
            <div class="grid row center-block" id="officialRow">
            {%- for image in site.static_files -%}
            {%- if image.path contains "assets/images/gallery/LN_v7.0" -%}
                <div class="col-sm-3 grid-item">
                    <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}{{ image.path }}'>Full Image</a>" href="{{ site.baseurl }}{{ image.path}}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/LN_v7.0/{{ image.basename | append: ".jpg" }}">
                    </a>
                </div>
            {%- endif -%}
            {%- endfor -%}
            </div>
        </div>
        <h4>Volume 7.5</h4>
        <div class="images-container">
            <div class="grid row center-block" id="officialRow">
            {%- for image in site.static_files -%}
            {%- if image.path contains "assets/images/gallery/LN_v7.5" -%}
                <div class="col-sm-3 grid-item">
                    <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}{{ image.path }}'>Full Image</a>" href="{{ site.baseurl }}{{ image.path}}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/LN_v7.5/{{ image.basename | append: ".jpg" }}">
                    </a>
                </div>
            {%- endif -%}
            {%- endfor -%}
            </div>
        </div>
        <h4>Volume 8</h4>
        <div class="images-container">
            <div class="grid row center-block" id="officialRow">
            {%- for image in site.static_files -%}
            {%- if image.path contains "assets/images/gallery/LN_v8" -%}
                <div class="col-sm-3 grid-item">
                    <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}{{ image.path }}'>Full Image</a>" href="{{ site.baseurl }}{{ image.path}}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/LN_v8/{{ image.basename | append: ".jpg" }}">
                    </a>
                </div>
            {%- endif -%}
            {%- endfor -%}
            </div>
        </div>
        <h4>Volume 9</h4>
        <div class="images-container">
            <div class="grid row center-block" id="officialRow">
            {%- for image in site.static_files -%}
            {%- if image.path contains "assets/images/gallery/LN_v9" -%}
                <div class="col-sm-3 grid-item">
                    <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}{{ image.path }}'>Full Image</a>" href="{{ site.baseurl }}{{ image.path}}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/LN_v9/{{ image.basename | append: ".jpg" }}">
                    </a>
                </div>
            {%- endif -%}
            {%- endfor -%}
            </div>
        </div>
        <h4>Volume 11</h4>
        <div class="images-container">
            <div class="grid row center-block" id="officialRow">
            {%- for image in site.static_files -%}
            {%- if image.path contains "assets/images/gallery/LN_v11.0" -%}
                <div class="col-sm-3 grid-item">
                    <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}{{ image.path }}'>Full Image</a>" href="{{ site.baseurl }}{{ image.path}}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/LN_v11.0/{{ image.basename | append: ".jpg" }}">
                    </a>
                </div>
            {%- endif -%}
            {%- endfor -%}
            </div>
        </div>
        <h4>Volume 11.5</h4>
        <div class="images-container">
            <div class="grid row center-block" id="officialRow">
            {%- for image in site.static_files -%}
            {%- if image.path contains "assets/images/gallery/LN_v11.5" -%}
                <div class="col-sm-3 grid-item">
                    <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}{{ image.path }}'>Full Image</a>" href="{{ site.baseurl }}{{ image.path}}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/LN_v11.5/{{ image.basename | append: ".jpg" }}">
                    </a>
                </div>
            {%- endif -%}
            {%- endfor -%}
            </div>
        </div>
        <h4>Volume 11.75</h4>
        <div class="images-container">
            <div class="grid row center-block" id="officialRow">
            {%- for image in site.static_files -%}
            {%- if image.path contains "assets/images/gallery/LN_v11.75" -%}
                <div class="col-sm-3 grid-item">
                    <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}{{ image.path }}'>Full Image</a>" href="{{ site.baseurl }}{{ image.path}}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/LN_v11.75/{{ image.basename | append: ".jpg" }}">
                    </a>
                </div>
            {%- endif -%}
            {%- endfor -%}
            </div>
        </div>
        <h4>Volume 12 (2nd Year, Vol. 1)</h4>
        <div class="images-container">
            <div class="grid row center-block" id="officialRow">
            {%- for image in site.static_files -%}
            {%- if image.path contains "assets/images/gallery/LN_v12" -%}
                <div class="col-sm-3 grid-item">
                    <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}{{ image.path }}'>Full Image</a>" href="{{ site.baseurl }}{{ image.path}}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/LN_v12/{{ image.basename | append: ".jpg" }}">
                    </a>
                </div>
            {%- endif -%}
            {%- endfor -%}
            </div>
        </div>
        <h3>Edited Official LN/Manga/Anime Artwork</h3>
        <div class="images-container">
            <div class="grid row center-block" id="editsRow">
            {%- for image in site.static_files -%}
            {%- if image.path contains "assets/images/gallery/edits" -%}
                {%- assign has_source = false -%}
                {%- assign source = image -%}
                {%- for s in site.data.edits_sources -%}
                    {%- if image.path contains s.name -%}
                        {%- assign source = s -%}
                        {%- assign has_source = true -%}
                    {%- endif -%}
                {%- endfor -%}
                <div class="col-sm-3 grid-item">
                    <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}{{ image.path }}'>Full Image</a>{% if has_source %} {% if source.edited %} </br> Edited by: {{ source.edited }} {% else %} - <a target='_blank' href='{{ source.link }}'>Source</a>{% endif %}{% endif %}" href="{{ site.baseurl }}{{ image.path }}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/edits/{{ image.basename | append: ".jpg" }}">
                    </a>
                </div>
            {%- endif -%}
            {%- endfor -%}
            </div>
        </div>
        <h3>Fan Comics</h3>
        {% assign posted_fancomics = '' | split: '' %}
        {%- for comic in site.data.fancomics -%}
        <h4>{%- if comic.name == "" -%} 🍆 {%- else -%} "{{ comic.name }}" {%- endif -%}</h4>
        <div class="images-container">
            <div class="grid row center-block">
            {%- for image in comic.images -%}
                {% assign posted_fancomics = posted_fancomics | concat: image %}
                {% assign imagepath = site.baseurl | append: "/assets/images/gallery/thumbnails/fancomics/" | append: image %}
                {% assign size = image | size | minus: 4 %}
                <div class="col-sm-3 grid-item">
                    <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ imagepath }}'>Full Image</a>{% if comic.source %} - <a target='_blank' href='{{ comic.source }}'>Source</a>{% endif %}" href="{{ imagepath }}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/fancomics/{{ image | slice: 0, size | append: ".jpg" }}">
                    </a>
                </div>
            {%- endfor -%}
            </div>
        </div>
        {%- endfor -%}
        <h4>One Page Comics</h4>
        <div class="images-container">
            <div class="grid row center-block" id="comicsRow">
            {%- for image in site.static_files -%}
            {%- if image.path contains "assets/images/gallery/fancomics" -%}
                {% if posted_fancomics contains image.name %}
                    {% continue %}
                {% endif %}
                {%- assign has_source = false -%}
                {%- assign source = image -%}
                {%- for s in site.data.fancomics_sources -%}
                    {%- if image.path contains s.name -%}
                        {%- assign source = s -%}
                        {%- assign has_source = true -%}
                    {%- endif -%}
                {%- endfor -%}
                <div class="col-sm-3 grid-item">
                    <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}{{ image.path }}'>Full Image</a>{% if has_source %} {% if source.edited %} </br> Edited by: {{ source.edited }} {% else %} - <a target='_blank' href='{{ source.link }}'>Source</a>{% endif %}{% endif %}" href="{{ site.baseurl }}{{ image.path }}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/fancomics/{{ image.basename | append: ".jpg" }}">
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
                    <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}{{ image.path }}'>Full Image</a>{%- if has_source -%}
                    {%- if source.artist -%}
                            </br> {{ source.artist }}
                    {% else %} - <a target='_blank' href='{{ source.link }}'>Source</a>{%- if source.edited -%}</br> Edited by: {{ source.edited }}{%- endif -%}
                    {%- endif -%}{%- endif -%}" href="{{ site.baseurl }}{{ image.path }}">
                        <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/fanart/{% if image.extname == ".png" %}{{ image.basename | append: ".jpg" }}{% else %}{{ image.name }}{% endif %}">
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