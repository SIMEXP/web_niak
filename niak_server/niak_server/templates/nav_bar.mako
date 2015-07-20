<!-- Fixed navbar -->

<div class="navbar navbar-inverse navbar-fixed-top headroom">
    <div class="container">
        <div class="navbar-header">
            <!-- Button for smallest screens -->
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="${request.route_url('home')}">
                <img src="${request.static_url('niak_server:static/img/angelniak.png')}" alt="Progressus HTML5 template">
            </a>
        </div>
        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav pull-right">
                 %if request.matched_route.name=='home':
                    <li class="active">
                 %else:
                    <li>
                 %endif
                    <a href="${request.route_url('home')}">Home</a>
                 </li>


            </ul>
        </div>
        <!--/.nav-collapse -->
    </div>
</div>
<!-- /.navbar -->

<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
