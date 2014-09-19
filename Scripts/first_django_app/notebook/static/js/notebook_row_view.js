var NotebookRowView = Backbone.View.extend({
    events: {
        "click .delete-row":    "delete_row"
        ,"blur .description": "edit_value"
    }
    ,initialize: function(){
        console.log('NotebookRowView initialize')
        this.template = _.template($("#notebook-row-template").html())
        this.listenTo(this.model, "destroy", this.remove)
    }
    ,render: function(){
        console.log('NotebookRowView render')
        var json  = this.model.toJSON()
        var view = this.template(json)
        this.$el.html(view)
        return this.$el;
    }
    ,delete_row: function(){
        console.log('NotebookRowView delete_row')
        this.model.destroy()
    }
    ,edit_value: function(){
        console.log('NotebookRowView edit_value')
        var res = this.model.set({
            description: this.$('.description').text()
        },{validate: true});
        if (!res) this.render();
    }
})