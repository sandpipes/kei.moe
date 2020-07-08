---
permalink: /ss
layout: default
title: Short Stories
description: Classroom of the Elite features many short stories featuring the POVs of many different characters. Here is the collection of Kei Short Stories.
---
<section class="msetup mcontent">
    <div class="col">
        {% for item in site.data.shortstories %}
        <p><a href="{{ item.link }}" class="ss-link">{{ item.name }}</a></p>
        {% endfor %}
    </div>
</section>