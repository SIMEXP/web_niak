<%inherit file="main_template.mako"/>

<header id="head" class="secondary"></header>
<!-- container -->
<div class="container">
    <ol class="breadcrumb">
        <li>
            <a href="${request.route_url('home')}">Home</a>
        </li>
        <li class="active">User access</li>
    </ol>
    <div class="row">
        <!-- Article main content -->
        <article class="col-xs-12 maincontent">
            <header class="page-header">
                <h1 class="page-title">Sign in</h1>
            </header>
            <div class="col-md-6 col-md-offset-3 col-sm-8 col-sm-offset-2">
                <div class="panel panel-default">
                    <div class="panel-body">
                        <h3 class="thin text-center">Sign in to your account</h3>
                        <p class="text-center text-muted">Lorem ipsum dolor sit amet, <a href="${request.route_url('simple_form')}">Register</a> adipisicing elit. Quo nulla quibusdam cum doloremque incidunt nemo sunt a tenetur omnis odio. </p>
                        <hr>

                        <div class="top-margin">
                            ${fig_form | n}
                        </div>
                        <hr>
                        </div>
                        ##${login_form | n}
                    </div>
                </div>
            </div>
        </article>
        <!-- /Article -->
    </div>
</div>
