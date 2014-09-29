//создание объекта для работы во всем приложении
var app = {}

$(function () {
    //расширяю класс моделью mybackbone
    app.MyObject = Backbone.Model.extend({
        //параметры по умолчанию
        defaults: {
            name: 'name',
            description: '-',
            size: 10
        },
        //функция инициализации, вызывается после создания объекта
        initialize: function() {
            console.log('Object created')
            //добавляем прослушивание события изменения объекта
            this.on('change', function(){
                console.log('Object changed')
                //преобразую объект mybackbone в JSON объект JS
                var json = app.myObject.toJSON()
                console.log(json)
                //возвращает json объект, который содержит только измеившуюся часть объекта
                json = app.myObject.changedAttributes()
                console.log(json)
            })
        },
        //добавляем функцию валидации свойств объекта
        validate: function(attributes){
            if (attributes.size > 40){
                console.log('Incorrect size')
                return 'Incorrect size'
            }
        },
        //добавление своей функции
        increase_size: function(){
                app.myObject.set({
                    size: this.get('size') + 10
                },{//в сетторе указываем, что нужно выполнять валидацию
                    validate: true
                })
        }
    })

    //создаю объект и заполняю список свойств
    app.myObject = new app.MyObject({
        name: 'new object',
        description: 'new object for test'
    })

    //преобразую объект mybackbone в JSON объект JS
    var json = app.myObject.toJSON()
    console.log(json)

    //изменение атрибутов объекта
    app.myObject.set({
        //изменение значения существующего атрибута
        size: 25,
        //добавление нового атрибута
        length: 33
    })

    //получение атрибутов
    console.log(app.myObject.get('size'))

    $('#simple-button').on('click', function(){
        app.myObject.increase_size()
    })
})