---
permalink: /gallery-edits
layout: gallery
title: Edited Artwork Gallery
description: Official Artwork of Kei Karuizawa that have been edited by the members of Kei Camp can be found here.
---
<h1 class="title">Edited Official LN/Manga/Anime Artwork</h1>
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
            <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}{{ image.path }}'>Full Image</a>
            {%- if has_source -%}
                {%- if source.artist -%}
                    </br> {{ source.artist }}
                {% elsif source.sources %}
                    - Sources: {% for src in source.sources %} <a target='_blank' href='{{ src }}'>{{ forloop.index }}</a>{% endfor %}
                {% elsif source.link %}
                    - <a target='_blank' href='{{ source.link }}'>Source</a>
                {%- endif -%}
                {%- if source.edited -%}
                    </br> Edited by: {{ source.edited }}
                {%- endif -%}
            {%- endif -%}" href="{{ site.baseurl }}{{ image.path }}">
                <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/edits/{% if image.extname == ".png" or image.extname == ".gif" %}{{ image.basename | append: ".jpg" }}{% else %}{{ image.name }}{% endif %}">
            </a>
        </div>
    {%- endif -%}
    {%- endfor -%}
    {%- for vid in site.data.edits_sources -%}
    {%- if vid.externalVid -%}
        <div class="col-sm-3 grid-item">
            <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ vid.ytlink }}'>Direct Link</a>
            {%- if vid.artist -%}
                </br> {{ source.artist }}
            {% elsif vid.link %}
                - <a target='_blank' href='{{ source.link }}'>Source</a>
            {%- endif -%}
            {%- if vid.edited -%}
                </br> Edited by: {{ vid.edited }}
            {%- endif -%}
            " href="{{ vid.ytlink }}">
                <img class="pic" src="{{ vid.thumbnail }}">
            </a>
        </div>
    {%- endif -%}
    {%- endfor -%}
    </div>
</div>
