var NotebookRowModel = Backbone.Model.extend({
    defaults: {
        description: 'New note'
        ,status: 0
        ,order: 0
    }
    ,initialize: function(){
        console.log('NotebookRowModel initialize')
        json = this.toJSON()
        console.log(json)
    }
    ,validate: function(attrs){}
})

var NotebookModel = Backbone.Collection.extend({
    model: NotebookRowModel
})