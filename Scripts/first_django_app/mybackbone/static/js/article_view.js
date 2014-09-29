var ArticleView = Backbone.View.extend({
    events: {
        "click .change-size":   "change_size",
        "click .delete-row":    "delete_row",
        "blur .desc":   "edit_value",
        "blur .name":   "edit_value",
        "blur .size":   "edit_value"
    },

    initialize: function() {
        this.template = _.template($("#article-template").html())
        this.listenTo(this.model, "change", this.render);
        //удаление
        this.listenTo(this.model, "destroy", this.remove);
        this.render()
    },

    render: function() {
        var json  = this.model.toJSON()
        var view = this.template(json)
        this.$el.html(view)
        console.log(json)
    },

    delete_row: function(){
        this.model.destroy()
    },

    change_size: function(event){
        var diff = parseInt($(event.target).attr('data-rel'))
        var size = parseInt(this.model.get('size'))
        this.model.set({
            size: size + diff
        }, {validate: true})
    },

    edit_value: function(){
        this.model.set({
            name: this.$('.name').text(),
            description: this.$('.desc').text(),
            size: parseInt(this.$('input.size').attr('value'))
        }, {validate: true})
    }
})