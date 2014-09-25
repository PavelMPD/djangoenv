var NotebookView = Backbone.View.extend({
    events: {
        "click .add-notebook-row":    "add_notebook_row" //ко всем елементам с class = add-notebook-row добавляется событие add_notebook_row
        ,"click .to-json": "to_json"
        ,"click [data-sort]": "render_list" //привязка события к атрибуту (позволяет передавать его значение в функцию)
        ,"click .model-save": "model_save"
    }
    ,initialize: function(){
        console.log('NotebookView initialize')
        //загружается шаблон
        this.template = _.template($("#notebook-template").html())
        //шаблон отрисовывается в this.$el = елементу, который задается при создании view NotebookView el: '#notebook-container'
        this.$el.html(this.template())
        //создаем коллекцию
        this.coll = new NotebookModel()
        //прослушиваются все события
        this.listenTo(this.coll, "all", this.render)
        //добавляем событие на прослушивание добавления нового елемента в коллекцию
        this.listenTo(this.coll, "add", this.add_one_row)
        //запрашивает с сервера данные
        this.coll.fetch();
    }
    ,render: function(){
        console.log('NotebookView render')
        this.coll.each(function(obj,index){
            //obj.get('название поля модели')
        })//проход по всем элементам коллекции
        //this.$('.rockets-count')//доступ к элементам страницы
    }
    ,add_notebook_row: function(){
        console.log('NotebookView add_notebook_row')
        //добавляет в коллекцию новый элемент, тем самым генерируя событие "add", которое в свою очередь вызывает метод add_one_row
        this.coll.add({})
    }
    ,add_one_row: function(model){
        console.log('NotebookView add_one_row')
        //создается view NotebookRowView и передается объект модели NotebookRowModel
        var view = new NotebookRowView({model: model})
        this.$('.notebook-row-list').append(view.render())//в объекте модели вызывается метод render, результат метода отрисовывается во всех елементах страницы с class = notebook-row-list
    }
    ,to_json: function() {
        console.log('NotebookView to_json')
        var json = this.coll.toJSON()
        this.$('.json-out').html(JSON.stringify(json))
    }
    ,render_list: function (e) {
        console.log('NotebookView render_list')
        this.$('.notebook-row-list').html('');
        //this.coll.sortParam = $(e.target).attr('data-sort');
        //this.coll.sortMode = this.coll.sortMode*(-1);
        this.coll.sort();
        var that = this;
        this.coll.each(function(model,index){
            that.add_one_row(model);
        })
    }
    ,model_save: function(){
        console.log('NotebookView model_save')
        this.coll.each(function(obj,index){
            obj.save()
        })//проход по всем элементам коллекции и отправляет для каждого запрос на сохранение
    }
})
