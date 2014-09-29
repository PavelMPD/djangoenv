$(function(){
    var article_model = new ArticleModel()
    var article_view = new ArticleView({
        model: article_model,
        el: '#article'
    })
})
