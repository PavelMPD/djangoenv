// создаем объект
var app = app || {};

$(function(){
//    var model = new NotebookRowModel()
//    var view = new NotebookRowView({
//        model: model,
//        el: '#notebook-container'
//    })
    app.notebookView = new NotebookView({
        el: '#notebook-container'
    })

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method))
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                csrftoken = $("input[name='csrfmiddlewaretoken']").val()
                console.log(csrftoken)
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    })
})
