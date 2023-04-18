---
permalink: /scenes
layout: default
title: Scenes
description: Kei's scenes in the light novel can be found here.
---
<section class="mainContent">
    <div class="col pad-bottom">
        {% for item in site.data.scenes %}
        <p class="h6">{{ item.name }}</p>
        <ul class="square">
            {% for s in item.chapters %}
            <li><a href="{%- if s.rehosted -%}{{ s.link }}{%- else -%}{{ s.link }}{%- endif -%}" class="ss-link">{{ s.name }}</a></li>
            {% endfor %}
        </ul>
        {% endfor %}
    </div>
</section>