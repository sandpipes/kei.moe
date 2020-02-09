---
layout: default
title: Fanfics
---
<section class="msetup mcontent">
    <div class="col">
        {%- for item in site.data.fanfics -%}
        <p><a href="{{ item.link }}" class="ss-link">{{ item.name }}</a></p>        
        {% endfor %}
        <br>
        <p>If you'd like a fanfic to be added here, contact me on discord!</p>
    </div>
</section>