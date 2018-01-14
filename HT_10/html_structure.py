# Generate html code with titles from DB
def generate_html_code(category_1, category_2, category_3, category_4):
    html_file = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Hometask - 91</title>
        <link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
        <script src="http://code.jquery.com/jquery-latest.js"></script>
        <script src="js/bootstrap.min.js"></script>

        <style>
        body {
            background-color: #1D1D1D;
            padding: 30px;
            margin: 0px;
        }
        #snowflakeContainer {
            position: absolute;
            left: 0px;
            top: 0px;
        }
        .snowflake {
            padding-left: 15px;
            font-family: Cambria, Georgia, serif;
            font-size: 14px;
            line-height: 24px;
            position: fixed;
            color: #FFFFFF;
            user-select: none;
            z-index: 1000;
        }
        .snowflake:hover {
            cursor: default;
        }
        </style>

    </head>
    <body>
    <div id="snowflakeContainer">
        <p class="snowflake">*</p>
    </div>
    <h1 style="text-align: center; color: gray;">GeekHub Python Hometask 9</h1>
    <div class="panel-group" id="collapse-group" style="
        padding: 10px;">
     <div class="panel panel-default">
     <div class="panel-heading">
     <h4 class="panel-title">
     <a data-toggle="collapse" data-parent="#collapse-group" href="#el1">Ask Stories</a>
     </h4>
     </div>
     <div id="el1" class="panel-collapse collapse in">
     <div class="panel-body">''' + category_1 + '''</div>
     </div>
     </div>

     <div class="panel panel-default">
     <div class="panel-heading">
     <h4 class="panel-title">
     <a data-toggle="collapse" data-parent="#collapse-group" href="#el2">Show Stories</a>
     </h4>
     </div>
     <div id="el2" class="panel-collapse collapse">
     <div class="panel-body">''' + category_2 + '''</div>
     </div>
     </div>

     <div class="panel panel-default">
     <div class="panel-heading">
     <h4 class="panel-title">
     <a data-toggle="collapse" data-parent="#collapse-group" href="#el3">New Stories</a>
     </h4>
     </div>
     <div id="el3" class="panel-collapse collapse">
     <div class="panel-body">''' + category_3 + '''</div>
     </div>
     </div>

     <div class="panel panel-default">
     <div class="panel-heading">
     <h4 class="panel-title">
     <a data-toggle="collapse" data-parent="#collapse-group" href="#el4">Job Stories</a>
     </h4>
     </div>
     <div id="el4" class="panel-collapse collapse">
     <div class="panel-body">''' + category_4 + '''</div>
     </div>
     </div>

    </div>
    <script src="js/fallingsnow_v6.js"></script>
    <script src="js/prefixfree.min.js"></script>
    </body>
    '''

    return html_file