var NotebookRowModel = Backbone.Model.extend({
    defaults: {
        description: 'New note'
        ,status: 0
        ,order: 0
    }
    ,urlRoot: '/notebook/save/'//будет использоваться при сохранении
    ,initialize: function(){
        console.log('NotebookRowModel initialize')
        json = this.toJSON()
        console.log(json)
    }
    ,validate: function(attrs){}
})

var NotebookModel = Backbone.Collection.extend({
    model: NotebookRowModel
    //,sortParam: 'status'
    //,sortMode: 1//1 - обычный порядок, -1 обратный порядок
    ,url: '/notebook/load/'
    ,comparator: function(a,b) {
        //if (a.get(this.sortParam) > b.get(this.sortParam)) return -1*this.sortMode;
        //if (a.get(this.sortParam) < b.get(this.sortParam)) return this.sortMode;
        return 0
    }
})