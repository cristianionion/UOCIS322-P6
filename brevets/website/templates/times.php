<!DOCTYPE html>
<html lang="en">
    <body>
        <h1> listALL times </h1>
        <ul>
            <?php
            $json = file_get_contents('http://'.$_ENV['BACKEND_ADDR'].':'.$_ENV['BACKEND_PORT'].'/listAll');
            $obj = json_decode($json);
            {% for i in range(info|length)%}
                <br>open time................{{info[i].open}}
                <br>close time...............{{info[i].close}}
                <br>
                <br>
            {% endfor %}
            ?>

        </ul>

        <h1> listALLcsv times </h1>
        <ul>
            <?php
            $json = file_get_contents('http://'.$_ENV['BACKEND_ADDR'].':'.$_ENV['BACKEND_PORT'].'/listAll/csv');
            $obj = json_decode($json);
            {% for i in range(info|length)%}
                <br>open time................{{info[i].open}}
                <br>close time...............{{info[i].close}}
                <br>
                <br>
            {% endfor %}
            ?>

        </ul>
 
    <h1> listOpen times </h1>
    <ul>
        <?php
        $json = file_get_contents('http://'.$_ENV['BACKEND_ADDR'].':'.$_ENV['BACKEND_PORT'].'/listOpen');
        $obj = json_decode($json);
        {% for i in range(info|length)%}
            <br>open time................{{info[i].open}}
            <br>
            <br>
        {% endfor %}
        ?>

    </ul>

    <h1> listOpencsv times </h1>
    <ul>
        <?php
        $json = file_get_contents('http://'.$_ENV['BACKEND_ADDR'].':'.$_ENV['BACKEND_PORT'].'/listOpen/csv');
        $obj = json_decode($json);
        {% for i in range(info|length)%}
            <br>open time................{{info[i].open}}
            <br>close time...............{{info[i].close}}
            <br>
            <br>
        {% endfor %}
        ?>

    </ul>

    <h1> listClose times </h1>
    <ul>
        <?php
        $json = file_get_contents('http://'.$_ENV['BACKEND_ADDR'].':'.$_ENV['BACKEND_PORT'].'/listClose');
        $obj = json_decode($json);
        {% for i in range(info|length)%}
            <br>open time................{{info[i].open}}
            <br>close time...............{{info[i].close}}
            <br>
            <br>
        {% endfor %}
        ?>

    </ul>

    <h1> listClosecsv times </h1>
    <ul>
        <?php
        $json = file_get_contents('http://'.$_ENV['BACKEND_ADDR'].':'.$_ENV['BACKEND_PORT'].'/listClose/csv');
        $obj = json_decode($json);
        {% for i in range(info|length)%}
            <br>open time................{{info[i].open}}
            <br>close time...............{{info[i].close}}
            <br>
            <br>
        {% endfor %}
        ?>

    </ul>
    </body>

</html>