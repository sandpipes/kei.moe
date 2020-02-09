---
layout: default
title: Gallery
---
<section class="msetup mcontent" id="gallery-d">
    <div class="container-fluid">
        <h3>Official LN/Manga/Anime Artwork</h3>
        <div class="row gallery-row" id="fanartRow"> 
            {%- assign image_array = "" | split: ',' -%}
            {%- for image in site.static_files -%}
                {%- if image.path contains "assets/images/gallery/official" -%}
                    {%- assign image_array = image_array | push: image -%}
                {%- endif -%}
            {%- endfor -%}
            {%- assign each_length = image_array.size | divided_by: 4 -%}
            {%- assign mod = image_array.size | modulo: 4 -%}
            {%- assign first_col_limit = each_length -%}
            {%- assign second_col_limit = each_length -%}
            {%- assign third_col_limit = each_length -%}
            {%- if mod == 1 -%} 
                {%- assign first_col_limit = first_col_limit | plus: 1 -%}
            {%- endif -%}
            {%- if mod == 2 -%} 
                {%- assign first_col_limit = first_col_limit | plus: 1 -%}
                {%- assign second_col_limit = each_length | plus: 1 -%}
            {%- endif -%}
            {%- if mod == 3 -%}
                {%- assign first_col_limit = first_col_limit | plus: 1 -%}
                {%- assign second_col_limit = each_length | plus: 1 -%}
                {%- assign third_col_limit = each_length | plus: 1 -%}
            {%- endif -%}
            {%- assign offset_index = 0 -%}
            <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">
                {%- for image in image_array limit: first_col_limit -%}
                <img data-src="{{ site.baseurl }}{{ image.path }}" class="img-fluid img-gal"/>
                {%- assign offset_index = offset_index | plus: 1 -%}
                {%- endfor -%}
            </div>
            <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">
                {%- for image in image_array limit: second_col_limit offset: offset_index -%}
                <img data-src="{{ site.baseurl }}{{ image.path }}" class="img-fluid img-gal"/>
                {%- assign offset_index = offset_index | plus: 1 -%}
                {%- endfor -%}
            </div>
            <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">
                {%- for image in image_array limit: third_col_limit offset: offset_index -%}
                <img data-src="{{ site.baseurl }}{{ image.path }}" class="img-fluid img-gal"/>
                {%- assign offset_index = offset_index | plus: 1 -%}
                {%- endfor -%}
            </div>
            <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">
                {%- for image in image_array offset: offset_index -%}
                <img data-src="{{ site.baseurl }}{{ image.path }}" class="img-fluid img-gal"/>
                {%- assign offset_index = offset_index | plus: 1 -%}
                {%- endfor -%}
            </div>
        </div>
        <h3>Fanart</h3>
        <div class="row gallery-row" id="fanartRow"> 
            {%- assign image_array = "" | split: ',' -%}
            {%- for image in site.static_files -%}
                {%- if image.path contains "assets/images/gallery/fanart" -%}
                    {%- assign image_array = image_array | push: image -%}
                {%- endif -%}
            {%- endfor -%}
            {%- assign each_length = image_array.size | divided_by: 4 -%}
            {%- assign mod = image_array.size | modulo: 4 -%}
            {%- assign first_col_limit = each_length -%}
            {%- assign second_col_limit = each_length -%}
            {%- assign third_col_limit = each_length -%}
            {%- if mod == 1 -%} 
                {%- assign first_col_limit = first_col_limit | plus: 1 -%}
            {%- endif -%}
            {%- if mod == 2 -%} 
                {%- assign first_col_limit = first_col_limit | plus: 1 -%}
                {%- assign second_col_limit = each_length | plus: 1 -%}
            {%- endif -%}
            {%- if mod == 3 -%}
                {%- assign first_col_limit = first_col_limit | plus: 1 -%}
                {%- assign second_col_limit = each_length | plus: 1 -%}
                {%- assign third_col_limit = each_length | plus: 1 -%}
            {%- endif -%}
            {%- assign offset_index = 0 -%}
            <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">
                {%- for image in image_array limit: first_col_limit -%}
                {%- assign has_source = false -%}
                {%- assign source = image -%}
                {%- for s in site.data.fanart_sources -%}
                    {%- if image.path contains s.name -%}
                        {%- assign source = s -%}
                        {%- assign has_source = true -%}
                    {%- endif -%}
                {%- endfor -%}
                {%- if has_source -%}
                <a href="{{ source.link }}" target="_blank">
                {%- endif -%}
                <img data-src="{{ site.baseurl }}{{ image.path }}" class="img-fluid img-gal"/>
                {%- if has_source -%}
                </a>
                {%- endif -%}
                {%- assign offset_index = offset_index | plus: 1 -%}
                {%- endfor -%}
            </div>
            <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">
                {%- for image in image_array limit: second_col_limit offset: offset_index -%}
                {%- assign has_source = false -%}
                {%- assign source = image -%}
                {%- for s in site.data.fanart_sources -%}
                    {%- if image.path contains s.name -%}
                        {%- assign source = s -%}
                        {%- assign has_source = true -%}
                    {%- endif -%}
                {%- endfor -%}
                {%- if has_source -%}
                <a href="{{ source.link }}" target="_blank">
                {%- endif -%}
                <img data-src="{{ site.baseurl }}{{ image.path }}" class="img-fluid img-gal"/>
                {%- if has_source -%}
                </a>
                {%- endif -%}
                {%- assign offset_index = offset_index | plus: 1 -%}
                {%- endfor -%}
            </div>
            <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">
                {%- for image in image_array limit: third_col_limit offset: offset_index -%}
                {%- assign has_source = false -%}
                {%- assign source = image -%}
                {%- for s in site.data.fanart_sources -%}
                    {%- if image.path contains s.name -%}
                        {%- assign source = s -%}
                        {%- assign has_source = true -%}
                    {%- endif -%}
                {%- endfor -%}
                {%- if has_source -%}
                <a href="{{ source.link }}" target="_blank">
                {%- endif -%}
                <img data-src="{{ site.baseurl }}{{ image.path }}" class="img-fluid img-gal"/>
                {%- if has_source -%}
                </a>
                {%- endif -%}
                {%- assign offset_index = offset_index | plus: 1 -%}
                {%- endfor -%}
            </div>
            <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">
                {%- for image in image_array offset: offset_index -%}
                {%- assign has_source = false -%}
                {%- assign source = image -%}
                {%- for s in site.data.fanart_sources -%}
                    {%- if image.path contains s.name -%}
                        {%- assign source = s -%}
                        {%- assign has_source = true -%}
                    {%- endif -%}
                {%- endfor -%}
                {%- if has_source -%}
                <a href="{{ source.link }}" target="_blank">
                {%- endif -%}
                <img data-src="{{ site.baseurl }}{{ image.path }}" class="img-fluid img-gal"/>
                {%- if has_source -%}
                </a>
                {%- endif -%}
                {%- assign offset_index = offset_index | plus: 1 -%}
                {%- endfor -%}
            </div>
        </div>
    </div>
</section>
<script>
var lazyLoadInstance = new LazyLoad({
    container: document.getElementById('gallery-d')
});
</script>