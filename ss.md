---
permalink: /ss
layout: default
title: Short Stories
---
<section class="msetup mcontent">
    <div class="col">
        {% for item in site.data.shortstories %}
        <p><a href="{{ item.link }}" class="ss-link">{{ item.name }}</a></p>
        {% endfor %}
    </div>
</section>