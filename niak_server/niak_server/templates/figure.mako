<%inherit file="main_template.mako"/>
<header id="head" class="secondary"></header>


## <IMG SRC=${figure_path | n} ALT="HELLO" WIDTH=32 HEIGHT=32>
<IMG SRC="${figure_url}" ALT="Loaded File" >
## <IMG SRC="${request.static_url(figure_path)}" ALT="HELLO" >
