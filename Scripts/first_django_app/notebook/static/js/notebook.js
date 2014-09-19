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
})
