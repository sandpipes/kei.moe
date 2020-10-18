---
permalink: /gallery-comics
layout: gallery
title: Comics Gallery
description: Translated comics featuring Kei Karuizawa found here.
---
<h1 class="title">Fan Comics</h1>
<p>Note: Comics with no name will have 🍆 as their titles.</p>
{% assign posted_fancomics = '' | split: '' %}
{%- for comic in site.data.fancomics -%}
<h4>{%- if comic.name == "" -%} 🍆 {%- else -%}{{ comic.name }}{%- endif -%}</h4>
{%- if comic.source -%}<h6><a href="{{ comic.source }}">Source</a></h6>{%- endif -%}
{%- if comic.translator -%}<h6>Translator: {{ comic.translator }}</h6>{%- endif -%}
{%- if comic.typesetter -%}<h6>Typesetter: {{ comic.typesetter }}</h6>{%- endif -%}
<div class="images-container">
    <div class="grid row center-block">
    {%- for image in comic.images -%}
        {% assign posted_fancomics = posted_fancomics | push: image %}
        {% assign imagepath = site.baseurl | append: "/assets/images/gallery/fancomics/" | append: image %}
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
            <a data-fancybox="gallery" data-caption="<a target='_blank' href='{{ site.baseurl }}{{ image.path }}'>Full Image</a>
            {% if has_source %} 
                {% if source.link %}
                        - <a target='_blank' href='{{ source.link }}'>Source</a>
                {% elsif source.artist %}
                        - {{ source.artist }}
                {% endif %}
                {% if source.edited %}
                    </br> Edited by: {{ source.edited }} 
                {% endif %}
            {% endif %}" href="{{ site.baseurl }}{{ image.path }}">
                <img class="pic" src="{{ site.baseurl }}/assets/images/gallery/thumbnails/fancomics/{{ image.basename | append: ".jpg" }}">
            </a>
        </div>
    {%- endif -%}
    {%- endfor -%}
    </div>
</div>
