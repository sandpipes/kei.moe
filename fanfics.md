---
permalink: /fanfics
layout: default
title: Fanfics
description: Kei's many fanfictions can be found here, written by Classroom of the Elite and Kei fans.
---
<section class="msetup mcontent">
    <div class="col fanfic-block">
        {% assign fanfics = site.data.fanfics | reverse %}
        {%- for item in fanfics -%}
        {%- if item.parts -%}
        <p style="margin-bottom: 0;">{{ item.name }} - {{ item.author }}</p>
        <ul>
            {%- for l in item.links-%}
            <li><a href="{{ l }}" class="ss-link">Part {{ forloop.index }}</a></li>
            {%- endfor -%}
        </ul>
        {%- elsif item.multiple -%}
        <p style="margin-bottom: 0;">{{ item.name }} - {{ item.author }}</p>
        <ul>
            {%- for l in item.links-%}
            <li><a href="{% if l.notExternal %}{{ site.url }}{% endif %}{{ l.link }}" class="ss-link">{{ l.name }}</a></li>
            {%- endfor -%}
        </ul>
        {%- else -%}
        <p><a href="{{ item.link }}" class="ss-link">{{ item.name }}</a> - {{ item.author }}</p>
        {%- endif -%}      
        {%- endfor -%}
        <br>
        <p>If you'd like a fanfic to be added here or if I'm missing some, contact me on discord!</p>
    </div>
</section>