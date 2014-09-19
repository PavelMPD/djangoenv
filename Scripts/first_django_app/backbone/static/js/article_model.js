var ArticleModel = Backbone.Model.extend({
    defaults: {
        name: 'New article',
        description: 'New article description',
        size: 100
    },
    validate: function(attrs){
        if (attrs.size > 150 || attrs.size < 50) {
            console.log('incorrect size')
            return 'incorrect size'
        }
    }
})
