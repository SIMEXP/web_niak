<%inherit file="main_template.mako"/>

<header id="head" class="secondary"></header>
<!-- container -->
<div class="container">
    <ol class="breadcrumb">
        <li>
            <a href="${request.virtual_root}">Home</a>
        </li>
        <li class="active">User access</li>
    </ol>
    <div class="row">
        <!-- Article main content -->
        <article class="col-xs-12 maincontent">
            <header class="page-header">
                <h1 class="page-title">Inputs</h1>
            </header>
            <div class="col-md-6 col-md-offset-3 col-sm-8 col-sm-offset-2">
                <div class="panel panel-default">
                    <div class="panel-body">
                        <h3 class="thin text-center">Where are your data</h3>
                        <p class="text-center text-muted">Hello, you can <a href=${fig_form | n} >Start here</a>  </p>
                        <hr>

                        <div class="top-margin">
##                             ${fig_form | n}
##                             ${fig | n}
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
