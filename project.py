{% extends "admin/index.html" %}
{% block extrastyle %}
{{ block.super }}
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<style>
    #django-telegrambot ul li {
        list-style-type: none;
    }
    ul.nolist{
        margin-left: 10px;
        padding-left: 0;
    }
    .dodgerblue{
        color: dodgerblue;
    }
    .botlist{
        font-size: 1.5em;
    }
    #django-telegrambot li {font-size: 1.1em;}
</style>
{% endblock %}
{% block extrahead %}
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/1.6.1/clipboard.min.js"></script>

<script src="https://use.fontawesome.com/c8dc42a356.js"></script>
<script>
    $( document ).ready(function() {

        var clipboard = new Clipboard('.btn');
        clipboard.on('success', function(e) {
            e.clearSelection();
        });

        clipboard.on('error', function(e) {
            console.error('Action:', e.action);
            console.error('Trigger:', e.trigger);
        });
    });
</script>
{% endblock %}
{% block breadcrumbs %}
    <div class="breadcrumbs">
        <a href="{% url 'admin:index' %}">Home</a> &rsaquo;
        <a href="{% url 'django-telegrambot' %}">Django Telegrambot</a>
    </div>
{% endblock %}
{% block content %}


    {{ block.super }}
    <div id = 'django-telegrambot' style = "float: left">
    <h1><a href="https://github.com/JungDev/django-telegrambot#django-telegrambot">Django-TelegramBot</a></h1>
    <p>
    The full documentation is at <a href="https://django-telegrambot.readthedocs.org">https://django-telegrambot.readthedocs.org</a>.
    </p>
    <h3>Bot update mode: <b>{{update_mode}}</b></h3>
    {% if update_mode == 'POLLING' %}<p>Please remember to start polling mode with commands:
        <ul class="nolist">
            {% for bot in bot_list %}
            <li>
                <kbd>$ python manage.py botpolling --username={{bot.username}}</kbd>
                <button class="btn btn-default btn-xs" data-clipboard-text="python manage.py botpolling --username={{bot.username}}">
                    <i class="fa fa-clipboard" aria-hidden="true"></i>
                </button>
            </li>
            {% endfor %}
        </ul>
    </p>
    {% endif %}

    {% if bot_list %}
    <h3>Bot List:</h3>
        <ul class="nolist botlist">
            {% for bot in bot_list %}
            <i class="fa fa-telegram dodgerblue" aria-hidden="true"></i>
            <b>{{ bot.first_name}}</b>
            <a class="btn btn-default btn-sm" href="https://t.me/{{ bot.username }}/?start=true"  role="button" title="start a chat">@{{ bot.username}}</a>
            <a class="btn btn-default btn-sm" href="https://t.me/{{ bot.username }}/?startgroup=true" role="button">Add to group/channel</a></li>
            {% endfor %}
        </ul>
    {% else %}
    <p>No bots are available. Please <a href="https://github.com/JungDev/django-telegrambot#configure-your-installation">configure it</a> in settings.py</p>
    {% endif %}
    </div>

{% endblock %}