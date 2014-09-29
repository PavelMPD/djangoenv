$(function(){
    //задаем шаблон
    var compiled = _.template($('#article-template').html());
    //создаем объект
    var article = {
        name: 'New article',
        size: 100,
        color: 'Green',
        nice: true
    }
    //заполняем шаблон данными из объекта и заполняем контейнер на странице
    $('#article').append(compiled(article));
})