$(function () {
        //создается объект
        var object = {};

        //_ - подчеркивание - это вызов библиотеки backbone
        //расширяем объект возможностями объекта Backbone.Events
        _.extend(object, Backbone.Events);

        //on - слушает события
        //слушается событие "alert" в контексте нашего объекта и вызывается функция function(msg)
        object.on("alert", function(msg) {
          alert("Triggered " + msg);
        });

        object.on("alert", function(msg) {
          console.log("Triggered " + msg);
        });

        //trigger - вызывает события
        object.trigger("alert", "my event");

        $('#simple-button').click(function(){
            object.trigger("alert", "Button click event");
        });
    }
);