---
permalink: /ss
layout: default
title: Short Stories
description: Classroom of the Elite features many short stories featuring the POVs of many different characters. Here is the collection of Kei Short Stories.
---
<section class="msetup mcontent">
    <div class="col pad-bottom">
        {% for item in site.data.shortstories %}
        <p class="h6">{{ item.name }}</p>
        <ul class="square">
            {% for s in item.stories %}
            <li><a href="{%- if s.rehosted -%}{{ site.url }}{{ s.link }}{%- else -%}{{ s.link }}{%- endif -%}" class="ss-link">{{ s.name }}</a></li>
            {% endfor %}
        </ul>
        {% endfor %}
    </div>
</section>