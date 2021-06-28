---
permalink: /scenes
layout: default
title: Scenes
description: Kei's many fanfictions can be found here, written by Classroom of the Elite and Kei fans.
---
<section class="mainContent">
    <div class="col pad-bottom">
        {% for item in site.data.scenes %}
        <p class="h6">{{ item.name }}</p>
        <ul class="square">
            {% for s in item.chapters %}
            <li><a href="{%- if s.rehosted -%}{{ site.url }}{{ s.link }}{%- else -%}{{ s.link }}{%- endif -%}" class="ss-link">{{ s.name }}</a></li>
            {% endfor %}
        </ul>
        {% endfor %}
    </div>
</section>